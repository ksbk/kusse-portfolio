# Kusse Portfolio

Source repository for **drkusse.com**, the professional portfolio website of Kusse Sukuta Bersha.

This repository includes the Django site source, planning documents, architecture decisions, and development history behind the portfolio.

## Purpose

The project presents selected work across research, software development, AI, data, and technical writing. It also serves as a public record of how the portfolio is planned, implemented, tested, and improved.

## Focus Areas

- Research background and scientific problem-solving
- Python, data, and applied AI
- Full-stack web development
- Research software and technical writing
- Public documentation and development traceability

## Status

Active development.

See:

- [Roadmap](docs/roadmap.md)
- [GitHub issues and milestones](https://github.com/ksbk/kusse-portfolio/issues)

## Tech Stack

- Python
- Django
- SQLite for local development
- HTML
- CSS
- uv
- mypy with django-stubs

## Local Setup

Install dependencies:

```bash
uv sync
```

Create a local environment file:

```bash
cp .env.example .env
```

Apply database migrations:

```bash
uv run python manage.py migrate
```

Seed the initial project records:

```bash
uv run python manage.py seed_projects
```

Run the development server:

```bash
uv run python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Quality Checks

```bash
uv run python manage.py check
uv run mypy config apps
uv run python manage.py test apps.pages apps.projects
uv run ruff check config apps
```

The same local quality gate can also be run with:

```bash
make quality
```

Run linting alone with:

```bash
make lint
```

## Project Structure

```text
apps/
  pages/       Static page views and templates
  projects/    Project portfolio models, views, templates, tests, and seed command

config/        Django settings, URLs, ASGI/WSGI, and context processors
templates/     Shared base template
static/        CSS and static assets
docs/          Project planning, requirements, architecture, and decisions
```

## Documentation

- [Project Charter](docs/project-charter.md)
- [Requirements](docs/requirements.md)
- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Content Architecture](docs/content-architecture.md)
- [Architecture Decisions](docs/decisions/)
- [Project Presentation Model](docs/projects/presentation-model.md)

## Notes

Project records can be edited through Django admin. The `seed_projects` command recreates the initial project records in a new database or development environment.

More automation, deployment documentation, and public evidence links will be added in later milestones.
