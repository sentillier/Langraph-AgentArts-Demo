"""The LangGraph agent: memory recall, tool calling and conversation state."""

from __future__ import annotations

import logging
from typing import Annotated, Any, TypedDict

import httpx
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from demo import identity, memory
from demo.config import get_settings
from demo.tools import build_tools

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are the AgentArts LangGraph demo agent.

You can:
- run Python in an isolated AgentArts sandbox (execute_python)
- recall what you know about the current user from AgentArts Memory (recall_memory)
- report the identity in effect for this conversation (whoami)

Guidelines:
1. Answer directly when no tool is needed.
2. Use execute_python for calculations, data processing or verification instead of guessing.
3. Prefer the memories already injected into your context; call recall_memory only
   when you need something more specific.
4. Answer in the language the user writes in, and keep answers concise.
"""

RECALL_PROMPT = """
Memories retrieved from AgentArts Memory about the current user:
{memories}

Use them when they are relevant, and never contradict them.
"""


class AgentState(TypedDict):
    """State shared between graph nodes."""

    messages: Annotated[list[AnyMessage], add_messages]
    actor_id: str
    recalled: list[str]


def _build_llm() -> ChatOpenAI:
    """Build the chat model, taking the credential from Agent Identity when configured."""
    settings = get_settings()
    api_key = identity.model_api_key() or settings.llm_api_key
    if not api_key:
        msg = (
            "No model credential available. Set OPENAI_API_KEY in .env, or configure "
            "Agent Identity with `uv run python -m demo.bootstrap identity`."
        )
        raise RuntimeError(msg)

    kwargs: dict[str, Any] = {
        "model": settings.llm_model,
        "api_key": api_key,
        "temperature": 0.2,
        # Proxy variables such as ALL_PROXY=socks5://... make httpx look for the
        # optional `socksio` dependency and fail the whole request. Model
        # endpoints are usually reachable directly, so ignore them by default.
        "http_client": httpx.Client(trust_env=settings.llm_trust_env, timeout=_timeout(settings)),
        "http_async_client": httpx.AsyncClient(
            trust_env=settings.llm_trust_env, timeout=_timeout(settings)
        ),
    }
    if settings.llm_base_url:
        kwargs["base_url"] = settings.llm_base_url
    return ChatOpenAI(**kwargs)


def _timeout(settings: Any) -> httpx.Timeout:
    return httpx.Timeout(settings.llm_timeout, connect=min(10.0, settings.llm_timeout))


def build_agent() -> Any:
    """Compile the LangGraph agent, wired to AgentArts Memory for state and recall."""
    settings = get_settings()
    llm = _build_llm()
    tools = build_tools()
    llm_with_tools = llm.bind_tools(tools) if tools else llm

    def recall(state: AgentState) -> dict[str, Any]:
        """Search the memory store for context relevant to the latest user message."""
        if not (settings.memory_enabled and settings.recall_enabled):
            return {"recalled": []}

        query = _last_human_text(state["messages"])
        if not query:
            return {"recalled": []}

        hits = memory.search_memories(
            query,
            actor_id=state.get("actor_id") or settings.actor_id,
            top_k=settings.recall_top_k,
        )
        return {"recalled": [hit["content"] for hit in hits if hit.get("content")]}

    def call_model(state: AgentState) -> dict[str, Any]:
        """Call the model with the system prompt, recalled memories and history."""
        system_prompt = SYSTEM_PROMPT
        recalled = state.get("recalled") or []
        if recalled:
            listed = "\n".join(f"- {item}" for item in recalled)
            system_prompt = f"{SYSTEM_PROMPT}\n{RECALL_PROMPT.format(memories=listed)}"

        response = llm_with_tools.invoke(
            [SystemMessage(content=system_prompt), *state["messages"]]
        )
        return {"messages": [response]}

    def should_continue(state: AgentState) -> str:
        """Route to the tool node while the model keeps requesting tools."""
        last = state["messages"][-1]
        if isinstance(last, AIMessage) and last.tool_calls:
            return "tools"
        return END

    builder = StateGraph(AgentState)
    builder.add_node("recall", recall)
    builder.add_node("agent", call_model)
    builder.add_edge(START, "recall")
    builder.add_edge("recall", "agent")

    if tools:
        builder.add_node("tools", ToolNode(tools))
        builder.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
        builder.add_edge("tools", "agent")
    else:
        builder.add_edge("agent", END)

    agent = builder.compile(checkpointer=memory.get_checkpointer(), store=memory.get_store())
    logger.info("Agent compiled with tools: %s", [tool.name for tool in tools])
    return agent


def invoke(agent: Any, message: str, thread_id: str, actor_id: str) -> dict[str, Any]:
    """Run one turn of the agent and normalise the result for the HTTP layer."""
    result = agent.invoke(
        {"messages": [HumanMessage(content=message)], "actor_id": actor_id},
        config={"configurable": {"thread_id": thread_id, "actor_id": actor_id}},
    )
    messages: list[AnyMessage] = result.get("messages", [])
    return {
        "response": message_text(messages[-1]) if messages else "",
        "tools_used": tools_used(messages),
        "recalled": result.get("recalled") or [],
    }


def message_text(message: AnyMessage) -> str:
    """Flatten a LangChain message content into plain text."""
    content = getattr(message, "content", message)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type") == "text":
                parts.append(str(block.get("text", "")))
        return "".join(parts) if parts else str(content)
    return str(content)


def tools_used(messages: list[AnyMessage]) -> list[str]:
    """Return the tool names requested during the current turn, in call order."""
    turn = messages[_last_human_index(messages) :]
    used: list[str] = []
    for message in turn:
        if isinstance(message, AIMessage):
            for call in message.tool_calls or []:
                name = call.get("name") if isinstance(call, dict) else None
                if name:
                    used.append(name)
    return used


def _last_human_text(messages: list[AnyMessage]) -> str:
    index = _last_human_index(messages)
    return message_text(messages[index]) if index >= 0 else ""


def _last_human_index(messages: list[AnyMessage]) -> int:
    for index in range(len(messages) - 1, -1, -1):
        if isinstance(messages[index], HumanMessage):
            return index
    return -1
