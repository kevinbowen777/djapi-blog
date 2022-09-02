djapi-blog - A blogging API built with the Django REST framework
================================================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

This repository runs a Django 4.0.7/DRF 3.13 API application demonstrating some of its
basic functionality using the concept of a blog.

Features
--------

 * Browseable Web API
 * SwaggerUI & ReDoc API documentation
 * User registration with email verification & social(GitHub) login
 * Bootstrap4 & crispy-forms decorations
 * Customizable user profiles with bio, profile picture & country flags
 * Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

Installation
------------

To install the djapi-blog project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/djapi-blog.git
   $ cd djapi-blog

Local install:
--------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser
   

Docker install:
---------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run djapi-blog, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Application URLs
----------------
 * Log In endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/login/>`_
 * Log Out endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/>`_
 * Password reset:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset>`_
 * Password reset confirmation:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm>`_
 * User registration endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/>`_
 * User list:
    `<http://127.0.0.1:8000/api/v1/users/>`_
 * User detail:
    `<http://127.0.0.1:8000/api/v1/users/1/>`_
 * API schema download:
    `<http://127.0.0.1:8000/api/schema/>`_
 * Redoc API browser:
    `<http://127.0.0.1:8000/api/schema/redoc/>`_
 * Swagger-UI:
    `<http://127.0.0.1:8000/api/schema/swagger-ui/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Live Application Demonstration on Heroku
----------------------------------------
`kbowen-djapi-blog <https://kbowen-djapi-blog.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the djapi-blog `Issues page <https://github.com/kevinbowen777/djapi-blog/issues>`_ on GitHub.
