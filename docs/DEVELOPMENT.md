# Develop AgentSkills

[简体中文](DEVELOPMENT.zh-CN.md)

AgentSkills is a collection of instruction packages rather than a compiled application. Most changes are Markdown and YAML; Python 3 is needed only to run the two bundled helper scripts.

## Prerequisites

- Git.
- A text editor.
- Python 3 for script syntax checks and helper smoke tests.
- Codex for end-to-end trigger and workflow checks.

There is no package manifest, lockfile, dependency bootstrap, build step, or CI workflow in the repository today.

## Repository structure

| Path | Responsibility |
| --- | --- |
| `skills/*/SKILL.md` | Authoritative metadata and workflow instructions loaded by Codex. |
| `skills/*/README.md` | Human-facing purpose, usage, examples, and bundled-resource guide. |
| `skills/*/README.zh-CN.md` | Simplified Chinese version of the human-facing skill guide. |
| `skills/*/agents/openai.yaml` | ChatGPT desktop display metadata and default prompt. |
| `skills/*/references/` | Detailed guidance loaded only when the workflow requires it. |
| `skills/*/assets/` | Templates copied and adapted for target projects. |
| `skills/*/scripts/` | Deterministic helpers for operations that benefit from code. |
| `docs/USAGE.md` | Repository-wide installation and usage source of truth. |
| `docs/USAGE.zh-CN.md` | Simplified Chinese version of the usage guide. |
| `docs/DEVELOPMENT.md` | Repository-wide development and validation source of truth. |
| `docs/DEVELOPMENT.zh-CN.md` | Simplified Chinese version of the development guide. |

## Skill contract

Each skill must be self-contained under `skills/skill-name/` and include a `SKILL.md` whose YAML front matter defines:

```yaml
---
name: skill-name
description: A concise statement of when the skill should trigger.
---
```

Keep `name` unique within this repository. The description is part of implicit skill selection, so put the primary use case and boundaries there. Keep the main workflow in `SKILL.md`; move conditional detail into `references/`, reusable starting files into `assets/`, and deterministic operations into `scripts/`.

`agents/openai.yaml` currently supplies `display_name`, `short_description`, and `default_prompt`. Keep its prompt aligned with the skill's public name and intended trigger.

## Normal change workflow

1. Read the target skill's `SKILL.md`, `README.md`, and `README.zh-CN.md`.
2. Read only the references, templates, or scripts affected by the change.
3. Preserve relative links so the skill continues to work after its folder is copied.
4. Update both per-skill README languages when behavior, outputs, requirements, or bundled resources change.
5. Update both languages of the root README and usage guide when a skill is added, renamed, removed, or changes its installation or invocation contract.
6. Run the relevant checks below and report exactly what passed.

## Validation

### Check Python syntax

From the repository root:

```bash
python3 -m py_compile \
  skills/project-blueprint/scripts/scaffold_project_docs.py \
  skills/write-project-guides/scripts/validate_project_guides.py
```

Python may create `__pycache__` directories; they are ignored by Git.

### Validate Markdown guides

The repository intentionally includes unresolved markers inside reusable assets. Use `--allow-placeholders` when validating the full tree:

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py \
  "$(pwd)" \
  --allow-placeholders
```

Treat this full-tree command as a diagnostic rather than a passing release gate. Warnings for placeholder markers inside `skills/*/assets/` are expected. The validator also reports placeholder-based link destinations in the Component-First UI templates as broken until a target project replaces them. Any finding outside reusable assets requires inspection, and `--strict` is not appropriate for the source repository while intentional template markers remain.

For a target project generated from the templates, run the validator without `--allow-placeholders` after adapting every marker:

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py /path/to/target-project
```

### Smoke-test the project scaffolder

Use an empty temporary directory because the script creates files:

```bash
target_dir="$(mktemp -d)"
python3 skills/project-blueprint/scripts/scaffold_project_docs.py \
  "$target_dir" \
  --project-name "Example Project" \
  --summary "Example project used to verify the scaffold."
test -f "$target_dir/docs/INDEX.md"
```

The expected result is a count of created files and a successful file check. The scaffolder must refuse to overwrite an existing destination unless `--skip-existing` is explicitly supplied.

### Review skill metadata

For every changed skill, inspect these facts directly:

- the front matter `name` matches the directory and invocation examples;
- the front matter `description` states positive triggers and important boundaries;
- every relative link from `SKILL.md` resolves;
- `agents/openai.yaml` names the correct skill in `default_prompt`;
- scripts use only documented dependencies and are safe by default;
- templates clearly remain templates and are not presented as completed project facts.
- English and Simplified Chinese guides retain matching commands, paths, and behavior claims.

### Test in Codex

Install or link the changed skill in an applicable `.agents/skills` location, then test at least one explicit prompt and one representative implicit prompt. Confirm that Codex reads the correct skill, follows conditional references, and reports validation honestly.

End-to-end Codex behavior cannot be established by static inspection alone; record it as unverified when this check is skipped.

## Adding a skill

Create the smallest self-contained structure needed:

```text
skills/skill-name/
  README.md
  README.zh-CN.md
  SKILL.md
  agents/openai.yaml
  assets/       # optional
  references/   # optional
  scripts/      # optional
```

Avoid empty optional directories. Add the skill to both languages of the root comparison table and usage guide, then validate its links and invocation examples.

## Documentation language

English guides and skill instructions are the primary source for behavior and commands; `*.zh-CN.md` files are the corresponding Simplified Chinese versions. When behavior changes in either language, update the paired document in the same change. Bundled templates may use the language appropriate to their target workflow; `project-blueprint` currently ships a Chinese project-documentation template.

## Release status

No automated versioning, packaging, publishing, or release procedure is present in the repository. Do not invent one in documentation or execute externally visible release steps as a validation check.
