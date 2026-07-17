# Project Documentation Review Checklist

## Structure

- Entry points exist and are concise.
- Index links every authoritative document.
- Task routing covers expected development work.
- Stable specs, plans, current status, history and decisions are separated.
- Every Phase plan has a corresponding phase log.

## Design completeness

- Scope, users, non-goals and operating boundaries are explicit.
- Component/package ownership and forbidden dependencies are clear.
- Core models, invariants, lifecycle and public APIs are concrete.
- Persistence, migration, concurrency, errors and recovery are covered where relevant.
- Security, privacy, accessibility and performance requirements are testable.
- Compatibility and versioning surfaces are identified.
- Framework/platform adapters do not duplicate domain logic.

## Execution readiness

- Phases are ordered by dependencies.
- Acceptance criteria are observable and verifiable.
- Test commands are marked required, optional or not yet available.
- Project status identifies the next executable task.
- Open decisions are labeled `TBD` with owner/impact when known.

## Hygiene

- All local Markdown links resolve.
- No template placeholders remain.
- No names, technologies or requirements leaked from unrelated projects.
- No contradictory defaults, versions, paths or terminology.
- No two documents claim to be the same source of truth.
- Logs contain no fabricated test results.
- Existing user-authored changes were preserved or intentionally migrated.

