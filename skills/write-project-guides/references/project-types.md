# Project-Type Guidance

Read only the relevant sections after detecting the project type. Mixed projects may use more than one section, but keep the reader journey coherent.

## CLI

- Show installation, `--help`, one minimal command, and one realistic workflow.
- Document stdin/stdout/stderr, exit codes, output formats, config lookup, and shell completion when implemented.
- Distinguish global installation from running from source.
- Include safe examples; label commands that overwrite files or modify remote state.

## Library or SDK

- State supported languages and runtime versions from package and CI evidence.
- Show package installation, import, initialization, one useful call, result handling, and error handling.
- Separate public API from internals. Link generated API reference when available.
- Document async behavior, thread safety, network behavior, retries, and compatibility only when relevant and verified.
- Include publishing and versioning details only for maintainers and only when established.

## Web application

- Distinguish end-user access from local developer startup.
- Document required frontend/backend services, ports, proxies, environment variables, and seed data.
- Define authentication assumptions and browser support only from evidence.
- Explain production build or deployment separately from development hot reload.

## HTTP service

- Show service startup, readiness verification, authentication setup, and one request/response example.
- State host/port defaults, required dependencies, configuration precedence, and persistence behavior.
- Link or generate API reference only from the authoritative contract.
- Keep production deployment, migrations, backup, rollback, and security warnings explicit and separate.

## Desktop or mobile application

- Separate user installation from source build.
- State supported operating systems, SDKs, signing requirements, permissions, and hardware constraints only from evidence.
- Document development launch, packaging, emulator/device setup, and release signing without exposing credentials.

## Plugin, extension, or integration

- Identify the host product and supported host versions.
- Explain installation or registration, required permissions, configuration, reload/restart, and removal.
- Provide a minimal host-specific verification path.
- Separate local development linking from distributable installation.

## Data or ML project

- Document dataset provenance, expected schema, storage location, preprocessing, reproducibility controls, and hardware needs.
- Distinguish training, evaluation, inference, and serving workflows.
- State model artifacts, licenses, metrics, and limitations only when evidenced.
- Never include private data paths, credentials, or claims that cannot be reproduced.

## Monorepo

- Begin with a component map and supported top-level workflows.
- Define workspace-level versus package-level commands and working directories.
- Put package-specific usage near the package when it has a distinct audience.
- Keep shared prerequisites, bootstrap, and validation authoritative at the root.
- Explain dependency or release coupling only as established by tooling.
