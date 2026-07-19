# AgentSkills

[简体中文](README.zh-CN.md)

AgentSkills is a collection of self-contained [Codex skills](https://developers.openai.com/codex/skills/) for repeatable software-development workflows. It is intended for people who want Codex to follow a durable process instead of rebuilding the same instructions in every task.

Each skill combines a required `SKILL.md` with task-specific references, reusable templates, optional scripts, and ChatGPT desktop metadata. The skills can be installed together or copied individually.

## Included skills

| Skill | Use it when you need to | Detailed guide |
| --- | --- | --- |
| `component-first-ui` | Build or review frontend UI through an existing component catalog, or bootstrap that catalog before implementation. | [Component-First UI guide](skills/component-first-ui/README.md) |
| `project-blueprint` | Turn an idea or codebase into an implementation-ready, modular project documentation system. | [Project Blueprint guide](skills/project-blueprint/README.md) |
| `write-project-guides` | Create or update evidence-based README, usage, development, contribution, and release-facing guides. | [Write Project Guides guide](skills/write-project-guides/README.md) |

## Quick start

Requirements:

- Codex in the ChatGPT desktop app, Codex CLI, or the IDE extension;
- Git for cloning the repository;
- Python 3 only if you want to run the bundled helper scripts.

Install all skills for the current user:

```bash
git clone https://github.com/KrisLee1/AgentSkills.git
mkdir -p ~/.agents/skills
cp -R AgentSkills/skills/. ~/.agents/skills/
```

Codex normally detects skill changes automatically. If the skills do not appear, restart Codex. You can then invoke a skill explicitly:

```text
Use $project-blueprint to design an implementation-ready documentation system for this project.
```

Codex can also select a skill implicitly when a request matches the skill's description.

The copy command replaces files in same-named destination folders. Inspect `~/.agents/skills` first if you already have local modifications to any of these skills.

## Documentation

- [Usage guide](docs/USAGE.md): install one or all skills, choose a scope, invoke each workflow, update, and troubleshoot.
- [Development guide](docs/DEVELOPMENT.md): repository structure, authoring conventions, validation, and helper-script checks.
- [Contributing](CONTRIBUTING.md): expectations for proposed changes and pull requests.
- [Skill authoring documentation](https://developers.openai.com/codex/skills/): current Codex skill format, discovery locations, and invocation behavior.

The user-facing guides explain how to operate the skills. Each skill's `SKILL.md` remains the authoritative instruction file that Codex loads when the skill is selected.

## Repository layout

```text
skills/
  component-first-ui/
    README.md                # User-facing skill guide
    README.zh-CN.md          # Simplified Chinese skill guide
    SKILL.md                 # Codex workflow instructions
    agents/openai.yaml       # ChatGPT desktop metadata
    assets/                  # UI documentation templates
    references/              # Bootstrap, library, and validation guidance
  project-blueprint/
    README.md                # User-facing skill guide
    README.zh-CN.md          # Simplified Chinese skill guide
    SKILL.md                 # Codex workflow instructions
    agents/openai.yaml       # ChatGPT desktop metadata
    assets/                  # Modular project-documentation template
    references/              # Discovery, structure, and review guidance
    scripts/                 # Safe documentation scaffolder
  write-project-guides/
    README.md                # User-facing skill guide
    README.zh-CN.md          # Simplified Chinese skill guide
    SKILL.md                 # Codex workflow instructions
    agents/openai.yaml       # ChatGPT desktop metadata
    assets/                  # Compact and Standard guide skeletons
    references/              # Selection, content, project-type, and release guidance
    scripts/                 # Markdown guide validator
docs/
  USAGE.md                   # Complete user workflows
  USAGE.zh-CN.md             # Simplified Chinese usage guide
  DEVELOPMENT.md             # Contributor and maintainer workflow
  DEVELOPMENT.zh-CN.md       # Simplified Chinese development guide
```

## Project boundaries

This repository distributes direct skill folders; it is not currently packaged as a Codex plugin. The skills contain instructions and local helper scripts, but they do not require a service, package manager, API key, or runtime configuration of their own.

## License

AgentSkills is licensed under the [MIT License](LICENSE).
