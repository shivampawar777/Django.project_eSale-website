#!/usr/bin/bash
# exit on error
set -o errexit
set -o pipefail


python manage.py collectstatic --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input