# AgentArts Agent 平台 Wiki 知识包

## 目标

将 AgentArts 平台能力整理为适合 Agent 检索和推理的知识包。

**SDK 锚点**：`agentarts-sdk-python`（**v0.1.6**，Python ≥ 3.10，包名 `agentarts-sdk`，**仅支持 `cn-southwest-2`**）。

## 官方材料基线（重要）

| 版本 | 位置 | 说明 |
| --- | --- | --- |
| **最新** | `AgentArts原始材料-0916/`（2026-09-14 ~ 2026-09-16，12 分册 / 4,864 页） | **本知识包的全部事实来源** |
| 旧版 | `AgentArts原始材料-0804/`（文档版本 02，2026-08-04） | 仅作历史对照，**不可再作为事实依据** |

0916 相对 0804 是**结构性变化**（文档体系重排 + 新增能力域），不是补充修订。完整差异清单与影响范围见 **[00-overview/release_delta_0916.md](00-overview/release_delta_0916.md)**。**引用 0804 结论前必须先查该清单。**

素材来源：0916 官方 12 分册（托管与运行智能体 / Managed Agents / 观测与优化智能体 / 资源与成员管理 / API 参考 2,385 页 / 低代码开发智能体 / 最佳实践 / 产品介绍 / 开始使用 / 常见问题 / 计费说明 / SDK 参考）+ SDK 仓库 `src/` 源码 + `docs/cn/` 中文文档。

## 知识组织

| 分区 | 文档 | 内容 |
| --- | --- | --- |
| 00-overview | [release_delta_0916.md](00-overview/release_delta_0916.md) | **0804 → 0916 版本差异基线**：分册映射、新增能力、术语变更、限额、影响清单 |
| 00-overview | [platform_architecture.md](00-overview/platform_architecture.md) | 平台定位、三种开发范式、架构分层、能力对照表、控制面/数据面分离、IAM 委托、入站身份认证 |
| 00-overview | [managed_agents.md](00-overview/managed_agents.md) | **Managed Agents**：环境/智能体/Skill/会话、出网网络、存储三选、内置工具、WebSocket 调用 |
| 09-knowledge-base | [knowledge_base.md](09-knowledge-base/knowledge_base.md) | **知识库**：平台知识库、第三方（General/KooSearch/RAGFlow）、格式与限额、RAG 检索 |
| 01-runtime | [runtime.md](01-runtime/runtime.md) | **平台侧托管运行时**（入站 HTTP+MCP、microVM、委托、入站认证、会话、存储、访问方式与灰度）+ AgentArtsRuntimeApp、装饰器、上下文、端点、Long Loop |
| 02-sandbox | [sandbox.md](02-sandbox/sandbox.md) | CodeInterpreter、code_session、代码/命令/文件操作 |
| 02-sandbox | [browser.md](02-sandbox/browser.md) | Browser、browser_session、页面自动化、Profile、**浏览器代理**、LiveView、人机接管 |
| 03-memory | [memory.md](03-memory/memory.md) | **分层记忆架构**（短期/长期）、**5 内置策略 + 自定义策略**、生成与检索链路、隔离与访问控制、MemoryClient、语义检索 |
| 03-memory | [memory_plugin.md](03-memory/memory_plugin.md) | 记忆插件安装、Claude/Codex/OpenCode/Hermes 接入、MCP Server |
| 04-gateway | [gateway.md](04-gateway/gateway.md) | GatewayClient、MCP 网关、**Target 四类型（REST API/MCP/APIG/云服务）**、**入站认证 + 出站身份**、工具发现游标、语义检索、Skill 四元组 |
| 05-identity | [identity.md](05-identity/identity.md) | **入站三认证**、**IAM 委托（部署委托 + 身份委托）**、平台侧权限、require_* 装饰器、OAuth2/APIKey/STS 三流、安全闭环 |
| 06-integration | [partner_agent_adaptation.md](06-integration/partner_agent_adaptation.md) | 伙伴 Agent 接入模型、LangGraph 适配器、接入决策树 |
| 07-operation | [field_validation.md](07-operation/field_validation.md) | 实验局验收、技术/业务指标、验收检查清单 |
| 07-operation | [observability.md](07-operation/observability.md) | Trace/Span、业务/运营指标、会话、日志、OTel 接入、标注与回流 |
| 07-operation | [evaluation.md](07-operation/evaluation.md) | 在线/离线评估、评测集、评估器、评估任务、报告与校准 |
| 07-operation | [optimization.md](07-operation/optimization.md) | **平台四类优化任务**：轨迹分析、工具优化、Skill 优化、模型优化（GRPO 强化学习）+ 传统调优方法论与回归门禁 |
| 08-code-dev | [scaffolding.md](08-code-dev/scaffolding.md) | 项目脚手架、四种模板、配置文件、Dockerfile 生成 |
| 08-code-dev | [cli_reference.md](08-code-dev/cli_reference.md) | 全 CLI 命令参考（init/dev/launch/invoke/runtime/gateway/memory/install） |
| 08-code-dev | [deployment.md](08-code-dev/deployment.md) | **管理面 API（直接 API 创建 runtime）**、控制台/SDK 双路径部署、版本与访问方式、灰度发布、MCP Server 部署、destroy、远程运维、文件传输、CI/CD |
| 08-code-dev | [framework_integration.md](08-code-dev/framework_integration.md) | LangChain/LangGraph/GoogleADK 集成、Memory/Identity 用法 |
| 10-security | [agent_security.md](10-security/agent_security.md) | **智能体安全（三层框架）**：开发态（镜像扫描 / Skills 扫描规划中）、运行态（**智能体卫士 AI Defender**：高危操作阻断·意图行为一致性检测·角色限定；权限与访问控制；安全护栏 Rails；内容审核）、AI Infra 安全（资产识别 / 漏洞管理 / 基线检查）。**注意：含【需求方输入】待补充项，已用徽标区分** |
| 10-security | [runtime_env_injection.md](10-security/runtime_env_injection.md) | **Runtime 环境变量注入**：按变量类型分三条路径——普通参数走 `env_vars`、模型 key 走 Identity 工作负载身份（`@require_api_key`）、MCP key 走 Gateway Target（`credential_provider_configuration`）、华为云 AK/SK 走用户运行时委托；含 CLI / SDK / 配置文件三形式、CI/CD 最佳实践、降级与不可变项约束 |

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
- **三种开发范式**：低代码（拖拽）／高代码（镜像托管到运行时）／**Managed Agents（配置化全托管）**
- **控制面/数据面分离**：控制面（资源 CRUD，AK/SK）与数据面（数据读写，API Key 或 IAM 签名）贯穿 Memory/Sandbox/Gateway/Runtime
- **控制面 vs 数据面（Runtime）**：控制面 `https://agentarts.{region}.myhuaweicloud.com`（如 `POST /v1/core/runtimes`）；数据面 `/runtimes/{name}/...`。**运行时数据面接口不签 body，其他接口签 body**
- **IAM 委托**：`AgentArtsRuntimeDeploymentAgency`（服务部署委托，下载镜像/挂载 SFS Turbo，**不可删除**）+ 用户运行时委托（`DefaultAgentArtsRuntimeAgency`，代表用户身份访问云服务）
- **入站 vs 出站认证**：入站验"谁在调用"（IAM/OAuth 2.0/API Key）；出站验"代表谁访问后端"（API Key/OAuth/IAM/无认证）。两者独立配置
- **Adapter Layer**：伙伴 Agent 通过适配层接入平台，而非直接绑定接口
- **Skill 四元组**：Knowledge + Policy + Executor + Verifier，封装外部能力为企业级 Skill
- **内置工具**：**代码解释器**（沙箱代码执行）+ **浏览器**（网页自动化），都遵循控制面/数据面分离与 session 隔离。**注意：0804 材料把两者合称"沙箱工具"且只有代码解释器，浏览器是 0916 新增**
- **知识与记忆分工**：知识库解决"Agent 知道什么"（静态、可共享）；记忆库解决"Agent 记得什么"（动态、按 actor 隔离）
- **会话亲和性**：Agent Gateway 按 `session-id` 路由到同一 microVM；**业务对象到 session 的映射由伙伴侧前端应用负责**
- **本地磁盘不可靠**：沙箱空闲释放时本地磁盘数据全部丢失——状态走 Memory，文件走 SFS Turbo / OBS

## Agent 读取原则

不要将文档作为普通说明书读取，而应作为 **Platform Capability Knowledge Base**，用于回答：

1. 平台有什么能力？→ [00-overview](00-overview/platform_architecture.md) 能力对照表 + 各专章
2. 如何接入已有 Agent？→ [06-integration](06-integration/partner_agent_adaptation.md) + [08-code-dev/framework_integration.md](08-code-dev/framework_integration.md)
3. 哪些能力由模型负责，哪些由 Runtime 负责？→ [00-overview](00-overview/platform_architecture.md) 第 5 节
4. 如何完成企业级上线？→ [08-code-dev/deployment.md](08-code-dev/deployment.md) + [07-operation/field_validation.md](07-operation/field_validation.md)
5. 如何完成“观测 -> 评估 -> 优化 -> 回归”闭环？→ [observability.md](07-operation/observability.md) + [evaluation.md](07-operation/evaluation.md) + [optimization.md](07-operation/optimization.md)
6. 如何让 Agent 操作网页，或给 AI 编程助手挂载长期记忆？→ [02-sandbox/browser.md](02-sandbox/browser.md) + [03-memory/memory_plugin.md](03-memory/memory_plugin.md)
7. 不想打镜像、想快速上线通用 Agent？→ [00-overview/managed_agents.md](00-overview/managed_agents.md)
8. 需要文档问答 / RAG？→ [09-knowledge-base/knowledge_base.md](09-knowledge-base/knowledge_base.md)
9. **想不经 CLI、直接用 API 创建和管理 runtime？**→ [08-code-dev/deployment.md](08-code-dev/deployment.md) 第 0 节「管理面 API」
10. 手上的旧结论还成立吗？→ [00-overview/release_delta_0916.md](00-overview/release_delta_0916.md)
11. 需要版本灰度、多端点、平滑更新镜像？→ [01-runtime/runtime.md](01-runtime/runtime.md) 第 2 节 + [08-code-dev/deployment.md](08-code-dev/deployment.md) 第 9 节
12. 如何诊断 Agent 表现差、并让平台自动优化？→ [07-operation/optimization.md](07-operation/optimization.md)

## 相关材料

- 联合开发实施包：`../AgentArts_Partner_Agent联合开发实施包_Phase0-3/`（Phase 0-3 + 8 周计划 + RACI）
- SDK 仓库：`../agentarts-sdk-python/`（源码 + examples + 官方文档）
- **最新官方材料（事实来源）**：`../../AgentArts原始材料-0916/`（12 分册 / 4,864 页，2026-09-14 ~ 09-16）
- **旧版官方材料（历史对照）**：`../../AgentArts原始材料-0804/`（文档版本 02，2026-08-04）
- 关键分册：托管与运行智能体（486 页）、Managed Agents（46 页）、观测与优化智能体（407 页）、API 参考（2,385 页，版本 03）、资源与成员管理（32 页）
- 版本差异清单：[00-overview/release_delta_0916.md](00-overview/release_delta_0916.md)
