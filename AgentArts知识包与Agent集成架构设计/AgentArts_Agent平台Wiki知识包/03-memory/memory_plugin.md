# Memory 插件（AI 编程助手长期记忆）

> SDK 锚点：`agentarts.toolkit.plugins.memory`（v0.1.5 起，v0.1.6 完善）。包含统一安装器 `installer/`、平台资产 `ai_agent/`、MCP Server `mcp/`、共享 Hook 脚本 `resources/`。
> CLI 入口：`agentarts memory install` / `agentarts memory uninstall`。

## 1. 定位与原理

前面的 [memory.md](memory.md) 讲的是**在你自己写的 Agent 代码里调用 Memory**。本篇讲另一半：把 AgentArts Memory 直接**挂到已有 AI 编程助手**上，让它跨会话记住你的偏好、项目决策和历史上下文。

```
AI 编程助手（Claude Code / Codex / OpenCode / Hermes）
        ↓  Hook 脚本 / Plugin / MemoryProvider
本地适配层（MCP Server stdio 或 provider 直连 SDK）
        ↓  MemoryClient（数据面，API Key）
华为云 AgentArts Memory Space
```

**为什么用插件而不是改助手源码**：插件通过各助手官方的扩展点（Hook、Plugin、MemoryProvider）接入，升级助手或换助手都不需要改业务；凭证留在本地配置/环境变量中，通过 SDK 统一走控制面/数据面。

## 2. 支持的平台

| 平台 | `install` 目标 | 接入机制 | 状态 |
| --- | --- | --- | --- |
| Claude Code | `claude` | 2 个 Hook（`UserPromptSubmit` / `PreCompact`）+ `settings.json` 注册 `agentarts_memory` MCP Server | ✅ |
| Codex | `codex` | Hook 脚本 + `hooks.json` + `config.toml` 开启 `[features].hooks`，并注册 MCP Server | ✅ |
| OpenCode | `opencode` | TypeScript 插件 `agentarts-memory-capture.ts` + `/recall`、`/remember` 命令 + MCP Server | ✅ |
| Hermes Agent | `hermes` | `MemoryProvider` 插件（`~/.hermes/plugins/agentarts/`），直连 SDK，另有 `ltm_search` / `ltm_search_summary` 工具 | ✅ |
| OpenClaw | `openclaw` | 占位实现，安装时提示 `not yet implemented` | ⚠️ 未实现 |

## 3. 前置条件

1. 已有 Memory Space，并拿到三个配置项：

| 配置 | 环境变量 | 说明 |
| --- | --- | --- |
| 区域 | `HUAWEICLOUD_SDK_REGION` | 默认 `cn-southwest-2` |
| Space ID | `AGENTARTS_MEMORY_SPACE_ID` | AgentArts 记忆库 ID |
| API Key | `HUAWEICLOUD_SDK_MEMORY_API_KEY` | Space 创建时生成，仅显示一次 |

2. Node.js（Claude Code / Codex 的 Hook 脚本是 `.mjs`）。
3. 目标助手已安装（安装器会检测 `~/.claude`、`~/.codex`、`~/.config/opencode`、`~/.hermes`）。

## 4. 安装与卸载

```bash
# 交互式：自动检测已安装的平台，选择一个
agentarts memory install

# 指定平台
agentarts memory install claude
agentarts memory install codex
agentarts memory install opencode
agentarts memory install hermes

# 安装到用户级配置（对所有项目生效）
agentarts memory install codex --global

# 全部自动确认（用于脚本/CI）
agentarts memory install claude --yes

# 卸载
agentarts memory uninstall claude
agentarts memory uninstall codex --global -y
```

| 参数 | 说明 |
| --- | --- |
| `target` | 位置参数，`hermes` / `claude` / `codex` / `opencode` / `openclaw`；省略则自动检测并交互选择 |
| `--global` | 安装/卸载用户级配置；默认是项目级 |
| `--yes/-y` | 自动确认所有提示（凭证校验、scope 选择等） |

安装/卸载的落点（项目级 / 全局级）：

| 平台 | 项目级目录 | 全局级目录 | 主要写入 |
| --- | --- | --- | --- |
| Claude Code | `.claude/` | `~/.claude/` | `agentarts-memory/scripts/*.mjs`、`settings.json`（hooks + mcpServers） |
| Codex | `.codex/` | `~/.codex/` | `agentarts-memory/scripts/*.mjs`、`hooks.json`、`config.toml`（`[features].hooks` + MCP Server） |
| OpenCode | `.opencode/` | `~/.config/opencode/` | `plugins/agentarts-memory-capture.ts`、`commands/recall.md`、`commands/remember.md`、`opencode.json` |
| Hermes | ——（固定用户级） | `~/.hermes/plugins/agentarts/` | `provider.py`、`plugin.yaml`、`.env`（凭证） |

> Hermes 为 `fixed_user_level`，安装始终是用户级，通过 `hermes memory setup` 交互式配置。

安装完成后需**重启对应助手**才会加载插件。

## 5. MCP Server 与工具

Code Agent 类平台（Claude Code / Codex / OpenCode）通过 stdio 启动 MCP Server：

```bash
python -m agentarts.toolkit.plugins.memory.mcp.server
```

服务名 `agentarts_memory`，由助手以子进程方式拉起，暴露 4 个工具：

| 工具 | 说明 | 关键参数 |
| --- | --- | --- |
| `search_memories` | 语义检索云端记忆 | `query`、`num`（默认 5，1-100）、`threshold`（默认 0.7，0-1） |
| `add_messages` | 记录对话消息到云端 | `messages: list[{role, content}]` |
| `list_memories` | 分页列出记忆记录 | `limit`（默认 10）、`offset` |
| `search_summary` | 列出摘要类记忆 | `query`、`num`（默认 3） |

Hermes provider 在 MCP 之外提供两个原生工具：

| 工具 | 说明 | 关键参数 |
| --- | --- | --- |
| `ltm_search` | 搜索长期记忆 | `query`（必填）、`top_k`（默认 5） |
| `ltm_search_summary` | 获取记忆摘要列表 | `limit`（默认 10） |

## 6. 运行时环境变量

| 变量 | 说明 |
| --- | --- |
| `AGENTARTS_MEMORY_SPACE_ID` | 绑定的 Space ID |
| `HUAWEICLOUD_SDK_MEMORY_API_KEY` | Space 数据面 API Key |
| `HUAWEICLOUD_SDK_REGION` | 区域，默认 `cn-southwest-2` |
| `AGENTARTS_MEMORY_PLATFORM` | 由安装器注入（`claude-code` / `codex` / `opencode`），用于推导默认 `user_id` |
| `AGENTARTS_MEMORY_USER_ID` | 覆盖默认 `user_id` |
| `AGENTARTS_MEMORY_PROJECT_NAME` | 覆盖默认 scope（默认 `default`） |
| `AGENTARTS_MEMORY_LOG_LEVEL` | 设为 `debug` 输出 SDK 调用日志 |

未显式设置 `user_id` 时的平台默认值：`claude-code → cc-user`、`codex → codex-user`、`opencode → opencode-user`、其他 → `__default__`。

## 7. 生命周期与行为

Claude Code / Codex 的 Hook 行为：

| Hook | 触发时机 | 行为 |
| --- | --- | --- |
| `UserPromptSubmit` | 用户提交 prompt 时 | 记录 prompt，并检索相关记忆注入上下文 |
| `PreCompact` | 上下文压缩前 | 重新检索并注入记忆，避免关键信息被裁掉 |

Hermes provider 的完整生命周期：

| 钩子 | 调用时机 | 职责 |
| --- | --- | --- |
| `system_prompt_block` | 组装系统 prompt | 注入记忆能力说明 |
| `prefetch` | 每次 LLM 调用前 | 搜索并注入相关记忆（用户画像 / 情景 / 语义 + 历史摘要） |
| `sync_turn` | 每轮对话后 | 写入对话内容 |
| `on_pre_compress` | 上下文压缩前 | 重新注入相关记忆 |
| `on_memory_write` | 内置 `MEMORY.md` 写入时 | 镜像到 AgentArts |
| `on_session_end` / `shutdown` | 对话结束 / 进程退出 | no-op（逐轮已落库）/ 清理连接 |

## 8. 常见问题

| 问题 | 原因 | 解决 |
| --- | --- | --- |
| `No supported platforms detected` | 未安装目标助手或目录不存在 | 先安装 Claude Code / Codex / OpenCode / Hermes |
| 搜索不到刚写入的记忆 | 记忆抽取是异步的 | 等待约 30s 后重试 |
| 认证失败 | API Key / 区域 / Space 状态异常 | 校验三个环境变量；确认 Space 状态为 `running` |
| 安装后不生效 | 助手未重启 | 重启对应助手 |
| 同一项目多助手重复建 session | 各助手各自缓存 session | 安装器使用共享的本地 session 缓存（24h TTL），首次创建的 session 会被其他助手复用 |
| Windows 下 Hook 路径异常 | 反斜杠需归一化 | 安装器已把路径统一为 `/`；如仍异常，重新 `agentarts memory install` |

## 9. 最佳实践

1. **一个项目一个 scope**：用 `AGENTARTS_MEMORY_PROJECT_NAME` 隔离不同项目的记忆
2. **凭证走环境变量/`.env`**：不要把 API Key 写进代码或提交到仓库
3. **先建 Space 再装插件**：`agentarts memory create` 拿到 Space ID 与 API Key 后再安装
4. **CI 用 `--yes`，本地手动确认**：CI 中避免交互阻塞
5. **卸载要配套**：不用时 `agentarts memory uninstall <target>`，避免 Hook 残留调用云端
6. **记忆写入是异步的**：不要把“立刻可检索”作为业务前提，关键信息同时落库到自己的存储
7. **敏感信息不入记忆**：写入前过滤密钥、Token、个人隐私数据
