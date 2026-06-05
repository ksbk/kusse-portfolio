.PHONY: check typecheck test migrate seed quality runserver lint install-hooks clean

check:
	uv run python manage.py check

typecheck:
	uv run mypy config apps

test:
	uv run python manage.py test apps.pages apps.projects

quality: check typecheck test lint

migrate:
	uv run python manage.py migrate

seed:
	uv run python manage.py seed_projects

runserver:
	uv run python manage.py runserver

lint:
	uv run ruff check config apps

install-hooks:
	uv run pre-commit install

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	rm -rf .mypy_cache .ruff_cache .pytest_cache htmlcov
	rm -f .coverage .coverage.* .dmypy.json
