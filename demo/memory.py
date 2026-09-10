"""AgentArts Memory capability.

Two distinct jobs are handled here:

* **Conversation state** - ``AgentArtsMemorySessionSaver`` persists the
  LangGraph checkpoint of every thread to a Memory space, so a conversation can
  be resumed from any process. The Memory backend also extracts long-term
  memories (semantic / episodic / user preference / summary) in the background.
* **Long-term recall** - ``AgentArtsMemoryStore`` performs semantic search over
  those extracted memories, scoped by ``actor_id``.
"""

from __future__ import annotations

import logging
from typing import Any

from agentarts.sdk.integration.langgraph import (
    AgentArtsMemorySessionSaver,
    AgentArtsMemoryStore,
)

from demo.config import get_settings

logger = logging.getLogger(__name__)

#: Namespace holding long-term memory records inside the Memory space.
NAMESPACE = ("memories",)

_checkpointer: Any | None = None
_store: AgentArtsMemoryStore | None = None

MISSING_CONFIG_HINT = (
    "Memory is not configured. Run `uv run python -m demo.bootstrap memory` "
    "or set AGENTARTS_MEMORY_SPACE_ID and HUAWEICLOUD_SDK_MEMORY_API_KEY in .env."
)


def is_configured() -> bool:
    """Whether a Memory space and API key are available."""
    return get_settings().memory_enabled


def get_checkpointer() -> Any:
    """Return the LangGraph checkpointer used to persist conversation state.

    Falls back to an in-process checkpointer when no Memory space is
    configured, so the demo still runs without cloud credentials.
    """
    settings = get_settings()
    if not settings.memory_enabled:
        logger.warning("Memory space not configured - using in-process checkpointer")
        return _in_memory_saver()

    global _checkpointer
    if _checkpointer is None:
        logger.info("Using AgentArts Memory checkpointer (space=%s)", settings.memory_space_id)
        _checkpointer = AgentArtsMemorySessionSaver(
            space_id=settings.memory_space_id,
            region=settings.region,
            api_key=settings.memory_api_key,
            verify_ssl=settings.verify_ssl,
        )
    return _checkpointer


def get_store() -> AgentArtsMemoryStore | None:
    """Return the cross-thread memory store, or ``None`` when unconfigured."""
    settings = get_settings()
    if not settings.memory_enabled:
        return None

    global _store
    if _store is None:
        _store = AgentArtsMemoryStore(
            space_id=settings.memory_space_id,
            region=settings.region,
            api_key=settings.memory_api_key,
            verify_ssl=settings.verify_ssl,
        )
    return _store


def search_memories(query: str, actor_id: str, top_k: int = 3) -> list[dict[str, Any]]:
    """Semantically search long-term memories for *actor_id*.

    Args:
        query: Natural-language search text.
        actor_id: Memory owner; memories are filtered by this identifier.
        top_k: Maximum number of memories to return.

    Returns:
        A list of ``{"content": str, "strategy_type": str, "score": float}``.
        An empty list is returned when memory is unconfigured or search fails.
    """
    store = get_store()
    if store is None or not query.strip():
        return []

    try:
        items = store.search(
            NAMESPACE,
            query=query,
            filter={"actor_id": actor_id},
            limit=max(1, top_k),
        )
    except Exception:
        logger.exception("Memory search failed")
        return []

    memories: list[dict[str, Any]] = []
    for item in items:
        value = item.value or {}
        content = value.get("content")
        if not content:
            continue
        memories.append(
            {
                "content": content,
                "strategy_type": value.get("strategy_type"),
                "score": getattr(item, "score", None),
            }
        )
    return memories


def _in_memory_saver() -> Any:
    try:
        from langgraph.checkpoint.memory import InMemorySaver

        return InMemorySaver()
    except ImportError:  # pragma: no cover - older langgraph releases
        from langgraph.checkpoint.memory import MemorySaver

        return MemorySaver()


def status() -> dict[str, Any]:
    """Describe the memory capability for ``/ping`` and the CLI banner."""
    settings = get_settings()
    return {
        "enabled": settings.memory_enabled,
        "space_id": settings.memory_space_id,
        "recall_enabled": settings.recall_enabled,
        "recall_top_k": settings.recall_top_k,
        "namespace": list(NAMESPACE),
    }
