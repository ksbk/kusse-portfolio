# Project Presentation Model

## Purpose

This document defines how technical projects should be presented in the portfolio in a clear, professional, and maintainable way.

The goal is to describe each project’s purpose, scope, technical approach, implementation details, current status, and supporting links without making the portfolio feel sales-heavy or overloaded.

## Principles

- Use neutral, professional language.
- Describe the work clearly without exaggeration.
- Prefer technical clarity over self-promotion.
- Keep the first version simple and extensible.
- Separate structured project data from page-specific presentation.
- Support both a project list page and future project detail pages.

## Initial Fields

### Core identity

- `title` — Human-readable project name.
- `slug` — URL-safe identifier.
- `summary` — Short overview for cards and list views.
- `category` — Broad grouping such as web, research software, AI/data, automation, or infrastructure.
- `status` — Current state, such as active, completed, paused, archived, or experimental.

### Project description

- `problem_context` — The situation, need, or technical challenge the project addresses.
- `technical_approach` — The implementation approach, architecture, or important technical decisions.
- `role` — The user’s role or responsibility in the project.
- `tech_stack` — Technologies, frameworks, languages, or tools used.

### Supporting links

- `repository_url` — Source repository when public.
- `live_url` — Live demo or deployed site when available.
- `documentation_url` — Supporting documentation, case study, or technical notes.

### Display and maintenance

- `featured` — Whether the project should appear in featured areas.
- `display_order` — Manual ordering for curated presentation.
- `created_at` — Record creation timestamp.
- `updated_at` — Record update timestamp.

## Initial Model Scope

The first implementation should support:

- A projects list page.
- Project cards with title, summary, category, status, and key links.
- A future detail page structure.
- Admin-editable project entries.
- Featured project selection.

## Deferred Fields and Features

The following should be deferred until needed:

- Screenshots and media galleries.
- Long-form case studies.
- Project metrics.
- Client/customer attribution.
- Testimonials.
- Multiple contributors.
- Related blog posts.
- Advanced filtering.
- Search.
- Tags as a separate model.
- Rich text editing.

## App Boundary

The `pages` app should continue to handle simple static public pages.

A dedicated `projects` app should handle structured project portfolio data, including models, admin configuration, list views, and detail views.

## Future Implementation Issues

Recommended next issues:

- `KP-3002 — Scaffold projects app`
- `KP-3003 — Add initial Project model`
- `KP-3004 — Configure projects admin`
- `KP-3005 — Implement projects list view`
- `KP-3006 — Implement project detail view`
- `KP-3007 — Add project tests`