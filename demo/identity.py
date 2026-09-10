"""Agent Identity capability.

Identity shows up in two places:

* **End-user identity** - the runtime extracts ``X-HW-AgentGateway-User-Id``
  (and the workload access token) from every request into
  ``AgentArtsRuntimeContext``. The demo uses that user id as the memory owner,
  so two callers hitting the same agent never see each other's memories.
* **Credential identity** - when a workload identity and an API key provider
  are configured, the model credential itself is fetched from Agent Identity at
  runtime via the ``@require_api_key`` decorator instead of being read from
  ``OPENAI_API_KEY``.
"""

from __future__ import annotations

import logging
from functools import lru_cache
from typing import Callable

from agentarts.sdk import AgentArtsRuntimeContext, IdentityClient, require_api_key

from demo.config import get_settings

logger = logging.getLogger(__name__)


def resolve_actor_id(payload_user_id: str | None = None) -> str:
    """Resolve the identity that owns this conversation.

    Precedence: explicit payload value, then the user id injected by the
    AgentArts runtime, then ``AGENTARTS_IDENTITY_USER_ID``, then the static demo
    actor id.
    """
    settings = get_settings()
    return (
        payload_user_id
        or AgentArtsRuntimeContext.get_user_id()
        or settings.identity_user_id
        or settings.actor_id
    )


def model_api_key() -> str | None:
    """Fetch the LLM API key from Agent Identity, or ``None`` when disabled."""
    settings = get_settings()
    if not settings.identity_enabled:
        return None

    ensure_workload_access_token()
    provider_name = settings.identity_api_key_provider
    try:
        api_key = _api_key_loader(provider_name, settings.verify_ssl)()
    except Exception:
        logger.exception("Failed to fetch API key from Agent Identity provider %s", provider_name)
        return None
    logger.info("Model API key loaded from Agent Identity provider %s", provider_name)
    return api_key


def ensure_workload_access_token() -> str | None:
    """Make sure a workload access token is present in the runtime context.

    Deployed agents receive the token through the request headers. For local
    runs the token is minted here from the workload identity configured by
    ``uv run python -m demo.bootstrap identity``.
    """
    token = AgentArtsRuntimeContext.get_workload_access_token()
    if token:
        return token

    settings = get_settings()
    if not settings.identity_workload_name:
        return None

    client = IdentityClient(
        region=settings.region,
        ignore_ssl_verification=not settings.verify_ssl,
    )
    token = client.create_workload_access_token(
        workload_name=settings.identity_workload_name,
        user_id=resolve_actor_id(),
    )
    AgentArtsRuntimeContext.set_workload_access_token(token)
    return token


@lru_cache(maxsize=4)
def _api_key_loader(provider_name: str, verify_ssl: bool) -> Callable[[], str | None]:
    """Build (and cache) a callable that injects the provider's API key."""

    @require_api_key(provider_name=provider_name, ignore_ssl_verification=not verify_ssl)
    def _load(api_key: str | None = None) -> str | None:
        return api_key

    return _load


def describe() -> dict:
    """Describe the current identity, used by the ``whoami`` tool and ``/ping``."""
    settings = get_settings()
    return {
        "actor_id": resolve_actor_id(),
        "identity_enabled": settings.identity_enabled,
        "workload_identity": settings.identity_workload_name,
        "api_key_provider": settings.identity_api_key_provider,
        "workload_access_token_present": bool(
            AgentArtsRuntimeContext.get_workload_access_token()
        ),
        "runtime_session_id": AgentArtsRuntimeContext.get_session_id(),
        "runtime_request_id": AgentArtsRuntimeContext.get_request_id(),
        "region": settings.region,
    }


def status() -> dict:
    """Describe the identity capability for ``/ping`` and the CLI banner."""
    settings = get_settings()
    return {
        "enabled": settings.identity_enabled,
        "workload_identity": settings.identity_workload_name,
        "api_key_provider": settings.identity_api_key_provider,
        "default_user_id": settings.identity_user_id,
    }
