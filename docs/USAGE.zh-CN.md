# AgentSkills 使用指南

[English](USAGE.md)

本指南介绍如何安装、选择、调用、更新和排查本仓库中的 skill。除非某一节另有说明，否则仓库命令都应从 AgentSkills 克隆目录中运行。

## 环境要求

- ChatGPT 桌面端中的 Codex、Codex CLI 或 IDE 扩展。
- 使用克隆安装方式时需要 Git。
- 仅 `project-blueprint` 和 `write-project-guides` 随附的辅助脚本需要 Python 3。

这些 skill 本身不需要 API 密钥、包管理器、后台服务或环境变量文件。

## 选择安装作用域

Codex 可以从多个作用域发现 skill。请根据需要使用范围最小的作用域：

| 作用域 | 目标目录 | 适用场景 |
| --- | --- | --- |
| 当前用户 | `~/.agents/skills` | 希望在自己的所有仓库中使用该 skill。 |
| 单个仓库 | 目标仓库内的 `.agents/skills` | 工作流属于该代码库，并需要与仓库贡献者共享。 |

这些目录用于编写和本地发现。本仓库目前没有打包为可安装的 plugin。

## 为当前用户安装全部 skill

```bash
git clone https://github.com/KrisLee1/AgentSkills.git
mkdir -p ~/.agents/skills
cp -R AgentSkills/skills/. ~/.agents/skills/
```

安装结果是在 `~/.agents/skills` 下直接创建每个 skill 的文件夹，并且每个文件夹根目录中都有 `SKILL.md`。

## 为当前用户安装单个 skill

从 AgentSkills 仓库根目录运行：

```bash
mkdir -p ~/.agents/skills
cp -R skills/project-blueprint ~/.agents/skills/
```

可以按需将 `project-blueprint` 替换为 `component-first-ui` 或 `write-project-guides`。

## 安装仓库级 skill

下面的示例假设 AgentSkills 克隆目录与目标仓库是同级目录。请从目标仓库根目录运行：

```bash
mkdir -p .agents/skills
cp -R ../AgentSkills/skills/component-first-ui .agents/skills/
```

只有在目标仓库的贡献和许可证政策允许时，才应提交复制后的 skill。

## 调用 skill

需要确定性地选择某个 skill 时，在提示中使用 `$skill-name`。当请求与 `SKILL.md` 中的 `description` 匹配时，Codex 也可能隐式选择该 skill。

### Component-First UI

此 skill 适用于页面、可复用组件、响应式布局、交互实现和 UI 审查：

```text
使用 $component-first-ui 基于当前项目已经记录的组件构建响应式设置页面。
```

如果目标项目还没有 `docs/ui-development.md`，该工作流会先创建基于仓库事实的 UI 入口文档和组件目录，然后继续原始 UI 任务。

参见 [Component-First UI 指南](../skills/component-first-ui/README.zh-CN.md)。

### Project Blueprint

此 skill 用于创建或重构可直接实施的设计文档、架构边界、阶段计划、状态、日志和 ADR：

```text
使用 $project-blueprint 将这份产品提案整理为一套可直接实施的文档系统。
```

对于现有仓库，该 skill 会检查并适配现有文档，而不会直接替换一套已经正常工作的文档系统。

参见 [Project Blueprint 指南](../skills/project-blueprint/README.zh-CN.md)。

### Write Project Guides

此 skill 用于编写有仓库证据支持的发布文档或内部使用与开发指南：

```text
使用 $write-project-guides 为当前仓库创建 README、使用指南和开发指南。
```

该工作流会根据项目的实际复杂度选择 Compact、Standard 或 Full 文档结构，并验证本地链接和未替换的模板标记。

参见 [Write Project Guides 指南](../skills/write-project-guides/README.zh-CN.md)。

## 选择合适的 skill

| 期望结果 | Skill |
| --- | --- |
| 在复用项目 UI 系统的前提下实现或审查前端界面 | `component-first-ui` |
| 定义架构、规范、阶段、验收标准、ADR、状态和开发历史 | `project-blueprint` |
| 说明如何安装、使用、开发、排查或发布现有项目 | `write-project-guides` |

两个文档类 skill 可以配合使用：`project-blueprint` 负责实现设计和项目执行记录，`write-project-guides` 负责用户与开发者使用路径。不要让它们重复维护对方负责的权威内容。

## 更新已安装的 skill

拉取仓库最新内容，检查目标目录中的同名 skill 是否存在本地修改，然后重新复制需要更新的 skill：

```bash
cd AgentSkills
git pull --ff-only
cp -R skills/write-project-guides ~/.agents/skills/
```

Codex 通常会自动检测更新。如果修改后的 skill 没有显示，请重启 Codex。

## 故障排查

### Skill 没有显示

确认文件夹没有多嵌套一层。下面的路径是正确的：

```text
~/.agents/skills/project-blueprint/SKILL.md
```

然后重启 Codex。在 Codex CLI 或 IDE 扩展中，可以使用 `/skills` 或输入 `$` 查看可用列表。

### 同一个 skill 显示两次

Codex 可以同时从仓库和用户作用域发现 skill。同名 skill 不会自动合并。请删除或禁用不需要的副本，或者从 skill 选择器中明确调用需要的版本。

### 无法使用辅助脚本

只有两个 skill 包含 Python 辅助脚本：

- `project-blueprint/scripts/scaffold_project_docs.py` 创建文档结构，默认不会覆盖现有文件。
- `write-project-guides/scripts/validate_project_guides.py` 检查 Markdown 链接、模板标记和疑似敏感内容。

没有 Python 时，核心工作流仍然可以通过指令和文件编辑完成；但在实际运行之前，与辅助脚本相关的操作或验证仍属于未验证状态。

### 生成的模板仍有占位符

模板有意包含双花括号项目元数据或 `TBD` 等标记。它们只是起点，不是可以直接交付的成品。交付前必须根据目标项目修改模板，并运行对应 skill 要求的验证。

## 删除

只删除对应 `.agents/skills` 目录中的准确 skill 文件夹。如果其中可能有本地修改，请先检查。删除后如果该 skill 仍然显示，请重启 Codex。
