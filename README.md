## djapi-blog - A blogging API based on the Django Rest Framework(DRF) 

 - A basic demonstration of DRF API functionality.

### Installation
 - `git clone https://github.com/kevinbowen777/djapi-blog.git`
 - `cd djapi-blog`
 - Local installation
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Open browser to http://127.0.0.1:8000

---
### URLs
 - Log In endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
 - Log Out endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
 - Password reset:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
 - Password reset confirmation:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
 - User registration endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
 - User list:
    http://127.0.0.1:8000/api/v1/users/
 - User detail:
    http://127.0.0.1:8000/api/v1/users/1/
 - API schema download:
    http://127.0.0.1:8000/api/schema/
 - Redoc API browser:
    http://127.0.0.1:8000/api/schema/redoc/
 - Swagger-UI:
    http://127.0.0.1:8000/api/schema/swagger-ui/


---
## Features
 - TBD

### Live Demo on Heroku:
 - [djapi-blog](https://kbowen-djapi-blog.herokuapp.com/api/v1/)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/djapi-blog/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/djapi-blog/issues)
      to view currently open bug reports or open a new issue.
