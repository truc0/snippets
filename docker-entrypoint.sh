#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py check --deploy
uwsgi --ini /code/uwsgi.ini
