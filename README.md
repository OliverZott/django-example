# Django Example Project

## Setup Django

Create Project and test server [Link](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-a-project)

```bash
django-admin startproject profiles_project .
py manage.py runserver
```

Create app inside project [Link](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app)

```bash
python manage.py startapp profiles_api
```

Enable app in project:

## Run & Debug

Run integrated development server

````bash
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
````

Endpoints:

- http://127.0.0.1:8000/api/hello-view
- http://127.0.0.1:8000/api/hello-viewset/1/
- http://127.0.0.1:8000/api/hello-viewset

### Prerequisites

```bash
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade -r ./requirements.txt
```

# Dev steps

1. user Authentication
    1. create superuser
2. API endpoints

## User Authentication

- Create UserModel and UserModelManager for django cli
- Configure django to use it instead of default provided by django
- DB Migration - create and migrate
    - `python .\manage.py makemigrations profiles_api`
    - `python .\manage.py migrate`
- [django docu](https://docs.djangoproject.com/en/4.1/topics/auth/)
- [django docu](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

Register custom user model to django admin-site, create superuser via CLI and user django admin on the server.

- Dummy user - user: **superuser@mail.com** pw: password
- `python .\manage.py createsuperuser`
- `python .\manage.py runserver`
    - `http://127.0.0.1:8000/admin`

## API endpoints

### API Views

- `views.py` and `urls.py`
- urls.py from project get forwarded to urls.py from app

### ViewSet

- same as API Views but using functions representing standard actions
- take care of boilerplate code (standard db operations)
- Using Router to make it available in API
- Only viewset are shown in http://127.0.0.1:8000/api

Example:

- http://127.0.0.1:8000/api/hello-viewset ...for get
- http://127.0.0.1:8000/api/hello-viewset/1 ... for update, delete, post, ...

ViewSet > API Views if:

- simple CRUD interface for database
- quick and simple api
- little to no customization in logic!
- api working with standard data structures

## User Profile Endpoint

- http://127.0.0.1:8000/api/profile_viewset/
- `viewsets.ModelViewSet`

1. Serializer
    - **ModelSerializer** specific for django database models
2. View with QuerySet
3. Permissions and Authentication
4. Filter (for searching)

## Authentication and Login

- http://127.0.0.1:8000/api/login/
- `ObtainAuthToken`

