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
