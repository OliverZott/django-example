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

### Prerequisites

```bash
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade -r ./requirements.txt
```

## Dev steps

1. user Authentication
    1. create superuser
2.

### User Authentication

- Create UserModel and UserModelManager for django cli
- Configure django to use it instead of default provided by django
- DB Migration - create and migrate
    - `python .\manage.py makemigrations profiles_api`
    - `python .\manage.py migrate`
- [django docu](https://docs.djangoproject.com/en/4.1/topics/auth/)
- [django docu](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

Register custom user model to django admin-site, create superuser via CLI and user django admin on the server.

- dummy **superuser@mail.com** with standard pw
- `python .\manage.py createsuperuser`
- `python .\manage.py runserver`
    - `http://127.0.0.1:8000/admin`
