# HelpBot-Backend

Third party Chat service

# Table content

## [General Information](#general-information)

- [Introduce](#introduce)
* [Matrix-Synapse Server Chat Workflow](#matrix-synapse-server-chat-workflow)
- [Sysem workflow](#system-workflow)
- [Database diagram](#database-diagram)
- [Test Coverage](#test-coverage)
- [Features](#features)

## [Deployment](#deployment)

- [Clone this repository](#1-clone-this-repository)
- [Set up .env file at root project folder base on example.env file](#2-set-up-env-file-at-root-project-folder-base-on-exampleenv-file)
- [Set up enviroment](#3-set-up-enviroment)
- [Run server](#6-run-server)

## [Status](#status)

## [Contact](#contact)

# General Information

## Introduce

- This project serves as the robust foundation for implementing a real-time chat service in your website. Built on the powerful Django framework, this backend provides a secure and scalable solution for handling chat functionality.

## Workflow

### Matrix-Synapse Server Chat Workflow

![Chat flow](/readme_img/matrix_synapse.png)

### System Workflow

![Work flow](/readme_img/system_work_flow.png)

### Database Diagram

Database diagram link: [_here_](https://www.mermaidchart.com/raw/2f76a97a-6dbc-4f46-a8ea-ad516bb257db?theme=light&version=v0.1&format=svg).

![Database diagram](/readme_img/dbdiagram.png)

## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Result

![Unittest](/readme_img/unittest.png))

## Technology Used

- Python - Version 3.10.12
- Django - Version 4.2.4
- Postgres - Version 13.4
- Django REST framework - Version 3.14.0
- Matrix-client - Version 0.4.0
- Pre-commit Python Flake8 - Version 6.1.0
- Pre-commit Python black - Version 23.7.0

## Features

List the ready features here:

- Create bot chat with script
- Change style widget chat
- Embedding widget chat to other websites
- Mornitoring Chat bot
- Managing account

# Deployment

## 1. Clone this repository

    $ git clone https://github.com/gavin-go-dang/HelpBot-Backend.git

## 2. Set up .env file at root project folder base on **example.env** file

```
DATABASE_URL=
CELERY_BROKER_URL=
USE_DOCKER=

SERVER_URL=
MATRIX_USER=
MATRIX_PASSWORD=

HOMESERVER_USERNAME=
HOMESERVER_PASSWORD=

DNS_SENTRY=
```

## 3. Set up enviroment

    $ virtualenv env
    $ source env/bin/active
    $ pip install -r requirements/local.txt

## 4. Run the migrations

    $ python3 manage.py migrate

## 5. Load data:

    $ python3 manage.py loaddata data_sample.json

## 6. Run Server

    $ python3 manage.py runserver

# Project status

Status: in progress

# Contact

Feel free to contact me! - Email: gavin.dang.goldenowl@gmail.com
