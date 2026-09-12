.. _`changelog`:

=========
Changelog
=========

``djapi-blog`` issues are filed on `GitHub <https://github.com/kevinbowen777/djapi-blog/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

djapi-blog 0.3.6 (2026-09-13)
=============================

Contributor-facing changes
--------------------------

-  (`#565 <https://github.com/kevinbowen777/djapi-blog/issues/565>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#568 <https://github.com/kevinbowen777/djapi-blog/issues/568>`_): Update testing to Python 3.14.7, 3.13.15, and 3.12.14

-  (`#568 <https://github.com/kevinbowen777/djapi-blog/issues/568>`_): Update django-debug-toolbar to 7.1.1

-  (`#568 <https://github.com/kevinbowen777/djapi-blog/issues/568>`_): Update gunicorn to 26.1.0

-  (`#568 <https://github.com/kevinbowen777/djapi-blog/issues/568>`_): Update nox to 2026.8.17

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update django-allauth to 65.19.2

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update django-debug-toolbar to 8.0.0

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update django-countries to 9.1.0

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Upgrade environs to 15.2.0

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Upgrade gunicorn to 26.2.0

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update towncrier to 26.9.0

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update psycopg to 3.3.5

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Update djlint to 1.46.1

-  (`#574 <https://github.com/kevinbowen777/djapi-blog/issues/574>`_): Replace master with main in static gh action

-  (`#575 <https://github.com/kevinbowen777/djapi-blog/issues/575>`_): Upgrade GitHub actions to latest versions


New features
------------

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Upgrade djangorestframework to 3.18.1

-  (`#573 <https://github.com/kevinbowen777/djapi-blog/issues/573>`_): Upgrade Django to 6.1.1

djapi-blog 0.3.5 (2026-08-21)
=============================

Improved documentation
----------------------

-  (`#542 <https://github.com/kevinbowen777/djapi-blog/issues/542>`_): Add towncrier 25.8.0.


New features
------------

-  (`#567 <https://github.com/kevinbowen777/djapi-blog/issues/567>`_): Upgrade to Django 6.0.8

djapi-blog 0.3.4 (2026-07-31)
=============================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#563 <https://github.com/kevinbowen777/djapi-blog/issues/563>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#557 <https://github.com/kevinbowen777/djapi-blog/issues/557>`_): Drop support for Python 3.11.


New features
------------

-  (`#526 <https://github.com/kevinbowen777/djapi-blog/issues/526>`_): Upgrade Django to 6.0.7.

djapi-blog 0.3.3 (2025-05-06)
=============================

Contributor-facing changes
--------------------------

-  (`#461 <https://github.com/kevinbowen777/djapi-blog/issues/461>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#467 <https://github.com/kevinbowen777/djapi-blog/issues/467>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#466 <https://github.com/kevinbowen777/djapi-blog/issues/466>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#410 <https://github.com/kevinbowen777/djapi-blog/issues/410>`_): Upgrade Docker image to Python 3.13

-  (`#471 <https://github.com/kevinbowen777/djapi-blog/issues/471>`_): Upgrade Django Rest Framework to 3.16.0.

-  (`#473 <https://github.com/kevinbowen777/djapi-blog/issues/473>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#476 <https://github.com/kevinbowen777/djapi-blog/issues/476>`_): Replace safety package with pip-audit.

djapi-blog 0.3.2 (2025-01-22)
=============================

Contributor-facing changes
--------------------------

-  (`#407 <https://github.com/kevinbowen777/djapi-blog/issues/407>`_): Add support for Python 3.13

-  (`#449 <https://github.com/kevinbowen777/djapi-blog/issues/449>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#440 <https://github.com/kevinbowen777/djapi-blog/issues/440>`_): Upgrade Django to 5.1.4

djapi-blog 0.3.0 (2023-12-23)
=============================

Contributor-facing changes
--------------------------

-  (`#155 <https://github.com/kevinbowen777/djapi-blog/issues/155>`_): Migrate to non-root Docker user & venv.

-  (`#212 <https://github.com/kevinbowen777/djapi-blog/issues/212>`_): Update Python to 3.12.0.

-  (`#308 <https://github.com/kevinbowen777/djapi-blog/issues/308>`_): Upgrade Poetry to 1.7.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#305 <https://github.com/kevinbowen777/djapi-blog/issues/305>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#316 <https://github.com/kevinbowen777/djapi-blog/issues/316>`_): Upgrade to Django 5.0.

djapi-blog 0.2.0 (2023-05-15)
=============================

Contributor-facing changes
--------------------------

-  (`#191 <https://github.com/kevinbowen777/djapi-blog/issues/191>`_): Install ruff. Drop flake8-* packages.

djapi-blog 0.1.0 (2023-05-08)
=============================

Contributor-facing changes
--------------------------

- : Implement Swagger-UI API View

- : Migrate from pipenv to Poetry

- : Mirror to GitLab.

-  (`#11 <https://github.com/kevinbowen777/djapi-blog/issues/11>`_): Add django-debug-toolbar.

-  (`#152 <https://github.com/kevinbowen777/djapi-blog/issues/152>`_): Migrate from SQLite to PostgreSQL

-  (`#164 <https://github.com/kevinbowen777/djapi-blog/issues/164>`_): Add support for Python 3.12.

-  (`#171 <https://github.com/kevinbowen777/djapi-blog/issues/171>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#175 <https://github.com/kevinbowen777/djapi-blog/issues/175>`_): Upgrade PostgreSQL to 15.2

-  (`#193 <https://github.com/kevinbowen777/djapi-blog/issues/193>`_): Upgrade Django to 4.2.1

-  (`#2 <https://github.com/kevinbowen777/djapi-blog/issues/2>`_): Implement nox for testing


Improved documentation
----------------------

- : Add Sphinx for documentation

djapi-blog 0.0.1 (2022-07-27)
=============================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.6

-  (`#5 <https://github.com/kevinbowen777/djapi-blog/issues/5>`_): Build Docker support for Heroku deployment.


Miscellaneous internal changes
------------------------------

- : Initial commit
