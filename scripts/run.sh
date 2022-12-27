#!/usr/bin/env bash

set -euxo pipefail

python manage.py collectstatic --no-input
#bash ./wait.sh "$POSTGRES_HOST:$POSTGRES_PORT"
python manage.py migrate --no-input
gunicorn severinvest.wsgi --bind 0.0.0.0:8000 --workers 4 --timeout 60
