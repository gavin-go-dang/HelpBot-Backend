# HelpBot-Backend

Third party Chat service

## Table content

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## General Information



### Introduce

- This project serves as the robust foundation for implementing a real-time chat service in your website. Built on the powerful Django framework, this backend provides a secure and scalable solution for handling chat functionality.


### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html






## Deployment

 ### 1. Clone this repository

    $ git clone https://github.com/gavin-go-dang/HelpBot-Backend.git

### 2.  Set up .env file at root project folder base on **example.env** file
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

### 3. Set up enviroment

    $ virtualenv env
    $ source env/bin/active
    $ pip install -r requirements/local.txt

### 4. Run Server
    $ python3 manage.py runserver
