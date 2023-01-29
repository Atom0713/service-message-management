# service-message-management
Service for sending and retrieving messages 
**[Design Document](https://www.notion.so/Design-Document-service-message-management-99fadbd5af8042acb54d8222759c0ed9)**
---

**Project structure**
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

**Requirements**

Python == ^3.10

**Manage dependencies**

We are using [poetry](https://python-poetry.org/) for dependency management.

To install run command `pip install poetry==1.3.2`.


**Run**

You can run the application using `poetry run flask run` and poetry will take care of the virtual environment for you.

If you prefere to have local virtual env:
- activate your virtual environment
- run `poetry install` and it will install dependencies from poetry.lock to you virtual environment
- run `flask run` to start the server


**Debugging**
Run app in debug mode `flask --debug run`


**Test**
