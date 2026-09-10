"""LangChain tools the LangGraph agent may call.

Each tool is a thin adapter over one AgentArts capability; failures are
returned as JSON instead of raised so the model can explain them to the user.
"""

from __future__ import annotations

import json
from typing import Any

from langchain_core.tools import BaseTool, tool

from demo import identity, memory, sandbox
from demo.config import get_settings


def _dumps(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, default=str)


@tool
def execute_python(code: str, description: str = "") -> str:
    """Run Python code in an isolated AgentArts sandbox and return its output.

    Use it for calculations, data transformation or verifying a result instead
    of guessing. Each call gets a fresh sandbox session that is torn down
    afterwards.

    Args:
        code: Python source code to execute.
        description: Short note about what the code is meant to do.
    """
    return _dumps(sandbox.execute_python(code, description))


@tool
def recall_memory(query: str, top_k: int = 3) -> str:
    """Search long-term memories previously extracted about the current user.

    Args:
        query: What to look for, for example "route preferences".
        top_k: Maximum number of memories to return.
    """
    settings = get_settings()
    actor_id = identity.resolve_actor_id()
    memories = memory.search_memories(query, actor_id=actor_id, top_k=top_k)
    return _dumps(
        {
            "actor_id": actor_id,
            "memory_enabled": settings.memory_enabled,
            "count": len(memories),
            "memories": memories,
        }
    )


@tool
def whoami() -> str:
    """Report the end user this conversation belongs to and the identity setup in effect."""
    return _dumps(identity.describe())


def build_tools() -> list[BaseTool]:
    """Return the tools whose backing capability is configured."""
    settings = get_settings()
    tools: list[BaseTool] = []
    if sandbox.is_configured():
        tools.append(execute_python)
    if settings.memory_enabled:
        tools.append(recall_memory)
    tools.append(whoami)
    return tools
