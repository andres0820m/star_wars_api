#!/bin/sh
python swapi_graphene/manage.py makemigrations
python swapi_graphene/manage.py migrate --noinput
python swapi_graphene/manage.py loaddata /usr/local/src/star_wars_api/swapi_graphene/*/fixtures/*.json
python swapi_graphene/manage.py runserver 0.0.0.0:8000
