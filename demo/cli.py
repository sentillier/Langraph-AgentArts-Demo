"""Small local chat client for the demo agent.

Talks to a running ``demo.app`` server over HTTP and keeps the ``thread_id``
between turns, so conversation state (and long-term memory) accumulates.

Usage:
    uv run python -m demo.cli --user-id alice
"""

from __future__ import annotations

import argparse
import json
import sys
from urllib.parse import urlparse

import httpx

from demo.config import get_settings

USER_ID_HEADER = "X-HW-AgentGateway-User-Id"


def _is_local(base_url: str) -> bool:
    host = urlparse(base_url).hostname or ""
    return host in {"127.0.0.1", "localhost", "::1"}


def _client_host(host: str) -> str:
    """Turn a wildcard listen address into something a client can dial."""
    return "127.0.0.1" if host in {"0.0.0.0", "::", "*"} else host


def _parse_args() -> argparse.Namespace:
    settings = get_settings()
    parser = argparse.ArgumentParser(description="Chat with the LangGraph AgentArts demo")
    parser.add_argument(
        "--url",
        default=f"http://{_client_host(settings.host)}:{settings.port}",
        help="Base URL of the agent server",
    )
    parser.add_argument("--user-id", default=None, help="End-user id sent to the agent")
    parser.add_argument("--thread-id", default=None, help="Resume an existing thread")
    parser.add_argument("--once", default=None, help="Send a single message and exit")
    parser.add_argument("--timeout", type=float, default=180.0, help="Request timeout in seconds")
    return parser.parse_args()


def _send(client: httpx.Client, args: argparse.Namespace, thread_id: str | None, message: str) -> dict:
    payload: dict = {"message": message}
    if thread_id:
        payload["thread_id"] = thread_id
    headers = {USER_ID_HEADER: args.user_id} if args.user_id else {}

    response = client.post("/invocations", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def _build_client(args: argparse.Namespace) -> httpx.Client:
    """Create the HTTP client.

    Proxy environment variables (``HTTP_PROXY``/``ALL_PROXY``) are ignored for
    localhost URLs, which would otherwise break local testing on machines with a
    system-wide proxy configured.
    """
    return httpx.Client(
        base_url=args.url,
        timeout=args.timeout,
        trust_env=not _is_local(args.url),
    )


def _print_result(result: dict) -> None:
    if "error" in result:
        print(f"error: {result['error']}")
        return
    print(f"agent: {result.get('response', '')}")
    used = result.get("tools_used") or []
    if used:
        print(f"       [tools: {', '.join(used)}]")
    recalled = result.get("recalled_memories") or []
    if recalled:
        print(f"       [recalled {len(recalled)} memory item(s)]")
    print(f"       [thread_id: {result.get('thread_id')}]")


def main() -> int:
    args = _parse_args()
    thread_id = args.thread_id

    with _build_client(args) as client:
        try:
            ping = client.get("/ping").json()
            print(f"connected to {args.url} (status: {ping.get('status')})")
        except httpx.HTTPError as exc:
            print(f"cannot reach {args.url}: {exc}")
            return 1

        if args.once:
            _print_result(_send(client, args, thread_id, args.once))
            return 0

        print("commands: :new (start a new thread), :quit, :json (dump last raw response)")
        last: dict = {}
        while True:
            try:
                message = input("you: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            if not message:
                continue
            if message in {":quit", ":exit"}:
                return 0
            if message == ":new":
                thread_id = None
                print("started a new thread")
                continue
            if message == ":json":
                print(json.dumps(last, ensure_ascii=False, indent=2))
                continue

            try:
                last = _send(client, args, thread_id, message)
            except httpx.HTTPStatusError as exc:
                print(f"request failed: {exc.response.status_code} {exc.response.text}")
                continue
            thread_id = last.get("thread_id") or thread_id
            _print_result(last)


if __name__ == "__main__":
    sys.exit(main())
