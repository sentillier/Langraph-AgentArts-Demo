# CLI 命令参考

> 入口：`agentarts`（Typer + Rich）。全局选项：`--version/-v`、`--verbose`（DEBUG 日志）。首次运行自动安装 shell 补全。

## 1. 顶层命令清单

| 命令 | 类型 | 说明 |
| --- | --- | --- |
| `init` | 单命令 | 初始化项目（见 [scaffolding.md](scaffolding.md)） |
| `config` | 子命令组 | Agent 配置管理（见 [scaffolding.md](scaffolding.md)） |
| `dev` | 单命令 | 本地开发服务 |
| `launch` | 单命令 | 云端/本地部署（`deploy` 是其 hidden 别名） |
| `invoke` | 单命令 | 调用已部署 Agent（与 `runtime invoke` 同函数） |
| `runtime` | 子命令组 | 运行时远程操作 |
| `destroy` | 单命令 | 销毁部署 |
| `gateway` | 子命令组 | MCP 网关管理 |
| `memory` | 子命令组 | Memory Space 管理 |

## 2. dev：本地开发

```bash
agentarts dev \
  --port 8080 \
  --host 0.0.0.0 \
  --reload \
  --config .agentarts_config.yaml \
  --env OPENAI_API_KEY=sk-xxx
```

| 参数 | 简写 | 默认 | 说明 |
| --- | --- | --- | --- |
| `--port` | `-p` | 8080 | 服务器端口 |
| `--host` | `-h` | 0.0.0.0 | 服务器主机 |
| `--reload` | — | False | 启用热重载 |
| `--config` | `-c` | None | 配置文件路径 |
| `--env` | `-e` | None | 环境变量 `KEY=VALUE`，可多次使用，**优先级高于配置文件** |

端点：`POST /invocations`（调用）、`GET /ping`（健康检查）。

## 3. launch / deploy：部署

```bash
agentarts launch \
  --agent my-agent \
  --mode cloud \
  --tag latest \
  --swr-org my-org \
  --swr-repo agent_my_agent \
  --description "My Agent" \
  --skip-build \
  --skip-ssl-verification
```

| 参数 | 简写 | 默认 | 说明 |
| --- | --- | --- | --- |
| `--agent` | `-a` | 默认 agent | Agent 名称 |
| `--mode` | `-m` | cloud | `local` 或 `cloud` |
| `--tag` | `-t` | latest | Docker 镜像标签 |
| `--local-port` | `-l` | None | 本地模式端口映射 |
| `--swr-org` | — | 配置值 | SWR 组织（覆盖配置） |
| `--swr-repo` | — | 配置值 | SWR 仓库（覆盖配置） |
| `--description` | `-d` | 配置值 | Agent 描述 |
| `--skip-build` | — | False | 跳过构建推送，用配置文件 `artifact_source.url` 直接创建 |
| `--skip-ssl-verification` | `-k` | False | 跳过 SSL 验证 |

部署流程详见 [deployment.md](deployment.md)。

## 4. invoke：调用 Agent

```bash
agentarts invoke '{"message": "hello"}' \
  --agent my-agent \
  --mode cloud \
  --region cn-southwest-2 \
  --endpoint my-endpoint \
  --session session-123 \
  --bearer-token xxx \
  --timeout 900 \
  --custom-path /custom
```

| 参数 | 简写 | 默认 | 说明 |
| --- | --- | --- | --- |
| `payload` | — | 必填 | JSON 字符串（位置参数） |
| `--agent` | `-a` | 默认 agent | Agent 名称 |
| `--mode` | `-m` | cloud | `local` 或 `cloud` |
| `--region` | `-r` | 配置值 | 区域（cloud 模式） |
| `--port` | `-p` | None（实际 8080） | 本地模式端口 |
| `--endpoint` | `-e` | None | 端点名称 |
| `--session` | `-s` | None | 会话 ID |
| `--bearer-token` | `-bt` | None | Bearer token |
| `--timeout` | — | 900 | 请求超时（秒） |
| `--user-id` | `-u` | None | OAuth2 出站凭据用户 ID |
| `--custom-path` | — | None | 追加到 `/invocations` 后的路径（需 `url_match_type: PREFIX_MATCH`） |

各模板支持的 payload 字段：

| 模板 | 支持字段 |
| --- | --- |
| `basic` / `langgraph` | `message` |
| `langchain` | `message`、`system_prompt` |
| `google-adk` | `message`、`system_instruction` |

## 5. destroy：销毁

```bash
agentarts destroy --agent my-agent --region cn-southwest-2 --yes
```

| 参数 | 简写 | 默认 | 说明 |
| --- | --- | --- | --- |
| `--agent` | `-a` | 默认 agent | Agent 名称 |
| `--region` | `-r` | 配置值 | 区域 |
| `--yes` | `-y` | False | 跳过确认提示 |
| `--skip-ssl-verification` | `-k` | False | 跳过 SSL 验证 |

详见 [deployment.md](deployment.md)。

## 6. runtime 子组

远程运行时操作，所有子命令仅支持云端模式。

| 子命令 | 说明 | 关键选项 |
| --- | --- | --- |
| `runtime invoke` | 调用（同顶层 invoke） | 同顶层 invoke |
| `runtime exec-command` | 远程执行命令 | `command`（必填）、`--session`（缺省时自动生成 UUID）、`--chunked`（流式）、`--timeout`（默认 60，**最大 3600**） |
| `runtime upload-files` | 上传文件 | `--agent`、`--session`、`--files/-f`（可多次）、`--path/-p`（默认 `/tmp/`）、`--file-mode/-m`（默认 0644） |
| `runtime download-files` | 下载文件 | `--agent`、`--session`、`--path/-p`（必填）、`--output/-o`、`--recursive`（目录走 tar） |
| `runtime start-session` | 创建会话 | `--agent`，返回 `session_id` |
| `runtime stop-session` | 停止会话 | `--agent`、`--session` |

后端 API 路径：

| 命令 | 路径 |
| --- | --- |
| `start-session` | `POST /runtimes/{agent}/sessions-start` |
| `stop-session` | `POST /runtimes/{agent}/sessions-stop` |
| `invoke` | `POST /runtimes/{agent}/invocations` |
| `exec-command` | `POST /runtimes/{agent}/commands` |
| `upload-files` | `POST /runtimes/{agent}/upload-files` |
| `download-files` | `GET /runtimes/{agent}/download-files` |

### exec-command 细节

- `--chunked`：启用 `application/x-ndjson` 流式输出
- 含 shell 元字符时自动包装为 `["sh", "-c", ...]`
- `--timeout`：默认 60s，**最大 3600s**（文档称 300s 是旧值，以代码为准）
- `--session` 缺省时自动生成 UUID，避免 V11 签名在 `None` session 上报错

### upload-files 细节

- 单文件最大 100MB
- 需 `file_transfer_config.enabled: true`（配置中开启）
- `--path` 必须以 `/` 结尾，默认 `/tmp/`
- `--file-user-id`（默认 1000）、`--file-group-id`（默认 1000）

## 7. gateway 子组

MCP 网关与目标管理，AK/SK 认证（`HUAWEICLOUD_SDK_AK` / `HUAWEICLOUD_SDK_SK`）。所有命令支持 `--skip-ssl-verification/-k`。

### 网关管理

| 命令 | 说明 | 关键选项 |
| --- | --- | --- |
| `gateway create` | 创建网关 | `--name/-n`、`--description/-d`、`--protocol-type`（默认 mcp）、`--authorizer-type`（默认 iam）、`--agency-name`、`--authorizer-configuration`（JSON）、`--protocol-configuration`（JSON）、`--log-delivery-configuration`（JSON）、`--outbound-network-configuration`（JSON）、`--tags`（JSON） |
| `gateway update <gateway_id>` | 更新 | `--description/-d`、`--protocol-configuration`、`--log-delivery-configuration`、`--tags` |
| `gateway delete <gateway_id>` | 删除（带确认） | — |
| `gateway get <gateway_id>` | 获取详情 | — |
| `gateway list` | 列表 | `--name`、`--status`、`--gateway-id`、`--tag-key-exists`、`--tag-key-matches`、`--tag-value-matches`、`--tag-match-policy`（ALL/ANY）、`--limit`（默认 50，1-100）、`--offset`（默认 0） |

### 目标管理

| 命令 | 说明 | 关键选项 |
| --- | --- | --- |
| `gateway create-target <gateway_id>` | 创建目标 | `--target-configuration`（JSON，必填）、`--name/-n`、`--description/-d`、`--credential-provider-configuration`（JSON） |
| `gateway update-target <gateway_id> <target_id>` | 更新 | `--name/-n`、`--description/-d`、`--target-configuration`、`--credential-provider-configuration` |
| `gateway delete-target <gateway_id> <target_id>` | 删除（带确认） | — |
| `gateway get-target <gateway_id> <target_id>` | 获取详情 | — |
| `gateway list-targets <gateway_id>` | 列表 | `--limit`（默认 50）、`--offset`（默认 0） |

> **文档/代码偏差**：中文文档 `gateway_cli.md` 用 `create-gateway`/`update-gateway` 等名称，代码实际注册为 `gateway create`/`update`/...。以代码为准。

## 8. memory 子组

Memory Space CRUD，AK/SK 认证，默认区域 `cn-north-4`。

| 命令 | 说明 | 关键选项 |
| --- | --- | --- |
| `memory create <name>` | 创建 Space | `--ttl/-t`（默认 168，1-8760）、`--description/-d`、`--strategies/-s`（逗号分隔）、`--tags`（`k=v,k=v`）、`--public/--private`（默认 public）、`--vpc-id`、`--subnet-id`（两者须同时提供）、`--region/-r`、`--output/-o`（默认 table，可选 json） |
| `memory get <space_id>` | 获取详情 | `--region/-r`、`--output/-o` |
| `memory list` | 列表 | `--limit/-l`（默认 20，≤100）、`--offset`（默认 0）、`--region/-r`、`--output/-o` |
| `memory update <space_id>` | 更新 | 同 create 的可选项 |
| `memory delete <space_id>` | 删除 | `--region/-r`、`--force/-f`（跳过确认） |
| `memory status <space_id>` | 查看状态（健康面板） | `--region/-r`、`--output/-o` |

### 记忆插件安装（`memory install` / `memory uninstall`）

把 AgentArts Memory 挂载到 AI 编程助手，详见 [03-memory/memory_plugin.md](../03-memory/memory_plugin.md)。

| 命令 | 说明 | 关键选项 |
| --- | --- | --- |
| `memory install [target]` | 安装记忆插件 | `target`：`claude` / `codex` / `opencode` / `hermes` / `openclaw`（省略则检测并交互选择）；`--global`（用户级）；`--yes/-y`（自动确认） |
| `memory uninstall [target]` | 卸载记忆插件 | 同 install；省略 target 时列出已安装项供选择 |

安装前会校验 `AGENTARTS_MEMORY_SPACE_ID`、`HUAWEICLOUD_SDK_MEMORY_API_KEY`、`HUAWEICLOUD_SDK_REGION`（交互式补齐）。OpenClaw 目前是占位实现，会提示 `not yet implemented`。

## 9. 会话管理标准流程

```bash
# 1. 创建会话
session_id=$(agentarts runtime start-session --agent my-agent --region cn-southwest-2 | jq -r .session_id)

# 2. 在会话中操作
agentarts invoke '{"message": "第一步"}' --agent my-agent --session $session_id
agentarts invoke '{"message": "第二步"}' --agent my-agent --session $session_id

# 3. 上传文件到会话
agentarts runtime upload-files --agent my-agent --session $session_id \
  --files ./data.csv --path /tmp/

# 4. 停止会话
agentarts runtime stop-session --agent my-agent --session $session_id
```

## 10. 常用命令组合

### 开发调试循环

```bash
agentarts init -n my-agent -t langgraph
cd my-agent && pip install -r requirements.txt
# 编辑 agent.py
agentarts dev --reload --env OPENAI_API_KEY=sk-xxx
```

### 部署与调用

```bash
agentarts config          # 生成 Dockerfile
agentarts launch --mode cloud
agentarts invoke '{"message": "test"}' --agent my-agent
agentarts destroy --agent my-agent -y
```

### Memory Space 管理

```bash
agentarts memory create my-space --strategies semantic,episodic --ttl 720
agentarts memory list --output json
agentarts memory status <space_id>
agentarts memory delete <space_id> -f
```

### Gateway 管理

```bash
agentarts gateway create --name my-gw --authorizer-type iam
agentarts gateway create-target <gateway_id> \
  --target-configuration '{"mcp_server": {"endpoint": "https://example.com/mcp", "server_type": "sse"}}'
agentarts gateway list
agentarts gateway list-targets <gateway_id>
```
