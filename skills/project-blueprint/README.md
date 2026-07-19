# Project Blueprint

[简体中文](README.zh-CN.md)

`project-blueprint` turns a product idea, proposal, empty repository, monolithic design document, or partially documented codebase into an implementation-ready documentation system for humans and AI agents.

It separates stable architecture and specifications from phase plans, current status, append-only history, and architecture decisions. The authoritative agent workflow is [SKILL.md](SKILL.md).

## Use this skill when

- planning a new application, library, service, CLI, plugin, or multi-package workspace;
- restructuring project documentation that mixes design, status, roadmap, and history;
- defining architecture boundaries, data flow, invariants, APIs, lifecycle, errors, persistence, or compatibility;
- creating phased implementation plans with explicit non-scope and testable acceptance criteria;
- establishing AI task routing, mutable status, append-only logs, and ADR conventions;
- auditing whether a project is ready for another agent to implement without redesigning it.

Use `write-project-guides` instead when the primary outcome is a README, installation guide, usage guide, troubleshooting guide, or contributor journey.

## Output model

For a modular project, the skill can establish this structure and adapt it to the target project:

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

The document roles remain distinct:

| Document class | Owns |
| --- | --- |
| Specification | Current normative behavior. |
| Phase plan | What one stage will deliver and how it will be accepted. |
| Project status | Mutable current truth and the next executable work. |
| Log | Append-only history of what happened and what was verified. |
| ADR | Why a durable architecture or compatibility decision was made. |
| Changelog | Public release changes, when a future release process establishes one. |

## Workflow summary

1. Inspect target-project instructions, source, manifests, tests, and existing documentation.
2. Resolve missing requirements only when they materially affect architecture; mark genuine open decisions as `TBD`.
3. Choose the smallest sufficient document map.
4. Create concise human and agent entry points plus task-to-document routing.
5. Write implementation-ready architecture, specifications, phases, tests, status, logs, and ADRs as applicable.
6. Validate links, routing, acceptance criteria, current status, and unresolved decisions.
7. Report changed files, important decisions, actual verification, remaining `TBD`s, and the recommended first implementation task.

## Example prompts

```text
Use $project-blueprint to turn this product proposal into an implementation-ready documentation system.

Use $project-blueprint to audit this repository's design docs and separate specifications, status, phase plans, decisions, and logs.

Use $project-blueprint to define the architecture and phased plan for this multi-package library without choosing unsupported technologies.
```

## Optional scaffolding helper

For a new or empty target project, run the bundled script from the AgentSkills repository root:

```bash
python3 skills/project-blueprint/scripts/scaffold_project_docs.py \
  /path/to/target-project \
  --project-name "Example Project" \
  --summary "A one-sentence description of the project."
```

The script copies the Chinese documentation template, substitutes the project name, summary, and current date, and refuses to overwrite existing files. It prints conflicts and exits without writing when destinations already exist. Use `--skip-existing` only after inspecting every conflict; it leaves existing files unchanged and creates only missing files.

The scaffold is a starting point. Replace or resolve its `TBD` values and adapt irrelevant sections before delivery.

## Bundled resources

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Required discovery, design, routing, history, scaffolding, and review workflow. |
| [discovery-and-architecture.md](references/discovery-and-architecture.md) | Repository discovery, architecture boundaries, and detail calibration. |
| [document-system.md](references/document-system.md) | Recommended document map, source-of-truth rules, and task routing. |
| [review-checklist.md](references/review-checklist.md) | Structure, completeness, execution readiness, and hygiene review. |
| [project-docs-template](assets/project-docs-template/DESIGN.md) | Chinese modular project-documentation starting point. |
| [scaffold_project_docs.py](scripts/scaffold_project_docs.py) | Dependency-free, non-overwriting template scaffolder. |
| [openai.yaml](agents/openai.yaml) | ChatGPT desktop display metadata and default invocation prompt. |

## Safety and limitations

- Existing documentation and user edits are preserved or deliberately migrated; scaffolding does not overwrite by default.
- The skill does not invent versions, technologies, support policies, release targets, or test results.
- Logs are append-only, while current specifications and project status are updated in place.
- Meaningful changes to public APIs, stored formats, protocols, dependencies, or security are treated as compatibility decisions.
- Small, short-lived projects may remain in one design document when a modular system would add no routing value.
