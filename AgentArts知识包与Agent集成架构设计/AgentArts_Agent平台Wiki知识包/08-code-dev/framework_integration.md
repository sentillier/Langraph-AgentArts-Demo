# 框架集成

> 如何把已有框架 Agent 接入 AgentArts 平台。核心范式：**零改动包装**——框架侧不改代码，`AgentArtsRuntimeApp` 只做外层 HTTP 适配。

## 1. 集成路径总览

| 框架 | 集成方式 | 安装 |
| --- | --- | --- |
| 任意框架 | `@app.entrypoint` 包装 `run`/`ainvoke` | `pip install agentarts-sdk` |
| LangGraph | 专用适配器（saver + store） | `pip install agentarts-sdk[langgraph]` |
| LangChain | `@app.entrypoint` 包装 `AgentExecutor.invoke` | `pip install agentarts-sdk[langchain]` |
| Google ADK | `@app.entrypoint` 包装 `Runner.run_async` | 模板 `google-adk` |
| AutoGen | `@app.entrypoint` 包装 `AssistantAgent.run` | `pip install agentarts-sdk[autogen]` |
| CrewAI | `@app.entrypoint` 包装 `Crew.kickoff` | `pip install agentarts-sdk[crewai]` |

## 2. 最简 Runtime Agent

所有集成的起点——理解 `AgentArtsRuntimeApp` + `@app.entrypoint` + `handler.run()` 三件套：

```python
from agentarts.sdk import AgentArtsRuntimeApp

app = AgentArtsRuntimeApp()

@app.entrypoint
def handler(payload: dict):
    message = payload.get("message", "")
    session_id = payload.get("session_id", "default-session")
    return {
        "response": f"You said: {message}",
        "session_id": session_id,
    }

if __name__ == "__main__":
    handler.run(host="0.0.0.0", port=8080)
```

要点：
- `payload` 由平台注入，是 JSON dict
- handler 可 sync 或 async
- 返回 dict 作为响应；返回 generator 自动转 SSE
- `handler.run()` 启动 HTTP 服务，暴露 `POST /invocations` 和 `GET /ping`

## 3. 包装已有 LangChain Agent

**零改动包装范式**：在模块加载时构建 `AgentExecutor`（昂贵对象只建一次），在 entrypoint 内仅 `invoke`。

```python
import os
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from agentarts.sdk import AgentArtsRuntimeApp

app = AgentArtsRuntimeApp()

def create_agent_with_tools():
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        temperature=0,
    )

    @tool
    def calculate(expression: str) -> str:
        """Evaluate a mathematical expression."""
        import math
        allowed_names = {"sqrt": math.sqrt, "sin": math.sin, "pi": math.pi}
        try:
            return str(eval(expression, {"__builtins__": {}}, allowed_names))
        except Exception as e:
            return f"Error: {e!s}"

    @tool
    def get_current_time() -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tools = [calculate, get_current_time]
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant with access to tools..."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor = create_agent_with_tools()

@app.entrypoint
def handler(payload: dict):
    message = payload.get("message", "")
    include_intermediate_steps = payload.get("include_intermediate_steps", False)
    if not message:
        return {"error": "message is required"}

    result = agent_executor.invoke({"input": message})

    intermediate_steps = None
    if include_intermediate_steps:
        intermediate_steps = [
            {"tool": step[0].tool, "input": step[0].tool_input, "output": step[1]}
            for step in result.get("intermediate_steps", [])
        ]
    return {"response": result["output"], "intermediate_steps": intermediate_steps}

if __name__ == "__main__":
    handler.run(host="0.0.0.0", port=8080)
```

要点：
- `payload` 字段可控制是否回传 `intermediate_steps`（工具调用轨迹）
- LangChain 侧完全不改，`AgentArtsRuntimeApp` 只做外层 HTTP 适配

## 4. 包装已有 LangGraph Agent（持久化 Checkpointer）

LangGraph 的深度集成：用 `AgentArtsMemorySessionSaver` 替换默认 checkpointer，把状态从本地内存/Redis 迁移到托管 Memory Service。

```python
import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, StateGraph
from agentarts.sdk import AgentArtsRuntimeApp
from agentarts.sdk.integration.langgraph import AgentArtsMemorySessionSaver

app = AgentArtsRuntimeApp()

def create_agent():
    model = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )

    def call_model(state: MessagesState):
        return {"messages": [model.invoke(state["messages"])]}

    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", call_model)
    workflow.set_entry_point("agent")
    workflow.set_finish_point("agent")

    # 用 AgentArts Memory 作为 LangGraph 的 checkpointer
    checkpointer = AgentArtsMemorySessionSaver(
        space_id=os.getenv("AGENTARTS_MEMORY_SPACE_ID"),
        api_key=os.getenv("HUAWEICLOUD_SDK_MEMORY_API_KEY"),
    )
    return workflow.compile(checkpointer=checkpointer)

agent = create_agent()

@app.entrypoint
async def handler(payload: dict):
    message = payload.get("message", "")
    thread_id = payload.get("thread_id")
    if not message:
        return {"error": "message is required", "thread_id": thread_id or ""}

    thread_id = thread_id or os.urandom(8).hex()
    config = {"configurable": {"thread_id": thread_id}}

    result = await agent.ainvoke({"messages": [HumanMessage(content=message)]}, config=config)
    last_message = result["messages"][-1]
    response_text = last_message.content if hasattr(last_message, "content") else str(last_message)
    return {"response": response_text, "thread_id": thread_id}

if __name__ == "__main__":
    handler.run(host="0.0.0.0", port=8080)
```

要点：
- `thread_id` 即 LangGraph 会话标识，同时映射到 Memory Service 的 `session_id`——同一 `thread_id` 跨多次调用自动续接历史
- 首次调用无 `thread_id` 时生成随机值，回传给调用方以便续接
- LangGraph 图本身完全不变，仅替换 checkpointer

所需环境变量：`AGENTARTS_MEMORY_SPACE_ID`、`HUAWEICLOUD_SDK_MEMORY_API_KEY`、`OPENAI_*`。

## 5. LangGraph 适配器 API

### AgentArtsMemorySessionSaver

继承 `langgraph.checkpoint.base.BaseCheckpointSaver`。

```python
AgentArtsMemorySessionSaver(
    space_id: str,
    region: str | None = None,
    api_key: str | None = None,
    max_messages: int = 10,
    serde: JsonPlusSerializer | None = None,
    verify_ssl: bool | str = True,
)
```

| 方法 | 说明 |
| --- | --- |
| `get_tuple(config)` | 从 Memory 取最近 `max_messages` 条，转成 `CheckpointTuple` |
| `put(config, checkpoint, metadata)` | **仅发送 delta**（`messages[last_count:]`），避免重复 |
| `put_writes(config, writes, task_id, task_path)` | 把 pending writes 写入独立的 UUID5 派生 session，与对话消息隔离 |
| `list(config, filter, before, limit)` | 列出 checkpoint（支持 `before` / `limit`） |
| `delete_thread(thread_id)` | 删除对话 session 与 writes session（软删除，后端异步清理） |
| `close()` / `aclose()` | 关闭同步/异步连接；支持 `with` / `async with` |
| `aget_tuple` / `aput` / `aput_writes` / `alist` / `adelete_thread` | 异步版本，用 `AsyncMemoryClient` |

**设计要点**：
- `thread_id` 直接映射为 `session_id`
- delta tracking：`_persisted_count` 按 session 维护
- pending writes 读取时普通 writes 取首次、ERROR/INTERRUPT/RESUME/SCHEDULED 取最后一次，保证可重放
- **整个应用生命周期复用同一 saver 实例**，不要为同一 session 创建多个实例

### AgentArtsMemoryStore

继承 `langgraph.store.base.BaseStore`，提供跨线程语义记忆存储。

```python
AgentArtsMemoryStore(
    space_id: str,
    region: str | None = None,
    api_key: str | None = None,
    verify_ssl: bool | str = True,
)
```

| 方法 | 说明 |
| --- | --- |
| `batch(ops)` / `abatch(ops)` | 批量执行 PutOp / SearchOp / GetOp / ListNamespacesOp |
| `_handle_put` | `op.value` 含 `session_id` 和 `content` 时写消息触发后端自动抽取记忆；`op.value=None` 时按 `op.key` 作为 `memory_id` 删除记忆（v0.1.6 起真正删除） |
| `_handle_get` | 以 `op.key` 作为 `memory_id` |
| `_handle_search` | 有 `query` 走语义搜索（带 score）；无 `query` 走 list；支持 namespace 通配与 `memory_type` 过滤 |
| `supports_ttl` | False |

Namespace 是层级路径（如 `("memories", "user-001")`），存于 message meta `store_namespace`。

### 消息转换函数

```python
from agentarts.sdk.integration.langgraph import (
    langgraph_to_memory_message,       # LangGraph → Memory
    memory_to_langgraph_message,       # Memory → LangGraph
    langgraph_messages_to_memory,      # 批量
    memory_messages_to_langgraph,      # 批量
)
```

映射规则：

| LangGraph 消息 | Memory 消息 |
| --- | --- |
| HumanMessage | TextMessage(role="user") |
| AIMessage 无 tool_calls | TextMessage(role="assistant") |
| AIMessage 有 tool_calls | ToolCallMessage(id, name, arguments) |
| SystemMessage | TextMessage(role="system") |
| ToolMessage | ToolResultMessage(tool_call_id, content) |
| FunctionMessage | ToolResultMessage(tool_call_id=name, ...) |

> v0.1.6 起转换器保留 `additional_kwargs` 与 `response_metadata`（写入 message meta），工具调用与模型元信息在 LangGraph ↔ Memory 往返中不再丢失。

## 6. 集成托管工具（Code Interpreter 沙箱）

把 Code Interpreter 作为 LangChain `@tool` 接入，与 LangGraph `ToolNode` 无缝组合：

```python
import json, os
from typing import Annotated, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from agentarts.sdk import AgentArtsRuntimeApp
from agentarts.sdk.tools import code_session

app = AgentArtsRuntimeApp()

@tool
def execute_python_tool(code: str, description: str) -> str | None:
    """Execute Python Code in the sandbox"""
    if description:
        code = f"# {description}\n{code}"
    api_key = os.environ.get("HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY", "")
    with code_session("your_region", "your_code_interpreter_name", api_key=api_key) as code_client:
        response = code_client.invoke(
            operate_type="execute_code",
            api_key=api_key,
            arguments={"code": code, "language": "python", "clear_context": False},
        )
    return json.dumps(response["result"])

llm = ChatOpenAI(model="DeepSeek-V3", api_key=..., base_url=..., max_tokens=1000)
llm = llm.bind_tools([execute_python_tool])

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def call_model(state: AgentState):
    if not state["messages"] or all(not isinstance(m, SystemMessage) for m in state["messages"]):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    else:
        messages = state["messages"]
    return {"messages": [llm.invoke(messages)]}

def should_continue(state):
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and last.tool_calls:
        return "tools"
    return END

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode([execute_python_tool]))
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", "__end__": "__end__"})
workflow.add_edge("tools", "agent")
agent = workflow.compile()

@app.entrypoint
def agent_chat(payload: dict):
    query = payload.get("message", "")
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    return result["messages"][-1].content

if __name__ == "__main__":
    app.run()
```

要点：
- `code_session(region, code_interpreter_name, api_key=...)` 是上下文管理器，自动管理 session
- `code_client.invoke(operate_type="execute_code", arguments={...})` 执行代码
- 沙箱可作为 `@tool` 包装后绑定到任意 LLM

### 6.1 集成 Browser（浏览器沙箱）

同理，把 `browser_session` 包装为 LangChain `@tool`，让 Agent 具备网页操作能力：

```python
from langchain_core.tools import tool
from agentarts.sdk.tools import browser_session

@tool
def browse(url: str, action: str = "page_info") -> str:
    """Open a URL and return page info or a screenshot reference."""
    with browser_session(
        "cn-southwest-2", "my-browser", "langgraph-session",
        allowed_domains=["example.com"],
    ) as browser:
        browser.navigate(url)
        if action == "screenshot":
            return str(browser.screenshot(format="jpeg"))
        return str(browser.get_page_info())
```

要点：
- `browser_session(region, browser_name, session_name, ...)` 自动 start/stop session
- 用 `allowed_domains` 收敛可访问域名；高风险操作配 live view + `take_control`
- 详见 [02-sandbox/browser.md](../02-sandbox/browser.md)

## 7. 直接使用 Memory Service

不依赖 LangGraph 的自研框架，直接用 `MemoryClient` 三件套：

```python
import os
from agentarts.sdk import AgentArtsRuntimeApp
from agentarts.sdk.memory import MemoryClient, SessionCreateRequest, TextMessage

app = AgentArtsRuntimeApp()
memory_client = MemoryClient(api_key=os.getenv("HUAWEICLOUD_SDK_MEMORY_API_KEY"))

@app.entrypoint
def handler(payload: dict):
    message = payload.get("message", "")
    session_id = payload.get("session_id")
    space_id = payload.get("space_id") or os.getenv("AGENTARTS_MEMORY_SPACE_ID")

    # 首次调用：创建会话
    if not session_id:
        session = memory_client.create_memory_session(SessionCreateRequest(space_id=space_id))
        session_id = session.session_id

    # 写入用户消息
    memory_client.add_messages(
        space_id=space_id, session_id=session_id,
        messages=[TextMessage(role="user", content=message)],
    )

    # 取最近 10 条作为上下文
    history = memory_client.get_last_k_messages(space_id=space_id, session_id=session_id, k=10)

    response_text = f"You said: {message}. I remember our conversation!"

    # 写入助手回复
    memory_client.add_messages(
        space_id=space_id, session_id=session_id,
        messages=[TextMessage(role="assistant", content=response_text)],
    )

    history_dicts = [{"role": m.role, "content": m.content} for m in history.messages]
    return {"response": response_text, "session_id": session_id, "history": history_dicts}

if __name__ == "__main__":
    handler.run(host="0.0.0.0", port=8080)
```

模式：无 `session_id` 则新建，有则续接；每次调用先写用户消息、再取历史、再写助手回复。

所需环境变量：`HUAWEICLOUD_SDK_MEMORY_API_KEY`、`HUAWEICLOUD_SDK_REGION`、`AGENTARTS_MEMORY_SPACE_ID`。

## 8. 身份与密钥管理

四种模式，均通过装饰器自动注入，业务代码不接触密钥。

### API Key 模式

```python
from agentarts.sdk import AgentArtsRuntimeContext, IdentityClient, require_api_key
from huaweicloudsdkagentidentity.v1 import AuthorizerType

user_id = f"user-{uuid.uuid4().hex[:8]}"
AgentArtsRuntimeContext.set_user_id(user_id)
client = IdentityClient(region="cn-southwest-301", ignore_ssl_verification=True)

# 注册凭证提供者
provider = client.create_api_key_credential_provider(
    name="my-llm-provider", api_key="sk-dummy-api-key-12345"
)

# 装饰目标函数，SDK 自动注入 api_key
@require_api_key(provider_name="my-llm-provider", ignore_ssl_verification=True)
def call_llm(api_key: str | None = None) -> None:
    print(f"Using API Key: {api_key}")

# 创建 Workload Identity + 获取 token
workload = client.create_workload_identity(name="workload-xxx", authorizer_type=AuthorizerType.NONE)
token = client.create_workload_access_token(workload_name=workload.name, user_id=user_id)

# 注入 token，调用装饰函数
AgentArtsRuntimeContext.set_workload_access_token(token)
call_llm()
```

### OAuth2 USER_FEDERATION 模式

```python
from agentarts.sdk import AgentArtsRuntimeContext, IdentityClient, require_access_token
from agentarts.sdk.identity.types import OAuth2Vendor

client = IdentityClient(region="ap-southeast-4", ignore_ssl_verification=True)

# 创建 OAuth2 凭据提供者（callback_url 需配置到 IdP 后台）
provider = client.create_oauth2_credential_provider(
    name="google-oauth", vendor=OAuth2Vendor.GOOGLEOAUTH2,
    client_id="dummy-client-id", client_secret="dummy-client-secret",
)

# 创建 workload identity，声明允许的回调 URL
workload = client.create_workload_identity(
    name="oauth-workload", authorizer_type=AuthorizerType.NONE,
    allowed_resource_oauth2_return_urls=["http://localhost:8000/callback"],
)
token = client.create_workload_access_token(workload_name=workload.name, user_id=user_id)
AgentArtsRuntimeContext.set_workload_access_token(token)

# 装饰目标函数
@require_access_token(
    provider_name="google-oauth",
    scopes=["https://www.googleapis.com/auth/userinfo.email"],
    auth_flow="USER_FEDERATION",
    on_auth_url=lambda url: print("请授权:", url),
    ignore_ssl_verification=True,
)
async def fetch_protected_data(access_token: str | None = None):
    return {"data": "...", "token": access_token}

# 触发流程（首次调用打印授权 URL，阻塞等待用户授权）
result = await fetch_protected_data()
```

回调服务器需调用 `client.complete_resource_token_auth(session_uri, user_identifier=UserIdentifier(user_id=user_id))` 完成会话绑定。

### STS Token 模式

```python
from agentarts.sdk import AgentArtsRuntimeContext, IdentityClient, require_sts_token
from agentarts.sdk.identity.types import StsCredentials

client = IdentityClient(region="ap-southeast-4", ignore_ssl_verification=True)

# 创建 STS 凭证提供者（agency_urn 来自 IAM 委托）
provider = client.create_sts_credential_provider(name="sts-iam-provider", agency_urn=agency_urn)

workload = client.create_workload_identity(name="sts-workload", authorizer_type=AuthorizerType.NONE)
token = client.create_workload_access_token(workload_name=workload.name, user_id=user_id)

@require_sts_token(
    provider_name="sts-iam-provider",
    agency_session_name="example-session",
    ignore_ssl_verification=True,
)
def access_huawei_resource(sts_credentials: StsCredentials | None = None) -> None:
    if sts_credentials:
        print(f"AK: {sts_credentials.access_key_id[:5]}...")
        print(f"SK: {sts_credentials.secret_access_key[:5]}...")
        print(f"SecurityToken length: {len(sts_credentials.security_token)}")

AgentArtsRuntimeContext.set_workload_access_token(token)
access_huawei_resource()
```

委托的信任策略需包含 `sts:agencies:assume` 和 `sts::SetContext` 两个 Action，`Principal.Service` 含 `service.AgentIdentity`。

### Context 并发隔离

`AgentArtsRuntimeContext` 基于 `contextvars`，asyncio 任务间天然隔离：

```python
import asyncio
from agentarts.sdk import AgentArtsRuntimeContext

AgentArtsRuntimeContext.set_user_id("user-main")

async def isolated_task(task_name: str, new_user_id: str) -> None:
    AgentArtsRuntimeContext.set_user_id(new_user_id)  # 仅当前 task 生效
    await asyncio.sleep(0.5)
    print(f"[{task_name}] final: {AgentArtsRuntimeContext.get_user_id()}")

await asyncio.gather(
    isolated_task("Task A", "user-a"),
    isolated_task("Task B", "user-b"),
)
# 主上下文 user_id 仍是 user-main
```

## 9. 集成决策指南

| 场景 | 推荐方案 |
| --- | --- |
| 已有 LangGraph Agent，需持久化 | `AgentArtsMemorySessionSaver` 作为 checkpointer |
| 已有 LangChain Agent | `@app.entrypoint` 包装 `AgentExecutor.invoke` |
| 已有 Google ADK Agent | `@app.entrypoint` 包装 `Runner.run_async` |
| 自研框架 Agent | `@app.entrypoint` 包装 + 直接用 `MemoryClient` |
| 需要代码执行能力 | 接入 `code_session` 作为 `@tool` |
| 需要网页操作能力 | 接入 `browser_session` 作为 `@tool`，或用 `Browser` 直接调用 |
| 需要外部 API | `GatewayClient` + Target |
| 需要用户级授权 | `require_access_token`（USER_FEDERATION） |
| 需要访问华为云资源 | `require_sts_token` |
| 需要调 LLM | `require_api_key` |

更多接入设计见 [06-integration/partner_agent_adaptation.md](../06-integration/partner_agent_adaptation.md)。
