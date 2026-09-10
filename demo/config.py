"""Configuration for the LangGraph + AgentArts demo.

Every setting is read from environment variables, optionally supplied by a
``.env`` file located in the project root.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


def _str(name: str, default: str | None = None) -> str | None:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        return default
    return raw.strip()


def _bool(name: str, default: bool) -> bool:
    raw = _str(name)
    if raw is None:
        return default
    return raw.lower() in {"1", "true", "yes", "on"}


def _int(name: str, default: int) -> int:
    raw = _str(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _float(name: str, default: float) -> float:
    raw = _str(name)
    if raw is None:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _auth_type() -> str:
    """Read the code interpreter auth type, defaulting to ``API_KEY``."""
    raw = _str("AGENTARTS_CODE_INTERPRETER_AUTH_TYPE", "API_KEY") or "API_KEY"
    normalized = raw.strip().upper().replace("-", "_")
    return normalized if normalized in {"API_KEY", "IAM"} else "API_KEY"


def _base_url() -> str | None:
    """Read the model base URL, tolerating a full completions endpoint.

    ``OPENAI_BASE_URL`` is a *base* URL; the OpenAI client appends
    ``/chat/completions`` itself. Pasting the full endpoint is a common slip, so
    strip the known suffixes instead of failing with an HTTP 404.
    """
    url = _str("OPENAI_BASE_URL")
    if not url:
        return None
    trimmed = url.rstrip("/")
    for suffix in ("/chat/completions", "/completions", "/responses"):
        if trimmed.endswith(suffix):
            return trimmed[: -len(suffix)]
    return trimmed


@dataclass(frozen=True)
class Settings:
    """Resolved demo configuration."""

    region: str
    verify_ssl: bool
    host: str
    port: int
    log_level: str

    llm_model: str
    llm_api_key: str | None
    llm_base_url: str | None
    llm_trust_env: bool
    llm_timeout: float

    memory_space_id: str | None
    memory_api_key: str | None
    actor_id: str
    assistant_id: str
    recall_enabled: bool
    recall_top_k: int

    sandbox_name: str | None
    sandbox_api_key: str | None
    sandbox_auth_type: str
    sandbox_endpoint: str | None

    identity_workload_name: str | None
    identity_api_key_provider: str | None
    identity_user_id: str | None

    @property
    def memory_enabled(self) -> bool:
        """True when a Memory space and its API key are both configured."""
        return bool(self.memory_space_id and self.memory_api_key)

    @property
    def sandbox_enabled(self) -> bool:
        """True when the sandbox can actually be used.

        ``IAM`` sessions authenticate with AK/SK, so only the interpreter name
        is required; ``API_KEY`` sessions additionally need the API key value.
        """
        if not self.sandbox_name:
            return False
        if self.sandbox_auth_type == "IAM":
            return True
        return bool(self.sandbox_api_key)

    @property
    def sandbox_uses_iam(self) -> bool:
        """True when sandbox sessions authenticate with AK/SK instead of an API key."""
        return self.sandbox_auth_type == "IAM"

    @property
    def sandbox_ready(self) -> bool:
        """True when the sandbox has credentials *and* a data plane endpoint."""
        return self.sandbox_enabled and bool(self.sandbox_endpoint)

    @property
    def identity_enabled(self) -> bool:
        """True when a workload identity and an API key provider are both configured."""
        return bool(self.identity_workload_name and self.identity_api_key_provider)

    @property
    def llm_ready(self) -> bool:
        """True when the agent has a usable model credential."""
        return bool(self.llm_api_key) or self.identity_enabled

    def capabilities(self) -> dict[str, bool]:
        """Capability matrix used by ``/ping``, responses and the CLI banner."""
        return {
            "runtime": True,
            "memory": self.memory_enabled,
            "sandbox": self.sandbox_ready,
            "identity": self.identity_enabled,
            "llm": self.llm_ready,
        }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the process-wide settings, loaded once."""
    return Settings(
        region=_str("HUAWEICLOUD_SDK_REGION", "cn-southwest-2") or "cn-southwest-2",
        verify_ssl=_bool("VERIFY_SSL", True),
        # 0.0.0.0 keeps the port mapping of a container reachable; the CLI maps
        # it back to 127.0.0.1 when it builds its own client URL.
        host=_str("AGENTARTS_DEMO_HOST", "0.0.0.0") or "0.0.0.0",
        port=_int("AGENTARTS_DEMO_PORT", 8080),
        log_level=_str("AGENTARTS_LOG_LEVEL", "INFO") or "INFO",
        llm_model=_str("OPENAI_MODEL_NAME", "deepseek-v3.2") or "deepseek-v3.2",
        llm_api_key=_str("OPENAI_API_KEY"),
        llm_base_url=_base_url(),
        llm_trust_env=_bool("AGENTARTS_DEMO_LLM_TRUST_ENV", False),
        llm_timeout=_float("AGENTARTS_DEMO_LLM_TIMEOUT", 120.0),
        memory_space_id=_str("AGENTARTS_MEMORY_SPACE_ID"),
        memory_api_key=_str("HUAWEICLOUD_SDK_MEMORY_API_KEY"),
        actor_id=_str("AGENTARTS_DEMO_ACTOR_ID", "demo-user") or "demo-user",
        assistant_id=_str("AGENTARTS_DEMO_ASSISTANT_ID", "langgraph-agentarts-demo")
        or "langgraph-agentarts-demo",
        recall_enabled=_bool("AGENTARTS_DEMO_RECALL_ENABLED", True),
        recall_top_k=_int("AGENTARTS_DEMO_RECALL_TOP_K", 3),
        sandbox_name=_str("AGENTARTS_CODE_INTERPRETER_NAME"),
        sandbox_api_key=_str("HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY"),
        sandbox_auth_type=_auth_type(),
        sandbox_endpoint=_str("AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT")
        or _str("AGENTARTS_RUNTIME_DATA_ENDPOINT"),
        identity_workload_name=_str("AGENTARTS_IDENTITY_WORKLOAD_NAME"),
        identity_api_key_provider=_str("AGENTARTS_IDENTITY_API_KEY_PROVIDER"),
        identity_user_id=_str("AGENTARTS_IDENTITY_USER_ID"),
    )


def reload_settings() -> Settings:
    """Drop the cache and re-read the environment (used by the bootstrap script)."""
    get_settings.cache_clear()
    return get_settings()
