# Document Selection

Choose the smallest map that keeps user and developer journeys easy to navigate. Preserve an existing coherent map unless restructuring has a clear benefit.

## Compact

Use one `README.md` when all of these are true:

- the project has one primary install and run path;
- configuration and troubleshooting are short;
- the developer workflow needs only a few commands;
- the README remains comfortably scannable after both journeys are included.

Recommended order:

1. Purpose and audience
2. Features or demonstrated outcome
3. Requirements
4. Quick start
5. Configuration and usage
6. Development
7. Troubleshooting or limitations
8. License and support links

Use `assets/compact/README.md` as a skeleton, not as mandatory wording.

## Standard

Use this default map when usage or development needs sustained explanation:

```text
README.md
docs/
  USAGE.md
  DEVELOPMENT.md
CONTRIBUTING.md   # only for an external contribution workflow
```

- Keep `README.md` as the landing page and shortest successful path.
- Put installation variants, configuration, workflows, and troubleshooting in `USAGE.md`.
- Put source setup, repository structure, checks, debugging, build, and release facts in `DEVELOPMENT.md`.
- Put community contribution mechanics in `CONTRIBUTING.md`; do not duplicate local setup.

Use the files under `assets/standard/` selectively.

## Full

Start with Standard, then add only justified modules such as:

```text
docs/
  INSTALLATION.md
  CONFIGURATION.md
  USAGE.md
  API.md
  DEVELOPMENT.md
  ARCHITECTURE.md
  TROUBLESHOOTING.md
  DEPLOYMENT.md
  UPGRADING.md
CONTRIBUTING.md
SECURITY.md       # only from an established security policy
```

Full is appropriate when at least one condition applies:

- multiple packages or independently deployed components;
- distinct operator and end-user workflows;
- several supported installation or platform paths;
- a substantial stable public API;
- complex configuration, migrations, compatibility, or recovery;
- contributors routinely need architectural boundaries to work safely.

Do not create empty future-facing modules. A missing module is better than a page of placeholders.

## Sources of truth

Assign one responsibility to each document:

| Document | Owns |
| --- | --- |
| README | Project promise, audience, shortest successful path, navigation |
| Usage | Complete user workflows, behavior, examples, troubleshooting |
| Configuration | Supported keys, defaults, precedence, security notes |
| Development | Local setup, source layout, checks, build, debug, maintainer workflow |
| Architecture | Stable boundaries and data flow needed by contributors |
| Contributing | Issue/PR process, contribution expectations, community conduct links |
| API | Supported public interface and compatibility notes |
| Deployment | Operator procedure, safety boundaries, rollback and verification |
| Upgrading | Version-to-version compatibility and migrations |

Link to generated API documentation rather than manually duplicating it when generation is authoritative.

## Existing documentation

- Keep established filenames when they are clear and consistently linked.
- Avoid case-only renames across platforms.
- Update inbound links in the same change when moving a document.
- Preserve useful prose and contributor knowledge; verify commands and stale claims line by line.
- Explain a large restructure in the handoff and list any redirects or compatibility files retained.
