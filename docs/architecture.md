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

## Security

- SECRET_KEY loaded from environment
- DEBUG controlled by environment
- ALLOWED_HOSTS controlled by environment
- `.env` ignored from Git
- No private client data committed
- No real secrets committed

## Deployment

The initial deployment target is still to be decided. The project should remain deployable to a standard Python/Django-friendly platform using environment variables for configuration.
