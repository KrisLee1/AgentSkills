# 开发 AgentSkills

[English](DEVELOPMENT.md)

AgentSkills 是一组指令包，而不是需要编译的应用程序。大多数修改只涉及 Markdown 和 YAML；只有运行两个随附辅助脚本时需要 Python 3。

## 前置要求

- Git。
- 文本编辑器。
- 用于脚本语法检查和辅助工具冒烟测试的 Python 3。
- 用于端到端触发与工作流检查的 Codex。

当前仓库没有包清单、锁文件、依赖初始化、构建步骤或 CI 工作流。

## 仓库结构

| 路径 | 职责 |
| --- | --- |
| `skills/*/SKILL.md` | Codex 加载的权威元数据和工作流指令。 |
| `skills/*/README.md` | 面向用户的英文用途、用法、示例和随附资源指南。 |
| `skills/*/README.zh-CN.md` | 与英文指南对应的简体中文版本。 |
| `skills/*/agents/openai.yaml` | ChatGPT 桌面端显示元数据和默认提示。 |
| `skills/*/references/` | 仅在工作流需要时加载的详细指南。 |
| `skills/*/assets/` | 复制并适配到目标项目的模板。 |
| `skills/*/scripts/` | 需要确定性行为时使用的辅助脚本。 |
| `docs/USAGE.md` | 仓库级英文安装和使用事实来源。 |
| `docs/USAGE.zh-CN.md` | 使用指南的简体中文版本。 |
| `docs/DEVELOPMENT.md` | 仓库级英文开发和验证事实来源。 |
| `docs/DEVELOPMENT.zh-CN.md` | 开发指南的简体中文版本。 |

## Skill 约定

每个 skill 必须自包含在 `skills/skill-name/` 下，并提供 `SKILL.md`。其 YAML front matter 需要定义：

```yaml
---
name: skill-name
description: A concise statement of when the skill should trigger.
---
```

`name` 在本仓库内必须唯一。`description` 会参与隐式 skill 选择，因此应优先说明主要用途和边界。主工作流保留在 `SKILL.md` 中；将条件性细节放入 `references/`，可复用起始文件放入 `assets/`，需要确定性执行的操作放入 `scripts/`。

当前 `agents/openai.yaml` 提供 `display_name`、`short_description` 和 `default_prompt`。其中的提示必须与 skill 的公开名称和预期触发场景一致。

## 常规修改流程

1. 阅读目标 skill 的 `SKILL.md`、`README.md` 和 `README.zh-CN.md`。
2. 只读取本次修改涉及的参考资料、模板或脚本。
3. 保持相对链接有效，确保 skill 文件夹复制后仍可正常使用。
4. 当行为、输出、要求或随附资源变化时，同步更新中英文 skill README。
5. 新增、重命名、删除 skill，或修改其安装与调用约定时，同步更新根 README 和使用指南的中英文版本。
6. 运行下文中适用的检查，并准确报告实际通过的内容。

## 验证

### 检查 Python 语法

从仓库根目录运行：

```bash
python3 -m py_compile \
  skills/project-blueprint/scripts/scaffold_project_docs.py \
  skills/write-project-guides/scripts/validate_project_guides.py
```

Python 可能会创建 `__pycache__` 目录；Git 已忽略这些目录。

### 验证 Markdown 指南

仓库中的可复用模板有意保留未替换标记。验证整个仓库时应使用 `--allow-placeholders`：

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py \
  "$(pwd)" \
  --allow-placeholders
```

应将这个全树命令视为诊断，而不是必须成功退出的发布门禁。`skills/*/assets/` 中的占位符警告属于预期行为。Component-First UI 模板中基于占位符的链接目标，在目标项目替换之前也会被报告为坏链接。所有出现在可复用模板之外的问题都需要检查；只要仓库还保留有意设置的模板标记，就不应对全树使用 `--strict`。

对于已经根据模板生成并完成适配的目标项目，运行验证器时不要使用 `--allow-placeholders`：

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py /path/to/target-project
```

### 冒烟测试项目脚手架

脚本会创建文件，因此应使用空的临时目录：

```bash
target_dir="$(mktemp -d)"
python3 skills/project-blueprint/scripts/scaffold_project_docs.py \
  "$target_dir" \
  --project-name "Example Project" \
  --summary "Example project used to verify the scaffold."
test -f "$target_dir/docs/INDEX.md"
```

预期结果是脚本输出创建文件数量，并且文件检查成功。如果没有显式提供 `--skip-existing`，脚手架必须拒绝覆盖现有目标文件。

### 审查 skill 元数据

对于每个修改过的 skill，直接检查以下事实：

- front matter 中的 `name` 与目录名和调用示例一致；
- front matter 中的 `description` 清楚说明正向触发条件和重要边界；
- `SKILL.md` 中的每个相对链接都能解析；
- `agents/openai.yaml` 的 `default_prompt` 使用了正确的 skill 名称；
- 脚本只使用已经记录的依赖，并且默认安全；
- 模板被清楚标记为模板，没有被描述为已完成的项目事实；
- 中英文用户指南结构对应，命令、路径和行为说明一致。

### 在 Codex 中测试

将修改后的 skill 安装或链接到适用的 `.agents/skills` 位置，然后至少测试一个显式提示和一个有代表性的隐式提示。确认 Codex 读取了正确的 skill、遵循条件性参考资料，并准确报告验证情况。

仅靠静态检查无法确认端到端 Codex 行为；如果跳过此检查，应将其记录为未验证。

## 新增 skill

创建满足需要的最小自包含结构：

```text
skills/skill-name/
  README.md
  README.zh-CN.md
  SKILL.md
  agents/openai.yaml
  assets/       # 可选
  references/   # 可选
  scripts/      # 可选
```

不要创建空的可选目录。将新 skill 添加到根目录中英文对照表和使用指南中，然后验证链接与调用示例。

## 文档语言

英文指南和 skill 指令是行为与命令的主要事实来源；`*.zh-CN.md` 是对应的简体中文版本。修改英文行为说明时，应在同一次变更中同步中文文档，反之亦然。随附模板可以使用适合其目标工作流的语言；`project-blueprint` 当前提供中文项目文档模板。

## 发布状态

仓库当前没有自动版本管理、打包、发布或发行流程。不要在文档中虚构相关流程，也不要仅为验证文档而执行对外可见的发布操作。
