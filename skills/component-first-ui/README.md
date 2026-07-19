# Component-First UI

[简体中文](README.zh-CN.md)

`component-first-ui` guides Codex through frontend implementation and review using a project-maintained UI knowledge base. It discovers reusable capabilities from documented catalogs, follows project stack and accessibility constraints, and updates durable UI documentation when the system changes.

The authoritative agent workflow is [SKILL.md](SKILL.md).

## Use this skill when

- implementing pages, responsive layouts, or reusable components;
- adding or reviewing interaction, motion, feedback, forms, navigation, or data display;
- choosing an implementation path among project components, approved libraries, and native platform behavior;
- bootstrapping UI development documentation for a project that does not yet have it;
- reviewing UI changes for component reuse, accessibility, documentation drift, and targeted validation.

It is not a generic visual-style preset. It follows the target repository's documented UI system and verified source facts.

## Required target-project entry point

The workflow expects `docs/ui-development.md` in the target project. That document routes Codex to the relevant component catalogs, constraints, stack evidence, and validation commands.

If it is missing, the skill performs a one-time UI-focused scan and creates at least:

```text
docs/
  ui-development.md
  ui/
    components/
      index.md
```

The catalog stays compact for roughly 30 or fewer reusable components. Larger systems are routed into category or feature catalogs without exceeding two navigation levels.

## Workflow summary

1. Read repository instructions and `docs/ui-development.md`.
2. Bootstrap the UI documentation only when the required entry point is missing or broadly invalid.
3. Translate the request into semantic capabilities and search the documented catalog.
4. Reuse, compose, extend, add from an approved library, or implement locally in that order.
5. Follow the project's component boundaries, styling, icons, motion, responsive behavior, and accessibility rules.
6. Run proportionate checks and inspect relevant interaction states.
7. Update the owning UI document or catalog when a durable capability or constraint changes.

## Example prompts

```text
Use $component-first-ui to implement a responsive account settings page using the project's existing components.

Use $component-first-ui to review this dialog implementation for reuse, keyboard behavior, focus management, and documentation drift.

Use $component-first-ui to add the missing reusable empty-state pattern without introducing a new dependency.
```

## Implementation decision order

| Priority | Path |
| --- | --- |
| 1 | Reuse a documented project component. |
| 2 | Compose documented primitives and patterns. |
| 3 | Add a missing component from the project's approved library. |
| 4 | Select a compatible dependency only when policy permits and a concrete gap exists. |
| 5 | Use semantic native elements and project code when a dependency is unnecessary or prohibited. |

Complex controls receive proportionate scrutiny for keyboard behavior, focus, ARIA, layering, scroll, dismissal, responsive behavior, touch, and reduced motion.

## Bundled resources

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Required workflow, decision order, implementation rules, and handoff contract. |
| [bootstrap-ui-docs.md](references/bootstrap-ui-docs.md) | Evidence to inspect and the one-time documentation bootstrap process. |
| [library-selection.md](references/library-selection.md) | Compatibility, accessibility, overlap, maintenance, and dependency decision criteria. |
| [validation-and-maintenance.md](references/validation-and-maintenance.md) | Targeted checks, interaction states, catalog updates, and drift handling. |
| [UI entry template](assets/ui-docs-template/docs/ui-development.md) | Starting point for stack evidence, constraints, routing, and validation commands. |
| [Component catalog template](assets/ui-docs-template/docs/ui/components/index.md) | Compact or routed reusable-component inventory. |
| [openai.yaml](agents/openai.yaml) | ChatGPT desktop display metadata and default invocation prompt. |

## Expected handoff

The skill reports the UI implemented or reviewed, components reused or added, dependency changes, documentation updates, and checks actually performed. It does not claim visual, browser, test, or build verification that was not run.

## Maintenance notes

- Keep the entry document concise and route detail behind links.
- Give each reusable component one authoritative catalog record.
- Do not catalog page-private fragments, temporary experiments, generated internals, or full prop APIs already expressed by source types.
- Repair isolated drift locally; rescan only the affected UI area unless most of the documented model is invalid.
