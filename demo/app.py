"""AgentArts runtime host for the LangGraph agent.

``AgentArtsRuntimeApp`` wraps the graph behind the standard AgentArts surface:

* ``POST /invocations`` - run one conversation turn
* ``GET  /ping``        - liveness probe
* ``WS   /ws``          - streaming endpoint (unused by this demo)

Run locally with ``uv run python -m demo.app``.
"""

from __future__ import annotations

import logging
import uuid
from typing import Any

from agentarts.sdk import AgentArtsRuntimeApp, RequestContext
from agentarts.sdk.runtime.model import PingStatus

from demo import identity, sandbox
from demo.config import get_settings
from demo.graph import build_agent, invoke
from demo.memory import status as memory_status

logger = logging.getLogger(__name__)

app = AgentArtsRuntimeApp()
settings = get_settings()

_agent: Any | None = None


def get_agent() -> Any:
    """Build the LangGraph agent on first use."""
    global _agent
    if _agent is None:
        _agent = build_agent()
    return _agent


@app.entrypoint
def handler(payload: dict, context: RequestContext | None = None) -> dict:
    """Run one conversation turn.

    Args:
        payload: Request body with ``message``, plus optional ``thread_id`` and
            ``user_id`` overrides.
        context: Request context injected by the runtime (session and request id).

    Returns:
        The agent reply together with the conversation identifiers and the
        capabilities that were actually exercised.
    """
    message = (payload.get("message") or payload.get("query") or "").strip()
    if not message:
        return {"error": "message is required"}

    actor_id = identity.resolve_actor_id(payload.get("user_id"))
    thread_id = payload.get("thread_id") or payload.get("session_id")
    if not thread_id and context is not None:
        thread_id = context.session_id
    thread_id = thread_id or uuid.uuid4().hex

    logger.info("Invocation thread=%s actor=%s", thread_id, actor_id)
    result = invoke(get_agent(), message=message, thread_id=thread_id, actor_id=actor_id)

    return {
        "response": result["response"],
        "thread_id": thread_id,
        "user_id": actor_id,
        "tools_used": result["tools_used"],
        "recalled_memories": result["recalled"],
    }


@app.ping
def health() -> PingStatus:
    """Report liveness; the same handler is used by AgentArts readiness probes."""
    return PingStatus.HEALTHY


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    logger.info("Capabilities: %s", settings.capabilities())
    logger.info("Memory: %s", memory_status())
    logger.info("Sandbox: %s", sandbox.status())
    logger.info("Identity: %s", identity.status())
    print(f"Starting LangGraph AgentArts demo on http://{settings.host}:{settings.port}")
    print("  POST /invocations - run a conversation turn")
    print("  GET  /ping        - health check")
    app.run(host=settings.host, port=settings.port)
