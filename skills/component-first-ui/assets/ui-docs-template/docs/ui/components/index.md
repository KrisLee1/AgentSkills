# UI Component Catalog

Search this documentation by semantic capability when the exact component name is unknown:

```bash
rg -i "<component|capability|interaction>" docs/ui
```

## Catalog mode

{{USE_ONE_OF_THE_FOLLOWING_MODES_AND_DELETE_THE_OTHER}}

### Compact catalog

Use this table when the project has roughly 30 or fewer reusable components.

| Component | Import | Purpose | Capabilities and boundaries | Status |
| --- | --- | --- | --- | --- |
| {{COMPONENT_NAME}} | `{{CANONICAL_IMPORT}}` | {{PURPOSE}} | {{CAPABILITIES_AND_BOUNDARIES}} | {{STATUS}} |

### Routed catalog

Use this table when components are split by semantic category or feature domain. Keep representative aliases in `Includes`; list complete component records only in the linked owning catalog.

| Category | Includes and search terms | Catalog |
| --- | --- | --- |
| {{CATEGORY}} | {{REPRESENTATIVE_COMPONENTS_AND_ALIASES}} | [{{CATALOG_LABEL}}]({{CATALOG_PATH}}) |

## Shared rules

- Search this catalog before creating a component.
- Reuse or compose documented capabilities before extending the system.
- Keep feature-specific UI in its feature catalog.
- Record each reusable component authoritatively in one catalog only.
- Keep full prop definitions in source types, stories, and tests.
- Update the owning catalog whenever a reusable component or public capability changes.
