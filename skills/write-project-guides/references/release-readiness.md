# Release Readiness Review

Use this review for public release and final delivery. Report unavailable evidence instead of silently passing it.

## Accuracy

- Confirm project name, package names, executables, paths, ports, environment keys, and default values against source.
- Confirm version and platform claims against manifests, CI, packaging, or explicit policy.
- Confirm every documented script exists and is invoked from the correct working directory.
- Distinguish commands actually executed from commands checked only by inspection.
- Remove stale instructions that conflict with current automation.

## New-user journey

- Start from a clean or isolated environment when practical.
- Follow the shortest documented install and quick-start path exactly.
- Verify that prerequisites appear before use and expected success is observable.
- Ensure failures direct the reader toward useful diagnostics or troubleshooting.
- Avoid assuming contributor-only tools in the end-user path.

## Developer journey

- Verify dependency bootstrap and the normal local run path.
- Verify at least the smallest representative test and static-check path.
- Confirm generated files, local services, fixtures, and cleanup expectations.
- Ensure full-suite or release commands are labeled if not executed.
- Check that CI uses compatible commands and versions.

## Navigation and maintenance

- Run the bundled guide validator.
- Check local links, heading anchors, image paths, and filename casing.
- Ensure the README links to each authoritative guide.
- Remove unresolved template syntax, copied names, and empty sections.
- Keep each fact in one authoritative location and replace duplication with links.

## Public-safety checks

- Search documentation history and examples for tokens, credentials, private endpoints, email addresses, personal paths, and internal infrastructure names.
- Do not publish real `.env` content. Use clearly fake values and an allowlisted `.env.example` when appropriate.
- Check screenshots, logs, fixtures, and example outputs for sensitive data.
- Do not create a license, security contact, support promise, SLA, or contribution policy by assumption.
- Confirm that destructive, privileged, migration, deployment, and production-affecting commands carry clear scope and warnings.

## Handoff evidence

List:

- documents changed;
- user journey executed and result;
- development checks executed and result;
- static-only verification;
- unverified platforms or workflows;
- remaining release blockers or explicit `TBD` decisions.
