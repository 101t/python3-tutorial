# Django News Site

## Installation Application

Make sure `virtualenv` installed on your computer by:

Installing Project on Unix (Linux/MacOS)

```bash
sudo apt install python3-pip

pip install virtualenv --user

cd 010-django-news-site/

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.pip
```

Installing Project on Windows, download python from `https://python.org`, then download **python3.X**

```bash
python -m pip install virtualenv --user

cd 010-django-news-site/

virtualenv env

env/Scripts/activate

pip install -r requirements.pip
```

Migrate db and add superuser

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

run application

```bash
python manage.py runserver 0.0.0.0:8000
```