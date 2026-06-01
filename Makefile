.PHONY: check typecheck test migrate seed quality runserver

check:
	uv run python manage.py check

typecheck:
	uv run mypy config apps

test:
	uv run python manage.py test apps.pages apps.projects

quality: check typecheck test

migrate:
	uv run python manage.py migrate

seed:
	uv run python manage.py seed_projects

runserver:
	uv run python manage.py runserver
