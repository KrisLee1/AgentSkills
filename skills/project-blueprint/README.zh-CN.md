# Project Blueprint

[English](README.md)

`project-blueprint` 将产品想法、提案、空仓库、单体设计文档或文档不完整的代码库，整理为可供人类和 AI agent 直接使用的实施级文档系统。

它将稳定的架构与规范、阶段计划、当前状态、只追加历史和架构决策相互分离。权威 agent 工作流位于 [SKILL.md](SKILL.md)。

## 适用场景

- 规划新的应用、库、服务、CLI、plugin 或多包工作区；
- 重构混合了设计、状态、路线图和历史记录的项目文档；
- 定义架构边界、数据流、不变量、API、生命周期、错误、持久化或兼容性；
- 创建包含明确非目标和可测试验收标准的阶段实施计划；
- 建立 AI 任务路由、可更新状态、只追加日志和 ADR 约定；
- 审查项目是否已经能让另一个 agent 在不重新设计系统的情况下开始实施。

如果主要目标是 README、安装指南、使用指南、故障排查或贡献者流程，请使用 `write-project-guides`。

## 输出模型

对于模块化项目，该 skill 可以建立并根据目标项目调整以下结构：

```text
AGENTS.md
DESIGN.md
docs/
  INDEX.md
  PROJECT_STATUS.md
  architecture/
  specifications/
  engineering/
  phases/
  decisions/
  logs/
```

不同文档职责保持独立：

| 文档类别 | 负责内容 |
| --- | --- |
| Specification | 当前有效的规范行为。 |
| Phase plan | 某一阶段要交付的内容及其验收方式。 |
| Project status | 可更新的当前事实和下一项可执行工作。 |
| Log | 已发生事件和实际验证情况的只追加历史。 |
| ADR | 做出长期架构或兼容性决定的原因。 |
| Changelog | 将来建立发布流程后，记录面向用户的版本变化。 |

## 工作流概览

1. 检查目标项目的指令、源代码、清单、测试和现有文档。
2. 只在缺失要求会实质影响架构时解决它；真正开放的决定标记为 `TBD`。
3. 选择满足需要的最小文档结构。
4. 创建简洁的人类和 agent 入口，以及任务到文档的路由。
5. 根据项目需要编写可直接实施的架构、规范、阶段、测试、状态、日志和 ADR。
6. 验证链接、路由、验收标准、当前状态和未决决定。
7. 报告修改的文件、重要决定、实际验证、剩余 `TBD` 和建议的第一项实施任务。

## 示例提示

```text
使用 $project-blueprint 将这份产品提案整理为一套可直接实施的文档系统。

使用 $project-blueprint 审查当前仓库的设计文档，并分离规范、状态、阶段计划、决策和日志。

使用 $project-blueprint 为这个多包库定义架构和阶段计划，不要选择没有依据的技术。
```

## 可选脚手架工具

对于新的或空的目标项目，从 AgentSkills 仓库根目录运行随附脚本：

```bash
python3 skills/project-blueprint/scripts/scaffold_project_docs.py \
  /path/to/target-project \
  --project-name "Example Project" \
  --summary "A one-sentence description of the project."
```

该脚本会复制中文文档模板，替换项目名称、摘要和当前日期，并拒绝覆盖现有文件。如果目标已经存在，脚本会列出冲突并在不写入的情况下退出。只有在检查所有冲突后才能使用 `--skip-existing`；此参数保留现有文件，只创建缺失文件。

脚手架只是起点。交付前需要替换或解决其中的 `TBD`，并删除或调整不适用的部分。

## 随附资源

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 必需的发现、设计、路由、历史、脚手架和审查工作流。 |
| [discovery-and-architecture.md](references/discovery-and-architecture.md) | 仓库发现、架构边界和细节层级校准。 |
| [document-system.md](references/document-system.md) | 推荐文档结构、权威来源规则和任务路由。 |
| [review-checklist.md](references/review-checklist.md) | 结构、完整性、执行准备度和文档卫生审查。 |
| [项目文档模板](assets/project-docs-template/DESIGN.md) | 中文模块化项目文档起点。 |
| [scaffold_project_docs.py](scripts/scaffold_project_docs.py) | 无第三方依赖、默认不覆盖的模板脚手架。 |
| [openai.yaml](agents/openai.yaml) | ChatGPT 桌面端显示元数据和默认调用提示。 |

## 安全性和限制

- 保留现有文档和用户修改，或在明确迁移后再调整；脚手架默认不会覆盖文件。
- 该 skill 不会虚构版本、技术、支持政策、发布目标或测试结果。
- 日志只追加，当前规范和项目状态则原地更新。
- 对公共 API、存储格式、协议、依赖或安全的实质修改会被视为兼容性决策。
- 对于小型、短期项目，如果模块化系统没有提供额外路由价值，可以继续使用单一设计文档。
