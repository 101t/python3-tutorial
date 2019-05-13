# Django News Site

## Installation Application

Make sure `virtualenv` installed on your computer by:

```bash
sudo apt install python3-pip
pip install virtualenv --user
```

Installing Project on Unix (Linux/MacOS)

```bash
cd 010-django-news-site/

virtualenv -p python3 env

source env/bin/activate

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