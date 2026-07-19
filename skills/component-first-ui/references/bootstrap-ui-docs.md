# Bootstrap UI Documentation

Read this reference only when `docs/ui-development.md` is missing or the existing UI documentation is broadly invalid.

## Contents

- [Bootstrap workflow](#bootstrap-workflow)
- [Evidence to inspect](#evidence-to-inspect)
- [Catalog only reusable capabilities](#catalog-only-reusable-capabilities)
- [Choose the documentation shape](#choose-the-documentation-shape)
- [Populate the templates](#populate-the-templates)
- [Validate bootstrap output](#validate-bootstrap-output)

## Bootstrap workflow

1. Resolve the repository root, workspace/package boundaries, and applicable agent instructions.
2. Inspect existing UI or design-system documentation before inventing a parallel system. Preserve useful project terminology and link or consolidate existing sources.
3. Scan UI-relevant project evidence while excluding dependencies, build output, generated files, caches, and vendored code.
4. Build an evidence-backed UI profile.
5. Create the minimum sufficient documentation map from `assets/ui-docs-template`.
6. Validate every documented path and command that can be checked safely.
7. Continue the user's original UI task using the newly created documentation.

Do not stop after producing documentation unless documentation was the entire request.

## Evidence to inspect

Inspect only relevant files for each category:

| Category | Typical evidence |
| --- | --- |
| Workspace | manifests, lockfiles, workspace configuration, package boundaries |
| Runtime | framework, rendering mode, router, language, supported platforms |
| Styling | CSS tooling, theme provider, tokens, reset, global styles, dark mode |
| UI dependencies | installed packages plus actual imports and configuration |
| Components | component directories, public exports, stories, tests, usage sites |
| Architecture | aliases, shared/feature boundaries, ownership, dependency direction |
| Interaction | form patterns, overlays, feedback, loading, empty and error states |
| Quality gates | typecheck, lint, test, build, Storybook, visual or browser commands |
| Constraints | accessibility, responsive targets, browser support, dependency policy |

Do not treat an installed package as the approved standard without confirming configuration or real usage. Do not infer supported variants from a filename alone; inspect public types, exports, stories, tests, or representative call sites.

## Catalog only reusable capabilities

Include:

- shared primitives and patterns;
- stable feature-level components reused within a domain;
- important variants, slots, behaviors, and usage boundaries;
- canonical import paths and lifecycle status.

Exclude:

- page-private layout fragments;
- generated or vendored internals;
- every prop already available from source types;
- speculative components that do not exist;
- temporary experiments and one-off exceptions.

Use semantic categories such as primitives, forms, overlays, navigation, data display, feedback, layout, and feature domains. Capture aliases and capability terms that help future agents find a component without knowing its exact name.

## Choose the documentation shape

Always create:

```text
docs/ui-development.md
docs/ui/components/index.md
```

For roughly 30 or fewer reusable components, keep a concise component table in `components/index.md`.

For larger systems, make `components/index.md` a routing table and create only the applicable catalogs, for example:

```text
docs/ui/components/primitives.md
docs/ui/components/forms.md
docs/ui/components/overlays.md
docs/ui/components/navigation.md
docs/ui/components/data-display.md
docs/ui/components/feedback.md
docs/ui/features/billing.md
```

Split when any of these are true:

- the catalog exceeds about 30–40 reusable components;
- a document exceeds about 250–300 lines;
- independent feature domains have distinct reusable UI;
- most tasks need only a small fraction of the file.

Split a category again near 40–50 components, but keep routing at no more than two levels. Link every catalog directly from an index. Avoid empty category files.

## Populate the templates

Copy and adapt:

- `assets/ui-docs-template/docs/ui-development.md` as the required entry point;
- `assets/ui-docs-template/docs/ui/components/index.md` as the initial catalog or router.

Replace every `{{PLACEHOLDER}}`, remove inapplicable sections and examples, and use repository-relative links. Keep the entry document around 100–200 lines when possible. Put only global stack facts, durable constraints, architecture, routing, validation commands, and maintenance rules there.

If detailed dependency policy, UI patterns, or feature catalogs are necessary, create task-routed documents below `docs/ui/` and link them from the entry document. Do not duplicate the same rule or component record across files.

## Validate bootstrap output

- Confirm documented component imports resolve through the project's actual alias/export rules.
- Confirm catalog files and task-routing links exist.
- Confirm stack choices reflect actual usage, not only dependencies.
- Confirm documented validation commands exist in project scripts or tooling.
- Search generated documentation for unresolved template markers.
- Record unknown durable decisions as `TBD` instead of inventing policy.

Once this bootstrap succeeds, future UI tasks must use the documentation-first workflow and avoid complete rescans unless substantial drift is proven.
