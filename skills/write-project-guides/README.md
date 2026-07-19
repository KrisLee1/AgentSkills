# Write Project Guides

[简体中文](README.zh-CN.md)

`write-project-guides` creates or updates project documentation from repository evidence. Its goal is to let a new user reach a working result and a new developer make a verified change without relying on private knowledge.

The skill covers README files, installation and usage guides, development setup, contribution guidance, troubleshooting, and release-readiness review. The authoritative agent workflow is [SKILL.md](SKILL.md).

## Use this skill when

- creating a root README or quick start;
- documenting installation, configuration, workflows, upgrades, or troubleshooting;
- writing a development setup and validation guide;
- auditing stale commands, paths, examples, or documentation structure;
- preparing repository guides for private delivery or public release;
- checking Markdown guides for broken local links, unresolved template markers, or likely sensitive values.

Use `project-blueprint` instead when the main outcome is architecture, normative specifications, phase plans, mutable status, ADRs, or development history.

## Document maps

The workflow selects the smallest map that keeps user and developer journeys clear:

| Map | Typical shape | Use when |
| --- | --- | --- |
| Compact | One `README.md` | A small single-purpose project has short usage and development paths. |
| Standard | `README.md`, `docs/USAGE.md`, `docs/DEVELOPMENT.md`, optional `CONTRIBUTING.md` | A normal application, library, plugin, or integration needs sustained user and developer guidance. |
| Full | Standard plus only justified modules such as configuration, API, architecture, deployment, troubleshooting, or upgrading | Multiple components, public APIs, operations, or compatibility make separate sources of truth necessary. |

The skill does not create empty future-facing documents or invent a license, security contact, support promise, compatibility range, benchmark, roadmap, or release procedure.

## Workflow summary

1. Inspect instructions, current docs, manifests, automation, source entry points, tests, examples, packaging, and license evidence.
2. Build a fact sheet and identify contradictions or genuinely unresolved details.
3. Select Compact, Standard, or Full and assign one authoritative home to each fact.
4. Write copyable user and developer journeys for the actual project type.
5. Run the shortest safe quick-start and development checks that are practical; inspect unsupported release or production commands statically.
6. Validate links, placeholders, examples, and likely sensitive values.
7. Report changed documents, commands actually run, static-only checks, omissions, and unresolved facts.

## Example prompts

```text
Use $write-project-guides to create a release-ready README, usage guide, and development guide for this repository.

Use $write-project-guides to audit these docs against the current source and fix stale commands and broken navigation.

Use $write-project-guides to create the smallest complete documentation map for this CLI and verify its quick start.
```

## Markdown validator

Run the dependency-free validator from the AgentSkills repository root:

```bash
python3 skills/write-project-guides/scripts/validate_project_guides.py /path/to/target-project
```

It scans Markdown files while excluding common dependency, build, version-control, and cache directories. It reports:

- broken local links as errors;
- missing Markdown heading anchors as warnings;
- unresolved template markers as errors;
- likely secrets and personal absolute paths as warnings;
- invalid UTF-8 Markdown as errors.

Useful flags:

| Flag | Behavior |
| --- | --- |
| `--allow-placeholders` | Downgrades unresolved template markers to warnings. Use only while intentionally validating reusable templates. |
| `--strict` | Returns failure when any warning is present. |

The validator does not fetch external URLs or prove that documented application commands work. Those claims require targeted execution or static repository evidence.

## Bundled resources

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Required inspection, document selection, writing, verification, and handoff workflow. |
| [document-selection.md](references/document-selection.md) | Compact, Standard, and Full maps plus source-of-truth ownership. |
| [content-checklists.md](references/content-checklists.md) | Root README, usage, development, contribution, example, and safety checks. |
| [project-types.md](references/project-types.md) | Guidance for CLI, library, web, HTTP, desktop/mobile, plugin, data/ML, and monorepo projects. |
| [release-readiness.md](references/release-readiness.md) | Accuracy, clean-user journey, developer journey, navigation, and public-safety review. |
| [Compact README template](assets/compact/README.md) | One-file starting point for small projects. |
| [Standard README template](assets/standard/README.md) | Landing-page skeleton for the Standard map. |
| [Standard usage template](assets/standard/docs/USAGE.md) | Installation, configuration, workflows, troubleshooting, and support skeleton. |
| [Standard development template](assets/standard/docs/DEVELOPMENT.md) | Setup, structure, checks, packaging, and constraints skeleton. |
| [Standard contribution template](assets/standard/CONTRIBUTING.md) | Optional contribution process skeleton when external contributions are established. |
| [validate_project_guides.py](scripts/validate_project_guides.py) | Dependency-free Markdown guide validator. |
| [openai.yaml](agents/openai.yaml) | ChatGPT desktop display metadata and default invocation prompt. |

## Expected handoff

The skill states which documents were created or updated, why the selected map fits, which commands actually passed, which claims were checked only by inspection, and what remains unresolved or intentionally omitted.

Reusable asset files intentionally contain placeholders. A delivered target project's public guides must not.
