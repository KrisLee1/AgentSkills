# Library Selection

Read this reference before recommending, adding, replacing, or mixing UI, icon, or motion libraries.

## Decision order

1. Obey the current user's explicit library and dependency constraints.
2. Follow the durable policy in `docs/ui-development.md` and linked library documentation.
3. Prefer libraries already configured and used by the project.
4. Add from the approved library before selecting another library.
5. Introduce a new dependency only for a concrete capability gap.
6. Use native platform features or project code when dependencies are prohibited or unnecessary.

Treat one-off user instructions as task-local unless the user establishes a durable project convention. Update project documentation only for durable choices.

## Evaluate a new dependency

Check current primary documentation and project evidence rather than relying on memory. Evaluate:

- framework, language, renderer, SSR/RSC, browser, and platform compatibility;
- peer dependencies and compatibility with installed versions;
- accessibility behavior and keyboard/focus support;
- styled versus headless fit with the project's styling and tokens;
- theming, variants, composition, and escape hatches;
- bundle and tree-shaking characteristics appropriate to the project;
- maintenance status, release stability, license, and migration burden;
- overlap with installed libraries and the cost of multiple visual/behavior systems;
- official installation or code-generation workflow.

If two options are viable, prefer the one that fits existing conventions with the least new surface area. Document the selected responsibility and why existing options were insufficient.

## UI component libraries

- Prefer the project's design system and approved primitives.
- Keep one coherent source for each responsibility unless a documented exception exists.
- Distinguish styled systems from headless primitives; do not add both reflexively.
- Use the library's supported composition, theming, and generation patterns.
- Inspect generated code before integrating it and preserve project configuration.

## Icon libraries

- Reuse the documented icon family for consistent stroke, fill, optical size, and naming.
- Avoid emoji, Unicode symbols, or arbitrary mixed SVG styles as product icons.
- Do not add a large icon dependency for one simple asset when a project-approved local SVG is more appropriate.
- Make decorative icons hidden from assistive technology and label meaningful icon-only controls.
- Prefer `currentColor` and existing sizing conventions for local SVG components.

## Motion libraries

- Use CSS for simple hover, color, opacity, and small transform transitions.
- Reuse the approved motion library for orchestration, gesture, layout, or complex enter/exit animation.
- Do not add a motion dependency for a trivial transition.
- Respect `prefers-reduced-motion`; never make motion the only signal of state.
- Keep transitions interruptible and avoid blocking input.

## Implementing without new dependencies

Prefer semantic native elements such as `button`, `input`, `select`, `details`, and `dialog` where they meet the support requirements. Reuse project utilities before writing new infrastructure.

For custom interactive components, verify the relevant behavior:

- keyboard navigation and activation;
- visible focus, focus movement, trapping, and restoration;
- accessible name, role, state, and relationships;
- Escape, outside interaction, dismissal, and disabled behavior;
- portal, layering, scroll locking, clipping, and positioning;
- loading, empty, error, selected, and destructive states;
- pointer, touch, viewport, and reduced-motion behavior.

Do not represent a complex accessible control as finished merely because its default visual state renders correctly.

## Record the decision

After a durable dependency change, update the UI documentation with:

- library and owned responsibility;
- canonical import or generation method;
- allowed usage and relevant constraints;
- replaced or overlapping library status;
- validation or migration implications.
