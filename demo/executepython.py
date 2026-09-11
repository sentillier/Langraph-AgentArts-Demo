"""Execute Python through an AgentArts Runtime session."""
from __future__ import annotations
import os
from agentarts.sdk.service.runtime_client import RuntimeClient

def execute_python(code: str) -> dict:
    """Run *code* in the deployed Runtime container and return stdout/stderr."""
    agent = os.getenv("AGENTARTS_RUNTIME_AGENT_NAME")
    endpoint = os.getenv("AGENTARTS_RUNTIME_DATA_ENDPOINT")
    if not agent or not endpoint:
        return {"ok": False, "error": "Set AGENTARTS_RUNTIME_AGENT_NAME and AGENTARTS_RUNTIME_DATA_ENDPOINT."}
    client = RuntimeClient(data_endpoint=endpoint, region_id=os.getenv("HUAWEICLOUD_SDK_REGION", "cn-southwest-2"), verify_ssl=os.getenv("VERIFY_SSL", "true").lower() != "false")
    session = client.start_session(agent_name=agent, user_id=os.getenv("AGENTARTS_DEMO_ACTOR_ID", "demo-user"))
    sid = session.get("session_id")
    if not sid:
        return {"ok": False, "error": f"Runtime did not return session_id: {session}"}
    try:
        command = ["python", "-c", code]
        result = client.exec_command(agent_name=agent, session_id=sid, command=command, timeout=900)
        return {"ok": True, "session_id": sid, "result": result}
    except Exception as exc:
        return {"ok": False, "session_id": sid, "error": f"{type(exc).__name__}: {exc}"}
    finally:
        try:
            client.stop_session(agent_name=agent, session_id=sid)
        except Exception:
            pass
