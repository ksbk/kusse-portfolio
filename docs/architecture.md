# drkusse.com Architecture

drkusse.com is a server-rendered professional portfolio website built with Django.

## Backend

- Django
- SQLite for local development
- Django templates
- Django admin for content management if needed

## Frontend

- HTML
- CSS
- JavaScript
- Mobile-first responsive layout

## Main Content Areas

- Pages
- Projects
- Research
- Technical portfolio
- CV
- Contact

## Security

- SECRET_KEY loaded from environment
- DEBUG controlled by environment
- ALLOWED_HOSTS controlled by environment
- `.env` ignored from Git
- No private client data committed
- No real secrets committed

## Public Evidence

The repository includes documentation, issues, milestones, commits, screenshots, and release notes to make the development process auditable.
