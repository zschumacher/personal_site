install:
	asdf install
	poetry install

freeze:
	poetry run python -m app.freezer

serve:
	poetry run flask run

fmt:
	poetry run isort . && \
	poetry run black --exclude .venv .