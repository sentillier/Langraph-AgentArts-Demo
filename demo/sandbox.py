"""Code Interpreter sandbox capability.

Wraps ``agentarts.sdk.code_session`` so the agent can run Python in an
isolated AgentArts sandbox instead of on the host running the agent.
"""

from __future__ import annotations

import logging
import os

from agentarts.sdk import code_session
# ToolsAPIError derives from BaseException, so ``except Exception`` alone misses it.
from agentarts.sdk.service.tools_http import ToolsAPIError

from demo.config import get_settings

logger = logging.getLogger(__name__)

MISSING_CONFIG_HINT = (
    "Sandbox is not configured. Set AGENTARTS_CODE_INTERPRETER_NAME in .env, plus "
    "HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY when the interpreter uses API_KEY auth "
    "(IAM auth only needs AK/SK). Run `uv run python -m demo.bootstrap sandbox` to bind one."
)

MISSING_ENDPOINT_HINT = (
    "Sandbox data plane endpoint is not configured. Copy the interpreter's access endpoint "
    "(https://<id>.<region>.huaweicloud-agentarts.com) from the AgentArts console into "
    "AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT, or run "
    "`uv run python -m demo.bootstrap sandbox --name <name>` to have it filled in automatically."
)


def is_configured() -> bool:
    """Whether the sandbox capability has everything it needs."""
    return get_settings().sandbox_ready


def _data_plane_endpoint() -> str | None:
    """Return the data plane endpoint the SDK will use for sandbox sessions."""
    settings = get_settings()
    return settings.sandbox_endpoint or os.getenv("AGENTARTS_RUNTIME_DATA_ENDPOINT")


def execute_python(code: str, description: str = "") -> dict:
    """Execute *code* in the AgentArts code interpreter sandbox.

    A fresh sandbox session is opened for each call and stopped afterwards, so
    no state leaks between invocations.

    Args:
        code: Python source code to execute.
        description: Optional note prepended as a comment.

    Returns:
        ``{"ok": True, "result": ...}`` on success,
        ``{"ok": False, "error": ...}`` otherwise. The error is returned rather
        than raised so the LLM can recover and explain the failure.
    """
    settings = get_settings()
    if not settings.sandbox_enabled:
        return {"ok": False, "error": MISSING_CONFIG_HINT}
    if not _data_plane_endpoint():
        return {"ok": False, "error": MISSING_ENDPOINT_HINT}

    if description:
        code = f"# {description}\n{code}"

    api_key = None if settings.sandbox_uses_iam else settings.sandbox_api_key
    try:
        with code_session(
            settings.region,
            settings.sandbox_name,
            auth_type=settings.sandbox_auth_type,
            api_key=api_key,
            verify_ssl=settings.verify_ssl,
        ) as client:
            response = client.invoke(
                operate_type="execute_code",
                api_key=api_key,
                arguments={
                    "code": code,
                    "language": "python",
                    "clear_context": False,
                },
            )
    except (ToolsAPIError, Exception) as exc:
        logger.exception("Sandbox execution failed")
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}

    return {"ok": True, "result": response.get("result")}


def status() -> dict:
    """Describe the sandbox capability for ``/ping`` and the CLI banner."""
    settings = get_settings()
    return {
        "enabled": settings.sandbox_enabled,
        "ready": settings.sandbox_ready,
        "code_interpreter": settings.sandbox_name,
        "auth_type": settings.sandbox_auth_type,
        "data_plane_endpoint": settings.sandbox_endpoint,
    }
