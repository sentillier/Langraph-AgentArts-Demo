# API 调用速查

## 1. 先选调用场景

| 目标 | 首选指南 |
| --- | --- |
| 单/多智能体 | [使用API调用单/多智能体](https://support.huaweicloud.com/api-agentarts/agentarts_07_0046.md)；企业 IAM 场景看 [IAM认证](https://support.huaweicloud.com/api-agentarts/agentarts_07_0052.md) |
| 工作流 | [使用API调用工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0047.md) |
| 图像理解工作流 | [图像理解工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0048.md) |
| 文档解析智能体/工作流 | [智能体](https://support.huaweicloud.com/api-agentarts/agentarts_07_0049.md) / [工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0050.md) |
| 托管运行时 | [运行时 API Key](https://support.huaweicloud.com/api-agentarts/agentarts_07_0035.md) 或 [运行时 IAM](https://support.huaweicloud.com/api-agentarts/agentarts_07_0033.md) |
| 观测/Trace | [使用API调用观测接口](https://support.huaweicloud.com/api-agentarts/agentarts_07_0037.md) |
| 评估/评测集 | [使用API调用评估接口](https://support.huaweicloud.com/api-agentarts/agentarts_07_0039.md) |

## 2. 通用请求骨架

官方请求由 Endpoint、URI、请求方法、请求头和请求体组成；字段定义以具体 API 页面为准。先读 [构造请求](https://support.huaweicloud.com/api-agentarts/agentarts_07_0004.md)。

```http
<METHOD> https://<endpoint>/<resource-path>
Host: <endpoint>
Content-Type: application/json
Authorization: <credential-or-signature>

{
  "<request-field>": "<value>"
}
```

- **Endpoint/区域**：使用目标区域的 AgentArts 服务 Endpoint。不要把示例区域、租户 ID 或资源 ID 当成固定值。
- **路径与方法**：从具体 API 条目确认，尤其注意控制面 `/v1/...` 与运行时数据面路径的区别。
- **请求体**：严格按 API 页面中的 `Request Body`、必填项、枚举和长度限制构造。
- **分页**：列表 API 通常需要按官方定义传入分页大小、游标或页码；不要自行假设字段名。

## 3. 认证选择

| 方式 | 适用 | 要点 |
| --- | --- | --- |
| API Key | 智能体/工作流和部分运行时调用，接入轻量 | 在请求头携带平台颁发的 API Key/Authorization 参数；失效时重新获取。 |
| IAM AK/SK | 管理面 API、企业级集成、需要 IAM 权限控制 | 使用 AK/SK 对请求签名；签名字段、时间戳和服务区域必须按官方指南生成。 |
| API 签名 SDK | 观测、评估等接口示例中的签名调用 | 按官方 SDK/签名示例生成 `Authorization`、`X-Sdk-Date` 等字段，不要手写简化签名。 |

认证细节见 [认证鉴权](https://support.huaweicloud.com/api-agentarts/agentarts_07_0005.md)。账号根用户和 IAM 用户权限要求以每个 API 条目的“权限和授权项”为准。

## 4. 响应与错误处理

先读 [返回结果](https://support.huaweicloud.com/api-agentarts/agentarts_07_0006.md) 和 [状态码](https://support.huaweicloud.com/api-agentarts/agentarts_07_0016.md)。处理逻辑至少应包含：

1. 按 HTTP 状态码判断成功、客户端参数错误、认证失败、权限不足、限流或服务端错误。
2. 解析响应体中的业务 code、message、data（具体结构以 API 页面为准）。
3. 对异步创建/更新/删除操作保存任务 ID，并按对应查询 API 轮询最终状态。
4. 对 401/Authorization failed 重新获取凭证；对 403 检查 IAM 策略、委托和入站/出站身份；对 429/5xx 使用带上限的退避重试。
5. 记录 request ID、区域、资源 ID 和脱敏后的请求参数，便于审计和排障。

## 5. API 调用前检查清单

- [ ] 已确认区域、Endpoint、资源类型和资源 ID/名称。
- [ ] 已选择 API Key 或 IAM，并确认凭证未过期。
- [ ] IAM 用户已获得具体 API 所需身份策略。
- [ ] 已阅读目标 API 的请求参数、响应字段、配额和幂等/异步说明。
- [ ] 涉及文件、图像或文档时，已按对应指南准备上传或引用方式。
- [ ] 已设计超时、轮询、重试和错误记录策略。
