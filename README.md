# LangGraph + AgentArts Demo

一个基于 **LangGraph** 构建、运行在 **华为云 AgentArts** 上的 Agent 示例，用一个工程把四类云能力串起来：

| 能力 | 在 demo 中的体现 | 代码位置 |
|------|------------------|----------|
| 运行托管 | `AgentArtsRuntimeApp` 把 LangGraph 图暴露为标准 HTTP 服务（`/invocations`、`/ping`、`/ws`） | `demo/app.py` |
| 沙箱工具 | 代码解释器（Code Interpreter）沙箱执行 Python，作为工具暴露给模型 | `demo/sandbox.py`、`demo/tools.py` |
| 记忆 | 会话状态持久化到 Memory Space + 每轮自动语义召回长期记忆 | `demo/memory.py`、`demo/graph.py` |
| Identity | 请求级用户身份（决定记忆归属）+ 从 Agent Identity 动态获取模型凭据 | `demo/identity.py` |

## 架构

```
POST /invocations
      │
      ▼
┌──────────────────────────────────────────────────────────────┐
│ AgentArtsRuntimeApp (demo/app.py)                            │
│   解析请求头 → AgentArtsRuntimeContext（user_id / session_id）│
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ LangGraph (demo/graph.py)                                    │
│                                                              │
│   recall ──▶ agent ──▶ (tool_calls?) ──▶ tools ──▶ agent     │
│     │          │                                 │           │
│     │          │                                 ├─ execute_python → 代码解释器沙箱
│     │          │                                 ├─ recall_memory  → Memory 语义检索
│     │          │                                 └─ whoami         → Identity 上下文
│     │          │                                             │
│     │          └── ChatOpenAI（凭据可来自 Agent Identity）    │
│     │                                                        │
│     └── AgentArtsMemoryStore.search(actor_id=当前用户)        │
│                                                              │
│   checkpointer = AgentArtsMemorySessionSaver(thread_id)      │
└──────────────────────────────────────────────────────────────┘
```

要点：

- **短期记忆**：`AgentArtsMemorySessionSaver` 以 `thread_id` 为会话 ID，把每一轮对话写进 Memory Space；服务重启后同一 `thread_id` 仍可续聊。
- **长期记忆**：Memory Space 内置 4 种抽取策略（`semantic` / `episodic` / `user_preference` / `summary`）在后台自动抽取记忆；`recall` 节点每轮调用 `AgentArtsMemoryStore.search` 做语义检索，把 Top-K 记忆注入系统提示词，模型也可以用 `recall_memory` 工具按需深入检索。
- **多租户隔离**：记忆检索按 `actor_id` 过滤，`actor_id` 来自请求头中的用户身份（见下文 Identity 部分）。

## 目录结构

```
Langgraph-agentarts-demo/
├── pyproject.toml          # uv 工程与依赖（agentarts-sdk 指向本地 ../agentarts-sdk-python）
├── uv.lock                 # 依赖锁定文件
├── requirements.txt        # 容器镜像依赖（agentarts-sdk 走 PyPI，而非本地 editable 路径）
├── Dockerfile              # 由 agentarts config 生成，CMD 为 python -m demo.app
├── .dockerignore           # 构建上下文排除 .venv/.env 等
├── .agentarts_config.yaml  # 部署配置（base / swr_config / runtime.*）
├── .env.example            # 环境变量模板
├── README.md               # 本文档
├── demo/
│   ├── config.py           # 读取 .env，汇总所有配置与能力开关
│   ├── app.py              # 运行托管：AgentArtsRuntimeApp + /invocations 入口
│   ├── graph.py            # LangGraph 图：recall → agent → tools
│   ├── tools.py            # 暴露给模型的工具（沙箱 / 记忆 / identity）
│   ├── sandbox.py          # 代码解释器沙箱能力
│   ├── memory.py           # 记忆能力（checkpointer + store 检索）
│   ├── identity.py         # Identity 能力（用户身份 + 凭据获取）
│   ├── bootstrap.py        # 一次性创建 Memory Space / 工作负载身份
│   └── cli.py              # 本地对话客户端
```

## 环境准备

前置条件：`uv`（>= 0.5）、Python >= 3.10（本工程默认 3.12）、以及一个 OpenAI 兼容的模型服务。

> 依赖中的 `agentarts-sdk` 默认指向同级目录 `../agentarts-sdk-python`（见 `pyproject.toml` 的 `[tool.uv.sources]`）。只想跑起来、不改 SDK 的话，删掉 `[tool.uv.sources]` 并改用 PyPI 上的 `agentarts-sdk` 即可（容器镜像里的 `requirements.txt` 就是这么做的）。

```bash
cd Langgraph-agentarts-demo

# 1. 创建虚拟环境（.venv）并安装依赖
uv venv --python 3.12
uv sync
```

`agentarts-sdk` 通过本地路径依赖 `../agentarts-sdk-python`（editable），修改 SDK 代码后无需重新安装。

## 环境变量

复制模板后按需填写：`cp .env.example .env`（`.env` 已被 `.gitignore` 忽略）。

### 1. 华为云认证（创建/管理云资源时必需）

| 变量 | 必填 | 说明 |
|------|------|------|
| `HUAWEICLOUD_SDK_AK` | 是 | 华为云 Access Key，用于控制面（创建 Memory Space、工作负载身份等） |
| `HUAWEICLOUD_SDK_SK` | 是 | 华为云 Secret Key |
| `HUAWEICLOUD_SDK_REGION` | 否 | 区域，默认 `cn-southwest-2`（也支持 `HUAWEICLOUD_REGION`、`OS_REGION_NAME`） |
| `VERIFY_SSL` | 否 | 是否校验 HTTPS 证书，默认 `true`；内网自签证书环境可设 `false` |

### 2. 模型（必需）

| 变量 | 必填 | 说明 |
|------|------|------|
| `OPENAI_API_KEY` | 是* | 模型 API Key（*配置了 Agent Identity 时可省略，改由云端下发） |
| `OPENAI_BASE_URL` | 否 | OpenAI 兼容端点；华为云 MaaS 官方形式为 `https://api.modelarts-maas.com/v2/chat/completions`（末尾 `/chat/completions` 会被自动去掉，填 `.../v2` 亦可）；留空使用默认端点 |
| `OPENAI_MODEL_NAME` | 否 | 模型名，默认 `deepseek-v3.2`；已实测可用：`glm-5.2` |

### 3. 记忆（Memory）

| 变量 | 必填 | 说明 |
|------|------|------|
| `AGENTARTS_MEMORY_SPACE_ID` | 用记忆时必填 | Memory Space ID，由 `bootstrap memory` 自动写入 |
| `HUAWEICLOUD_SDK_MEMORY_API_KEY` | 用记忆时必填 | 数据面 API Key，由 `bootstrap memory` 自动写入 |
| `AGENTARTS_MEMORY_SPACE_NAME` | 否 | 创建 Space 时的名称，默认 `langgraph-agentarts-demo-space` |

### 4. 沙箱（Code Interpreter）

| 变量 | 必填 | 说明 |
|------|------|------|
| `AGENTARTS_CODE_INTERPRETER_NAME` | 用沙箱时必填 | 代码解释器实例名称（命名规则：小写字母开头、字母/数字/连字符、2–40 字符） |
| `AGENTARTS_CODE_INTERPRETER_AUTH_TYPE` | 否 | 会话认证方式，`API_KEY`（默认）或 `IAM`；`IAM` 用 AK/SK 签名，无需下面的 API Key |
| `HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY` | 认证方式为 `API_KEY` 时必填 | 代码解释器会话鉴权用的 API Key 值（在控制台创建/绑定 API Key 后获得） |
| `AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT` | 用沙箱时必填 | 实例的访问端点（控制台实例详情里的 access endpoint，如 `https://xxx.cn-southwest-2.huaweicloud-agentarts.com`）；SDK 没有内置默认值，缺失时会话请求无法路由 |

### 5. Identity

| 变量 | 必填 | 说明 |
|------|------|------|
| `AGENTARTS_IDENTITY_WORKLOAD_NAME` | 用 Identity 时必填 | 工作负载身份名称，由 `bootstrap identity` 自动写入 |
| `AGENTARTS_IDENTITY_API_KEY_PROVIDER` | 用 Identity 时必填 | API Key 凭据提供商名称，由 `bootstrap identity` 自动写入 |
| `AGENTARTS_IDENTITY_SEED_API_KEY` | 否 | bootstrap 时托管给凭据提供商的密钥，默认取 `OPENAI_API_KEY` |
| `AGENTARTS_IDENTITY_USER_ID` | 否 | 本地调试时的默认用户 ID，默认 `demo-user` |

### 6. Agent 行为与运行时（可选）

| 变量 | 必填 | 说明 |
|------|------|------|
| `AGENTARTS_DEMO_ACTOR_ID` | 否 | 未提供用户身份时的兜底 `actor_id`，默认 `demo-user` |
| `AGENTARTS_DEMO_ASSISTANT_ID` | 否 | 创建记忆会话时使用的 assistant 标识 |
| `AGENTARTS_DEMO_RECALL_ENABLED` | 否 | 是否每轮自动召回长期记忆，默认 `true` |
| `AGENTARTS_DEMO_RECALL_TOP_K` | 否 | 每轮注入的记忆条数，默认 `3` |
| `AGENTARTS_DEMO_HOST` | 否 | 监听地址，默认 `0.0.0.0`（容器端口映射需要；只想本机可访问就改成 `127.0.0.1`，`demo/cli.py` 会自动把通配地址换回 `127.0.0.1`） |
| `AGENTARTS_DEMO_PORT` | 否 | 监听端口，默认 `8080` |
| `AGENTARTS_LOG_LEVEL` | 否 | SDK/应用日志级别，默认 `INFO` |

> 私有化或测试环境还可以使用 SDK 原生端点变量：`AGENTARTS_CONTROL_ENDPOINT`、`AGENTARTS_MEMORY_DATA_ENDPOINT`、`AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT`、`HUAWEICLOUD_SDK_AGENTIDENTITY_ENDPOINT`、`HUAWEICLOUD_SDK_IAM_ENDPOINT`。

## 快速开始

### 第 1 步：检查配置

```bash
uv run python -m demo.bootstrap status
```

输出会展示区域、模型、以及 memory / sandbox / identity 三项能力是否已就绪。

### 第 2 步：创建 Memory Space（一次性）

```bash
uv run python -m demo.bootstrap memory
```

该命令在控制面创建一个 Memory Space（内置 4 种抽取策略），验证数据面可用后，把 `AGENTARTS_MEMORY_SPACE_ID` 与 `HUAWEICLOUD_SDK_MEMORY_API_KEY` 写回 `.env`（API Key 只在创建时返回一次）。

### 第 3 步（可选）：托管模型凭据到 Agent Identity

```bash
uv run python -m demo.bootstrap identity
```

该命令会创建 API Key 凭据提供商（默认托管 `OPENAI_API_KEY` 的值）与工作负载身份，做一次「下发凭据」往返校验，并把名称写回 `.env`。之后 Agent 启动时会通过 `@require_api_key` 从 Agent Identity 获取模型密钥，`OPENAI_API_KEY` 不再需要出现在运行环境中。

### 第 4 步：配置沙箱（可选）

```bash
# 先看看当前区域有哪些代码解释器（会列出名称 / ID / 访问端点）
uv run python -m demo.bootstrap sandbox

# 绑定已有实例（自动读取其认证方式并写回 .env）
uv run python -m demo.bootstrap sandbox --name your-code-interpreter

# 或新建一个：IAM 认证只需要 AK/SK，不涉及 API Key
uv run python -m demo.bootstrap sandbox --name langgraph-demo-sandbox --create --auth-type IAM

# 如坚持用 API_KEY 认证（API Key 需先在控制台创建）
uv run python -m demo.bootstrap sandbox --name langgraph-demo-sandbox --create \
  --auth-type API_KEY --api-key-name your-api-key-name --api-key <key 值>
```

命令会把 `AGENTARTS_CODE_INTERPRETER_NAME`、`AGENTARTS_CODE_INTERPRETER_AUTH_TYPE`、实例的访问端点（`AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT`），以及传入的 `--api-key` 写入 `.env`。若使用 `API_KEY` 认证且没传 `--api-key`，需要手动把控制台里的 Key 值填进 `HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY`。

> 若账号缺少控制面权限（`list_code_interpreters` 报 `Current user is unassigned`），改用控制台手动获取：实例名 + API Key + 访问端点，分别填入上面三个变量。

### 第 5 步：启动 Agent

```bash
uv run python -m demo.app
# Starting LangGraph AgentArts demo on http://127.0.0.1:8080
```

### 第 6 步：调用

```bash
# 健康检查
curl http://127.0.0.1:8080/ping
# {"status":"Healthy","time_of_last_update":...}

# 第一轮：让 Agent 用沙箱算数
curl -X POST http://127.0.0.1:8080/invocations \
  -H 'Content-Type: application/json' \
  -H 'X-HW-AgentGateway-User-Id: alice' \
  -d '{"message": "用沙箱算一下 1 到 100 之间最大的质数"}'

# 第二轮：带同一个 thread_id 续聊（状态从 Memory Space 恢复）
curl -X POST http://127.0.0.1:8080/invocations \
  -H 'Content-Type: application/json' \
  -H 'X-HW-AgentGateway-User-Id: alice' \
  -d '{"message": "我刚才问了什么？", "thread_id": "<上一步返回的 thread_id>"}'
```

或者使用内置的对话客户端：

```bash
uv run python -m demo.cli --user-id alice
# you: 帮我记住我偏好高速路线
# agent: ...
# you: :new     # 开新线程
# you: :quit
```

## 接口协议

### `POST /invocations`

请求体：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `message` | string | 是 | 用户消息（也兼容 `query`） |
| `thread_id` | string | 否 | 会话 ID；不传则使用运行时下发的会话 ID，仍为空则自动生成 |
| `user_id` | string | 否 | 覆盖用户身份，用于记忆归属 |

响应体：

```json
{
  "response": "1 到 100 之间最大的质数是 97。",
  "thread_id": "6f1a...",
  "user_id": "alice",
  "tools_used": ["execute_python"],
  "recalled_memories": ["用户偏好高速路线"]
}
```

### `GET /ping`

返回 `{"status": "Healthy" | "HealthyBusy" | "Unhealthy", "time_of_last_update": <epoch>}`，可直接用于存活/就绪探针。

### 请求头（由 AgentArts 网关注入）

| 请求头 | 作用 |
|--------|------|
| `X-HW-AgentGateway-User-Id` | 终端用户身份 → 记忆归属（`actor_id`） |
| `x-hw-agentarts-session-id` | 会话 ID → 默认 `thread_id` |
| `X-HW-AgentGateway-Workload-Access-Token` | 工作负载访问令牌 → 调用 Agent Identity 换取凭据 |

本地调试时手动带上这些请求头，即可模拟网关行为（`demo/cli.py` 会自动带 `X-HW-AgentGateway-User-Id`）。

## 能力说明

### 运行托管

`demo/app.py` 用 `AgentArtsRuntimeApp` 注册入口函数：入参签名带 `context: RequestContext` 时，运行时会注入请求上下文（会话 ID、请求 ID），并自动把请求头解析进 `AgentArtsRuntimeContext`。返回 `dict` 即普通 JSON 响应，返回生成器则自动变成 SSE 流式响应。

### 沙箱工具

`demo/sandbox.py` 每次调用都通过 `code_session(...)` 开启一个新的代码解释器会话并在结束时销毁，代码不会在 Agent 进程内执行。

- 认证方式由 `AGENTARTS_CODE_INTERPRETER_AUTH_TYPE` 决定：`API_KEY` 用 API Key 鉴权；`IAM` 用 AK/SK 签名（V11 HMAC-SHA256），两者都只影响会话层，控制面创建实例仍用 AK/SK。
- `API_KEY` 模式要求 `AGENTARTS_CODE_INTERPRETER_NAME` + `HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY`；`IAM` 模式只要求实例名称。
- 会话请求还需要 `AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT`（SDK 无默认值）；三项齐全时 `sandbox.status()` 的 `ready` 才为 `true`。
- 未配置沙箱时该工具不会暴露给模型（避免模型调用一个注定失败的工具）。

### 记忆

- 会话状态：`AgentArtsMemorySessionSaver(space_id=..., api_key=...)` 作为 `compile(checkpointer=...)` 的检查点存储。
- 长期召回：`recall` 节点用最近一条用户消息做语义检索，结果写入状态字段 `recalled`，由 `agent` 节点拼接进系统提示词（不会污染持久化的对话历史）。
- 未配置 Memory Space 时自动退化为进程内 `InMemorySaver`，图逻辑不变，便于离线调试。

### Identity

- **用户身份**：`identity.resolve_actor_id()` 的优先级为「请求体 `user_id` → 运行时请求头 → `AGENTARTS_IDENTITY_USER_ID` → `AGENTARTS_DEMO_ACTOR_ID`」。同一个 Agent 被不同用户调用时，记忆天然隔离。
- **凭据身份**：配置了工作负载身份 + 凭据提供商后，`identity.model_api_key()` 会用 `@require_api_key` 装饰器从 Agent Identity 取回模型密钥；已部署时令牌来自请求头，本地调试时由 `ensure_workload_access_token()` 现场换取。
- **可观测性**：模型可以调用 `whoami` 工具（或查看 `/invocations` 响应中的 `user_id`）确认当前生效的身份。

## 离线/降级运行

没有云资源的也能把服务和图跑起来，各能力会按配置情况自动降级：

| 未配置项 | 行为 |
|----------|------|
| Memory Space | 检查点退回进程内存储；不自动召回；不暴露 `recall_memory` 工具 |
| 代码解释器 | 不暴露 `execute_python` 工具 |
| Agent Identity | 使用 `.env` 中的 `OPENAI_API_KEY` |
| 用户身份请求头 | 使用 `AGENTARTS_DEMO_ACTOR_ID`（默认 `demo-user`） |

## 创建云上运行时环境（部署到 AgentArts）

前面几步都是在本地跑（`demo/app.py` 直接起 ASGI 服务）。要变成云上运行时，AgentArts 提供了三种创建方式，另外有两个"本地等价"命令可先用来自检镜像。
以下命令统一省略 `uv run` 前缀；本 demo 里请写成 `uv run agentarts ...`，或先 `source .venv/bin/activate` 后直接 `agentarts ...`。

### 三种创建方式

| 方式 | 命令 | 适用场景 | 约束 |
|------|------|----------|------|
| CLI 一键部署 | `agentarts deploy`（别名 `agentarts launch`） | 常规发布 | 需要 Docker 在运行 + `Dockerfile` + SWR 权限 |
| 复用已有镜像 | `agentarts deploy --skip-build` | CI/CD、镜像已发布、外部镜像仓库 | 必须在配置里设 `runtime.artifact_source.url`，且仅 `cloud` 模式可用 |
| 控制面 API | `RuntimeClient(...).create_or_update_agent(...)` | 脚本化、批量、平台集成 | 需自备控制面 endpoint 与鉴权 |

`agentarts deploy` 的执行顺序是：校验 `.agentarts_config.yaml` → 构建 Docker 镜像 → 推送 SWR → 调控制面创建/更新运行时 → 校验状态并输出访问端点。同名再次部署即更新（首次为新建）。

```bash
agentarts deploy                                   # 默认 --mode cloud
agentarts deploy -a demo-agent -t v1.0.0 -d "LangGraph + AgentArts demo"
agentarts deploy --swr-org my-org --swr-repo my-repo
agentarts deploy --skip-build                      # 用配置里的镜像 URL 直接创建运行时
```

SDK 直连控制面（CLI 内部走的就是这条路径）：

```python
from agentarts.sdk.service.runtime_client import RuntimeClient
from agentarts.sdk.utils.constant import get_control_plane_endpoint

client = RuntimeClient(control_endpoint=get_control_plane_endpoint("cn-southwest-2"))
client.create_or_update_agent(
    agent_name="demo-agent",
    description="LangGraph + AgentArts demo",
    artifact_source_config={
        "url": "swr.cn-southwest-2.myhuaweicloud.com/org/repo:latest",
        "commands": [],
    },
    invoke_config={"protocol": "HTTP", "port": 8080},
    network_config={"network_mode": "PUBLIC"},
    identity_configuration={"authorizer_type": "IAM"},
    env_vars=[{"key": "OPENAI_API_KEY", "value": "..."}],
)
```

### 上线前自检：两个本地等价命令

| 命令 | 作用 |
|------|------|
| `agentarts deploy --mode local [-l 端口]` | 本地构建镜像并起容器，验证镜像本身没问题（不占云资源）。注意 CLI 用的是**同端口映射**（`-p 8090:8090`），`-l` 必须等于 `runtime.invoke_config.port`（本 demo 为 8080），否则容器起来了但端口不通 |
| `agentarts dev [--reload] [-p 端口] [-e KEY=VALUE]` | 本机开发服务器（`/invocations`、`/ping`），等价于现在的 `python -m demo.app` |

> 容器里必须监听 `0.0.0.0`，否则端口映射访问不到。本 demo 已把 `AGENTARTS_DEMO_HOST` 默认值设为 `0.0.0.0`（`demo/cli.py` 会自动把通配地址换回 `127.0.0.1`）。

> `--mode local` 只负责"构建镜像 + 起容器"，**不会注入环境变量**（`run_container` 不支持 `-e`）。要在本地容器里跑真实能力，起容器时自己带上：
> ```bash
> agentarts deploy --mode local                      # 首次：构建镜像并起容器
> docker rm -f demo-agent
> docker run -d --name demo-agent --env-file .env -p 8080:8080 demo-agent:latest
> ```
> 云上模式没有这个问题：`runtime.environment_variables`（`agentarts config set-env`）会由平台注入容器。

### 本目录已生成的部署文件

| 文件 | 说明 |
|------|------|
| `requirements.txt` | 镜像依赖：`agentarts-sdk`（PyPI）+ langgraph/langchain-openai/httpx/python-dotenv |
| `.dockerignore` | 排除 `.venv`、`.env`、`__pycache__` 等，避免把本地虚拟环境打进镜像 |
| `.agentarts_config.yaml` | `agentarts config` 生成，入口 `demo.app:app`、区域 `cn-southwest-2`、SWR org/repo、`runtime.*` |
| `Dockerfile` | 生成自模板：`FROM python:3.12-slim` → 建非 root 用户 → 装 `requirements.txt` → `CMD ["python", "-m", "demo.app"]` |

> `.agentarts_config.yaml` 会被 `config set-env` 写入明文密钥，因此已加入 `.gitignore`，请勿提交。

### 前置条件

- 本地 Docker 已启动（`deploy` 会检查 Docker 与 `Dockerfile`；`--skip-build` 时跳过）
- `.agentarts_config.yaml` 已生成
- 已配置 `HUAWEICLOUD_SDK_AK` / `HUAWEICLOUD_SDK_SK` / `HUAWEICLOUD_SDK_REGION`
- SWR 可用：首次会自动创建组织与仓库（`--swr-org` / `--swr-repo` 可覆盖）
- 控制面权限：账号需被授予 AgentArts 运行时相关权限，否则会报 `Current user is unassigned, access denied`

### 把本 demo 迁到云上要改的四处

1. **配置文件**：`agentarts config` 会生成 `.agentarts_config.yaml` 和 `Dockerfile`（也可 `agentarts init -t langgraph` 生成同构文件后拷进来）
2. **entrypoint**：填 `demo.app:app`。生成的 Dockerfile 实际执行 `python -m <module>`，本 demo 的 `demo/app.py` 已带 `__main__` 入口，所以模块名 `demo.app` 即可
3. **依赖文件**：镜像构建读 `base.dependency_file`（`requirements.txt`）。本 demo 开发期用 uv/`pyproject.toml`，上云前需导出一份，至少包含 `agentarts-sdk`、`langgraph>=1.0.0`、`langchain-core>=0.1.0`、`langchain-openai>=0.1.0`、`httpx`、`python-dotenv`
4. **环境变量**：云上不读 `.env`，要写进配置（`bootstrap` 回填 `.env` 的那些值在这里改成配置项）

```bash
agentarts config set base.region cn-southwest-2
agentarts config set base.entrypoint demo.app:app
agentarts config set base.dependency_file requirements.txt

agentarts config set-env OPENAI_API_KEY <你的 key>
agentarts config set-env OPENAI_BASE_URL https://api.modelarts-maas.com/v2/chat/completions
agentarts config set-env OPENAI_MODEL_NAME glm-5.2
agentarts config set-env HUAWEICLOUD_SDK_AK <ak>
agentarts config set-env HUAWEICLOUD_SDK_SK <sk>
agentarts config set-env HUAWEICLOUD_SDK_REGION cn-southwest-2

agentarts config set-env AGENTARTS_CODE_INTERPRETER_NAME codeinterpreter-dzh
agentarts config set-env HUAWEICLOUD_SDK_CODE_INTERPRETER_API_KEY <沙箱 API Key>
agentarts config set-env AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT <沙箱访问端点>

agentarts config list-env        # 回看已配置的变量
agentarts deploy                 # 部署
```

> Memory / Identity 权限开通后，同理补 `AGENTARTS_MEMORY_SPACE_ID`、`HUAWEICLOUD_SDK_MEMORY_API_KEY`、`AGENTARTS_IDENTITY_*`。

### 创建运行时能配什么

`.agentarts_config.yaml` 的 `runtime.*` 决定云上运行时的形态：

| 配置项 | 说明 |
|--------|------|
| `runtime.invoke_config` | `protocol`（`HTTP`）、`port`（默认 8080）、`file_transfer_config.enabled`（文件传输开关）、`url_match_type` |
| `runtime.network_config` | `network_mode`：`PUBLIC`（公网）/ `VPC`（需填 `vpc_id`、`subnet_id`、`security_group_id`） |
| `runtime.identity_configuration` | `authorizer_type`：`IAM` / `custom_jwt`（`discovery_url`、`allowed_audience`、`allowed_clients`、`allowed_scopes`）/ `key_auth`（`api_keys`） |
| `runtime.artifact_source` | `url`（镜像地址）、`commands`（容器启动命令）、`swr_instance_id` |
| `runtime.environment_variables` | 注入容器的环境变量 |
| `runtime.storage_config` | `sfs_turbo`（`sfs_turbo_id` / `sfs_path` / `mount_path` / `read_only`）、`session_storage.mount_path` |
| `runtime.observability` | `tracing` / `metrics` / `logs` 开关 |
| `runtime.arch` | CPU 架构：`x86_64` / `arm64` |
| `runtime.execution_agency_name` | 委托（agency），让运行时能访问其他云服务 |
| `runtime.agent_gateway_id` | 绑定的出站网关 |
| `runtime.tags` | 资源标签 |

### 部署后怎么用

```bash
# 调用（默认 cloud 模式）
agentarts invoke '{"message": "你好"}'
agentarts invoke '{"message": "用沙箱算 1 到 100 之间最大的质数"}' -u alice

# 数据面操作（仅云上，面向已部署 Agent）
agentarts runtime start-session -a demo-agent                       # 拿 session_id
agentarts runtime invoke '{"message": "hi"}' -a demo-agent -s <session-id>
agentarts runtime exec-command "ls -la" -a demo-agent -s <session-id>
agentarts runtime upload-files -a demo-agent -s <session-id> -f data.csv   # 需 file_transfer_config.enabled=true
agentarts runtime download-files -a demo-agent -s <session-id> -p /tmp/out.log -o ./out.log
agentarts runtime stop-session -a demo-agent -s <session-id>

# 释放
agentarts destroy -a demo-agent
```

> 云上运行时调用沙箱/记忆等数据面服务走的是运行时的网络出口，若用 `VPC` 模式，请确认能通到对应的 `*.huaweicloud-agentarts.com` 端点。

## 常见问题

- **`/invocations` 返回 500 `RuntimeError: No model credential available`**：未设置 `OPENAI_API_KEY`，也未配置 Agent Identity。
- **日志出现 `Could not load existing config`/`warning: Provider might already exist`**：`bootstrap identity` 重复执行时会命中已存在的资源，属正常现象；如需重建请先在控制台清理或改用新的名称。
- **记忆召回为空**：长期记忆由 Memory 服务在后台异步抽取，刚聊完的几轮可能需要等待（本 demo 的 Space 设置为空闲 30 秒触发抽取）；同时确认检索用的 `actor_id` 与写入时一致。
- **本地访问被代理拦截**：若系统配置了 `ALL_PROXY`/`HTTP_PROXY`，`demo.cli` 会对 localhost 自动绕过代理；使用 `curl` 时可加 `--noproxy '*'`。
- **想抓代码解释器的异常却抓不到**：SDK 的 `ToolsAPIError` 继承自 `BaseException` 而非 `Exception`，`except Exception` 不会命中它；本 demo 在 `demo/sandbox.py`、`demo/bootstrap.py` 中显式捕获了该异常。
- **`.env` 被写坏/写空**：`bootstrap` 每次写回前会把原文件备份成 `.env.bak`（已在 `.gitignore` 中忽略），可直接改名恢复。
- **沙箱调用报权限/鉴权错误**：确认 `AGENTARTS_CODE_INTERPRETER_NAME`、API Key（`API_KEY` 认证时）与 `HUAWEICLOUD_SDK_REGION` 属于同一区域；若实例是 IAM 认证创建的，请把 `AGENTARTS_CODE_INTERPRETER_AUTH_TYPE` 设为 `IAM`，否则会因缺少 API Key 而失败。
- **沙箱报 `Invalid URL ... No scheme supplied`**：缺少 `AGENTARTS_CODEINTERPRETER_DATA_ENDPOINT`，把实例的 access endpoint 填上即可（`bootstrap sandbox` 会自动写入）。
- **`agentarts deploy` 报 `Docker is not available` / `Dockerfile not found`**：先启动 Docker Desktop，并确认当前目录有 `Dockerfile`（`agentarts config` 会生成）；只想验代码可先用 `agentarts dev`，不想本地构建可改用 `--skip-build`。
- **`agentarts deploy --skip-build` 报 `No artifact URL found in configuration file`**：`--skip-build` 只认配置里的镜像地址，请在 `.agentarts_config.yaml` 补 `runtime.artifact_source.url`。
- **部署时报 `Current user is unassigned, access denied` / 各类 403**：账号尚未被授予 AgentArts 控制面权限（与沙箱控制面、Memory、Identity 的 403 同源），需先在控制台开通后再部署。
- **`agentarts deploy --mode local` 后 `localhost:<端口>/ping` 无响应**：CLI 用的是同端口映射（`-p N:N`），`-l` 必须等于 `runtime.invoke_config.port`（本 demo 为 8080）；另外容器内必须监听 `0.0.0.0`。
- **本地容器里 `/invocations` 报 `No model credential available`**：`--mode local` 不注入环境变量，用 `docker run --env-file .env ...` 起容器（见"上线前自检"一节）。
