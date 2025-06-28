install:
	poetry install

run *ARGS:
	poetry run mdsh {{ARGS}}

example:
	poetry run mdsh resources/ledger.md --from 2025-01-01 --to 2025-02-01 --file resources/ledger.j 

lint:
	poetry run ruff check --fix