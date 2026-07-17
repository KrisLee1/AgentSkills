# Discovery and Architecture Guide

Read this reference when requirements are incomplete, a repository already exists, or architectural boundaries must be derived.

## Discovery checklist

Determine:

- Product purpose and primary users.
- Library, application, service, CLI, plugin, SDK, or mixed workspace.
- Distribution and deployment model.
- Supported runtimes, frameworks, browsers, operating systems, and minimum versions.
- Client/server/offline boundaries.
- Data ownership, persistence, synchronization, import/export, and migrations.
- Public API consumers and compatibility expectations.
- Security, privacy, accessibility, performance, and licensing constraints.
- Expected phases, release target, and explicit non-goals.

Ask a question only when the answer materially changes architecture or would authorize a different scope. Otherwise make a labeled, reversible assumption.

## Repository inspection

Read in this order:

1. Workspace instructions and existing `AGENTS.md`.
2. Root manifests, workspace files, build configuration, and package boundaries.
3. Existing README/design/status/roadmap documents.
4. Source entry points and public exports.
5. Tests, CI, release tooling, and persistence schemas.

Preserve existing user changes. If documentation and implementation disagree, record the discrepancy instead of silently choosing one.

## Architecture decisions

For each subsystem define:

- responsibility and non-responsibility;
- public inputs/outputs;
- owned state and lifecycle;
- dependencies and forbidden dependencies;
- failure behavior and cleanup;
- test boundary;
- compatibility surface.

Prefer one implementation of domain logic with thin framework/platform adapters. Separate pure domain logic from environment effects when this improves portability and testing.

## Detail calibration

- Small prototype: scope, architecture sketch, core model, Phase plan, status and tests may be enough.
- Reusable library: add public API, packaging, compatibility, adapters, migration and tarball smoke tests.
- Stateful app/service: add data model, state transitions, persistence, concurrency, auth/security, observability and recovery.
- Multi-package workspace: add dependency graph, package ownership, release/version strategy and cross-package testing.

Avoid premature implementation details that do not constrain behavior. Include exact types, formats and algorithms when ambiguity would force implementers to redesign.

