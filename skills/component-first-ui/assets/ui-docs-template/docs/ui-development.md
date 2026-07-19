# UI Development

This file is the required entry point for UI work. Read it before inspecting or changing UI code. Discover reusable UI through the linked catalogs; do not rescan the complete source tree while this documentation remains valid.

## Stack summary

| Area | Choice | Evidence |
| --- | --- | --- |
| Framework/runtime | {{FRAMEWORK_AND_RUNTIME}} | {{FRAMEWORK_EVIDENCE}} |
| Language | {{LANGUAGE}} | {{LANGUAGE_EVIDENCE}} |
| Styling/theme | {{STYLING_AND_THEME}} | {{STYLING_EVIDENCE}} |
| UI components | {{UI_COMPONENT_SYSTEM}} | {{UI_COMPONENT_EVIDENCE}} |
| Icons | {{ICON_SYSTEM}} | {{ICON_EVIDENCE}} |
| Motion | {{MOTION_SYSTEM}} | {{MOTION_EVIDENCE}} |
| Package manager | {{PACKAGE_MANAGER}} | {{PACKAGE_MANAGER_EVIDENCE}} |

## Global constraints

- {{GLOBAL_CONSTRAINT_1}}
- {{GLOBAL_CONSTRAINT_2}}
- {{GLOBAL_CONSTRAINT_3}}

## UI architecture

| Layer | Location | Ownership rule |
| --- | --- | --- |
| Shared primitives | `{{PRIMITIVE_PATH}}` | {{PRIMITIVE_RULE}} |
| Shared patterns | `{{PATTERN_PATH}}` | {{PATTERN_RULE}} |
| Feature UI | `{{FEATURE_PATH_PATTERN}}` | {{FEATURE_RULE}} |
| Tokens/theme | `{{TOKEN_PATH}}` | {{TOKEN_RULE}} |
| Public exports | `{{EXPORT_PATH}}` | {{EXPORT_RULE}} |

## Documentation routing

| Need | Read |
| --- | --- |
| Discover a reusable component | [UI component catalog](ui/components/index.md) |
| {{ROUTING_NEED_1}} | [{{ROUTING_LABEL_1}}]({{ROUTING_PATH_1}}) |
| {{ROUTING_NEED_2}} | [{{ROUTING_LABEL_2}}]({{ROUTING_PATH_2}}) |

If the category or component name is unclear, search by semantic capability:

```bash
rg -i "<component|capability|interaction>" docs/ui
```

Open candidate source files only after finding them in the catalog or when directly editing them.

## Component decision order

1. Reuse a documented component.
2. Compose documented primitives and patterns.
3. Add from the approved UI library.
4. Select a compatible dependency only when policy permits and a concrete gap exists.
5. Implement with native platform features and project code when dependencies are prohibited or unnecessary.

## Validation

| Check | Command or procedure |
| --- | --- |
| Type checking | `{{TYPECHECK_COMMAND}}` |
| Lint | `{{LINT_COMMAND}}` |
| Tests | `{{TEST_COMMAND}}` |
| Build | `{{BUILD_COMMAND}}` |
| Component/visual review | {{VISUAL_REVIEW_PROCEDURE}} |

## Maintenance contract

Update this documentation in the same task when reusable UI capabilities, durable constraints, dependencies, canonical paths, routing, or validation commands change.

- Update only the owning catalog for an existing component category.
- Update an index only when routing or category structure changes.
- Do not catalog page-private components, temporary exceptions, duplicated full prop APIs, or internal details that do not affect reuse.
- Repair targeted inconsistencies when found. Rescan only an affected area unless most of this UI model is invalid.
