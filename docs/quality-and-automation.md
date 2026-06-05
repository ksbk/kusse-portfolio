# Quality and Automation Plan

This document defines the current quality checks and deferred automation for the Kusse Portfolio project.

The goal is to keep the project reliable and reviewable without adding unnecessary automation before it is useful.

## Current Quality Checks

The project currently uses a four-part local quality gate: Django system check, mypy, tests, and Ruff.

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

For manual accessibility and semantic review, use the fast checklist in
`docs/dev-tools/audits/accessibility-checklist.md`.

## Quality Tools

The following tools are active. Future automation remains deferred until it reduces real project risk.

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
Status: active.

Purpose:

- Run lightweight checks before commits.
- Catch formatting or linting issues early.
- Avoid committing avoidable mistakes.

Pre-commit currently runs Ruff only. mypy and Django tests are intentionally not run in pre-commit — they are slower and belong in the full quality gate (`make quality`).

Install hooks once after `uv sync`:

```bash
make install-hooks
```

The hook runs automatically on each `git commit`.

Initial hooks should stay small and fast.

### GitHub Actions CI
Status: active.

Purpose:

- Run project checks on pushed commits and pull requests.
- Make the public repository more reviewable.
- Provide visible evidence that the project passes its quality gates.

CI runs `make quality`, which includes the Django system check, mypy, tests, and Ruff.

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
