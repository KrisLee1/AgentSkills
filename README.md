# AgentSkills

Personal [Codex Skills](https://developers.openai.com/codex/skills/) for repeatable development workflows.

## Included skills

| Skill | Purpose |
| --- | --- |
| [`project-blueprint`](skills/project-blueprint/SKILL.md) | Creates a modular, AI-ready project documentation system: architecture, specifications, phases, decisions, status, and append-only logs. |

## Install

Clone this repository, then copy the skill directory into your local Codex skills directory:

```bash
git clone https://github.com/<your-github-username>/AgentSkills.git
mkdir -p ~/.codex/skills
cp -R AgentSkills/skills/project-blueprint ~/.codex/skills/
```

Restart Codex (or start a new task) after installing. The skill can then be invoked with `$project-blueprint`.

## Use

For example:

```text
Use $project-blueprint to design an implementation-ready documentation system for my new project.
```

See the skill's [full instructions](skills/project-blueprint/SKILL.md) for its workflow and the bundled scaffold template.

## Repository layout

```text
skills/
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
