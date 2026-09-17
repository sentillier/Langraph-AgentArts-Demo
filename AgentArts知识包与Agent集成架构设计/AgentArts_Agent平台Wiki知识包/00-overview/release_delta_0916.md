# AgentArts 官方材料版本差异（0804 → 0916）

> 本文件是知识包的**版本基线锚点**。此前知识包与《整体架构设计v1/v2》的官方事实来源为 `AgentArts原始材料-0804`（各分册文档版本 02，2026-08-04）。当前最新材料为 `AgentArts原始材料-0916`（2026-09-14 ~ 2026-09-16）。
>
> **结论：0916 材料相对 0804 发生了结构性变化，不是补充修订，而是文档体系重排 + 新增大能力域。凡引用 0804 的结论均需按本文件复核。**

## 1. 分册映射：文档体系重排

| 0804 分册（版本 02，08-04） | 0916 分册（版本，09-1x） | 变化性质 |
| --- | --- | --- |
| 高代码开发（254 页） | 托管与运行智能体（486 页） | **改名 + 大幅扩写**，章节从"组件库 + 部署"重排为"运行时 → 记忆库 → 网关 → 代码解释器 → 浏览器 → 知识库 → 身份认证 → 网络配置 → 运行时 SDK" |
| 智能体运营运维（270 页） | 观测与优化智能体（407 页） | **改名 + 新增第 3 章「智能体优化」**（0804 只有观测 + 评估两章） |
| —（不存在） | Managed Agents（46 页） | **全新分册**：第三种开发范式（全托管智能体） |
| —（不存在） | 资源与成员管理（32 页） | **全新分册**：套餐用量 / 成员许可 / 授权管理 / 资源订阅 / CTS 云审计 |
| 产品介绍（19 页，版本 01） | 产品介绍（23 页，版本 02） | 新增「订阅套餐」「资产广场」「基本概念」 |
| 开始使用（47 页） | 开始使用（42 页） | 新增「选择开发路径」「创建 Managed Agents」 |
| 低代码开发（813 页） | 低代码开发智能体（728 页） | 改名 + 重排 |
| API 参考（1555 页，版本 02） | API 参考（2385 页，**版本 03，2026-09-14**） | **大幅扩写**，管理面 API 成体系 |
| OfficeAce (PC版)（232 页） | —（已下线） | 移出 |
| SDK 参考 / 常见问题 / 最佳实践 / 计费说明 | 同名保留 | 内容扩写 |

## 2. 新增能力域（0804 完全没有）

| 能力域 | 0916 位置 | 说明 |
| --- | --- | --- |
| **浏览器（Browser）** | 托管与运行智能体 ch8；API 参考 4.4.3–4.4.6、4.4.9 | 0804 的"沙箱工具"**仅含代码解释器**，不含浏览器。浏览器是独立托管能力：会话、配置文件（Profile）、代理配置、人机接管 |
| **知识库（含第三方知识库）** | 托管与运行智能体 ch9 | 平台知识库 + 第三方知识库（General / KooSearch / RAGFlow）+ 第三方通用知识库接入规范 |
| **Managed Agents** | 全新分册 | 环境（Environment）+ 智能体（Agent）+ Skill + 会话，表单化声明、全托管、无镜像 |
| **智能体优化** | 观测与优化智能体 ch3 | 轨迹分析、工具优化、Skill 优化、模型优化（在线强化学习 RL/GRPO） |
| **委托（Agency）机制** | 托管与运行智能体 4.4.1 | `AgentArtsRuntimeDeploymentAgency`（服务部署委托）+ 用户运行时委托（智能体身份委托，默认 `DefaultAgentArtsRuntimeAgency`） |
| **入站身份认证** | 托管与运行智能体 4.4.2 | 运行时入站三方式：IAM（AK/SK 签名）、API Key、OAuth 2.0；含 V11-HMAC-SHA256 / SDK-ECDSA-P256SHA256 签名算法 |
| **存储配置体系** | 托管与运行智能体 4.10；Managed Agents 3.2 | SFS Turbo / 会话存储 / OBS 三种，含字段级继承、挂载约束、OBS 回写语义 |
| **灰度发布** | 托管与运行智能体 4.12.3 | 由访问方式（Endpoint）权重实现，Miracle PolicyItem 路由 |
| **成员许可与云审计** | 资源与成员管理 | 成员许可（先到先得 + `agentarts::updateMemberPermit`）、CTS 关键操作审计 |
| **运行时管理面 API 全集** | API 参考 4.7 | CreateCoreRuntime / ListCoreRuntimes / ShowCoreRuntime / UpdateCoreRuntime / DeleteCoreRuntime / ListCoreRuntimeSpecs / RuntimeVersions / RuntimeEndpoints / Ingresses |

> ⚠️ **另一类差异：0804 就已存在、但此前知识包缺失的能力**
>
> 版本重排之外还有一处**遗漏补登**：**智能体卫士 AI Defender**（运行时安全防护：高危操作阻断 / 意图行为一致性检测 / 角色限定）在 **0804 计费说明 3、开始使用、最佳实践、低代码开发中均已存在**，**不是 0916 新增**，但此前知识包与《整体架构设计v1/v2》**完全未覆盖**。本次补齐，见 [10-security/agent_security.md](../10-security/agent_security.md)。
>
> 同时补登官方在运行时的 **4.4「权限与访问控制」**（委托 + URN/AgentIdentity + 入站三认证）被官方明确定位为"**智能体运行时的安全底座**"，以及低代码侧的三层**安全护栏（Rails）**体系（错误码 `AgentArts.101047`–`101050` 反证输入/执行/输出三层护栏）。

## 3. 关键术语与概念变更（旧文档会误导）

| 0804 说法 | 0916 正确说法 | 影响 |
| --- | --- | --- |
| 沙箱工具 | **代码解释器**（Ch7）+ **浏览器**（Ch8） | 知识包 `02-sandbox/sandbox.md` 中的"沙箱工具"措辞需改为"代码解释器"；浏览器需独立成章 |
| 上报高代码智能体数据 | 上报智能体运行时数据 | 观测章节术语 |
| 查看高代码应用运行数据 | 查看托管智能体数据 | 观测章节术语 |
| 查看沙箱工具数据信息 | 查看代码解释器数据信息 | 观测章节术语 |
| 上报第三方智能体 Trace、Metric、Log 数据 | 上报第三方智能体观测数据（SDK 接入含 **AgentScope**） | 0804 只有 LangChain/LangGraph；0916 增加 AgentScope |
| 组件库（沙箱工具 / 记忆库 / 网关） | 运行时 / 记忆库 / 网关 / 代码解释器 / 浏览器 / 知识库 | 能力分区重排 |
| 记忆库 = Space + Session + Message + Memory | 增加**分层记忆架构**、**5 种内置策略（含程序性记忆）**、**自定义策略**、**生成/检索链路参数** | 记忆章节需重写原理部分 |
| Target 类型：OpenAPI Schemas / MCP Servers / APIG / 云服务 | Target 类型：**REST API / MCP / APIG / 云服务** | `OpenAPI Schemas` 改称 `REST API` |
| —（无出站认证概念） | **出站身份（OutBound 身份）**：API Key / OAuth / IAM / 无认证，可复用、多 Target 绑定 | Gateway 章节新增 |
| —（无入站认证概念细分） | 网关入站认证：IAM / OAuth 2.0 / API Key | Gateway 章节新增 |
| —（无会话 ID 请求头规范） | `X-Hw-Agentarts-Session-Id`（Agent）、`X-Hw-Agentarts-Code-InterpreterSession-Id`、`X-Hw-Agentarts-Browser-Session-Id` | Runtime 章节需明确 |

## 4. 规格与限额（0916 明确给出，设计必须遵守）

| 项 | 限额 | 来源 |
| --- | --- | --- |
| 智能体运行时 / 账号 | 1,000 个 | 托管与运行智能体 4.1 |
| 版本 / 运行时 | 1,000 个 | 托管与运行智能体 4.1 |
| 访问方式 / 运行时 | 10 个 | 托管与运行智能体 4.1 |
| 启动命令 / 运行时 | 10 条 | 托管与运行智能体 4.1 |
| 标签 / 运行时 | 20 个 | 托管与运行智能体 4.1 |
| 会话 ID | 英文/数字/`-`/`_`，≤ 64 字符 | 托管与运行智能体 4.9 |
| 空闲会话超时 | 60–604,800 秒，默认 900 秒 | 托管与运行智能体 4.9 |
| 最大存活时间 | 60–604,800 秒，默认 86,400 秒 | 托管与运行智能体 4.9 |
| 上传文件 | 单文件 100MB / 多文件合计 500MB | 托管与运行智能体 4.9 |
| 记忆库 / 租户 | 默认 10 个 | 托管与运行智能体 5.1 |
| 自定义记忆策略 / 记忆库 | 10 个 | 托管与运行智能体 5.1 |
| 短期记忆保留期 | 7–365 天，默认 90 天 | 托管与运行智能体 5.2.2 |
| 长期记忆 min_score | 0–1，默认 0.75 | 托管与运行智能体 5.2.5 |
| 长期记忆 top_k | 1–100，默认 10 | 托管与运行智能体 5.2.5 |
| 长期记忆触发：会话空闲 | 10–86,400 秒，默认 10 秒 | 托管与运行智能体 5.2.4 |
| 长期记忆触发：累计 Token | 1,000–1,073,741,824，默认 4,096 | 托管与运行智能体 5.2.4 |
| 长期记忆触发：累计消息数 | 3–10,000，默认 10 | 托管与运行智能体 5.2.4 |
| SFS Turbo 挂载 / 运行时 | 5 个（私网） | Managed Agents 3.2 / 托管与运行智能体 4.10 |
| OBS 挂载 / 运行时 | 10 个（最多 5 个桶，私网） | Managed Agents 3.2 |
| 会话存储 / 运行时 | 1 个 | 托管与运行智能体 4.9 |
| Managed Agents 环境 / 租户 | 1,000 个 | Managed Agents 3.1 |
| Managed Agents 智能体 / 租户 | 1,000 个 | Managed Agents 4.1 |
| Managed Agents 会话空闲超时 | 1–10,080 分钟，默认 15 分钟 | Managed Agents 4.1 |
| Managed Agents 最大存活时间 | 1–168 小时，默认 24 小时 | Managed Agents 4.1 |
| 知识库 FAQ Excel | 单文件 ≤ 100,000 条 | 托管与运行智能体 9.1 |
| 记忆库/知识库存储空间 | 按套餐：1GB / 4GB / 40GB / 200GB / 800GB | 计费说明 3 |

## 5. 版本号与运行环境约束

| 项 | 值 | 来源 |
| --- | --- | --- |
| SDK 版本锚点 | `agentarts-sdk` **v0.1.6**（2026-08，新增记忆插件） | 托管与运行智能体 12.1 + SDK 仓库 `pyproject.toml` |
| Python | ≥ 3.10（v0.1.5 起适配 3.13） | 托管与运行智能体 12.1 |
| 支持区域 | **仅 西南-贵阳一 `cn-southwest-2`** | 托管与运行智能体 12.1 |
| 镜像架构 | **必须 ARM64**，x86 镜像调用失败 | 托管与运行智能体 4.1 / 12.4 |
| 控制面端点 | `https://agentarts.{region}.myhuaweicloud.com` | SDK `utils/constant.py` |
| 入站端口 | 默认 8080，Host `0.0.0.0` | 托管与运行智能体 4.3.1 |

## 6. 对既有知识包与《整体架构设计v2》的影响清单

| 受影响文档 | 必须复核的点 |
| --- | --- |
| `00-overview/platform_architecture.md` | 能力对照表补 知识库 / 浏览器 / Managed Agents / 智能体优化 / 委托；开发范式从二选一改为三选一 |
| `01-runtime/runtime.md` | 补入站协议（HTTP + MCP）、入站身份认证三方式、委托、microVM 与 Agent Gateway 按 session-id 路由、访问方式与灰度、存储配置、会话生命周期参数 |
| `02-sandbox/sandbox.md` | "沙箱工具"改为"代码解释器"；补控制面 API 名与限额 |
| `02-sandbox/browser.md` | 补会话管理、Profile、代理配置、快捷操作全集 |
| `03-memory/memory.md` | 重写原理：分层记忆架构、5 内置策略、自定义策略（抽取/整合/反思）、生成与检索链路参数、隔离维度、观测指标 |
| `04-gateway/gateway.md` | Target 类型改名（OpenAPI Schemas → REST API）；补出站身份、入站认证、工具发现 cursor 机制、MCP 版本、语义检索 |
| `05-identity/identity.md` | 补委托两件套、入站身份认证三方式、镜像签名算法、平台侧权限策略（AgentArtsFullAccessPolicy / AgentIdentityFullAccessPolicy） |
| `06-integration/partner_agent_adaptation.md` | 补"Runtime vs Managed Agents"选型；接入形态不再只有高代码 |
| `07-operation/observability.md` | 术语改名；补 AgentScope SDK 接入 |
| `07-operation/evaluation.md` | 评估器增至 52 个；补 Skill / Rubric / Token 效率 / 文本判定类 |
| `07-operation/optimization.md` | **重度更新**：从"BadCase 归因 + Prompt/Model/RAG/Tool 调优"升级为平台化四类优化任务 |
| `07-operation/field_validation.md` | 补 Managed Agents 与知识库的验收项 |
| `08-code-dev/deployment.md` | 补控制台部署 / SDK 部署双路径、运行时镜像更新、灰度发布、端点管理 |
| `08-code-dev/cli_reference.md` | 补 `config` 命令、`runtime` 全子命令、`gateway` 命令 |
| 《整体架构设计v2》 | 架构总图需补 知识库 / 浏览器 / 委托 / 入站认证 / 灰度 / Managed Agents 分支 —— **✅ 已完成：产出 [《整体架构设计v3》](../../整体架构设计/整体架构设计v3.md)**（第 0 节含 14 条事实纠错 + 8 项新增能力域清单），v1/v2 已加"已被取代"提示；配套绘图 prompt 见 [架构图Prompt.md](../../整体架构设计/架构图Prompt.md) |
