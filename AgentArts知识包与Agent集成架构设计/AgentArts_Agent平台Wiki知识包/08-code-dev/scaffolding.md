# 项目脚手架与模板

> `agentarts init` 命令生成项目骨架，`agentarts config` 生成配置与 Dockerfile。本篇覆盖项目结构、模板系统、配置文件。

## 1. init：创建项目

```bash
agentarts init
```

交互式提示输入项目名、模板、路径、区域。或全参数：

```bash
agentarts init \
  --name my-agent \
  --template langgraph \
  --path . \
  --region cn-southwest-2 \
  --swr-org my-org \
  --swr-repo agent_my_agent
```

| 参数 | 简写 | 默认 | 说明 |
| --- | --- | --- | --- |
| `--name` | `-n` | 交互式提示 | 项目名（自动转小写） |
| `--template` | `-t` | 交互式选择 | `basic` / `langgraph` / `langchain` / `google-adk` |
| `--path` | `-p` | `.` | 项目创建路径 |
| `--region` | `-r` | 交互式（默认 `cn-southwest-2`） | 华为云区域 |
| `--swr-org` | — | 自动生成 | SWR 组织 |
| `--swr-repo` | — | `agent_{name}` | SWR 仓库 |

## 2. 四种模板

`init` 对每个模板生成 4 个文件：`agent.py`、`requirements.txt`、`.agentarts_config.yaml`、`Dockerfile`。

| 模板 | 用途 | agent.py 生成内容 | 注入的环境变量 |
| --- | --- | --- | --- |
| `basic` | 最小骨架，无 LLM 依赖 | `AgentArtsRuntimeApp` + 同步 `handler`，返回 `{"response": ..., "agent": name}` | 无 |
| `langgraph` | LangGraph 状态工作流 | `State(TypedDict)` + `LangGraphAgent` 类，`_build_graph()` 用 `StateGraph`，异步 handler；懒加载 `ChatOpenAI` | `OPENAI_API_KEY`、`OPENAI_MODEL_NAME`（默认 `gpt-4o-mini`）、`OPENAI_BASE_URL` |
| `langchain` | LangChain 工具集成 | `LangChainAgent` 类，`_get_llm()` 懒加载，支持 `system_prompt` | 同 langgraph |
| `google-adk` | Google ADK / Gemini | `GoogleADKAgent` 类，用 `google.adk.agents.Agent` + `Runner` + `InMemorySessionService`；模块加载时校验 `GOOGLE_API_KEY` | `GOOGLE_API_KEY`、`GOOGLE_MODEL_NAME`（默认 `gemini-2.0-flash`） |

各模板的 `requirements.txt`：

| 模板 | 依赖 |
| --- | --- |
| `basic` | `agentarts-sdk` |
| `langgraph` | `agentarts-sdk`、`langgraph>=1.0.0`、`langchain>=0.1.0`、`langchain-openai>=0.1.0`、`langchain-core>=0.1.0` |
| `langchain` | `agentarts-sdk`、`langchain>=0.1.0`、`langchain-openai>=0.1.0`、`langchain-core>=0.1.0` |
| `google-adk` | `agentarts-sdk`、`google-adk>=0.1.0`、`google-genai>=0.3.0` |

## 3. 生成的项目结构

以 `langgraph` 模板为例：

```
my-agent/
├── agent.py                    # Agent 入口（含 @app.entrypoint）
├── requirements.txt            # 依赖
├── .agentarts_config.yaml      # AgentArts 配置
└── Dockerfile                  # 部署镜像
```

### agent.py（langgraph 模板核心结构）

```python
import os
from typing import Dict, Any, TypedDict, Annotated
from operator import add

from agentarts.sdk import AgentArtsRuntimeApp, RequestContext

app = AgentArtsRuntimeApp()

class State(TypedDict):
    messages: Annotated[list, add]
    query: str
    response: str

class LangGraphAgent:
    def __init__(self):
        self.model_name = os.environ.get("OPENAI_MODEL_NAME", "gpt-4o-mini")
        self._graph = None

    def _build_graph(self):
        from langgraph.graph import StateGraph, END
        from langchain_openai import ChatOpenAI
        # ... 构建图
        return workflow.compile()

    async def run(self, query: str, session_id: str = None) -> Dict[str, Any]:
        graph = self._graph or self._build_graph()
        self._graph = graph
        result = await graph.ainvoke({"messages": [], "query": query, "response": ""})
        return {"response": result.get("response", "")}

_agent = LangGraphAgent()

@app.entrypoint
async def handler(payload: Dict[str, Any], context: RequestContext = None) -> Dict[str, Any]:
    query = payload.get("message", "")
    return await _agent.run(query)

if __name__ == "__main__":
    app.run()
```

## 4. .agentarts_config.yaml 结构

`init` 生成的配置文件固定结构：

```yaml
default_agent: my-agent
agents:
  my-agent:
    base:
      name: my-agent
      entrypoint: agent:app          # 固定
      region: cn-southwest-2
      dependency_file: requirements.txt
      platform: linux/arm64          # 自动检测
      language: python
      base_image: python:3.10-slim
    swr_config:
      organization: auto-generated
      repository: agent_my_agent
      organization_auto_create: true
      repository_auto_create: true
    runtime:
      arch: arm64
      invoke_config:
        file_transfer_config:
          enabled: false
        url_match_type: ACCURATE_MATCH
      network_config:
        network_mode: PUBLIC
      identity_configuration:
        authorizer_type: IAM
      observability:
        tracing:
          enabled: false
        metrics:
          enabled: false
        logs:
          enabled: false
      storage_config:
        sfs_turbo:
          sfs_turbo_id: null
          sfs_path: null
          mount_path: null      # 使用 SFS Turbo 时必填
          read_only: false
        session_storage:
          mount_path: null      # 容器内 session 存储挂载路径
      environment_variables:
        OPENAI_API_KEY: ""
        OPENAI_MODEL_NAME: gpt-4o-mini
        OPENAI_BASE_URL: ""
      tags: []
```

## 5. Dockerfile 生成

由 `toolkit/utils/templates/docker/Dockerfile.j2` + `render_dockerfile()` 渲染，占位符：

| 占位符 | 默认 | 说明 |
| --- | --- | --- |
| `{base_image}` | `python:3.10-slim` | 基础镜像 |
| `{env_section}` | — | 环境变量注入 |
| `{user_section}` | — | 用户权限设置 |
| `{dependency_section}` | — | 依赖安装 |
| `{port}` | 8080 | 暴露端口 |
| `{cmd_section}` | — | 启动命令 |

可用 `PYTHON_BASE_IMAGE` 环境变量覆盖默认基础镜像：`export PYTHON_BASE_IMAGE="python:3.11-slim"`。

## 6. config：配置管理

`agentarts config` 子组管理 Agent 配置：

| 子命令 | 说明 |
| --- | --- |
| `config`（无子命令） | 交互式创建/更新 agent 配置，自动生成 Dockerfile |
| `config list` | 列出所有已配置 agent |
| `config set-default <name>` | 设置默认 agent |
| `config get [key]` | 获取配置值或完整详情 |
| `config set <key> <value>` | 设置配置值（`base.name` 自动转小写并校验） |
| `config remove <name>` | 删除 agent 配置 |
| `config set-env <key> <value>` | 设置环境变量 |
| `config remove-env <key>` | 删除环境变量 |
| `config list-env` | 列出环境变量 |

配置键用点分隔路径：

| 路径前缀 | 说明 |
| --- | --- |
| `base.*` | name / entrypoint / region / dependency_file / platform / language / base_image |
| `swr_config.*` | organization / repository / organization_auto_create / repository_auto_create |
| `runtime.*` | invoke_config.protocol/port、identity_configuration.authorizer_type、storage_config.session_storage.mount_path 等 |

### 手动配置 artifact_source.url

预构建镜像场景，跳过构建直接用外部镜像：

```bash
agentarts config set runtime.artifact_source.url "swr.cn-southwest-2.myhuaweicloud.com/my-org/my-repo:v1.0"
```

## 7. 后续步骤

`init` 完成后的标准流程：

```bash
cd my-agent
pip install -r requirements.txt       # 安装依赖
# 编辑 agent.py，实现业务逻辑
agentarts config                      # 生成/更新配置和 Dockerfile
agentarts dev                         # 本地开发调试
agentarts launch --mode cloud         # 云端部署
```
