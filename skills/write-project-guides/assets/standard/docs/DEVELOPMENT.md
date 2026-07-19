# Develop {{PROJECT_NAME}}

## Prerequisites

- {{TOOLCHAIN_AND_VERSION_SOURCE}}
- {{REQUIRED_EXTERNAL_SERVICE}}

## Set up the source tree

Run these commands from {{WORKING_DIRECTORY}}:

```sh
{{DEPENDENCY_SETUP}}
{{LOCAL_CONFIGURATION_SETUP}}
```

Do not put real credentials in committed files. {{LOCAL_SECRET_GUIDANCE}}

## Repository structure

| Path | Responsibility |
| --- | --- |
| `{{PATH}}` | {{RESPONSIBILITY}} |

## Develop locally

```sh
{{DEVELOPMENT_COMMAND}}
```

{{LOCAL_SERVICES_PORTS_AND_DEBUGGING}}

## Check changes

```sh
{{TARGETED_TEST_COMMAND}}
{{LINT_FORMAT_TYPECHECK_COMMANDS}}
{{FULL_TEST_COMMAND}}
{{BUILD_COMMAND}}
```

{{GENERATED_FILE_AND_FIXTURE_POLICY}}

## Package and release

{{EVIDENCED_MAINTAINER_WORKFLOW_OR_LINK}}

Do not execute publishing or deployment commands as a documentation check.

## Known development constraints

- {{VERIFIED_CONSTRAINT}}
