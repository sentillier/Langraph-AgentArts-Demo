# AgentArts Agent 平台 API 参考 Wiki 知识包

## 用途

本知识包面向需要调用 AgentArts API 的 Agent、集成开发者和自动化编排器，提供“先定位场景，再定位 API，再打开官方详情”的检索路径。它从 `AgentArts_Agent平台Wiki知识包/00-overview/official_llms_index.txt` 的 **API参考** 章节整理而来。

- **API 条目**：265 个具体操作，按动作、资源域和生命周期组织。
- **调用指南**：17 个官方页面，覆盖构造请求、认证、返回结果、状态码、运行时、智能体/工作流、观测、评估和文档/图像输入。
- **权威性**：本包中的摘要用于索引；请求字段、枚举、配额和错误码以对应官方页面为准。
- **来源**：华为云 AgentArts API 参考，入口 <https://support.huaweicloud.com/api-agentarts/agentarts_07_0002.md>。

## Agent 快速路由

1. **调用已部署单/多智能体或工作流**：先读 [调用场景指南](01-invocation/invocation_guides.md)，再按认证方式选择 API Key 或 IAM。
2. **创建/发布/管理托管运行时**：查 [资源 API 矩阵](02-resource-apis/resource_api_matrix.md) 中“运行时”域。
3. **操作浏览器、代码解释器、网关或记忆空间**：按资源域查矩阵，再在 [完整目录](00-overview/api_catalog.md) 打开具体官方条目。
4. **做评测、Trace 观测或数据集管理**：查“评估任务 / 评估器 / 评测集 / 观测数据 / Trace”域。
5. **不确定请求格式或签名**：先读 [API 调用速查](00-overview/api_quickstart.md)。

## 文件导航

| 文件 | 适用问题 |
| --- | --- |
| [api_quickstart.md](00-overview/api_quickstart.md) | 请求结构、认证选择、响应、错误处理和调用流程 |
| [api_catalog.md](00-overview/api_catalog.md) | 265 个 API 的完整可检索目录和官方链接 |
| [api_index.txt](00-overview/api_index.txt) | 适合程序/Agent 关键词检索的扁平索引 |
| [api_index.jsonl](00-overview/api_index.jsonl) | 适合程序读取的结构化索引 |
| [invocation_guides.md](01-invocation/invocation_guides.md) | 17 个官方 API 使用指南和场景入口 |
| [resource_api_matrix.md](02-resource-apis/resource_api_matrix.md) | 按资源域查看 CRUD、查询、动作类 API |

## 使用约定

- 看到 `Batch`、`Create`、`List`、`Show`、`Update`、`Delete` 等前缀时，优先按动作定位；同一资源的完整生命周期通常分散在多个动作下。
- `Core*` 多为控制面资源 API；`Ops*` 多为观测、评估和运营 API；`Runtime`/`Invoke` 类条目与数据面调用相关。具体以官方条目为准。
- 任何会改变资源状态的动作都应先确认区域、资源 ID/名称、版本或会话 ID，以及调用身份的权限。
