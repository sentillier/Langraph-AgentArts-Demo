"""One-time provisioning of the cloud resources this demo needs.

    uv run python -m demo.bootstrap status    # show resolved configuration
    uv run python -m demo.bootstrap memory    # create the Memory space
    uv run python -m demo.bootstrap identity  # create the workload identity + API key provider

The ``memory`` and ``identity`` commands write the resulting identifiers back
into ``.env``, so the agent picks them up on the next start.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from agentarts.sdk import CodeInterpreter, IdentityClient, MemoryClient
# ToolsAPIError derives from BaseException, so ``except Exception`` alone misses it.
from agentarts.sdk.service.tools_http import ToolsAPIError

from demo import identity, sandbox
from demo.config import ENV_FILE, get_settings
from demo.memory import status as memory_status

MEMORY_STRATEGIES = ["semantic", "episodic", "user_preference", "summary"]
DEFAULT_PROVIDER_NAME = "langgraph-agentarts-demo-llm-key"
DEFAULT_WORKLOAD_NAME = "langgraph-agentarts-demo-workload"


def upsert_env(path: Path, values: dict[str, str]) -> None:
    """Write *values* into the dotenv file, replacing existing keys in place."""
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    if original.strip():
        # Keep a recoverable copy in case a run writes values you did not intend.
        path.with_name(path.name + ".bak").write_text(original, encoding="utf-8")

    lines = original.splitlines()
    remaining = dict(values)
    output: list[str] = []

    for line in lines:
        key = line.split("=", 1)[0].strip() if "=" in line else None
        if key in remaining:
            output.append(f"{key}={remaining.pop(key)}")
        else:
            output.append(line)

    if remaining:
        if output and output[-1] != "":
            output.append("")
        output.extend(f"{key}={value}" for key, value in remaining.items())

    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"[ok] updated {path}")


def _require_credentials(action: str) -> bool:
    """Check AK/SK and explain where they were looked for when missing."""
    if os.getenv("HUAWEICLOUD_SDK_AK") and os.getenv("HUAWEICLOUD_SDK_SK"):
        return True

    print(f"[error] HUAWEICLOUD_SDK_AK / HUAWEICLOUD_SDK_SK are required to {action}.")
    if not ENV_FILE.exists():
        print(f"        {ENV_FILE} does not exist - run: cp .env.example .env")
    elif not ENV_FILE.read_text(encoding="utf-8").strip():
        print(f"        {ENV_FILE} is empty - fill in your AK/SK (see .env.example).")
    else:
        print(f"        Checked the environment and {ENV_FILE}: both keys must be non-empty.")
    return False


def _as_url(endpoint: str) -> str:
    """Normalise an access endpoint into a full HTTPS URL."""
    endpoint = endpoint.strip()
    if endpoint.startswith(("http://", "https://")):
        return endpoint
    return f"https://{endpoint}"


def bootstrap_memory() -> int:
    """Create a Memory space with all four built-in extraction strategies."""
    settings = get_settings()
    if settings.memory_enabled:
        print(
            "Memory is already configured "
            f"(space={settings.memory_space_id}). Delete those keys in .env to recreate it."
        )
        return 0
    if not _require_credentials("create a memory space"):
        return 1

    name = os.getenv("AGENTARTS_MEMORY_SPACE_NAME", "langgraph-agentarts-demo-space")
    print(f"Creating Memory space '{name}' in {settings.region} ...")

    client = MemoryClient(region_name=settings.region, verify_ssl=settings.verify_ssl)
    try:
        space = client.create_space(
            name=name,
            description="Memory space for the LangGraph + AgentArts demo",
            memory_strategies_builtin=MEMORY_STRATEGIES,
            memory_extract_idle_seconds=30,
        )
        print(f"  space id : {space.id}")
        print(f"  strategies: {space.memory_strategies_builtin}")

        print("Waiting 5s for the API key to propagate to the data plane ...")
        time.sleep(5)

        session = client.create_memory_session(
            space_id=space.id,
            actor_id=settings.actor_id,
            assistant_id=settings.assistant_id,
        )
        print(f"  data plane verified with session {session.id}")
    finally:
        client.close()

    upsert_env(
        ENV_FILE,
        {
            "AGENTARTS_MEMORY_SPACE_ID": space.id,
            "HUAWEICLOUD_SDK_MEMORY_API_KEY": space.api_key or "",
            "HUAWEICLOUD_SDK_REGION": settings.region,
        },
    )
    print("Memory ready. Restart the agent to pick up the new space.")
    return 0


def bootstrap_identity() -> int:
    """Create an API key credential provider plus a workload identity for it."""
    settings = get_settings()
    provider_name = settings.identity_api_key_provider or DEFAULT_PROVIDER_NAME
    workload_name = settings.identity_workload_name or DEFAULT_WORKLOAD_NAME
    seed_key = os.getenv("AGENTARTS_IDENTITY_SEED_API_KEY") or settings.llm_api_key

    if not seed_key:
        print(
            "[error] No credential to store. Set OPENAI_API_KEY (or "
            "AGENTARTS_IDENTITY_SEED_API_KEY) to the API key the provider should hold."
        )
        return 1
    if not _require_credentials("create an API key provider and a workload identity"):
        return 1

    user_id = settings.identity_user_id or settings.actor_id
    client = IdentityClient(
        region=settings.region,
        ignore_ssl_verification=not settings.verify_ssl,
    )

    print(f"Creating API key credential provider '{provider_name}' ...")
    client.create_api_key_credential_provider(name=provider_name, api_key=seed_key)

    print(f"Creating workload identity '{workload_name}' ...")
    client.create_workload_identity(name=workload_name)

    print(f"Minting a workload access token for user '{user_id}' ...")
    token = client.create_workload_access_token(workload_name=workload_name, user_id=user_id)

    print("Reading the API key back through Agent Identity ...")
    fetched = client.get_resource_api_key(
        provider_name=provider_name,
        workload_access_token=token,
    )
    print(f"  round trip ok (key length: {len(fetched)})")

    upsert_env(
        ENV_FILE,
        {
            "AGENTARTS_IDENTITY_WORKLOAD_NAME": workload_name,
            "AGENTARTS_IDENTITY_API_KEY_PROVIDER": provider_name,
            "AGENTARTS_IDENTITY_USER_ID": user_id,
            "HUAWEICLOUD_SDK_REGION": settings.region,
        },
    )
    print("Identity ready. The agent now fetches its model key from Agent Identity.")
    return 0


def show_status() -> int:
    """Print the resolved configuration and the capability matrix."""
    settings = get_settings()
    print(f"region        : {settings.region}")
    print(f"model         : {settings.llm_model}")
    print(f"endpoint      : {settings.llm_base_url or '(default OpenAI endpoint)'}")
    print(f"capabilities  : {settings.capabilities()}")
    print(f"memory        : {memory_status()}")
    print(f"sandbox       : {sandbox.status()}")
    print(f"identity      : {identity.status()}")
    print(f"dotenv file   : {ENV_FILE} ({'found' if ENV_FILE.exists() else 'missing'})")
    return 0


def bootstrap_sandbox(args: argparse.Namespace) -> int:
    """List code interpreters and bind one to ``.env``, creating it when asked."""
    settings = get_settings()
    if not _require_credentials("manage code interpreters"):
        return 1

    client = CodeInterpreter(region=settings.region, verify_ssl=settings.verify_ssl)
    try:
        listing = client.list_code_interpreters(limit=50)
    except (ToolsAPIError, Exception) as exc:
        print(f"[error] could not list code interpreters: {type(exc).__name__}: {exc}")
        return 1

    items = listing.get("items") or []
    print(f"Code interpreters in {settings.region}:")
    if not items:
        print("  (none)")
    for item in items:
        endpoint = item.get("access_endpoint") or "-"
        print(f"  - {item.get('name')}  id={item.get('id')}  endpoint={endpoint}")

    name = args.name or settings.sandbox_name
    if not name:
        if args.create:
            print("\n[error] --create needs --name: choose a name for the new interpreter.")
            print(
                "  uv run python -m demo.bootstrap sandbox --name langgraph-demo-sandbox "
                "--create --auth-type IAM"
            )
            return 1
        print("\nBind an existing interpreter with --name, or create one:")
        if items:
            print(f"  uv run python -m demo.bootstrap sandbox --name {items[0].get('name')}")
        print(
            "  uv run python -m demo.bootstrap sandbox --name langgraph-demo-sandbox "
            "--create --auth-type IAM"
        )
        return 0

    existing = next((item for item in items if item.get("name") == name), None)
    if existing:
        print(f"\nUsing the existing interpreter '{name}'.")
        detail = existing
        if not args.auth_type and detail.get("id"):
            try:
                detail = {**detail, **client.get_code_interpreter(detail["id"])}
            except (ToolsAPIError, Exception) as exc:
                print(f"  (details unavailable, using list info: {type(exc).__name__})")
    else:
        if not args.create:
            if args.name:
                print(f"\n'{name}' does not exist. Add --create to create it.")
                return 1
            print(f"\nThe interpreter configured in .env ('{name}') was not found in this region.")
            print("Bind another one with --name, or create it with --create.")
            return 0

        auth_type = (args.auth_type or settings.sandbox_auth_type).upper()
        if auth_type == "API_KEY" and not args.api_key_name:
            print("[error] API_KEY auth needs an existing AgentArts API key: pass its name via --api-key-name.")
            print("        Or create the interpreter with --auth-type IAM (AK/SK signing, no API key needed).")
            return 1

        print(f"\nCreating code interpreter '{name}' (auth_type={auth_type}) ...")
        try:
            detail = client.create_code_interpreter(
                name=name,
                auth_type=auth_type,
                api_key_name=args.api_key_name,
                description="Sandbox for the LangGraph + AgentArts demo",
            )
        except (ToolsAPIError, Exception) as exc:
            print(f"[error] could not create '{name}': {type(exc).__name__}: {exc}")
            return 1
        print(f"  created id={detail.get('id')} endpoint={detail.get('access_endpoint') or '-'}")

    auth_type = (args.auth_type or detail.get("auth_type") or settings.sandbox_auth_type).upper()
    values = {
        "AGENTARTS_CODE_INTERPRETER_NAME": detail.get("name") or name,
        "AGENTARTS_CODE_INTERPRETER_AUTH_TYPE": auth_type,
        "HUAWEICLOUD_SDK_REGION": settings.region,
    }
    access_endpoint = detail.get("access_endpoint")
    if access_endpoint:
        values["AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT"] = _as_url(access_endpoint)
    if args.api_key:
        values["HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY"] = args.api_key
    upsert_env(ENV_FILE, values)

    if access_endpoint:
        print(f"Data plane endpoint: {_as_url(access_endpoint)}")
    else:
        print(
            "Note: no access endpoint was returned - copy it from the console into "
            "AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT, otherwise sandbox calls cannot be routed."
        )
    if auth_type == "API_KEY" and not (args.api_key or settings.sandbox_api_key):
        print(
            "Note: this interpreter uses API_KEY auth - put the key value from the console into "
            "HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY."
        )
    print("Sandbox ready. Restart the agent to pick it up.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Provision resources for the AgentArts demo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status", help="Show resolved configuration and capabilities")
    subparsers.add_parser("memory", help="Create the Memory space")
    subparsers.add_parser("identity", help="Create the workload identity and API key provider")

    sandbox_parser = subparsers.add_parser("sandbox", help="List, create or bind a code interpreter")
    sandbox_parser.add_argument("--name", help="Interpreter name (defaults to the .env value)")
    sandbox_parser.add_argument(
        "--create", action="store_true", help="Create the interpreter when it does not exist"
    )
    sandbox_parser.add_argument(
        "--auth-type", choices=["API_KEY", "IAM"], help="Session auth type (default: keep the current one)"
    )
    sandbox_parser.add_argument(
        "--api-key-name", help="Existing AgentArts API key name, required by --auth-type API_KEY"
    )
    sandbox_parser.add_argument("--api-key", help="API key value to store in .env (optional)")

    args = parser.parse_args()
    if args.command == "memory":
        return bootstrap_memory()
    if args.command == "identity":
        return bootstrap_identity()
    if args.command == "sandbox":
        return bootstrap_sandbox(args)
    return show_status()


if __name__ == "__main__":
    sys.exit(main())
