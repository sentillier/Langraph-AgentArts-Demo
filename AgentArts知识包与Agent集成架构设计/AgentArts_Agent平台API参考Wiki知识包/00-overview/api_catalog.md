# AgentArts API 完整目录

> 来源：官方 API 参考章节；共 **265** 个具体 API 操作。按动作分组，保留官方标题、英文操作名、资源域、摘要和权威链接。

## 批量（Batch，30）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 批量添加评估任务的自定义标签值 | `BatchAddOpsEvaluationTaskCustomLabelValues` | 评估任务 | 该接口用于批量添加评估任务的自定义标签值，支持为多个数据项设置标签值，适用于数据标注和分类管理的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchAddOpsEvaluationTaskCustomLabelValues.md) |
| 添加评估任务自定义标签 | `BatchAddOpsEvaluationTaskCustomLabels` | 评估任务 | 该接口用于为评估任务添加自定义标签，支持批量添加多个标签类型，适用于任务分类管理和数据标记的场景。适用场景：为评估任务添加新的分类标记和特征标签。为评估任务添加新的分类标记和特征标签。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchAddOpsEvaluationTaskCustomLabels.md) |
| 批量添加浏览器配置标签 | `BatchCreateCoreBrowserProfileTags` | 浏览器 | 该API用于批量添加浏览器配置标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreBrowserProfileTags.md) |
| 批量添加浏览器标签 | `BatchCreateCoreBrowserTags` | 浏览器 | 该API用于批量添加浏览器标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreBrowserTags.md) |
| 批量添加代码解释器标签 | `BatchCreateCoreCodeInterpreterTags` | 代码解释器 | 该API用于批量添加代码解释器标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreCodeInterpreterTags.md) |
| 批量添加网关标签 | `BatchCreateCoreGatewayTags` | 网关 | 批量添加网关标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreGatewayTags.md) |
| 批量为RuntimeEndpoint打资源标签 | `BatchCreateCoreRuntimeEndpointTags` | 运行时 | 该接口用于批量为运行时访问方式打资源标签。适用场景：为运行时访问方式资源批量添加标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreRuntimeEndpointTags.md) |
| 批量为Runtime打资源标签 | `BatchCreateCoreRuntimeTags` | 运行时 | 该接口用于批量为运行时打资源标签。适用场景：为运行时资源批量添加标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreRuntimeTags.md) |
| 批量添加记忆库标签 | `BatchCreateCoreSpaceTags` | 记忆空间 | 该接口用于批量为记忆库打资源标签。适用场景：为记忆库资源批量添加标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateCoreSpaceTags.md) |
| 批量添加评测集条目 | `BatchCreateOpsDatasetItems` | 评测集 | 该接口用于向指定评测集的草稿态批量注入数据行，支持增量添加、覆盖更新或基于历史版本还原数据，并强制校验数据与Schema的符合性。适用场景：数据初始化：在创建评测集后，通过API批量导入首批业务数据或基准测试集。数据初始化：在创建评测集后，通过API批量导入首批业务数据或基准测试集。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateOpsDatasetItems.md) |
| 批量创建数据集TMS标签 | `BatchCreateOpsDatasetTags` | 评测集 | 该接口用于批量创建指定数据集的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateOpsDatasetTags.md) |
| 批量创建评估任务TMS标签 | `BatchCreateOpsEvaluationTaskTags` | 评估任务 | 该接口用于批量创建指定评估任务的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateOpsEvaluationTaskTags.md) |
| 批量创建评估器TMS标签 | `BatchCreateOpsEvaluatorTags` | 评估器 | 该接口用于批量创建指定评估器的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchCreateOpsEvaluatorTags.md) |
| 批量删除浏览器配置标签 | `BatchDeleteCoreBrowserProfileTags` | 浏览器 | 该API用于批量删除浏览器配置标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreBrowserProfileTags.md) |
| 批量删除浏览器标签 | `BatchDeleteCoreBrowserTags` | 浏览器 | 该API用于批量删除浏览器标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreBrowserTags.md) |
| 批量删除代码解释器标签 | `BatchDeleteCoreCodeInterpreterTags` | 代码解释器 | 该API用于批量删除代码解释器标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreCodeInterpreterTags.md) |
| 批量删除网关标签 | `BatchDeleteCoreGatewayTags` | 网关 | 批量删除网关标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreGatewayTags.md) |
| 批量删除RuntimeEndpoint资源标签 | `BatchDeleteCoreRuntimeEndpointTags` | 运行时 | 该接口用于批量删除运行时访问方式的资源标签。适用场景：为运行时访问方式资源批量删除标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreRuntimeEndpointTags.md) |
| 批量删除Runtime资源标签 | `BatchDeleteCoreRuntimeTags` | 运行时 | 该接口用于批量删除运行时的资源标签。适用场景：为运行时资源批量删除标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreRuntimeTags.md) |
| 批量删除记忆库标签 | `BatchDeleteCoreSpaceTags` | 记忆空间 | 该接口用于批量删除记忆库的资源标签。适用场景：为记忆库资源批量删除标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteCoreSpaceTags.md) |
| 批量删除评测集条目 | `BatchDeleteOpsDatasetItems` | 评测集 | 该接口用于通过指定条目ID列表，从当前评测集的草稿版本中批量移除特定的数据行，实现对评测集内容的清理。适用场景：数据清洗：在数据导入后，批量剔除经人工或自动化检测识别出的错误数据、脏数据或重复样本。数据清洗：在数据导入后，批量剔除经人工或自动化检测识别出的错误数据、脏数据或重复样本。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsDatasetItems.md) |
| 批量删除数据集TMS标签 | `BatchDeleteOpsDatasetTags` | 评测集 | 该接口用于批量删除指定数据集的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsDatasetTags.md) |
| 批量删除评测集 | `BatchDeleteOpsDatasets` | 评测集 | 该接口用于通过指定评测集ID列表批量删除不再使用的评测集资源，清理以释放存储空间。适用场景：资源清理：在业务周期结束或项目归档时，批量清理过时的测试数据。资源清理：在业务周期结束或项目归档时，批量清理过时的测试数据。批量操作：支持一次性处理多个ID，适用于批量删除。批量操作：支持一次性处理多个ID，适用于批量删除。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsDatasets.md) |
| 批量删除评估任务TMS标签 | `BatchDeleteOpsEvaluationTaskTags` | 评估任务 | 该接口用于批量删除指定评估任务的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsEvaluationTaskTags.md) |
| 批量删除任务 | `BatchDeleteOpsEvaluationTasks` | 评估任务 | 该接口用于批量删除指定的评估任务，支持一次性删除多个任务，批量返回删除结果，适用于任务清理的场景。适用场景：清理不再需要的历史评估任务。清理不再需要的历史评估任务。批量删除测试或错误创建的任务。批量删除测试或错误创建的任务。管理项目中的任务列表以保持系统整洁。管理项目中的任务列表以保持系统整洁。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsEvaluationTasks.md) |
| 批量删除评估器 | `BatchDeleteOpsEvaluator` | 评估器 | 该接口用于通过评估器ID列表批量移除不再使用的评估工具定义，适用场景：冗余清理：定期移除测试阶段产生的临时评估器或已过时的评价准则，保持评估器仓库的整洁。冗余清理：定期移除测试阶段产生的临时评估器或已过时的评价准则，保持评估器仓库的整洁。评价体系更迭：当业务评测标准发生重大调整，需要彻底废弃并清理旧版评估逻辑时使用。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsEvaluator.md) |
| 批量删除评估器TMS标签 | `BatchDeleteOpsEvaluatorTags` | 评估器 | 该接口用于批量删除指定评估器的TMS标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsEvaluatorTags.md) |
| 批量删除评测集合成任务 | `BatchDeleteOpsSynthesisTasks` | 评测集合成 | 该接口用于通过指定任务ID列表集中清理多个评测集合成任务及其关联的历史记录。适用场景：环境清理：在完成大规模合成实验或多轮对比测试后，批量回收过期的测试任务以释放管理空间。环境清理：在完成大规模合成实验或多轮对比测试后，批量回收过期的测试任务以释放管理空间。任务删除：在后台管理系统中，支持用户通过勾选方式一次性销毁多个冗余的任务条目。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDeleteOpsSynthesisTasks.md) |
| 批量解绑模型代理 | `BatchDisassociateModelProxies` | 其他 | 批量解绑模型代理。当模型代理没有任何模型提供商关联时，会自动删除。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchDisassociateModelProxies.md) |
| 更新评估任务的自定义标签值 | `BatchUpdateOpsEvaluationTaskCustomLabelValues` | 评估任务 | 该接口用于批量更新评估任务的自定义标签值，支持修改现有标签值的标注内容。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/BatchUpdateOpsEvaluationTaskCustomLabelValues.md) |

## 创建（Create，23）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 创建 Automation CDP WebSocket 流 | `CreateAutomationStream` | 浏览器自动化 | 该接口通过 WebSocket 协议透传 Chrome DevTools Protocol（CDP）消息，供 Agent 或 SDK 以程序化方式控制浏览器。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateAutomationStream.md) |
| 创建浏览器 | `CreateCoreBrowser` | 浏览器 | 该API用于创建一个浏览器。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreBrowser.md) |
| 创建浏览器配置 | `CreateCoreBrowserProfile` | 浏览器 | 该API用于创建一个浏览器配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreBrowserProfile.md) |
| 创建代码解释器 | `CreateCoreCodeInterpreter` | 代码解释器 | 该API用于创建一个代码解释器。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreCodeInterpreter.md) |
| 创建网关 | `CreateCoreGateway` | 网关 | 使用指定配置创建一个新的网关。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreGateway.md) |
| 创建目标服务 | `CreateCoreGatewayTarget` | 网关 | 为指定网关创建目标服务。目标服务定义了网关可以连接的端点。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreGatewayTarget.md) |
| 创建网关 | `CreateCoreIngress` | Ingress入口 | 该接口用于创建一个新的Ingress配置。适用场景：创建Agent运行时入口网关配置。异步任务确认方式：调用创建接口后，通过查询Ingress详情接口（GET /v1/core/ingresses/{ingress_id}）查询status字段，当status变为ACTIVE时表示创建成功，变为FAILED时表示创建失败。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreIngress.md) |
| 创建VPC入站网络 | `CreateCoreIngressNetwork` | Ingress入口 | 该接口用于为某一个Agent网关ID创建指定VPC的入站网络。该接口会为该VPC创建对应网关的访问地址和域名。适用场景：Agent运行时需要在VPC网络内部调用场景下，为该VPC网络配置网关调用入口。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreIngressNetwork.md) |
| 创建runtime | `CreateCoreRuntime` | 运行时 | 该接口用于创建Agent运行时，支持为该运行时进行入站认证，网络访问，可观测配置等。该接口会同时创建运行时以及对应的初始版本。适用场景：部署一个已经开发完成的Agent应用。为Agent应用配置入站认证。为Agent应用配置入口和出口网络。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreRuntime.md) |
| 创建runtime访问方式 | `CreateCoreRuntimeEndpoint` | 运行时 | 该接口用于为某一个具体的Agent运行时创建访问方式，支持为该访问方式绑定版本以及对应的灰度策略。适用场景：某一个具体的Agent运行时存在多个版本，通过配置访问方式来指定调用某一个具体版本。某一个具体的Agent运行时修改后需要进行灰度发布，通过配置访问方式，为老版本和新版本配置流量权重。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreRuntimeEndpoint.md) |
| 创建Space | `CreateCoreSpace` | 记忆空间 | 创建新的记忆空间，用于存放某一类业务的短长期记忆数据，包括访问方式、抽取策略、密钥绑定等相关配置。当模型配置非空，agentarts:ModelProviderType 条件值会被赋值为builtin，不为空时为custom。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreSpace.md) |
| 创建 API Key | `CreateCoreSpaceApiKey` | 记忆空间 | 创建新的 API Key，用于数据面访问认证。API Key 先于 Space 创建，创建后通过 CreateSpace 的 api_key_id 参数绑定到 Space。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreSpaceApiKey.md) |
| 创建自定义记忆策略 | `CreateCoreSpaceCustomizedStrategy` | 记忆空间 | 为指定 Space 创建自定义记忆策略。需指定策略名称、类型及步骤列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCoreSpaceCustomizedStrategy.md) |
| 创建模型提供商 | `CreateCustomModelProvider` | 模型服务 | 使用指定配置创建一个新的模型提供商。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCustomModelProvider.md) |
| 创建模型服务 | `CreateCustomModelProviderModel` | 模型服务 | 使用指定配置创建一个新的模型。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateCustomModelProviderModel.md) |
| 创建 LiveView RFB WebSocket 流 | `CreateLivestreamStream` | 其他 | 该接口通过 WebSocket 协议透传 RFB（Remote Framebuffer）二进制帧，提供浏览器桌面的实时视频流，并支持键鼠输入（人工接管模式）。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateLivestreamStream.md) |
| 创建模型代理 | `CreateModelProxy` | 其他 | 创建模型代理。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateModelProxy.md) |
| 将智能体信息同步至观测页面 | `CreateOpsAgentObservation` | 观测数据 | 通过此接口可以在观测页面查看该智能体上报的数据信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsAgentObservation.md) |
| 创建评测集 | `CreateOpsDataset` | 评测集 | 该接口用于创建结构化评测集，支持定义评测集的字段，为Agent的评估任务提供标准化的数据来源。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsDataset.md) |
| 创建评估任务 | `CreateOpsEvaluationTask` | 评估任务 | 该接口用于创建新的评估任务，支持离线和在线评估模式，灵活配置评估参数和数据源，适用于各类模型评估和数据质量验证的场景。适用场景：启动新的离线评估任务进行模型质量测试。启动新的离线评估任务进行模型质量测试。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsEvaluationTask.md) |
| 新建评估器 | `CreateOpsEvaluator` | 评估器 | 该接口用于在系统中注册并创建一个新的评估器（Evaluator），通过定义具体的评估逻辑、判分准则及参数配置，为模型输出的质量度量提供标准化工具。适用场景：自定义评价体系构建：针对特定业务领域（如法律、医疗），创建符合行业规范的判分插件或规则脚本。自定义评价体系构建：针对特定业务领域（如法律、医疗），创建符合行业规范的判分插件或规则脚本。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsEvaluator.md) |
| 创建标签 | `CreateOpsLabel` | 标签 | 该接口用于创建新标签，支持文本标签和布尔类型的自定义标签，适用于资源分类、数据标注和标签管理的场景。适用场景：在评估任务管理中，创建新的标签以便对任务进行分类标记（如按业务线、优先级分类）。在评估任务管理中，创建新的标签以便对任务进行分类标记（如按业务线、优先级分类）。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsLabel.md) |
| 创建评测集合成任务 | `CreateOpsSynthesisTask` | 评测集合成 | 该接口用于利用大模型能力发起异步的数据合成任务，通过种子数据泛化（Seed-based Generalization）等手段自动生成高质量、多样化的训练或评测样本。适用场景：数据样本扩充：在现有数据量不足时，基于少量种子数据生成大规模同分布的模拟数据，提升模型训练效果。 | [打开](https://support.huaweicloud.com/api-agentarts/CreateOpsSynthesisTask.md) |

## 删除（Delete，21）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 删除浏览器 | `DeleteCoreBrowser` | 浏览器 | 删除指定的浏览器。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreBrowser.md) |
| 删除浏览器配置 | `DeleteCoreBrowserProfile` | 浏览器 | 删除指定的浏览器配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreBrowserProfile.md) |
| 删除代码解释器 | `DeleteCoreCodeInterpreter` | 代码解释器 | 删除指定的代码解释器。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreCodeInterpreter.md) |
| 删除网关 | `DeleteCoreGateway` | 网关 | 永久删除指定 ID 的网关。此操作无法撤销。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreGateway.md) |
| 删除目标服务 | `DeleteCoreGatewayTarget` | 网关 | 永久删除指定目标服务。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreGatewayTarget.md) |
| 删除网关 | `DeleteCoreIngress` | Ingress入口 | 该接口用于根据ingress_id删除Ingress配置。（异步接口）适用场景：删除不再继续使用的Ingress配置。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreIngress.md) |
| 删除VPC入站网络 | `DeleteCoreIngressNetwork` | Ingress入口 | 该接口用于根据网关ID以及入站网络ID异步删除某一个具体的Agent网关入站网络。调用该接口之后，将无法通过该入站网络的入口IP或者域名进行Agent调用。适用场景：删除不再继续使用的Agent网关入站网络。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreIngressNetwork.md) |
| 删除runtime | `DeleteCoreRuntime` | 运行时 | 该接口用于根据Agent运行时ID删除对应的Agent运行时。该接口会删除运行时及其关联的所有版本和访问方式记录。适用场景：删除某一个具体的Agent运行时及其相关记录。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreRuntime.md) |
| 删除runtime访问方式 | `DeleteCoreRuntimeEndpoint` | 运行时 | 该接口用于根据Agent运行时ID以及访问方式ID删除对应的Agent运行时访问方式。访问方式删除后无法通过该访问方式进行Agent调用。适用场景：删除某一个具体的Agent运行时访问方式及其相关记录。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreRuntimeEndpoint.md) |
| 删除记忆空间 | `DeleteCoreSpace` | 记忆空间 | 删除记忆空间，将清空所有记忆数据和配置，不可恢复。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreSpace.md) |
| 删除自定义记忆策略 | `DeleteCoreSpaceCustomizedStrategy` | 记忆空间 | 删除指定Space下的自定义记忆策略，不可恢复。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCoreSpaceCustomizedStrategy.md) |
| 删除模型提供商 | `DeleteCustomModelProvider` | 模型服务 | 永久删除指定ID的模型提供商。此操作无法撤销。当模型提供商关联了模型代理时，无法删除，请先解绑模型代理。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCustomModelProvider.md) |
| 删除模型服务 | `DeleteCustomModelProviderModel` | 模型服务 | 永久删除指定ID的模型。此操作无法撤销。当其所属的模型提供商关联了模型代理时，至少保留一个模型。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteCustomModelProviderModel.md) |
| 将智能体信息在观测页面删除 | `DeleteOpsAgentObservation` | 观测数据 | 删除智能体后在观测页面无法查看该智能体上报的信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsAgentObservation.md) |
| 删除评测集 | `DeleteOpsDataset` | 评测集 | 该接口用于通过指定评测集ID彻底删除评测集中的所有的数据条目、Schema定义和历史版本。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsDataset.md) |
| 删除评测集版本 | `DeleteOpsDatasetVersion` | 评测集 | 该接口用于永久删除指定的评测集历史版本及其关联的所有条目快照数据。适用场景：合规性清理：根据数据保留政策或合规性要求，物理删除过期的、包含敏感信息的历史数据版本。合规性清理：根据数据保留政策或合规性要求，物理删除过期的、包含敏感信息的历史数据版本。删除冗余：在评测集生命周期后期，移除冗余的中间过程版本，保持资产列表的整洁。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsDatasetVersion.md) |
| 删除评估任务自定义标签值 | `DeleteOpsEvaluationTaskCustomLabelValues` | 评估任务 | 该接口用于删除评估任务的自定义标签值，支持批量移除指定标签项。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsEvaluationTaskCustomLabelValues.md) |
| 删除评估任务自定义标签 | `DeleteOpsEvaluationTaskCustomLabels` | 评估任务 | 该接口用于删除评估任务的指定自定义标签，支持移除不需要的标签项，适用于标签管理和数据清理的场景。适用场景：清理评估任务中不再使用的标签项。清理评估任务中不再使用的标签项。调整评估数据的分类和标记。调整评估数据的分类和标记。优化标签结构以提高数据管理效率。优化标签结构以提高数据管理效率。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsEvaluationTaskCustomLabels.md) |
| 删除单个评估器 | `DeleteOpsEvaluator` | 评估器 | 该接口用于通过指定的评估器ID删除对应的评估工具定义，是从系统资产库中彻底移除单条评测标准的不可逆操作。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsEvaluator.md) |
| 删除评估器特定版本 | `DeleteOpsEvaluatorVersion` | 评估器 | 该接口用于从指定评估器的版本序列中永久移除特定的历史快照。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsEvaluatorVersion.md) |
| 删除评测集合成任务 | `DeleteOpsSynthesisTask` | 评测集合成 | 该接口用于删除指定的数据集合成任务，通过移除任务记录及其关联的临时数据，实现任务列表清理。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DeleteOpsSynthesisTask.md) |

## 更新（Update，21）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 更新浏览器 Stream 状态 | `UpdateBrowserStream` | 其他 | 该 API 用于更新浏览器会话的 Stream 状态。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateBrowserStream.md) |
| 更新浏览器 | `UpdateCoreBrowser` | 浏览器 | 该API用于更新浏览器配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreBrowser.md) |
| 更新代码解释器 | `UpdateCoreCodeInterpreter` | 代码解释器 | 该API用于更新代码解释器配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreCodeInterpreter.md) |
| 更新网关 | `UpdateCoreGateway` | 网关 | 使用新配置更新现有网关。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreGateway.md) |
| 更新目标服务 | `UpdateCoreGatewayTarget` | 网关 | 更新现有目标服务的配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreGatewayTarget.md) |
| 更新网关 | `UpdateCoreIngress` | Ingress入口 | 该接口用于根据ingress_id更新Ingress的配置信息。（异步接口）适用场景：修改Ingress的描述信息。启用或禁用公网访问。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreIngress.md) |
| 更新runtime | `UpdateCoreRuntime` | 运行时 | 该接口用于根据Agent运行时ID修改对应的Agent运行时的配置信息，支持修改Agent镜像，网络配置，运行时委托，环境变量，可观测配置。该接口每次调用会生成一个新的运行时版本（更新tags除外）。version字段默认为v1、v2自增长，用户也可自定义。适用场景：修改某一个具体的Agent运行时的镜像版本、环境变量、网络配置。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreRuntime.md) |
| 更新runtime访问方式 | `UpdateCoreRuntimeEndpoint` | 运行时 | 该接口用于根据Agent运行时ID和访问方式ID修改对应的Agent运行时访问方式的配置信息，支持修改访问方式对应的版本信息以及多版本之间的权重分配信息。适用场景：修改某一个具体的Agent运行时访问方式的绑定版本。修改某一个具体的Agent运行时访问方式的多版本权重配置。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreRuntimeEndpoint.md) |
| 更新记忆空间相关配置 | `UpdateCoreSpace` | 记忆空间 | 更新记忆空间相关配置，涉及名称、策略等。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreSpace.md) |
| 更新自定义记忆策略 | `UpdateCoreSpaceCustomizedStrategy` | 记忆空间 | 更新指定Space下的自定义记忆策略配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreSpaceCustomizedStrategy.md) |
| 更新Space网络配置 | `UpdateCoreSpaceNetwork` | 记忆空间 | 更新指定Space的网络访问配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCoreSpaceNetwork.md) |
| 更新模型提供商 | `UpdateCustomModelProvider` | 模型服务 | 更新模型提供商。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCustomModelProvider.md) |
| 更新模型服务 | `UpdateCustomModelProviderModel` | 模型服务 | 更新模型服务。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateCustomModelProviderModel.md) |
| 更新智能体信息 | `UpdateOpsAgentObservation` | 观测数据 | 更新智能体信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsAgentObservation.md) |
| 修改评测集 | `UpdateOpsDataset` | 评测集 | 该接口用于更新现有评测集的名称和业务描述等信息，旨在确保资产信息的准确性与时效性，且操作不涉及对Schema字段定义的变更。适用场景：描述完善：在评测集创建后，补充更详细的业务背景、用途说明或标注说明。描述完善：在评测集创建后，补充更详细的业务背景、用途说明或标注说明。名称更改：根据业务需求变更或内部命名规范调整，修改评测集的显示名称。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsDataset.md) |
| 更新评测集条目 | `UpdateOpsDatasetItem` | 评测集 | 该接口用于对指定评测集草稿版本中已存在的特定数据行进行修改，确保条目内容符合Schema结构校验。适用场景：样本内容完善：针对多轮对话或复杂数据集，补充缺失的字段信息或优化对话轮次逻辑。样本内容完善：针对多轮对话或复杂数据集，补充缺失的字段信息或优化对话轮次逻辑。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsDatasetItem.md) |
| 更新评估任务洞察结果的用户反馈 | `UpdateOpsEvaluationTaskInsights` | 评估任务 | 该接口用于更新用户对于洞察内容的反馈。适用场景：用户反馈建议。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsEvaluationTaskInsights.md) |
| 校正评估结果 | `UpdateOpsEvaluationTaskResult` | 评估任务 | 该接口用于对已生成的自动化评估结果执行人工校正，允许通过更新得分与修正理由来覆盖评价，确保最终评测结论的客观性与权威性。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsEvaluationTaskResult.md) |
| 更新标签 | `UpdateOpsLabel` | 标签 | 该接口用于更新标签信息，支持修改标签名称、描述和标注项，适用于标签内容维护和完善的场景。适用场景：更新标签的描述信息以反映最新使用场景。更新标签的描述信息以反映最新使用场景。添加或修改标签的支持选项和枚举值。添加或修改标签的支持选项和枚举值。修正标签配置以适应业务需求变化。修正标签配置以适应业务需求变化。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsLabel.md) |
| 更新评测集合成任务状态 | `UpdateOpsSynthesisTask` | 评测集合成 | 该接口用于对指定的评测集合成任务执行生命周期状态控制，支持触发任务启动或手动中止执行。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsSynthesisTask.md) |
| trace数据点赞、点踩 | `UpdateOpsTraceFeedback` | Trace调用链 | 该接口用于给调用链数据进行评价(点赞/点踩)。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/UpdateOpsTraceFeedback.md) |

## 查询列表（List，76）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 查询账号下所有浏览器配置标签列表 | `ListAllCoreBrowserProfileTags` | 浏览器 | 该API用于查询账号下所有浏览器配置标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreBrowserProfileTags.md) |
| 查询账号下所有浏览器标签列表 | `ListAllCoreBrowserTags` | 浏览器 | 该API用于查询账号下所有浏览器标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreBrowserTags.md) |
| 查询账号下所有代码解释器标签列表 | `ListAllCoreCodeInterpreterTags` | 代码解释器 | 该API用于查询账号下所有代码解释器标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreCodeInterpreterTags.md) |
| 查询账号下所有网关标签列表 | `ListAllCoreGatewayTags` | 网关 | 查询账号下所有网关标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreGatewayTags.md) |
| 查询账号下所有RuntimeEndpoint标签列表 | `ListAllCoreRuntimeEndpointTags` | 运行时 | 该接口用于查询本账号下所有运行时访问方式资源的标签列表。适用场景：查询账号下所有运行时访问方式资源的标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreRuntimeEndpointTags.md) |
| 查询账号下所有Runtime标签列表 | `ListAllCoreRuntimeTags` | 运行时 | 该接口用于查询本账号下所有运行时资源的标签列表。适用场景：查询账号下所有运行时资源的标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreRuntimeTags.md) |
| 查询账号下所有记忆库标签列表 | `ListAllCoreSpaceTags` | 记忆空间 | 该接口用于查询本账号下所有记忆库资源的标签列表。适用场景：查询账号下所有记忆库资源的标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllCoreSpaceTags.md) |
| 查询账号下所有数据集TMS标签 | `ListAllOpsDatasetTmsTags` | 评测集 | 该接口用于查询账号下所有数据集的TMS标签列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllOpsDatasetTmsTags.md) |
| 查询账号下所有评估任务TMS标签 | `ListAllOpsEvaluationTaskTmsTags` | 评估任务 | 该接口用于查询账号下所有评估任务的TMS标签列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllOpsEvaluationTaskTmsTags.md) |
| 查询账号下所有评估器TMS标签 | `ListAllOpsEvaluatorTmsTags` | 评估器 | 该接口用于查询账号下所有评估器的TMS标签列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListAllOpsEvaluatorTmsTags.md) |
| 查询浏览器配置标签列表 | `ListCoreBrowserProfileTags` | 浏览器 | 该API用于查询浏览器配置标签列表。请参见如何调用API。当前API调用无需身份策略权限。GET /v1/browser-profiles/{profile_id}/tags无状态码：200状态码：400状态码：401状态码：403状态码：404状态码：429状态码：500状态码：200查询浏览器配置标签列表成功。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowserProfileTags.md) |
| 查询浏览器配置列表 | `ListCoreBrowserProfiles` | 浏览器 | 该API用于查询浏览器配置列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowserProfiles.md) |
| 根据标签查询浏览器配置列表 | `ListCoreBrowserProfilesByTags` | 浏览器 | 该API用于根据标签查询浏览器配置列表。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowserProfilesByTags.md) |
| 查询浏览器会话列表 | `ListCoreBrowserSessions` | 浏览器 | 该API用于查询浏览器会话列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowserSessions.md) |
| 查询浏览器标签列表 | `ListCoreBrowserTags` | 浏览器 | 该API用于查询浏览器标签列表。请参见如何调用API。当前API调用无需身份策略权限。GET /v1/browsers/{browser_id}/tags无状态码：200状态码：400状态码：401状态码：403状态码：404状态码：429状态码：500状态码：200查询浏览器标签列表成功。状态码：400请求参数错误。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowserTags.md) |
| 查询浏览器列表 | `ListCoreBrowsers` | 浏览器 | 该API用于查询浏览器列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowsers.md) |
| 根据标签查询浏览器列表 | `ListCoreBrowsersByTags` | 浏览器 | 该API用于根据标签查询浏览器列表。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreBrowsersByTags.md) |
| 查询代码解释器标签列表 | `ListCoreCodeInterpreterTags` | 代码解释器 | 该API用于查询代码解释器标签列表。请参见如何调用API。当前API调用无需身份策略权限。GET /v1/code-interpreters/{code_interpreter_id}/tags无状态码：200状态码：400状态码：401状态码：403状态码：404状态码：429状态码：500状态码：200查询代码解释器标签列表成功。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreterTags.md) |
| 查询代码解释器列表 | `ListCoreCodeInterpreters` | 代码解释器 | 该API用于查询代码解释器列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.md) |
| 根据标签查询代码解释器列表 | `ListCoreCodeInterpretersByTags` | 代码解释器 | 该API用于根据标签查询代码解释器列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpretersByTags.md) |
| 查询账号配额 | `ListCoreGatewayQuotas` | 网关 | 获取当前认证账号的网关相关的有效配额信息，包括配额类型、最小值、最大值、配额值和已使用数量。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewayQuotas.md) |
| 查询网关支持特性列表 | `ListCoreGatewaySupportedFeatures` | 网关 | 查询网关支持特性列表。请参见如何调用API。当前API调用无需身份策略权限。GET /v1/core/gateway-supported-features无状态码：200状态码：500状态码：401状态码：429无状态码：200成功查询网关支持特性列表状态码：500内部服务器错误状态码：401认证信息无法识别状态码：429请求频率超限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewaySupportedFeatures.md) |
| 查询网关支持服务列表 | `ListCoreGatewaySupportedServices` | 网关 | 当选择云服务Open API类型的target时，获取支持的主力核心服务列表。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewaySupportedServices.md) |
| 查询网关标签列表 | `ListCoreGatewayTags` | 网关 | 查询网关标签列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewayTags.md) |
| 列出目标服务 | `ListCoreGatewayTargets` | 网关 | 列出指定网关的所有目标服务，支持分页功能。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewayTargets.md) |
| 列出所有网关 | `ListCoreGateways` | 网关 | 检索所有网关的列表，支持可选的过滤和分页功能。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGateways.md) |
| 根据标签查询网关列表 | `ListCoreGatewaysByTags` | 网关 | 根据标签过滤条件查询网关列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreGatewaysByTags.md) |
| 查询VPC入站网络列表 | `ListCoreIngressNetworks` | Ingress入口 | 该接口用于查询某一个具体的Agent网关下的所有入站网络列表，不支持分页。适用场景：查询某一个具体的Agent网关下的所有入站网络列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreIngressNetworks.md) |
| 批量查询网关 | `ListCoreIngresses` | Ingress入口 | 该接口用于查询Ingress列表，支持按名称模糊匹配和分页查询。适用场景：查询租户下的所有Ingress列表。根据Ingress名称进行模糊查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreIngresses.md) |
| 查询Runtime资源实例列表 | `ListCoreRuntimeByTags` | 运行时 | 该接口用于根据标签过滤条件查询智能体运行时的资源列表。适用场景：根据标签条件查找对应的智能体运行时资源。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeByTags.md) |
| 查询RuntimeEndpoint资源实例列表 | `ListCoreRuntimeEndpointByTags` | 运行时 | 该接口用于根据标签过滤条件查询智能体运行时访问方式的资源列表。适用场景：根据标签条件查找对应的智能体运行时访问方式资源。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeEndpointByTags.md) |
| 查询RuntimeEndpoint标签列表 | `ListCoreRuntimeEndpointTags` | 运行时 | 该接口用于查询运行时访问方式的资源标签。适用场景：查询运行时访问方式的资源标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeEndpointTags.md) |
| 批量查询runtime访问方式 | `ListCoreRuntimeEndpoints` | 运行时 | 该接口用于根据运行时ID查询某一个具体的Agent运行时下的访问方式列表。支持分页查询。适用场景：根据Agent运行时ID查询该运行时的访问方式列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeEndpoints.md) |
| 查询当前可用的运行时规格 | `ListCoreRuntimeSpecs` | 运行时 | 该接口用于查询当前租户可用的智能体运行时CPU和内存规格组合列表。租户默认只能配置2U8G规格，如果需要配置其他规格，请提交工单申请。适用场景：创建或更新运行时前，查询可用的资源规格组合。接口约束：默认只返回2U8G规格，其他规格需要通过工单申请加入白名单后才会返回。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeSpecs.md) |
| 查询Runtime标签列表 | `ListCoreRuntimeTags` | 运行时 | 该接口用于查询运行时的资源标签。适用场景：查询运行时的资源标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeTags.md) |
| 批量查询版本 | `ListCoreRuntimeVersions` | 运行时 | 该接口用于根据运行时ID查询某一个具体的Agent运行时下的版本列表。支持分页查询。适用场景：根据Agent运行时ID查询该运行时的版本列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimeVersions.md) |
| 批量查询runtime | `ListCoreRuntimes` | 运行时 | 该接口用于查询Agent运行时列表。支持按多种条件筛选和分页查询。适用场景：根据Agent运行时名称查询运行时列表，支持精确匹配和模糊匹配。根据Agent运行时ID进行精确查询，支持批量查询多个运行时ID。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreRuntimes.md) |
| 获取内置记忆策略列表 | `ListCoreSpaceBuiltinStrategies` | 记忆空间 | 返回系统预置的内置记忆策略及其步骤详情，内置策略全局共享。内置策略不可修改，用户可根据内置策略创建自定义策略。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreSpaceBuiltinStrategies.md) |
| 根据标签查询记忆库列表 | `ListCoreSpaceByTags` | 记忆空间 | 该接口用于根据标签过滤条件查询智能体记忆库的资源列表。适用场景：根据标签条件查找对应的智能体记忆库资源。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreSpaceByTags.md) |
| 列出异步任务 | `ListCoreSpaceJobs` | 记忆空间 | 分页列出指定Space下的异步任务。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreSpaceJobs.md) |
| 查询记忆库标签列表 | `ListCoreSpaceTags` | 记忆空间 | 该接口用于查询记忆库的资源标签。适用场景：查询记忆库的资源标签。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreSpaceTags.md) |
| 列出所有Space | `ListCoreSpaces` | 记忆空间 | 查询租户下的所有记忆空间信息，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCoreSpaces.md) |
| 列出所有模型服务 | `ListCustomModelProviderModels` | 模型服务 | 检索所有模型服务，支持可选的过滤和分页功能。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCustomModelProviderModels.md) |
| 列出所有模型提供商 | `ListCustomModelProviders` | 模型服务 | 检索所有模型提供商，支持可选的过滤和分页功能。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListCustomModelProviders.md) |
| 查询模型管理配额 | `ListModelManagementQuotas` | 其他 | 获取当前认证账号的模型提供商、模型代理、模型的有效配额信息，包括配额类型、最小值、最大值、配额值和已使用数量。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListModelManagementQuotas.md) |
| 列出所有模型代理 | `ListModelProxies` | 其他 | 列出所有模型代理。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListModelProxies.md) |
| 根据条件查询日志 | `ListOpsAgentLog` | 观测数据 | 该接口用于条件查询日志。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsAgentLog.md) |
| 查询组件列表，包括工具，模型，skill列表 | `ListOpsAgentMetricLabelValues` | 观测数据 | 查询组件列表，包括工具，模型，skill列表。请参见如何调用API。当前API调用无需身份策略权限。POST /v1/ops/observation/agents/metric/label-values状态码：200状态码：400状态码：403状态码：429状态码：500状态码：200参数解释：响应码，用于标识接口调用结果。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsAgentMetricLabelValues.md) |
| 查询智能体列表 | `ListOpsAgentObservation` | 观测数据 | 在观测页面查询智能体列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsAgentObservation.md) |
| 查询agentRun的日志 | `ListOpsAgentRunLog` | 观测数据 | 该接口用于查询agentRun的日志。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsAgentRunLog.md) |
| 查询调用链span指标 | `ListOpsAgentSpanMetric` | 观测数据 | 该接口用于查询调用链详情页面中每个span的数据信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsAgentSpanMetric.md) |
| 获取评测集条目列表 | `ListOpsDatasetItems` | 评测集 | 该接口用于分页检索指定评测集的具体数据记录，支持查看当前草稿态数据或特定历史发布版本的数据样本。适用场景：内容预览：在评测集详情页分页展示具体的数据行，供用户直观核查数据质量。内容预览：在评测集详情页分页展示具体的数据行，供用户直观核查数据质量。版本溯源：通过指定版本ID，检索并对比历史发布版本中的样本数据。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetItems.md) |
| 获取评测集导入任务列表 | `ListOpsDatasetItemsImportTasks` | 评测集 | 该接口用于分页查询指定评测集下所有异步导入任务的执行状态、实时进度及详细统计信息，支持通过任务ID进行精确过滤。适用场景：进度查看：在提交大规模数据导入请求后，实时跟踪任务的完成百分比与当前处理状态。进度查看：在提交大规模数据导入请求后，实时跟踪任务的完成百分比与当前处理状态。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetItemsImportTasks.md) |
| 获取评测集 Schema | `ListOpsDatasetSchemas` | 评测集 | 该接口用于专门检索指定评测集信息，获取所有字段的名称、数据类型及约束规则，为数据处理提供标准的Schema视图。适用场景：数据导入校验：在用户上传或导入数据前，核对本地文件格式是否与评测集定义的字段规范一致。数据导入校验：在用户上传或导入数据前，核对本地文件格式是否与评测集定义的字段规范一致。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetSchemas.md) |
| 查询数据集TMS标签列表 | `ListOpsDatasetTags` | 评测集 | 该接口用于查询指定数据集的TMS标签列表。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetTags.md) |
| 获取评测集版本列表 | `ListOpsDatasetVersions` | 评测集 | 接口用于通过分页方式查询指定数据集下所有已成功发布的历史版本记录，按发布时间倒序排列，为用户提供数据集变更历史。适用场景：版本回溯：查看数据集的发布历史，追踪数据集随时间演进的变更记录。版本回溯：查看数据集的发布历史，追踪数据集随时间演进的变更记录。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetVersions.md) |
| 获取评测集列表 | `ListOpsDatasets` | 评测集 | 该接口用于分页查询当前项目下的评测集列表，支持按名称模糊检索和更新人筛选，帮助用户实现对评测集资产的全局视图管理。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasets.md) |
| 根据标签过滤查询数据集资源实例 | `ListOpsDatasetsByTags` | 评测集 | 该接口用于根据标签过滤查询数据集资源实例列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsDatasetsByTags.md) |
| 获取模型信息 | `ListOpsEvaluationModels` | 其他 | 该接口用于获取系统中所有可用的基础大模型及微调模型的详细列表，涵盖模型能力类型、状态及访问参数。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationModels.md) |
| 查询评估任务的自定义标签值 | `ListOpsEvaluationTaskCustomLabelValues` | 评估任务 | 该接口用于查询评估任务的自定义标签值，支持按标签ID和项目ID进行过滤查询，适用于标签数据查询和分析的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationTaskCustomLabelValues.md) |
| 查询评估任务的自定义标签列表 | `ListOpsEvaluationTaskCustomLabels` | 评估任务 | 该接口用于查询评估任务的所有自定义标签，返回标签ID、类型、创建时间等详细信息，支持分页查询和筛选，适用于标签管理和查询的场景。适用场景：查看评估任务使用的所有分类标记。查看评估任务使用的所有分类标记。分析自定义标签的使用情况和分布特征。分析自定义标签的使用情况和分布特征。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationTaskCustomLabels.md) |
| 查看任务评估结果 | `ListOpsEvaluationTaskResults` | 评估任务 | 该接口用于获取评估任务的详细评估结果，包括各项评估指标的分数、用时和详细信息，适用于任务结果分析和质量评估的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationTaskResults.md) |
| 查看评估任务列表 | `ListOpsEvaluationTasks` | 评估任务 | 该接口用于获取评估任务列表信息，支持条件筛选和分页查询，返回任务的基本信息和执行状态，适用于任务管理和监控的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationTasks.md) |
| 根据标签过滤查询评估任务资源实例 | `ListOpsEvaluationTasksByTags` | 评估任务 | 该接口用于根据标签过滤查询评估任务资源实例列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluationTasksByTags.md) |
| 获取评估器筛选选项列表 | `ListOpsEvaluatorFilterOptions` | 评估器 | 该接口用于获取评估器列表页面可用的筛选维度及其枚举值。前端通过此接口动态渲染筛选下拉框，帮助用户快速定位所需的评估器。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluatorFilterOptions.md) |
| 查询评估器TMS标签列表 | `ListOpsEvaluatorTags` | 评估器 | 该接口用于查询指定评估器的TMS标签列表。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluatorTags.md) |
| 获取评估器模板列表 | `ListOpsEvaluatorTemplates` | 评估器 | 该接口用于获取系统中的所有评估器模板信息列表，支持分页查询和条件筛选，适用于需要查看和管理评估器模板的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluatorTemplates.md) |
| 获取评估器所有版本信息 | `ListOpsEvaluatorVersions` | 评估器 | 该接口用于查询指定评估器下所有已发布的历史版本列表，提供各版本的发布时间、逻辑快照及版本状态。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluatorVersions.md) |
| 获取评估器信息列表 | `ListOpsEvaluators` | 评估器 | 该接口用于分页查询当前租户下所有已注册的评估器信息，支持按名称、类型或创建时间进行过滤评估器。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluators.md) |
| 根据标签过滤查询评估器资源实例 | `ListOpsEvaluatorsByTags` | 评估器 | 该接口用于根据标签过滤查询评估器资源实例列表，支持分页查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsEvaluatorsByTags.md) |
| 获取标签列表 | `ListOpsLabels` | 标签 | 该接口用于获取系统中所有标签的信息列表，支持分页查询和类型筛选，适用于标签管理和选择查询的场景。适用场景：查看系统中可用的所有标签资源。查看系统中可用的所有标签资源。在评估任务中选择合适的标签进行分类。在评估任务中选择合适的标签进行分类。看标签的详细信息，维护标签体系的完整性。看标签的详细信息，维护标签体系的完整性。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsLabels.md) |
| 查询会话列表 | `ListOpsSession` | 会话 | 该接口用于查询会话列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsSession.md) |
| 查询合成的条目列表 | `ListOpsSynthesisItems` | 其他 | 该接口用于分页查询特定合成任务所生成的详细条目数据，支持在任务运行中和检索样本内容。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsSynthesisItems.md) |
| 查询评测集合成任务列表 | `ListOpsSynthesisTasks` | 评测集合成 | 该接口用于分页查询当前租户下所有已提交的评测集合成异步任务，支持按任务名称、状态等多种过滤条件进行检索，提供任务执行进度。适用场景：任务进度查看：在发起大规模数据合成后，通过此接口批量获取任务的运行状态（如：进行中、已完成、已失败）。任务进度查看：在发起大规模数据合成后，通过此接口批量获取任务的运行状态（如：进行中、已完成、已失败）。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsSynthesisTasks.md) |
| 获取三方托管智能体列表 | `ListOpsThirdPartyAgents` | 第三方智能体 | 该接口用于分页获取三方托管智能体和智能体运行时的配置列表，包含基本信息和调试状态。适用场景：列表查询：查看租户下所有已配置的三方智能体和智能体运行时。列表查询：查看租户下所有已配置的三方智能体和智能体运行时。筛选查询：按类型（third_party_agent/agent_runtime）筛选。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsThirdPartyAgents.md) |
| 查询trace列表 | `ListOpsTrace` | Trace调用链 | 该接口用于分页查询调用链列表。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ListOpsTrace.md) |

## 查询详情/状态（Show，56）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 查询浏览器 Session | `ShowBrowserSession` | 其他 | 该 API 用于查询一个浏览器 Session 的详情，包括状态、视口、streams 等元数据。请参见如何调用API。当前API调用无需身份策略权限。GET https://agentarts.com/v1/browsers/{browser_name}/sessions-get状态码：200无无无请参见错误码。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowBrowserSession.md) |
| 查询session | `ShowCodeInterpreterSession` | 其他 | 该API用于查询一个代码解释器的Session详情。请参见如何调用API。当前API调用无需身份策略权限。GET /v1/code-interpreters/{code_interpreter_name}/sessions-get状态码：200状态码：401状态码：200OK状态码：400请求参数错误。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCodeInterpreterSession.md) |
| 查询浏览器详情 | `ShowCoreBrowser` | 浏览器 | 该API用于查询浏览器详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreBrowser.md) |
| 根据标签查询浏览器数量 | `ShowCoreBrowserNumsByTags` | 浏览器 | 该API用于根据标签查询浏览器数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreBrowserNumsByTags.md) |
| 查询浏览器配置详情 | `ShowCoreBrowserProfile` | 浏览器 | 该API用于查询浏览器配置详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreBrowserProfile.md) |
| 根据标签查询浏览器配置数量 | `ShowCoreBrowserProfileNumsByTags` | 浏览器 | 该API用于根据标签查询浏览器配置数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreBrowserProfileNumsByTags.md) |
| 查询浏览器会话详情 | `ShowCoreBrowserSession` | 浏览器 | 该API用于查询浏览器会话详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreBrowserSession.md) |
| 查询代码解释器详情 | `ShowCoreCodeInterpreter` | 代码解释器 | 该API用于查询代码解释器详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreCodeInterpreter.md) |
| 根据标签查询代码解释器数量 | `ShowCoreCodeInterpreterNumsByTags` | 代码解释器 | 该API用于根据标签查询代码解释器数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreCodeInterpreterNumsByTags.md) |
| 获取网关详情 | `ShowCoreGateway` | 网关 | 通过 ID 获取指定网关的详细信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreGateway.md) |
| 根据标签查询网关数量 | `ShowCoreGatewayNumsByTags` | 网关 | 根据标签查询网关数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreGatewayNumsByTags.md) |
| 获取目标服务详情 | `ShowCoreGatewayTarget` | 网关 | 获取指定目标服务的详细信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreGatewayTarget.md) |
| 查询网关详情 | `ShowCoreIngress` | Ingress入口 | 该接口用于根据ingress_id查询Ingress的详细信息。适用场景：查询某一个具体的Ingress详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreIngress.md) |
| 查询VPC入站网络详情 | `ShowCoreIngressNetwork` | Ingress入口 | 该接口用于根据网关ID以及入站网络ID查询某一个具体的Agent网关入站网络详情。适用场景：查询某一个具体的Agent网关入站网络详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreIngressNetwork.md) |
| 查询单个runtime及指定版本详情 | `ShowCoreRuntime` | 运行时 | 该接口用于根据Agent运行时ID查询对应的Agent运行时详细信息。该接口可通过version参数指定查询特定版本，不指定则返回最新版本。适用场景：查询某一个具体的Agent运行时最新版本、指定版本的详细信息。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreRuntime.md) |
| 查询单个runtime访问方式 | `ShowCoreRuntimeEndpoint` | 运行时 | 该接口用于根据Agent运行时ID和访问方式ID查询对应的Agent运行时访问方式详细信息。适用场景：查询某一个具体的Agent运行时访问方式的详细信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreRuntimeEndpoint.md) |
| 查询RuntimeEndpoint资源实例数量 | `ShowCoreRuntimeEndpointNumsByTags` | 运行时 | 该接口用于根据标签过滤条件查询智能体运行时访问方式的资源数量。适用场景：根据标签条件查找对应的智能体运行时访问方式资源数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreRuntimeEndpointNumsByTags.md) |
| 查询Runtime资源实例数量 | `ShowCoreRuntimeNumsByTags` | 运行时 | 该接口用于根据标签过滤条件查询智能体运行时的资源数量。适用场景：根据标签条件查找对应的智能体运行时资源数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreRuntimeNumsByTags.md) |
| 获取Space详情 | `ShowCoreSpace` | 记忆空间 | 根据记忆空间ID获取记忆空间详细信息，包含完整配置和记忆策略。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreSpace.md) |
| 查询异步任务详情 | `ShowCoreSpaceJob` | 记忆空间 | 查询服务异步任务详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreSpaceJob.md) |
| 根据标签查询记忆库数量 | `ShowCoreSpaceNumsByTags` | 记忆空间 | 该接口用于根据标签过滤条件查询记忆库的资源数量。适用场景：根据标签条件查找对应的记忆库的资源数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCoreSpaceNumsByTags.md) |
| 获取模型提供商详情 | `ShowCustomModelProvider` | 模型服务 | 获取模型提供商详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCustomModelProvider.md) |
| 获取模型服务详情 | `ShowCustomModelProviderModel` | 模型服务 | 获取模型服务详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowCustomModelProviderModel.md) |
| 查询时间范围内智能体的总数、草稿数、发布态数 | `ShowOpsAgentMetric` | 观测数据 | 该接口用于查询指定时间范围内智能体（单智能体、工作流、多智能体）的总数、草稿数、发布态数。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsAgentMetric.md) |
| 查询指标的数据 | `ShowOpsAgentMetricGauge` | 观测数据 | 该接口用于查询智能体指标的数据信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsAgentMetricGauge.md) |
| 查询指标的topN | `ShowOpsAgentMetricTopN` | 观测数据 | 该接口用于查询智能体指标的topN排行柱状图数据。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsAgentMetricTopN.md) |
| 查询指标趋势图 | `ShowOpsAgentMetricTrend` | 观测数据 | 该接口用于查询智能体的指标趋势图。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsAgentMetricTrend.md) |
| 获取评测集详情 | `ShowOpsDataset` | 评测集 | 该接口用于根据评测集ID获取其完整的元数据配置，包括字段结构定义、基本属性及关联的历史发布版本列表。适用场景：评测配置校验：在启动评估任务前，开发者通过此接口确认评测集的字段是否符合评估任务输入要求。评测配置校验：在启动评估任务前，开发者通过此接口确认评测集的字段是否符合评估任务输入要求。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsDataset.md) |
| 获取评测集条目详情 | `ShowOpsDatasetItem` | 评测集 | 该接口用于精确获取评测集中某一行特定数据条目的完整内容，通过评测集ID与条目ID的双重定位。适用场景：单条样本核对：在对模型评测结果产生疑问时，调取对应原始数据条目的全量信息进行比对。单条样本核对：在对模型评测结果产生疑问时，调取对应原始数据条目的全量信息进行比对。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsDatasetItem.md) |
| 根据标签统计数据集资源实例数量 | `ShowOpsDatasetNumsByTags` | 评测集 | 该接口用于根据标签统计数据集资源实例数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsDatasetNumsByTags.md) |
| 获取评测集版本详情 | `ShowOpsDatasetVersion` | 评测集 | 该接口用于通过指定版本ID检索特定历史版本的完整元数据，包含发布时的Schema结构快照、数据规模统计及版本属性。适用场景：历史版本对比：核对已发布评测集在特定时间点的字段定义、数据规模和配置参数。历史版本对比：核对已发布评测集在特定时间点的字段定义、数据规模和配置参数。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsDatasetVersion.md) |
| 获取单个模型信息 | `ShowOpsEvaluationModel` | 其他 | 该接口用于通过模型ID获取特定大模型的详细元数据，包含其技术规格、版本信息、支持的协议能力及服务终点。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationModel.md) |
| 查询配额维度的免费配额和总配额信息 | `ShowOpsEvaluationQuota` | 其他 | 该接口用于查询配额维度的免费配额和总配额信息。适用场景：查询评测任务或合成任务的免费配额使用情况。查询评测任务或合成任务的免费配额使用情况。查询指定配额维度的总配额限制和已用数量。查询指定配额维度的总配额限制和已用数量。不传type参数时，返回所有7个配额维度的信息。不传type参数时，返回所有7个配额维度的信息。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationQuota.md) |
| 查看评估任务详情 | `ShowOpsEvaluationTask` | 评估任务 | 该接口用于获取评估任务的详细信息，包括任务配置、状态、统计结果等完整信息，适用于任务详情查看的场景。适用场景：查看评估任务的完整配置和执行状态。查看评估任务的完整配置和执行状态。分析任务运行过程中的性能和结果统计信息。分析任务运行过程中的性能和结果统计信息。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTask.md) |
| 统计一个任务的所有自定义标签的标签项分布 | `ShowOpsEvaluationTaskChartsLabelsDistribution` | 评估任务 | 该接口用于统计评估任务中自定义标签的分布情况，支持文本标签和布尔标签的分类统计，适用于数据特征分析和标签管理的场景。适用场景：- 分析评估数据中标签的分布特征和规律。- 自定义标签的使用频率和覆盖范围。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskChartsLabelsDistribution.md) |
| 统计每个任务的评估器得分分布 | `ShowOpsEvaluationTaskChartsScoreDistribution` | 评估任务 | 该接口用于获取评估任务中各评估器的得分分布情况，统计不同分数区间的样本数量，适用于评估结果可视化分析的场景。适用场景：- 查看评估得分的分布特征和集中趋势。- 识别评估结果中高分和低分样本的比例。- 分析评估模型的评分一致性和区分度。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskChartsScoreDistribution.md) |
| 某个任务的所有评估器得分统计 | `ShowOpsEvaluationTaskChartsScoreStats` | 评估任务 | 该接口用于获取指定评测任务中各评估维度的得分分布与汇总统计，通过聚合多个评估器的分值数据，生成反映模型各方面能力指标视图。适用场景：模型能力多维诊断：对比同一任务下不同评估器（如：逻辑性得分 vs 准确性得分）的统计表现，精准识别模型的优势与短板。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskChartsScoreStats.md) |
| 获取任务的成功数和失败数 | `ShowOpsEvaluationTaskChartsStatus` | 评估任务 | 该接口用于获取指定评测任务的执行状态分布统计，返回任务中各数据条目的成功与失败数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskChartsStatus.md) |
| 获取评估任务的洞察结果 | `ShowOpsEvaluationTaskInsights` | 评估任务 | 该接口用于获取评估任务的洞察结果，返回任务综合指标评分、高频异常分布及对应的链路诊断结果与修复策略的文本内容。适用场景：获取任务维度的多维量化评分结果，用于衡量并对比被评估对象的综合基准表现。获取任务维度的多维量化评分结果，用于衡量并对比被评估对象的综合基准表现。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskInsights.md) |
| 根据标签统计评估任务资源实例数量 | `ShowOpsEvaluationTaskNumsByTags` | 评估任务 | 该接口用于根据标签统计评估任务资源实例数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTaskNumsByTags.md) |
| 获取评估任务统计结果 | `ShowOpsEvaluationTasksChartsCompareResult` | 评估任务 | 该接口用于统计不同评估任务的对比结果报告，包含评估器得分情况、得分概览、任务消耗总token统计，适用于数据特征分析和评估任务管理的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTasksChartsCompareResult.md) |
| 获取评估任务对比结果 | `ShowOpsEvaluationTasksCompareResult` | 评估任务 | 该接口用于统计不同评估任务的对比结果，包含每个任务在每个评估器的得分情况、每个评估器得分、任务状态、任务耗时、任务消耗总token，适用于数据特征分析和评估任务管理的场景。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluationTasksCompareResult.md) |
| 获取评估器信息 | `ShowOpsEvaluator` | 评估器 | 该接口用于通过指定的评估器ID检索其完整定义信息，包括判分逻辑、参数配置、关联模型及元数据详情，是核对特定评测标准执行细节的核心入口。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluator.md) |
| 根据标签统计评估器资源实例数量 | `ShowOpsEvaluatorNumsByTags` | 评估器 | 该接口用于根据标签统计评估器资源实例数量。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluatorNumsByTags.md) |
| 获取评估器模板 | `ShowOpsEvaluatorTemplate` | 评估器 | 该接口用于根据模板ID获取特定评估器模板的详细信息，支持查询模板的完整配置和使用说明，适用于需要深入了解特定模板配置的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluatorTemplate.md) |
| 获取评估器单个版本信息 | `ShowOpsEvaluatorVersion` | 评估器 | 该接口用于通过评估器ID与版本ID获取特定版本的详细快照信息，包括该版本固化的判分逻辑、Prompt 模板、参数权重及生效配置。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsEvaluatorVersion.md) |
| 获取标签详情 | `ShowOpsLabel` | 标签 | 该接口用于获取标签的详细信息，包括标签名称、类型、描述和关联的标注项，适用于标签详情查看和标签管理的场景。适用场景：查看标签的完整配置信息和关联内容。查看标签的完整配置信息和关联内容。审核和验证标签的使用范围和限制。审核和验证标签的使用范围和限制。标签系统维护和数据质量检查。标签系统维护和数据质量检查。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsLabel.md) |
| 获取当前项目的配额 | `ShowOpsQuota` | 其他 | 该接口用于获取当前项目的配额信息，支持查询各类任务的数量上限和剩余配额，适用于资源管理和容量规划的场景。适用场景：任务创建前查询当前项目的资源限制和剩余容量，避免因配额不足导致任务创建失败。任务创建前查询当前项目的资源限制和剩余容量，避免因配额不足导致任务创建失败。查看各类任务的已用配额和总量，掌握项目的资源消耗状况。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsQuota.md) |
| 查询会话详情 | `ShowOpsSession` | 会话 | 该接口用于查询会话详情。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSession.md) |
| 查询租户关联的AOM信息 | `ShowOpsSubscriptionAomInfo` | 其他 | 该接口用于查询租户关联的AOM信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSubscriptionAomInfo.md) |
| 查询租户关联的APM信息 | `ShowOpsSubscriptionApmInfo` | 其他 | 该接口用于查询租户关联的APM信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSubscriptionApmInfo.md) |
| 查询租户关联的AOM /APM /LTS信息 | `ShowOpsSubscriptionInfo` | 其他 | 查询租户关联的AOM/APM/LTS信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSubscriptionInfo.md) |
| 查询租户关联的LTS信息 | `ShowOpsSubscriptionLtsInfo` | 其他 | 该接口用于查询租户关联的LTS信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSubscriptionLtsInfo.md) |
| 查询评测集合成任务详情 | `ShowOpsSynthesisTask` | 评测集合成 | 该接口用于通过任务ID检索特定评测集合成任务的完整信息，涵盖任务配置快照、实时执行状态及生成统计。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsSynthesisTask.md) |
| 获取三方托管智能体配置 | `ShowOpsThirdPartyAgent` | 第三方智能体 | 该接口用于获取三方托管智能体的配置信息，包含调用参数和调试状态。配置信息在调试接口调用成功后自动保存至数据库。适用场景：查看配置：查看三方智能体已保存的调用配置信息。查看配置：查看三方智能体已保存的调用配置信息。确认调试状态：确认三方智能体是否已调试通过，评估任务创建时需引用已调试通过的配置。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsThirdPartyAgent.md) |
| 查询调用链详细信息 | `ShowOpsTrace` | Trace调用链 | 该接口用于查询调用链详细信息。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ShowOpsTrace.md) |

## 启动（Start，3）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 启动浏览器 Session | `StartBrowserSession` | 其他 | 该 API 用于启动一个浏览器 Session。Gateway 拉起 Sandbox 容器后调用此接口，容器内 browser-server 启动 Chrome 及相关组件，轮询 /ping 直到状态非 Initing 即视为就绪。支持可选配置：视口大小、浏览器 Profile 加载、代理配置、域名白/黑名单。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/StartBrowserSession.md) |
| 启动session | `StartCodeInterpreterSession` | 其他 | 该API用于启动一个代码解释器的Session。请参见如何调用API。当前API调用无需身份策略权限。PUT /v1/code-interpreters/{code_interpreter_name}/sessions-start状态码：200状态码：401状态码：200OK状态码：400请求参数错误。 | [打开](https://support.huaweicloud.com/api-agentarts/StartCodeInterpreterSession.md) |
| 创建智能体运行时会话 | `StartRuntimeSession` | 运行时数据面 | 该接口用于创建智能体运行时会话。请参见如何调用API。当前API调用无需身份策略权限。POST /runtimes/{runtime_name}/sessions-start状态码：200状态码：401状态码：500启动运行时会话, gateway_domain为运行时的访问域名，可以在智能体运行时的运行时详情页面中获取无请参见错误码。 | [打开](https://support.huaweicloud.com/api-agentarts/StartRuntimeSession.md) |

## 停止（Stop，5）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 停止浏览器 Session | `StopBrowserSession` | 其他 | 该 API 用于停止指定的浏览器 Session。停止时将触发以下动作：关闭所有客户端 WebSocket 连接（automation %%livestream）关闭所有客户端 WebSocket 连接（automation %%livestream）通知 Sandbox 销毁容器通知 Sandbox 销毁容器请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/StopBrowserSession.md) |
| 停止session | `StopCodeInterpreterSession` | 其他 | 该API用于停止指定的代码解释器的Session。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/StopCodeInterpreterSession.md) |
| 终止浏览器会话 | `StopCoreBrowserSession` | 浏览器 | 该API用于终止浏览器会话。在调用15s后会话终止。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/StopCoreBrowserSession.md) |
| 暂停评估任务 | `StopOpsEvaluationTask` | 评估任务 | 该接口用于暂停正在运行的评估任务，支持临时任务执行控制，适用于任务调度的场景。适用场景：暂停长时间运行的评估任务以释放资源。暂停长时间运行的评估任务以释放资源。在发现问题时临时停止任务执行。在发现问题时临时停止任务执行。调整任务执行优先级和时间安排。调整任务执行优先级和时间安排。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/StopOpsEvaluationTask.md) |
| 停止智能体运行时会话 | `StopRuntimeSession` | 运行时数据面 | 该接口用于根据会话唯一标识对智能体运行时的会话进行销毁操作。适用场景：适用场景：使用智能体运行时（高代码）接口创建会话后，需要将会话对应的实例进行停止的场景。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/StopRuntimeSession.md) |

## 执行（Execute，6）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 执行数据面请求调用 | `ExecuteCode` | 其他 | 该API用于在沙箱中执行各类操作请求，比如执行代码、执行命令、写入文件、读取文件、列出文件、删除文档等操作。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ExecuteCode.md) |
| 调用智能体运行时 | `ExecuteRuntime` | 运行时数据面 | 该接口用于调用已经部署好的高代码智能体运行时，部署智能体运行时请参见部署智能体运行时。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/InvokeRuntime1.md) |
| 调用智能体运行时--执行命令 | `ExecuteRuntimeCommands` | 运行时数据面 | 该接口用于调用已经部署好的高代码智能体运行时，在智能体内执行命令。部署智能体运行时请参见部署智能体运行时。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ExecuteRuntimeCommands.md) |
| 调用智能体运行时--下载文件 | `ExecuteRuntimeDownloadFiles` | 运行时数据面 | 该接口用于调用已经部署好的高代码智能体运行时，在智能体内下载文件。部署智能体运行时请参见部署智能体运行时。请参见如何调用API。当前API调用无需身份策略权限。 | [打开](https://support.huaweicloud.com/api-agentarts/ExecuteRuntimeDownloadFiles.md) |
| 调用智能体运行时--上传文件 | `ExecuteRuntimeUploadFiles` | 运行时数据面 | 该接口用于调用已经部署好的高代码智能体运行时，上传文件到智能体内的目标路径。 | [打开](https://support.huaweicloud.com/api-agentarts/ExecuteRuntimeUploadFiles.md) |
| 调用智能体运行时的自定义接口 | `ExecuteRuntimeWithPrefix` | 运行时数据面 | 该接口用于使用前缀匹配方式调用已经部署好的高代码智能体运行时的自定义接口，使用该接口需要确保智能体运行时的URL的匹配模式设置为PREFIX_MATCH前缀匹配，部署智能体运行时请参见部署智能体运行时。此API实际上支持所有 HTTP 方法（包括不限于POST、GET、DELETE、PUT等），请按照后端实际的接口方法进行调用。 | [打开](https://support.huaweicloud.com/api-agentarts/ExecuteRuntimeWithPrefix.md) |

## 调用（Invoke，4）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 执行浏览器操作 | `InvokeBrowser` | 其他 | 该 API 用于在浏览器 Session 中执行结构化操作，包括导航、鼠标点击/拖拽、键盘输入、滚动、截图、获取页面信息、Tab 管理等。请求体采用 UNION 结构（对齐 AWS BrowserAction），action 对象中每次仅设置一个成员。同一 Session 内的 invoke 请求串行执行（session 级锁）。 | [打开](https://support.huaweicloud.com/api-agentarts/InvokeBrowser.md) |
| 调用MCP网关 | `InvokeMcpGateway` | 其他 | 该接口用于调用已创建并配置好Target的MCP网关。请参见如何调用API。当前API调用无需身份策略权限。POST /mcp状态码：200状态码：401状态码：500无请参见错误码。 | [打开](https://support.huaweicloud.com/api-agentarts/InvokeMcpGateway.md) |
| 细粒度评估 | `InvokeOpsFineGrainedEvaluation` | 其他 | 该接口提供细粒度评估能力，基于评估器维度，无需预先创建评测集和评估任务，只需指定评估器并传入待评估数据即可完成评估，评估结果通过流式（SSE）或非流式方式返回。适用场景：场景1（dataset）：对已有的输入输出数据进行评估评分。场景1（dataset）：对已有的输入输出数据进行评估评分。 | [打开](https://support.huaweicloud.com/api-agentarts/InvokeOpsFineGrainedEvaluation.md) |
| 调用运行时 | `InvokeRuntime` | 运行时数据面 | 该接口用于运行场景化应用，支持在指定的智能体、工作流中执行。接口支持流式响应模式，可以根据需要返回增量执行结果，适用于实时交互场景。适用场景：在项目中运行预定义的工作流/智能体。在项目中运行预定义的工作流/智能体。支持调试模式和发布模式，适用于不同开发和生产环境。支持调试模式和发布模式，适用于不同开发和生产环境。 | [打开](https://support.huaweicloud.com/api-agentarts/InvokeRuntime.md) |

## 检查（Check，1）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 检查新建评估任务名称是否存在 | `CheckOpsEvaluationTaskName` | 评估任务 | 该接口用于检查指定的评估任务名称是否已存在，返回名称唯一性验证结果，适用于创建新任务前验证任务名称可用性的场景。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/CheckOpsEvaluationTaskName.md) |

## 重置（Reset，1）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 重置 API Key | `ResetCoreSpaceApiKey` | 记忆空间 | 异步重置指定 Space 的 API Key，旧 Key 立即失效。若当前处于由 API Key 认证切换至 IAM 认证的“宽限期”，调用本接口会导致原 API Key 立即失效。请参见如何调用API。 | [打开](https://support.huaweicloud.com/api-agentarts/ResetCoreSpaceApiKey.md) |

## 保存（Save，1）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 保存浏览器 Profile | `SaveBrowserProfile` | 其他 | 该 API 用于将当前浏览器 Session 的状态（cookie %%localStorage %%sessionStorage）保存到指定的 Profile。通过 CDP 提取浏览器状态后打包上传到 OBS，覆盖之前的 Profile 数据。Profile 不自动保存，需由 SDK %%Agent 在合适时机（如登录成功后）显式调用。 | [打开](https://support.huaweicloud.com/api-agentarts/SaveBrowserProfile.md) |

## 同步（Sync，1）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 同步网关目标工具列表 | `SyncCoreGatewayTargets` | 网关 | 同步网关目标工具列表，同步状态可通过查询目标详情查询。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/SyncCoreGatewayTargets.md) |

## 标注（Tag，1）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| Trace数据标注 | `TagOpsTraceLabel` | Trace调用链 | 该接口用于给调用链数据进行数据标注。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/TagOpsTraceLabel.md) |

## 发布（Publish，2）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 发布评测集版本 | `PublishOpsDatasetVersion` | 评测集 | 该接口用于将当前处于草稿状态的数据内容固化，生成一个不可变的历史快照版本，并分配唯一版本ID以确保数据在后续调用中的可追溯性。适用场景：版本固化：在完成评测集条目的增删改等一系列调整后，通过发布版本将当前数据状态锁定。版本固化：在完成评测集条目的增删改等一系列调整后，通过发布版本将当前数据状态锁定。 | [打开](https://support.huaweicloud.com/api-agentarts/PublishOpsDatasetVersion.md) |
| 发布评估器新版本 | `PublishOpsEvaluatorVersion` | 评估器 | 该接口用于为指定的评估器创建并发布一个全新的快照版本，通过固化当前的判分逻辑与参数配置，实现评测标准的版本化管理与历史可追溯。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/PublishOpsEvaluatorVersion.md) |

## 生成（Generate，2）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 智能生成G-Eval评估步骤 | `GenerateOpsEvaluatorEvaluationSteps` | 评估器 | 该接口用于根据用户提供的规则描述(criteria)，利用大模型自动生成结构化的评估步骤。通过自适应的方式降低用户编写评估提示词的门槛，提升评估器配置效率。约束限制：criteria长度必须在1到20000之间。criteria长度必须在1到20000之间。criteria必须包含{{}}格式的变量。 | [打开](https://support.huaweicloud.com/api-agentarts/GenerateOpsEvaluatorEvaluationSteps.md) |
| 获取多模态文件上传地址 | `GenerateOpsMultimodalUploadUrl` | 其他 | 该接口用于生成OBS预签名上传链接和对应的OBS路径，供用户上传多模态文件（如PPT等）。用户使用返回的上传链接将文件上传至OBS后，可在细粒度评估接口中传入OBS路径进行评估。约束限制：同一用户未使用的上传链接数量上限为5个。同一用户未使用的上传链接数量上限为5个。上传链接有效期为15分钟。上传链接有效期为15分钟。 | [打开](https://support.huaweicloud.com/api-agentarts/GenerateOpsMultimodalUploadUrl.md) |

## 导入（Import，2）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 评测集导入 | `ImportOpsDatasetItems` | 评测集 | 该接口用于从本地文件或历史版本中将海量数据批量导入至指定评测集的草稿版本中，支持多种格式解析及灵活的写入模式。适用场景：评测集同步：将存储在OBS（对象存储服务）中的海量生产数据或标注数据自动化同步至评测系统。评测集同步：将存储在OBS（对象存储服务）中的海量生产数据或标注数据自动化同步至评测系统。 | [打开](https://support.huaweicloud.com/api-agentarts/ImportOpsDatasetItems.md) |
| 导入结果到评测集 | `ImportOpsResults` | 其他 | 将条目导入到目标评测集，支持导入到现有评测集或创建新评测集。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/ImportOpsResults.md) |

## 调试（Debug，2）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 评估器调试 | `DebugOpsEvaluator` | 评估器 | 该接口用于对评估器的判分逻辑进行实时调试，通过输入样例数据验证评估器的解析能力、Prompt 效果及评分准确性。请参见如何调用API。账号根用户具备所有API的调用权限，如果使用账号下的IAM用户调用当前API，该IAM用户需具备如下身份策略权限，更多的权限说明请参见权限和授权项。 | [打开](https://support.huaweicloud.com/api-agentarts/DebugOpsEvaluator.md) |
| 调试三方托管智能体 | `DebugOpsThirdPartyAgent` | 第三方智能体 | 该接口用于调试三方托管智能体或智能体运行时，向Agent发送测试请求，验证调用配置的正确性。调试成功后，配置自动保存至数据库并记录调试状态。三方智能体的身份信息（ID、名称）从可观测服务获取，调用参数（API地址、鉴权、请求参数、响应模式等）由评估服务管理并持久化存储。 | [打开](https://support.huaweicloud.com/api-agentarts/DebugOpsThirdPartyAgent.md) |

## 其他（Other，7）

| 中文标题 | Operation | 资源域 | 官方摘要 | 官方详情 |
| --- | --- | --- | --- | --- |
| 智能体运行时身份策略授权参考 | `智能体运行时身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission2.md) |
| 沙箱工具身份策略授权参考 | `沙箱工具身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission0.md) |
| 网关身份策略授权参考 | `网关身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission1.md) |
| 观测身份策略授权参考 | `观测身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission3.md) |
| 记忆库身份策略授权参考 | `记忆库身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission5_0.md) |
| 评估身份策略授权参考 | `评估身份策略授权参考` | 其他 | 云服务在IAM预置了常用的权限，称为系统身份策略。如果IAM系统身份策略无法满足授权要求，管理员可以根据各服务支持的授权项，创建IAM自定义身份策略来进行精细的访问控制，IAM自定义身份策略是对系统身份策略的扩展和补充。 | [打开](https://support.huaweicloud.com/api-agentarts/Permission4.md) |
| 错误码 | `错误码` | 其他 | 当您调用API时，如果遇到“APIGW”开头的错误码，请参见API网关错误码进行处理。 | [打开](https://support.huaweicloud.com/api-agentarts/ErrorCode.md) |

