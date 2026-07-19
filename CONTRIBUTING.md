# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Thanks for helping improve AgentSkills.

Read the [development guide](docs/DEVELOPMENT.md) for the repository structure, authoring contract, and validation commands.

## Adding or changing a skill

1. Keep each skill self-contained under `skills/<skill-name>/`.
2. Include a `SKILL.md` with front matter containing a unique `name` and a clear `description`.
3. Keep instructions focused, concrete, and scoped to the skill's purpose.
4. Place reusable templates in `assets/`, reference material in `references/`, and executable helpers in `scripts/`.
5. Add or update the skill's human-facing `README.md` and `README.zh-CN.md` when behavior, outputs, requirements, or bundled resources change.
6. Avoid embedding personal data, credentials, or machine-specific paths.

## Before submitting a pull request

- Run the Markdown and script checks documented in the [development guide](docs/DEVELOPMENT.md).
- Ensure scripts are safe by default and do not overwrite user files without explicit confirmation.
- Update the English and Simplified Chinese root README and usage guide when adding, renaming, or removing a skill.
- Describe the problem and the intended behavior in the pull request.

## Code of conduct

Be respectful, constructive, and considerate in all project discussions.
