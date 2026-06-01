# Quality and Automation Plan

This document defines the current and planned quality checks for the Kusse Portfolio project.

The goal is to keep the project reliable and reviewable without adding unnecessary automation before it is useful.

## Current Quality Checks

The project currently uses three required local checks.

### Django system check

```bash
uv run python manage.py check
```

Purpose:

- Validate Django configuration.
- Catch common project setup issues.
- Confirm installed apps, settings, URLs, and models are valid.

### Type checking

```bash
uv run mypy config apps
```

Purpose:

- Check Python typing across the project.
- Support safer refactoring.
- Keep Django typing aligned with `django-stubs`.

### Tests

```bash
uv run python manage.py test apps.pages apps.projects
```

Purpose:

- Verify public page routes.
- Verify project model behavior.
- Verify project index and detail pages.
- Verify seed command behavior.

## Current Required Gate

Before committing feature, content, or template changes, run:

```bash
uv run python manage.py check
uv run mypy config apps
uv run python manage.py test apps.pages apps.projects
uv run ruff check config apps
```

Equivalent Makefile shortcut:

```bash
make quality
```

A change should not be committed if any of these checks fail.

## Planned Quality Improvements

The following tools are planned, but intentionally added step by step.

### Ruff
Status: active.

Purpose:

- Python linting.
- Import cleanup.
- Formatting consistency where appropriate.

Run with:

```bash
make lint
```

Configuration is conservative: rules E, F, W, and I are enabled. E501 (line length) is ignored. `make quality` now includes `make lint`.

Initial use should be conservative. The project should avoid enabling too many rules at once.

### Pre-commit
Status: planned.

Purpose:

- Run lightweight checks before commits.
- Catch formatting or linting issues early.
- Avoid committing avoidable mistakes.

Initial hooks should stay small and fast.

### GitHub Actions CI
Status: planned.

Purpose:

- Run project checks on pushed commits and pull requests.
- Make the public repository more reviewable.
- Provide visible evidence that the project passes its quality gates.

The first CI workflow should run:

```bash
uv run python manage.py check
uv run mypy config apps
uv run python manage.py test apps.pages apps.projects
```

Ruff can be added to CI after it is configured locally.

## Deferred Automation

The following are intentionally deferred:

- Deployment automation
- Docker-based CI
- Browser end-to-end tests
- Screenshot testing
- Coverage thresholds
- Security scanning
- Performance budgets

These may be useful later, but they are not required for the current project size.

## Guiding Principles

- Keep checks understandable.
- Add automation only when it reduces real risk.
- Prefer small, reviewable tooling changes.
- Do not block progress with unnecessary process.
- Make quality visible through documentation, tests, and GitHub history.
