#!/usr/bin/bash
# exit on error
set -o errexit

pip install --no-cache-dir -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate