# Write Project Guides

[English](README.md)

`write-project-guides` 根据仓库证据创建或更新项目文档。它的目标是让新用户无需私有知识就能获得可工作的结果，也让新开发者能够完成并验证一次修改。

该 skill 覆盖 README、安装与使用指南、开发环境、贡献指南、故障排查和发布准备度审查。权威 agent 工作流位于 [SKILL.md](SKILL.md)。

## 适用场景

- 创建根 README 或快速开始；
- 记录安装、配置、工作流、升级或故障排查；
- 编写开发环境和验证指南；
- 审查过期命令、路径、示例或文档结构；
- 为内部交付或公开发布准备仓库指南；
- 检查 Markdown 指南中的坏链接、未替换模板标记或疑似敏感内容。

如果主要目标是架构、规范、阶段计划、可更新状态、ADR 或开发历史，请使用 `project-blueprint`。

## 文档结构

该工作流会选择能够清楚表达用户和开发者路径的最小文档结构：

| 结构 | 典型形式 | 适用场景 |
| --- | --- | --- |
| Compact | 一个 `README.md` | 小型单一用途项目，使用与开发路径都很短。 |
| Standard | `README.md`、`docs/USAGE.md`、`docs/DEVELOPMENT.md`，以及可选 `CONTRIBUTING.md` | 普通应用、库、plugin 或集成需要持续的用户和开发者说明。 |
| Full | 在 Standard 基础上，仅增加有事实依据的配置、API、架构、部署、排障或升级文档 | 多组件、公共 API、运维或兼容性需要独立事实来源。 |

该 skill 不会创建没有内容的未来文档，也不会虚构许可证、安全联系方式、支持承诺、兼容范围、基准、路线图或发布流程。

## 工作流概览

1. 检查仓库指令、现有文档、清单、自动化、源码入口、测试、示例、打包和许可证证据。
2. 建立事实清单，并识别矛盾或真正未解决的细节。
3. 选择 Compact、Standard 或 Full，并为每类事实指定唯一权威位置。
4. 根据实际项目类型编写可复制的用户和开发者路径。
5. 在可行范围内运行最短的安全快速开始和开发检查；仅静态检查不适合执行的发布或生产命令。
6. 验证链接、占位符、示例和疑似敏感值。
7. 报告修改的文档、实际执行的命令、仅静态检查的内容、省略项和未解决事实。

## 示例提示

```text
使用 $write-project-guides 为当前仓库创建可发布的 README、使用指南和开发指南。

使用 $write-project-guides 根据当前源代码审查这些文档，并修复过期命令和坏链接。

使用 $write-project-guides 为这个 CLI 创建最小且完整的文档结构，并验证快速开始。
```

## Markdown 验证器

从 AgentSkills 仓库根目录运行无第三方依赖的验证器：

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py /path/to/target-project
```

验证器会扫描 Markdown 文件，并排除常见依赖、构建、版本控制和缓存目录。它会报告：

- 将损坏的本地链接报告为错误；
- 将找不到的 Markdown 标题锚点报告为警告；
- 将未替换的模板标记报告为错误；
- 将疑似密钥和个人绝对路径报告为警告；
- 将无效 UTF-8 Markdown 报告为错误。

可用参数：

| 参数 | 行为 |
| --- | --- |
| `--allow-placeholders` | 将未替换模板标记降级为警告。仅在有意验证可复用模板时使用。 |
| `--strict` | 存在任何警告时返回失败。 |

验证器不会访问外部 URL，也无法证明文档中的应用命令可以正常工作。这些结论需要有针对性的实际执行或静态仓库证据。

## 随附资源

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 必需的检查、文档选择、编写、验证和交付工作流。 |
| [document-selection.md](references/document-selection.md) | Compact、Standard、Full 结构和权威内容归属。 |
| [content-checklists.md](references/content-checklists.md) | 根 README、使用、开发、贡献、示例和安全检查。 |
| [project-types.md](references/project-types.md) | CLI、库、Web、HTTP、桌面/移动端、plugin、数据/ML 和 monorepo 指南。 |
| [release-readiness.md](references/release-readiness.md) | 准确性、全新用户路径、开发者路径、导航和公开安全审查。 |
| [Compact README 模板](assets/compact/README.md) | 小型项目的单文件起点。 |
| [Standard README 模板](assets/standard/README.md) | Standard 结构的入口页骨架。 |
| [Standard 使用模板](assets/standard/docs/USAGE.md) | 安装、配置、工作流、排障和支持骨架。 |
| [Standard 开发模板](assets/standard/docs/DEVELOPMENT.md) | 环境、结构、检查、打包和约束骨架。 |
| [Standard 贡献模板](assets/standard/CONTRIBUTING.md) | 已建立外部贡献流程时使用的可选骨架。 |
| [validate_project_guides.py](scripts/validate_project_guides.py) | 无第三方依赖的 Markdown 指南验证器。 |
| [openai.yaml](agents/openai.yaml) | ChatGPT 桌面端显示元数据和默认调用提示。 |

## 预期交付说明

该 skill 会说明创建或更新了哪些文档、为什么选择当前文档结构、哪些命令实际通过、哪些结论只经过静态检查，以及仍未解决或有意省略的内容。

可复用 asset 文件有意包含占位符；交付到目标项目的公开指南不能保留这些占位符。
