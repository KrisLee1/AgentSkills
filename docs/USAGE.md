# AgentSkills usage guide

[简体中文](USAGE.zh-CN.md)

This guide covers installing, selecting, invoking, updating, and troubleshooting the skills in this repository. Run repository commands from the AgentSkills clone unless a section says otherwise.

## Requirements

- Codex in the ChatGPT desktop app, Codex CLI, or the IDE extension.
- Git for the clone-based installation path.
- Python 3 only for the helper scripts included with `project-blueprint` and `write-project-guides`.

No API key, package manager, background service, or environment file is required by the skills themselves.

## Choose an installation scope

Codex discovers skills from multiple scopes. Use the smallest scope that matches who should receive the workflow:

| Scope | Destination | Use when |
| --- | --- | --- |
| Current user | `~/.agents/skills` | You want the skill available across your repositories. |
| One repository | `.agents/skills` inside the target repository | The workflow belongs to that codebase and should be shared with its contributors. |

These folders are authoring and local-discovery locations. This repository is not packaged as an installable plugin.

## Install all skills for the current user

```bash
git clone https://github.com/KrisLee1/AgentSkills.git
mkdir -p ~/.agents/skills
cp -R AgentSkills/skills/. ~/.agents/skills/
```

The result is one folder per skill directly under `~/.agents/skills`, with `SKILL.md` at the root of each folder.

## Install one skill for the current user

From the AgentSkills repository root:

```bash
mkdir -p ~/.agents/skills
cp -R skills/project-blueprint ~/.agents/skills/
```

Replace `project-blueprint` with `component-first-ui` or `write-project-guides` as needed.

## Install a repository-scoped skill

The following example assumes the AgentSkills clone and target repository are sibling directories. Run it from the target repository root:

```bash
mkdir -p .agents/skills
cp -R ../AgentSkills/skills/component-first-ui .agents/skills/
```

Commit the copied skill only when the repository's contribution and licensing policies allow it.

## Invoke a skill

Mention a skill with `$skill-name` when you want deterministic selection. Codex may also select a skill implicitly when the request matches its `description` in `SKILL.md`.

### Component-First UI

Use this skill for pages, reusable components, responsive layouts, interaction work, and UI review:

```text
Use $component-first-ui to build a responsive settings page using this project's documented components.
```

If the target project does not yet contain `docs/ui-development.md`, the workflow first creates an evidence-based UI entry document and component catalog, then continues the requested UI work.

See the [Component-First UI guide](../skills/component-first-ui/README.md).

### Project Blueprint

Use this skill to create or restructure implementation-ready design documentation, architecture boundaries, phased plans, status, logs, and ADRs:

```text
Use $project-blueprint to turn this product proposal into an implementation-ready documentation system.
```

For an existing repository, the skill inspects and adapts the current documentation. It does not blindly replace a working document system.

See the [Project Blueprint guide](../skills/project-blueprint/README.md).

### Write Project Guides

Use this skill for release-facing or internal usage and development guides backed by repository evidence:

```text
Use $write-project-guides to create a README, usage guide, and development guide for this repository.
```

The workflow chooses a Compact, Standard, or Full document map based on actual project complexity and verifies local links and unresolved template markers.

See the [Write Project Guides guide](../skills/write-project-guides/README.md).

## Choose the right skill

| Desired result | Skill |
| --- | --- |
| Implement or review a frontend interface while reusing the project's UI system | `component-first-ui` |
| Define architecture, specifications, phases, acceptance criteria, ADRs, status, and development history | `project-blueprint` |
| Explain how to install, use, develop, troubleshoot, or release an existing project | `write-project-guides` |

The documentation skills are complementary: `project-blueprint` owns implementation design and project execution records, while `write-project-guides` owns user and developer journeys. Avoid asking either skill to duplicate the other's source of truth.

## Update an installed skill

Pull the latest repository changes, inspect any same-named destination folder for local edits, then copy the desired skill again:

```bash
cd AgentSkills
git pull --ff-only
cp -R skills/write-project-guides ~/.agents/skills/
```

Codex normally detects the update automatically. Restart Codex if the revised skill does not appear.

## Troubleshooting

### The skill does not appear

Confirm that the folder is not nested one level too deeply. This path is valid:

```text
~/.agents/skills/project-blueprint/SKILL.md
```

Then restart Codex. In Codex CLI or the IDE extension, use `/skills` or type `$` to check the available list.

### The skill is listed twice

Codex can discover skills from repository and user scopes at the same time. Same-named skills are not merged. Remove or disable the unintended copy, or invoke the intended entry from the skill selector.

### A helper script is unavailable

Only two skills include Python helpers:

- `project-blueprint/scripts/scaffold_project_docs.py` scaffolds a documentation tree without overwriting existing files by default.
- `write-project-guides/scripts/validate_project_guides.py` checks Markdown links, template markers, and likely sensitive content.

The core workflows can still operate through instructions and file edits when Python is not available; the helper-specific operation or validation remains unverified until run.

### A generated template still contains placeholders

Templates intentionally contain markers such as double-braced project metadata or `TBD`. They are starting points, not finished deliverables. Adapt them to the target project and run the validation described by the relevant skill before handoff.

## Removal

Remove only the exact skill folder from the applicable `.agents/skills` directory. Inspect it first if it may contain local changes. Restart Codex if the removed skill remains visible.
