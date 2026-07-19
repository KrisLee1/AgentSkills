# AgentSkills

Personal [Codex Skills](https://developers.openai.com/codex/skills/) for repeatable development workflows.

## Included skills

| Skill | Purpose |
| --- | --- |
| [`component-first-ui`](skills/component-first-ui/SKILL.md) | Builds UI through a maintained, indexed component catalog with stack-aware library selection, targeted discovery, validation, and incremental documentation updates. |
| [`project-blueprint`](skills/project-blueprint/SKILL.md) | Creates a modular, AI-ready project documentation system: architecture, specifications, phases, decisions, status, and append-only logs. |

## Install

Clone this repository, then copy the skill directory into your local Codex skills directory:

```bash
git clone https://github.com/<your-github-username>/AgentSkills.git
mkdir -p ~/.codex/skills
cp -R AgentSkills/skills/project-blueprint ~/.codex/skills/
cp -R AgentSkills/skills/component-first-ui ~/.codex/skills/
```

Restart Codex (or start a new task) after installing. The skills can then be invoked with `$project-blueprint` or `$component-first-ui`.

## Use

For example:

```text
Use $project-blueprint to design an implementation-ready documentation system for my new project.
Use $component-first-ui to implement a responsive settings page from the project's documented UI components.
```

See each skill's linked instructions above for its workflow and bundled resources.

## Repository layout

```text
skills/
  component-first-ui/
    SKILL.md                 # Documentation-driven UI workflow
    agents/openai.yaml       # Codex UI metadata
    assets/                  # Reusable UI documentation template
    references/              # Bootstrap, selection, and validation guidance
  project-blueprint/
    SKILL.md                 # Skill instructions
    agents/openai.yaml       # Codex UI metadata
    assets/                  # Reusable project-documentation template
    references/              # Supporting guidance
    scripts/                 # Safe scaffolding utility
```

## Contributing

Contributions and suggestions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
