---
name: write-project-guides
description: Create, restructure, audit, or update evidence-based project usage and development documentation for private delivery or public open-source release. Use when Codex needs to write or improve a README, quick start, installation and configuration guide, user guide, developer setup guide, contribution guide, troubleshooting guide, or release-ready documentation; verify that documented commands, paths, prerequisites, and configuration match the repository rather than inventing them.
---

# Write Project Guides

Produce documentation that lets a new user reach a working result and a new developer make a verified change without private knowledge.

## Workflow

### 1. Inspect before writing

- Read repository instructions, existing documentation, manifests, lockfiles, task runners, CI workflows, examples, configuration samples, source entry points, tests, packaging, release files, and license material.
- Preserve valid project terminology and user-authored content. Treat existing docs as claims to verify, not automatic truth.
- Build a private fact sheet containing the project purpose, audiences, project type, supported environments, installation paths, executable entry points, configuration, common workflows, validation commands, distribution model, and unresolved facts.
- Prefer `rg` and targeted file reads. Do not load generated output, vendored dependencies, caches, or the entire repository by default.
- Ask only about facts that cannot be discovered and would materially change the result. Mark unresolved details clearly; never guess versions, ports, compatibility, performance, support policy, or release procedure.

### 2. Select the document map

Read [references/document-selection.md](references/document-selection.md) before creating or substantially restructuring documents.

- Use Compact for a small single-purpose project whose user and developer paths remain easy to scan in one `README.md`.
- Use Standard by default for a normal application or library: a concise `README.md`, `docs/USAGE.md`, and `docs/DEVELOPMENT.md`; add `CONTRIBUTING.md` only when external contribution is intended.
- Use Full for multi-package, multi-product, operationally complex, or public-API-heavy projects. Add only the modules justified by repository facts.
- Keep one authoritative home for each command, configuration contract, and compatibility statement. Link instead of duplicating details.
- Reuse the Markdown skeletons under `assets/` selectively. Replace every placeholder and remove irrelevant sections before delivery.

### 3. Write for the actual project

- Read [references/content-checklists.md](references/content-checklists.md) for the user and developer content requirements.
- Read [references/project-types.md](references/project-types.md) only for the detected project type.
- Match the repository's established documentation language unless the user specifies another language. Keep code, identifiers, and commands exact.
- Lead the root README with purpose, audience, proof of value, and the shortest successful path. Keep deep explanations in the appropriate guide.
- Make examples copyable and internally consistent. Define the working directory, prerequisite state, inputs, and expected result when ambiguity is likely.
- Separate required steps from optional alternatives. Label platform-specific instructions and destructive or production-affecting commands.
- Describe only public or user-approved interfaces. Exclude secrets, private endpoints, personal paths, internal operational details, and copied `.env` values.
- Do not create or change a license, contribution policy, support commitment, compatibility promise, roadmap, benchmark, badge, or security policy without evidence or explicit user direction.

### 4. Verify claims proportionally

- Confirm commands against manifests and automation before running them.
- Run the shortest safe quick-start path and relevant development checks when dependencies and environment make that practical. Do not start long-lived services without a bounded verification method.
- Do not execute publishing, deployment, migration, destructive, paid, privileged, credentialed, or externally visible steps merely to validate documentation. Verify those statically unless the user explicitly authorizes execution.
- Record what was executed, what was checked statically, and what remains unverified. Never convert a static inspection into a claim that a command passed.
- Run `python3 scripts/validate_project_guides.py /absolute/project/path` after editing. Fix broken local links and unresolved template markers before delivery.
- Read [references/release-readiness.md](references/release-readiness.md) for public-release work or final review.

### 5. Hand off

Report:

- documents created, restructured, or updated;
- the selected Compact, Standard, or Full map and why it fits;
- commands actually executed and their results;
- commands or claims checked only by inspection;
- unresolved facts, intentionally omitted sections, and recommended next documentation task.

## Boundaries

- Use project design or architecture documents as evidence, but do not turn release-facing guides into project-management logs or full internal specifications.
- For architecture-first planning, phase plans, ADRs, mutable status, or AI task routing, use a project-design documentation workflow instead of expanding this skill's public-guide scope.
- When diagnosing documentation without a request to edit it, report findings and proposed changes without modifying files.
