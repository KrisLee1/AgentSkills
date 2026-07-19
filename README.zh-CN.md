# AgentSkills

[English](README.md)

AgentSkills 是一组自包含的 [Codex skills](https://developers.openai.com/codex/skills/)，用于复用常见的软件开发工作流。它适合希望 Codex 持续遵循稳定流程，而不是在每次任务中重新编写相同指令的用户。

每个 skill 都包含必需的 `SKILL.md`，并可包含任务相关参考资料、可复用模板、辅助脚本和 ChatGPT 桌面端元数据。你可以一次安装全部 skill，也可以按需单独复制。

## 包含的 skill

| Skill | 适用场景 | 详细指南 |
| --- | --- | --- |
| `component-first-ui` | 基于现有组件目录构建或审查前端 UI，或者在实现前创建组件目录。 | [Component-First UI 指南](skills/component-first-ui/README.zh-CN.md) |
| `project-blueprint` | 将产品想法或代码库整理为可直接实施的模块化项目文档系统。 | [Project Blueprint 指南](skills/project-blueprint/README.zh-CN.md) |
| `write-project-guides` | 基于仓库事实创建或更新 README、使用、开发、贡献和发布文档。 | [Write Project Guides 指南](skills/write-project-guides/README.zh-CN.md) |

## 快速开始

环境要求：

- ChatGPT 桌面端中的 Codex、Codex CLI 或 IDE 扩展；
- 用于克隆仓库的 Git；
- 仅在运行随附辅助脚本时需要 Python 3。

为当前用户安装全部 skill：

```bash
git clone https://github.com/KrisLee1/AgentSkills.git
mkdir -p ~/.agents/skills
cp -R AgentSkills/skills/. ~/.agents/skills/
```

Codex 通常会自动检测 skill 变更。如果没有显示新安装的 skill，请重启 Codex。之后可以显式调用 skill：

```text
使用 $project-blueprint 为当前项目设计一套可直接实施的文档系统。
```

当请求与 `description` 匹配时，Codex 也可以隐式选择相应 skill。

上述复制命令会替换目标目录内同名 skill 文件夹中的文件。如果已经修改过 `~/.agents/skills` 中的本地副本，请先检查并备份相关内容。

## 文档

- [使用指南](docs/USAGE.zh-CN.md)：安装一个或全部 skill、选择作用域、调用工作流、更新和故障排查。
- [开发指南](docs/DEVELOPMENT.zh-CN.md)：仓库结构、编写约定、验证方式和辅助脚本检查。
- [贡献指南](CONTRIBUTING.zh-CN.md)：提交修改和拉取请求时需要遵守的要求。
- [Skill 编写文档](https://developers.openai.com/codex/skills/)：当前 Codex skill 格式、发现位置和调用方式。

面向用户的指南说明如何使用这些 skill。每个 skill 的 `SKILL.md` 仍是 Codex 选择该 skill 后加载的权威指令文件。

## 仓库结构

```text
skills/
  component-first-ui/
    README.md                # 英文用户指南
    README.zh-CN.md          # 中文用户指南
    SKILL.md                 # Codex 工作流指令
    agents/openai.yaml       # ChatGPT 桌面端元数据
    assets/                  # UI 文档模板
    references/              # 初始化、组件库和验证指南
  project-blueprint/
    README.md                # 英文用户指南
    README.zh-CN.md          # 中文用户指南
    SKILL.md                 # Codex 工作流指令
    agents/openai.yaml       # ChatGPT 桌面端元数据
    assets/                  # 模块化项目文档模板
    references/              # 发现、结构和审查指南
    scripts/                 # 安全的文档脚手架
  write-project-guides/
    README.md                # 英文用户指南
    README.zh-CN.md          # 中文用户指南
    SKILL.md                 # Codex 工作流指令
    agents/openai.yaml       # ChatGPT 桌面端元数据
    assets/                  # Compact 和 Standard 文档骨架
    references/              # 文档选择、内容、项目类型和发布指南
    scripts/                 # Markdown 文档验证器
docs/
  USAGE.md                   # 英文使用指南
  USAGE.zh-CN.md             # 中文使用指南
  DEVELOPMENT.md             # 英文开发指南
  DEVELOPMENT.zh-CN.md       # 中文开发指南
```

## 项目边界

本仓库发布的是可直接复制的 skill 文件夹，目前没有打包为 Codex plugin。这些 skill 包含指令和本地辅助脚本，本身不需要服务、包管理器、API 密钥或运行时配置。

## 许可证

AgentSkills 使用 [MIT License](LICENSE)。
