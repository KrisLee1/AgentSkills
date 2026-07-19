---
name: component-first-ui
description: Build, modify, or review frontend interfaces through project-maintained UI development documentation and a component-first workflow. Use when Codex implements pages, reusable components, design-system primitives, responsive layouts, interactions, or design mockups in a new or existing frontend project. Read the project's UI entry document before UI work; bootstrap it by scanning the project when absent; discover components through its indexed catalogs instead of repeatedly scanning the source tree; follow explicit requirements and documented framework, styling, UI, icon, motion, accessibility, and validation constraints; select compatible libraries or implement without new dependencies as required; and update the documentation after durable UI changes.
---

# Component-First UI

Develop UI from a maintained project knowledge base. Reuse documented capabilities, load only task-relevant context, and leave the UI documentation more accurate than you found it.

## Required entry point

1. Resolve the project root and read repository instructions such as `AGENTS.md`.
2. Read `docs/ui-development.md` before inspecting or changing UI code.
3. If the entry document exists, treat it as the operational index. Do not rescan the entire project merely to rediscover its UI stack or components.
4. If it does not exist, read [references/bootstrap-ui-docs.md](references/bootstrap-ui-docs.md), scan the project once, create the entry and catalog from [the UI entry template](assets/ui-docs-template/docs/ui-development.md) and [the component catalog template](assets/ui-docs-template/docs/ui/components/index.md), then continue the original UI task.
5. Apply this precedence: current explicit user requirements, durable project UI documentation, verified source/configuration facts, then this Skill's defaults.
6. When documentation contradicts verified code, follow the code for the current fact and repair the documentation in the same task.

The entry document is a routing surface, not a duplicate specification. Keep global rules and the task-to-document map there. Keep detailed component inventories in indexed catalog files.

## Load context progressively

When UI documentation exists:

- Read the entry document first.
- Follow its routing table to only the relevant component, feature, pattern, or library documents.
- Search `docs/ui/` by semantic capability when routing is unclear, for example `rg -i "dialog|modal|confirm|overlay" docs/ui`.
- Open component source only after the documentation identifies a candidate, or when the current change directly targets that source.
- Inspect manifests, configuration, and nearby implementation only as needed to confirm current APIs or resolve a contradiction.
- Do not read every catalog and do not scan the whole source tree by default.

For a small project, allow `docs/ui/components/index.md` to contain the concise component catalog. Split it into category or feature catalogs when it exceeds about 30–40 reusable components, 250–300 lines, or covers independent UI domains. Keep category files focused; split again near 40–50 components. Use at most two routing levels and list each component authoritatively in one catalog only.

## Discover before creating

1. Translate the requested interface into semantic capabilities such as action, selection, overlay, navigation, feedback, data display, or domain-specific composition.
2. Query the documented catalog by capability, aliases, and interaction—not only by the desired component name.
3. Inspect the most relevant candidates' source, exports, variants, slots, stories, and tests as needed.
4. Reuse or compose an existing component when its semantics and behavior fit.
5. Extend an existing component only with backward-compatible, generally reusable behavior.
6. Keep one-off or domain-specific UI inside its feature rather than inflating the shared system.

Treat a component as shared when it is a design-system primitive, is used or clearly expected in multiple places, encapsulates stable error-prone interaction, or enforces important visual/accessibility rules. Do not wrap every element or create universal components dominated by boolean props.

## Select an implementation path

Use this order unless the current request overrides it:

1. Reuse a documented project component.
2. Compose documented primitives and patterns.
3. Add a missing component from the project's approved library using its established installation or generation method.
4. Select a compatible library only when documented options cannot satisfy the requirement and project dependency policy permits it.
5. Implement with native platform features and project code when new dependencies are prohibited, the behavior is simple, or a local implementation is the better fit.

Read [references/library-selection.md](references/library-selection.md) before recommending, adding, replacing, or mixing UI, icon, or motion libraries. Do not introduce a second library for an already-covered responsibility without a documented gap and rationale.

When implementing without a library, prefer semantic platform elements and preserve keyboard, focus, ARIA, reduced-motion, layering, scroll, and state behavior. Give complex controls such as dialogs, comboboxes, menus, tooltips, and date pickers proportionate accessibility scrutiny.

## Implement within project conventions

- Follow documented component layers, directory ownership, naming, exports, styling, tokens, theme, responsive breakpoints, and state-management patterns.
- Prefer composition and explicit slots over copied markup or expanding boolean prop matrices.
- Use semantic HTML and expose clear focus states.
- Cover relevant loading, empty, error, disabled, selected, and destructive states.
- Use the existing icon family; do not substitute emoji or arbitrary glyphs for product icons.
- Use CSS for simple transitions. Use the approved motion library for orchestrated layout, gesture, or enter/exit behavior, and respect reduced motion.
- Preserve existing public APIs unless the task explicitly includes a migration.
- Add or update stories and tests according to documented project practice.

## Validate and maintain documentation

Read [references/validation-and-maintenance.md](references/validation-and-maintenance.md) before final verification.

1. Run the most targeted relevant checks, then the documented type, lint, test, build, Storybook, or visual checks proportionate to the change.
2. Inspect the interface at relevant viewport sizes and interaction states when browser or rendering tools are available.
3. Update UI documentation in the same task when a reusable component, public capability, durable constraint, dependency, path, pattern, or validation command changes.
4. Update only the owning catalog for an existing category. Update an index only when routing or category structure changes.
5. Do not catalog page-private components, temporary exceptions, full prop APIs already expressed by types, or implementation details that do not affect reuse.
6. Validate documentation links and import paths touched by the task. Do not claim checks that were not run.

## Handle documentation drift

- Repair a wrong import, missing component entry, or isolated mismatch through targeted inspection.
- Rescan only the affected UI area when a directory, library, or feature domain has moved substantially.
- Rebuild the documentation through the bootstrap workflow only when most paths, dependencies, or constraints are invalid.
- Do not trigger a full scan solely because a review date is old.

Finish by reporting the UI implemented, components reused or added, dependencies changed, documentation updated, and verification performed.
