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
│       |   dynamodb_client.py
|       |   table.py
│   └─── models
|       |   __init__.py
|       |   message.py
|       |
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
You can let poetry handle virtual environemt and run all commands with `poetry run [commands]`. Make commands take advantage of that property.

If you want to use your own virtual environment:
    - activate your virtual environment
    - run `poetry install` to install all required dependencies 

## Run

1. Start local dynamodb docker container `make run_local_dynamodb`

2. You can run the application using `make run`. The server will run on [http://127.0.0.1:5000](http://127.0.0.1:5000) by default.

## Development
### Code formatting

- Format imports `make isort`

- Code formatting `make black`
### Code statyc type/style checking 

- Style check `make flake8`

- Type check `make mypy`


## Debugging

Run app in debug mode `make run _debug`

## Test
Run tests `pytest`

## API Endpoints


### GET
`/messages/<recipient_email>?start=<date>&end=<date>`

### POST
`/message/<recipient_email>`

### DELETE
`/messages/<recipient_email>`
`/messages/<message_key>`
