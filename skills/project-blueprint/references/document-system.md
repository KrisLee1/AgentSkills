# Modular Project Documentation System

Use this reference to select and populate project documents. Omit irrelevant modules; preserve the separation of responsibilities.

## Recommended tree

```text
AGENTS.md
DESIGN.md
docs/
  INDEX.md
  PROJECT_STATUS.md
  architecture/
    overview.md
    boundaries.md
  specifications/
    domain-model.md
    public-api.md
    runtime.md
    persistence.md
  engineering/
    testing.md
    packaging.md
    coding-standards.md
  phases/
    phase-01-*.md
  decisions/
    README.md
    ADR-0001-*.md
  logs/
    README.md
    PROJECT_LOG.md
    phase-01.md
```

## Document responsibilities

### Root DESIGN.md

Keep it short. State purpose and link to index, status, architecture, active Phase, and logs. Do not copy the specifications into it.

### AGENTS.md

Define required reading order, forbidden dependency/scope rules, per-task documentation updates, test-reporting honesty, and Phase-close workflow.

### INDEX.md

List all authoritative documents and a task routing table. Define precedence when documents conflict and maintenance rules for each document class.

### Architecture

Describe stable system boundaries, dependency direction, data flow and non-goals. Avoid daily progress.

### Specifications

Describe current normative behavior. Use concrete models, invariants, APIs, lifecycle, errors, concurrency, security, performance and compatibility. Remove superseded prose after an ADR updates the active design.

### Phase plans

For each Phase include goal, dependencies, scope, explicit non-scope, deliverables, acceptance checklist, required test commands and close-report destination.

### PROJECT_STATUS.md

Maintain active Phase, status, current objective, completed/current checklist, subsystem/package state, blockers, next ordered tasks, latest actual verification and backlog. This file is mutable.

### Logs

Project log: append only major milestones. Phase log: append each development task with completed work, changed areas, API/data changes, commands/results, decisions, risks and next step. Append a comprehensive Phase-close report.

### ADRs

Use for decisions that affect architecture, public compatibility, persistence/protocol formats, important dependencies or security. Include status, context, decision, alternatives, consequences and migration.

## Avoiding duplicate truth

- Specification answers “how it must behave.”
- Phase plan answers “what this stage will deliver.”
- Status answers “where the project is now.”
- Log answers “what happened.”
- ADR answers “why an important choice was made.”
- Changelog answers “what users receive in a release.”

Do not repeat detailed API definitions in status or logs. Link to the authoritative specification.

## Task routing examples

| Task | Read |
|---|---|
| Domain types | Status, current Phase, domain model |
| Runtime lifecycle | Status, current Phase, architecture, runtime spec |
| Persistence migration | Status, persistence spec, migration ADRs, current Phase |
| Framework adapter | Status, runtime spec, adapter spec, package boundaries |
| Test/release | Status, current Phase, testing, packaging |
| Architecture change | Overview, affected specs, ADR index |

