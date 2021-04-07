release: python manage.py migrate
web: gunicorn vkdataanalytics.wsgi --log-file -
worker: celery -A vkdataanalytics worker --beat