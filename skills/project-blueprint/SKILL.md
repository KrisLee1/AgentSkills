---
name: project-blueprint
description: Design, create, restructure, or audit implementation-ready project documentation before or during software development. Use when Codex needs to turn a product idea, technical proposal, empty repository, monolithic design document, or partially documented codebase into a modular AI-readable documentation system with architecture and specifications, task-routing index, phased plans and acceptance criteria, mutable project status, append-only project and phase logs, ADRs, testing strategy, and contributor/agent instructions.
---

# Project Blueprint

Create a project-specific documentation system that lets humans understand the design and lets AI read only the context required for its current task.

## Workflow

### 1. Inspect before designing

- Inspect the target directory, existing source, manifests, documentation, `AGENTS.md`, and workspace instructions.
- Preserve user edits and existing terminology. Do not replace a working documentation system without explaining the migration.
- Identify the project type, users, distribution model, supported environments, key constraints, current maturity, and requested deliverables.
- Ask only blocking questions. Infer reversible details and mark genuine decisions as `TBD` rather than inventing requirements.
- Read [references/discovery-and-architecture.md](references/discovery-and-architecture.md) when the project scope or architecture is unclear.

### 2. Choose the smallest sufficient document map

- Read [references/document-system.md](references/document-system.md) before creating or restructuring documents.
- Use modular documents when the design is large, multi-package, multi-phase, or intended for repeated AI development.
- Keep a single design document only for small, short-lived projects whose specification remains easy to scan.
- Separate stable specifications, current status, future work, historical logs, and architecture decisions. Never use one file for all five roles.
- Adapt document names and sections to the project. Do not copy technology-specific sections into unrelated projects.

### 3. Establish navigation and AI routing

Create these entry points for modular projects:

- Root `DESIGN.md`: short human-facing navigation entry, not a duplicated specification.
- Root `AGENTS.md`: required reading order, implementation boundaries, update rules, and Phase-close procedure.
- `docs/INDEX.md`: authoritative index plus a task-to-document routing table.
- `docs/PROJECT_STATUS.md`: mutable current truth—active Phase, completed items, blockers, next work, and latest verification.

Require agents to read the index, project status, current Phase, and only task-relevant specifications. Do not tell agents to load the entire documentation tree by default.

### 4. Write implementation-ready design

Cover only relevant domains, but make each selected domain concrete:

- scope, non-goals, users, operating boundaries;
- architecture, component/package ownership, dependency direction, data flow;
- domain/data models, invariants, state transitions, public APIs and compatibility;
- environment lifecycle, persistence, concurrency, error recovery, security and performance;
- framework/platform adapters without duplicating core business logic;
- testing layers, build/package/release gates;
- phased implementation with explicit non-scope and verifiable acceptance criteria.

Prefer types, tables, state diagrams, error codes, examples, and testable rules over aspirational prose. Record meaningful tradeoffs as ADRs.

### 5. Create progress and history systems

Maintain distinct roles:

- `PROJECT_STATUS.md`: overwrite/update current facts after every task.
- `logs/PROJECT_LOG.md`: append only project-level milestones, Phase transitions, major API changes, blockers, and releases.
- `logs/phase-XX.md`: append detailed task records and the Phase-close report.
- `phases/phase-XX-*.md`: planned scope, non-scope, deliverables, dependencies, acceptance checklist.
- `decisions/ADR-NNNN-*.md`: durable architecture choices, alternatives, consequences, and migration.
- Future release `CHANGELOG.md`: public release changes; do not use development logs as a changelog.

Do not use subjective progress percentages. Use checklist state, package/component state, and actual test results.

### 6. Scaffold safely when useful

For a new or empty project, optionally run:

```bash
python3 scripts/scaffold_project_docs.py /absolute/project/path \
  --project-name "Project Name" \
  --summary "One-sentence project purpose"
```

The script copies [assets/project-docs-template](assets/project-docs-template) and substitutes project metadata. It refuses to overwrite existing files. Use `--skip-existing` only after inspecting every conflict, then adapt generated placeholders to the real project.

For existing projects, prefer deliberate edits over scaffolding. Never leave `{{PLACEHOLDER}}` text in delivered documentation.

### 7. Validate and hand off

Read [references/review-checklist.md](references/review-checklist.md) for final review.

- Validate every local Markdown link.
- Search for placeholders, copied project names, stale paths, contradictions, duplicated sources of truth, and unowned decisions.
- Verify task routing points to existing files.
- Verify each Phase has objective acceptance criteria and a matching phase log.
- Verify current status matches checked Phase items and actual test evidence.
- Report files created or changed, key decisions, validation performed, unresolved `TBD`s, and the recommended first implementation task.

## Quality bar

- Make the result specific enough that another AI can implement without redesigning the system.
- Keep the design flexible where product decisions are genuinely open.
- Do not smuggle unrelated requirements, frameworks, packages, names, or licenses from reference projects.
- Do not claim tests, builds, or validation ran when they did not.
- Keep logs append-only and specifications current.
- Treat public API, stored data format, protocol, and token/schema changes as compatibility decisions.

