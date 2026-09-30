# 官方 API 使用指南索引

> 共 17 个指南；这些页面解释调用流程，具体资源 API 见 [完整目录](../00-overview/api_catalog.md)。

- [使用前必读](https://support.huaweicloud.com/api-agentarts/agentarts_07_0001.md): 欢迎使用AgentArts服务。AgentArts是一个企业级一站式智能体构建与运营平台。它打破了传统开发壁垒，支持Agent开发人员通过可视化、低代码的方式，快速搭建从简单助手到复杂业务流的各类AI应用。您可以使用本文档提供API对AgentArts进行相关操作，如调用运行时等。支持的全部操作请参见API概览。
- [API概览](https://support.huaweicloud.com/api-agentarts/agentarts_07_0002.md): 华为云帮助中心，为用户提供产品简介、价格说明、购买指南、用户指南、API参考、最佳实践、常见问题、视频帮助等技术文档，帮助您快速上手使用华为云服务。
- [构造请求](https://support.huaweicloud.com/api-agentarts/agentarts_07_0004.md): 本节介绍REST API请求的组成，并以调用IAM服务的管理员创建IAM用户接口说明如何调用API。请求URI由如下部分组成。{URI-scheme}:// {Endpoint} / {resource-path} ?
- [认证鉴权](https://support.huaweicloud.com/api-agentarts/agentarts_07_0005.md): 智能体在初次部署时，可以选择认证方式。再次调整智能体，重新进行部署时，认证方式无法进行修改。如果认证方式选择错误，目前需要重新创建一个新的智能体。可以使用智能体的“复制”功能快速创建同样的一个智能体。AK/SK认证就是使用AK/SK对请求进行签名，在请求时将签名信息添加到消息头，从而通过身份认证。
- [返回结果](https://support.huaweicloud.com/api-agentarts/agentarts_07_0006.md): 请求发送以后，您会收到响应，包含状态码、响应消息头和消息体。状态码是一组从1xx到5xx的数字代码，状态码表示了请求响应的状态，完整的状态码列表请参见状态码。对于管理员创建IAM用户接口，如果调用后返回状态码为“201”，则表示请求成功。对应请求消息头，响应同样也有消息头，如“Content-type”。
- [状态码](https://support.huaweicloud.com/api-agentarts/agentarts_07_0016.md): 状态码如表1所示。
- [使用API调用运行时接口（IAM认证）](https://support.huaweicloud.com/api-agentarts/agentarts_07_0033.md): 本指南面向通过编写代码并将智能体托管到AgentArts运行时的开发者，介绍如何使用IAM认证（AK/SK 签名）方式调用已部署的智能体运行时API。与平台“低码开发智能体”模式不同，托管运行时允许您完全自定义智能体逻辑，并以标准HTTP服务形式部署。
- [使用API调用运行时接口（API Key认证）](https://support.huaweicloud.com/api-agentarts/agentarts_07_0035.md): 本指南面向通过编写代码并将智能体托管到AgentArts运行时的开发者，介绍如何使用API Key认证调用已部署的智能体运行时API。与IAM认证相比，API Key认证方式更为轻量，无需进行复杂的请求签名，仅需在请求头中携带平台颁发的鉴权参数即可完成鉴权。本指南将详细说明如何获取API Key、构造请求。
- [使用API调用观测接口](https://support.huaweicloud.com/api-agentarts/agentarts_07_0037.md): 此类接口与单/多智能体、工作流的调用方式有所差异。认证鉴权信息中的Authorization、X-Sdk-Date的值需要通过一个API签名SDK获取。
- [使用API调用评估接口](https://support.huaweicloud.com/api-agentarts/agentarts_07_0039.md): 本案例以Python调用评估功能中的“获取评测集列表”接口（GET /v1/ops/datasets）为例进行讲解。不需要在AgentArts平台上创建评测集也可以调用该接口。已开通AgentArts服务。
- [使用API调用单/多智能体](https://support.huaweicloud.com/api-agentarts/agentarts_07_0046.md): 在AgentArts平台上开发完成智能体后，其最终目的是要融入企业的核心业务流中。为了实现上述集成，AgentArts提供了标准的RESTful API。
- [使用API调用工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0047.md): 在AgentArts平台上开发完成工作流后，其最终目的是要融入企业的核心业务流中。为了实现上述集成，AgentArts提供了标准的RESTful API。
- [使用API调用图像理解工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0048.md): 本案例中搭建一个图像理解工作流，实现通过多模态模型进行图像识别，并通过标准的RESTful API进行调用。工作流部署时采用API Key认证，API调用也采用该方法。图像理解工作流的搭建、参数配置和文本类工作流存在差异，详见步骤一：搭建图像理解工作流。
- [使用API调用文档解析智能体](https://support.huaweicloud.com/api-agentarts/agentarts_07_0049.md): 在AgentArts平台上开发单智能体时，部分业务场景需要智能体具备文档理解能力，例如：合同审核场景中智能体需读取用户上传的合同文件并提取关键条款；技术文档分析场景中需对产品手册、接口文档进行结构化解析；报告生成场景中需先读取参考文档再进行内容总结。文档理解能力依赖智能体中挂载的文档解析插件或MCP实现。
- [使用API调用文档解析工作流](https://support.huaweicloud.com/api-agentarts/agentarts_07_0050.md): 在AgentArts平台上开发工作流时，部分业务场景需要工作流具备文档理解能力，例如：合同审核场景中需读取用户上传的合同文件并提取关键条款。文档理解能力依赖工作流中的插件节点、MCP节点或代码节点等方式实现。
- [常见问题](https://support.huaweicloud.com/api-agentarts/agentarts_07_0051.md): 调用API时出现{"code":401,"data":null,"message":"Authorization failed!"}报错，表示Authorization失效，请重新获取。调用智能体/工作流接口：请参考步骤二：获取API调用凭证（获取Authorization）重新获取Authorization。
- [使用API调用单/多智能体（IAM认证）](https://support.huaweicloud.com/api-agentarts/agentarts_07_0052.md): 本案例介绍如何通过IAM认证（AK/SK签名）的方式，调用智能体的API接口。与API Key认证的主要区别：IAM认证使用您华为云账号的访问密钥（AK/SK）进行请求签名，无需在平台单独管理API Key，更适合企业级应用集成场景，权限管控由统一的IAM服务管理。
