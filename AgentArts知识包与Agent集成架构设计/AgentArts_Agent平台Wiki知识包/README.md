# AgentArts Agent 平台 Wiki 知识包

## 目标

将 AgentArts 高代码开发与智能体运营运维能力整理为适合 Agent 检索和推理的知识包。
内容锚点：`agentarts-sdk-python`（v0.1.6，Python 3.10+，包名 `agentarts-sdk`）。

素材来源：SDK 仓库 `docs/cn/sdk_user_guide/` 6 份中文官方文档 + `src/` 源码 + `examples/`（含 `navigation_langgraph_memory/` 导航智能体示例）+ `docs/cn/toolkit_user_guide/` 8 份 CLI 文档 + `src/agentarts/toolkit/plugins/memory/` 记忆插件与 MCP Server；《高代码开发》用于高代码与控制台配置，《智能体运营运维》用于观测、评估和优化闭环。

## 知识组织

| 分区 | 文档 | 内容 |
| --- | --- | --- |
| 00-overview | [platform_architecture.md](00-overview/platform_architecture.md) | 平台定位、架构分层、能力对照表、控制面/数据面分离 |
| 01-runtime | [runtime.md](01-runtime/runtime.md) | AgentArtsRuntimeApp、装饰器、上下文、端点、Long Loop |
| 02-sandbox | [sandbox.md](02-sandbox/sandbox.md) | CodeInterpreter、code_session、代码/命令/文件操作 |
| 02-sandbox | [browser.md](02-sandbox/browser.md) | Browser、browser_session、页面自动化、Profile、人机接管 |
| 03-memory | [memory.md](03-memory/memory.md) | MemoryClient、Space/Session/Memory、策略分类、语义检索 |
| 03-memory | [memory_plugin.md](03-memory/memory_plugin.md) | 记忆插件安装、Claude/Codex/OpenCode/Hermes 接入、MCP Server |
| 04-gateway | [gateway.md](04-gateway/gateway.md) | GatewayClient、MCP 网关、Target、Skill 四元组 |
| 05-identity | [identity.md](05-identity/identity.md) | require_* 装饰器、OAuth2/APIKey/STS 三流、安全闭环 |
| 06-integration | [partner_agent_adaptation.md](06-integration/partner_agent_adaptation.md) | 伙伴 Agent 接入模型、LangGraph 适配器、接入决策树 |
| 07-operation | [field_validation.md](07-operation/field_validation.md) | 实验局验收、技术/业务指标、验收检查清单 |
| 07-operation | [observability.md](07-operation/observability.md) | Trace/Span、业务/运营指标、会话、日志、OTel 接入、标注与回流 |
| 07-operation | [evaluation.md](07-operation/evaluation.md) | 在线/离线评估、评测集、评估器、评估任务、报告与校准 |
| 07-operation | [optimization.md](07-operation/optimization.md) | BadCase 归因、Prompt/Model/RAG/Tool 优化、对比评估与回归门禁 |
| 08-code-dev | [scaffolding.md](08-code-dev/scaffolding.md) | 项目脚手架、四种模板、配置文件、Dockerfile 生成 |
| 08-code-dev | [cli_reference.md](08-code-dev/cli_reference.md) | 全 CLI 命令参考（init/dev/launch/invoke/runtime/gateway/memory/install） |
| 08-code-dev | [deployment.md](08-code-dev/deployment.md) | 部署流程、destroy、远程运维、文件传输、CI/CD |
| 08-code-dev | [framework_integration.md](08-code-dev/framework_integration.md) | LangChain/LangGraph/GoogleADK 集成、Memory/Identity 用法 |

## SDK 模块速查

| 模块 | 路径 | 关键类 |
| --- | --- | --- |
| runtime | sdk.runtime | AgentArtsRuntimeApp, RequestContext, PingStatus |
| memory | sdk.memory | MemoryClient, AsyncMemoryClient, MemorySession |
| tools | sdk.tools.code_interpreter | CodeInterpreter, code_session |
| tools | sdk.tools.browser | Browser, browser_session |
| plugins | toolkit.plugins.memory | AgentArtsMemoryClient、MCP Server、Claude/Codex/OpenCode/Hermes 适配 |
| gateway | sdk.gateway | GatewayClient |
| identity | sdk.identity + sdk.service.identity | IdentityClient, require_access_token/api_key/sts_token |
| integration | sdk.integration.langgraph | AgentArtsMemorySessionSaver, AgentArtsMemoryStore |
| service | sdk.service | RuntimeClient, IAMClient, SWRClient, MemoryHttpService |

CLI 入口：`agentarts`（init/config/dev/launch/invoke/runtime/destroy/gateway/memory）。其中 `agentarts memory` 既管理 Memory Space，也负责把记忆插件安装进 AI 编程助手（`memory install/uninstall`）。详见 [08-code-dev/cli_reference.md](08-code-dev/cli_reference.md)。

## 核心架构概念

- **职责边界**：模型负责理解/推理/规划；Runtime 负责执行/状态/权限/重试/审计
- **控制面/数据面分离**：控制面（资源 CRUD，AK/SK）与数据面（数据读写，API Key 或 IAM 签名）贯穿 Memory/Sandbox/Gateway
- **Adapter Layer**：伙伴 Agent 通过适配层接入平台，而非直接绑定接口
- **Skill 四元组**：Knowledge + Policy + Executor + Verifier，封装外部能力为企业级 Skill
- **双内置工具**：Code Interpreter（沙箱代码执行）+ Browser（浏览器自动化），都遵循控制面/数据面分离与 session 隔离

## Agent 读取原则

不要将文档作为普通说明书读取，而应作为 **Platform Capability Knowledge Base**，用于回答：

1. 平台有什么能力？→ [00-overview](00-overview/platform_architecture.md) 能力对照表 + 各专章
2. 如何接入已有 Agent？→ [06-integration](06-integration/partner_agent_adaptation.md) + [08-code-dev/framework_integration.md](08-code-dev/framework_integration.md)
3. 哪些能力由模型负责，哪些由 Runtime 负责？→ [00-overview](00-overview/platform_architecture.md) 第 5 节
4. 如何完成企业级上线？→ [08-code-dev/deployment.md](08-code-dev/deployment.md) + [07-operation/field_validation.md](07-operation/field_validation.md)
5. 如何完成“观测 -> 评估 -> 优化 -> 回归”闭环？→ [observability.md](07-operation/observability.md) + [evaluation.md](07-operation/evaluation.md) + [optimization.md](07-operation/optimization.md)
6. 如何让 Agent 操作网页，或给 AI 编程助手挂载长期记忆？→ [02-sandbox/browser.md](02-sandbox/browser.md) + [03-memory/memory_plugin.md](03-memory/memory_plugin.md)

## 相关材料

- 联合开发实施包：`../AgentArts_Partner_Agent联合开发实施包_Phase0-3/`（Phase 0-3 + 8 周计划 + RACI）
- SDK 仓库：`../agentarts-sdk-python/`（源码 + examples + 官方文档）
- 高代码开发 PDF：`../AgentArts原始材料/智果（AgentArts）智能体平台 高代码开发.pdf`（254 页，与 SDK 文档同源）
- 智能体运营运维 PDF：`../AgentArts原始材料/智果（AgentArts）智能体平台 智能体运营运维.pdf`（270 页，观测、评估和优化闭环的主来源）
