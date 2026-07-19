# Validation and Documentation Maintenance

Read this reference before final verification and handoff.

## Validate proportionately

Run the narrowest useful checks first, then the project-documented gates appropriate to the change:

1. component or feature tests;
2. type checking and linting;
3. broader tests and build;
4. Storybook or component rendering;
5. browser or visual inspection at relevant viewports.

For interaction changes, inspect the states that matter: default, hover, focus, active, selected, disabled, loading, empty, error, destructive, open/closed, and reduced motion. Check keyboard navigation, focus order/restoration, accessible names, responsive layout, overflow, text wrapping, theme modes, and touch targets when applicable.

Use the project's documented commands. Do not install unrelated tooling only to validate a small change. Report skipped checks and the reason.

## Maintain the operational index

Update `docs/ui-development.md` when a durable global fact changes:

- framework, styling, tokens, theme, or package manager;
- approved UI, icon, or motion responsibility;
- shared/feature directory or export convention;
- global accessibility, responsive, or dependency policy;
- routing to a new or renamed documentation category;
- validation command or required quality gate.

Keep task-local exceptions out of global documentation unless the user turns them into a durable rule.

## Maintain component catalogs

Update the owning catalog when:

- a reusable component is added, renamed, moved, deprecated, or removed;
- its canonical import changes;
- its important variants, slots, interaction capabilities, or reuse boundary change;
- a feature-private component becomes shared or a shared component becomes domain-owned.

Use concise records such as:

| Component | Import | Purpose | Capabilities | Status |
| --- | --- | --- | --- | --- |
| ConfirmDialog | `@/components/patterns/confirm-dialog` | Confirm consequential actions | async action, pending state, destructive variant | stable |

Describe semantic capabilities so agents can find components without exact names. Keep full props and implementation details in source types, stories, and tests.

Do not catalog:

- page-private fragments;
- generated or vendored internals;
- temporary experiments;
- style-only changes that do not alter reusable capability;
- duplicated records copied into multiple categories.

Update a category index only when routing changes. When a new category is required, create its catalog and add one route from the nearest index.

## Check for drift without rescanning

Use targeted checks when documentation exists:

- resolve only import paths used or edited by the task;
- inspect only affected package/configuration entries;
- compare only relevant public exports, stories, tests, and usage sites;
- search `docs/ui/` before searching source for reusable capabilities.

Handle drift by scope:

| Drift | Action |
| --- | --- |
| One wrong path or missing record | Inspect the component and repair its catalog entry |
| A category or feature moved | Rescan that UI area and rebuild the affected catalog/routing |
| Most dependencies, paths, and constraints are invalid | Run the full bootstrap workflow |

Do not rescan because a date is old. Rescan because verified contradictions show the documented model is no longer dependable.

## Documentation quality gate

Before finishing:

- verify links added or changed by the task;
- verify documented canonical imports touched by the task;
- ensure every component has one authoritative catalog record;
- ensure routing points to existing files;
- search changed documentation for unresolved placeholders;
- remove stale entries caused by renames or deletion;
- keep the entry document concise and move conditional detail behind links;
- state exactly which validation was performed.
