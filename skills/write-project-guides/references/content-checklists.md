# Content Checklists

Use these checklists as selection aids. Include only sections that have evidence and serve the intended audience.

## Repository fact sheet

Establish before drafting:

- one-sentence purpose and concrete audience;
- project type and major components;
- supported runtime, toolchain, operating systems, and architecture when known;
- package manager and lockfile policy;
- install, start, test, lint, format, type-check, build, package, and release commands;
- configuration sources, required keys, defaults, and precedence;
- public executable, library, HTTP, plugin, or UI entry points;
- data stores, migrations, external services, containers, and generated files;
- examples, fixtures, screenshots, and expected outputs already present;
- license, support, contribution, security, and release evidence;
- contradictions and unresolved facts.

## Root README

- State what the project does in concrete language.
- Identify who benefits and the main use case.
- Show the shortest supported success path near the top.
- State prerequisites before commands that depend on them.
- Include one representative example or outcome.
- Link to deeper user and developer guides.
- State maturity or limitations only when supported.
- Link to the actual license; do not infer one from package metadata alone.
- Avoid ornamental badges unless their endpoints and meaning are valid.

## Usage guide

- Define system requirements and supported installation paths.
- Clarify the working directory and whether commands are global, repository-local, or containerized.
- Describe initial setup and required external services.
- Document configuration keys, values, defaults, precedence, and secret-handling expectations.
- Cover the primary workflows in task order, with copyable examples.
- Explain observable results, exit behavior, generated artifacts, or response shape where helpful.
- Separate common paths from advanced or platform-specific paths.
- Document safe upgrade, migration, uninstall, or data cleanup only when applicable.
- Add troubleshooting entries tied to real failure modes and diagnostic commands.
- Point to a verified support or issue channel.

## Development guide

- List exact toolchain requirements and how versions are selected.
- Describe clone/bootstrap steps without assuming private global state.
- Explain environment files without exposing real secrets.
- Summarize repository structure by responsibility, not every directory.
- Define the normal edit-run-check loop.
- List test layers and targeted versus full-suite commands.
- List formatting, lint, type-check, code generation, and build commands.
- Describe debugging entry points, relevant logs, and fixture or local-service setup.
- Explain generated files and whether they should be committed.
- Define packaging and release steps only to the level supported by automation or maintainer docs.
- State platform caveats, known constraints, and safe cleanup steps.

## Contribution guide

Create only when the project welcomes or formally processes contributions.

- Link to development setup instead of duplicating it.
- State how to propose bugs, features, documentation changes, and security reports.
- Explain branch, commit, PR, review, and required-check expectations only when established.
- Require tests or docs appropriate to changed behavior.
- Link to a code of conduct only if it exists.
- Avoid promising response times or acceptance.

## Example quality

For each important example, verify:

- prerequisites and starting state are explicit;
- command, code, filename, port, and identifier spellings match the repository;
- placeholders are clearly identified as user-supplied values, not forgotten template tokens;
- expected output is stable or labeled illustrative;
- later examples do not contradict earlier configuration;
- shell syntax matches the named platform;
- commands do not expose credentials or unexpectedly mutate production state.

## Avoided content

Remove or qualify:

- aspirational features presented as shipped;
- unsupported version ranges or platforms;
- invented performance claims, popularity claims, or testimonials;
- copied commands from another ecosystem;
- personal absolute paths, internal hosts, tokens, and real `.env` values;
- full internal architecture, task status, design debates, and development logs;
- repeated instructions that will drift independently.
