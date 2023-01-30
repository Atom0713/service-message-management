run_local_dynamodb:
	docker run --rm -d -p 8000:8000 amazon/dynamodb-local

poetry_install:
	poetry install --no-root

run:
	poetry run flask run

run_debug:
	poetry run flask --debug run

mypy:
	poetry run mypy .

flake8:
	poetry run flake8 .

black:
	poetry run black .

isort:
	poetry run isort .

pytest:
	poetry run pytest .
