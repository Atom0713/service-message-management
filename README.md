# service-message-management
Service for sending and retrieving messages 
**[Design Document](https://sideways-snowplow-199.notion.site/Design-Document-service-message-management-99fadbd5af8042acb54d8222759c0ed9)**
---

<h1>Project structure</h1>

```
service-message-management
│   README.md
│   app.py
|   pyproject.toml
|   poetry.lock
└─── src
│   │
│   └─── datastore
│   │
│   └─── service
│       │   views.py
│       │   controller.py
│       │
|   └─── tests
│       |   conftest.py
|       |   unit
|       |   int
```

## Pre-requisites

- Docker version 20.10.21
- Python == ^3.10
- [dynamodb-local](https://hub.docker.com/r/amazon/dynamodb-local)

## Manage dependencies

We are using [poetry](https://python-poetry.org/) for dependency management.

To install run command `pip install poetry==1.3.2`.

## Note 
You can let poetry handle virtual environemt and run all commands with `poetry run [commands]`

exp. `poetry run pytest`

If you want to use your own virtual environment:
    - activate your virtual environment
    - run `poetry install` to install all required dependencies 

## Run

Start local dynamodb docker container `docker run --rm -d -p 8000:8000 amazon/dynamodb-local`

You can run the application using `flask run`. The server will run on [http://127.0.0.1:5000](http://127.0.0.1:5000) by default.


## Development
### Code formatting

- Format imorts `isort .`

- Code formatting `black .`
### Code statyc type/style checking 

- Style check `flake8 .`

- Type check `mypy .`


## Debugging

Run app in debug mode `flask --debug run`

## Test
Run tests `pytest`
