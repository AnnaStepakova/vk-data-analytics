# vk-data-analytics

This is the test task for internship project at `JetBrains`.
In this project I demonstrate some reports on VK data.

Commands you need to perform to start the project localy:
* activate your virtual environment
* `pip install -r requirements.txt`
* `python manage.py migrate`
* define environment variables in your environment (or in `.env` file):
     * SECRET_KEY
     * for database: USER, PASSWORD, DATABASE_URL
     * for VKApi: ACCESS_TOKEN
     * id of vk group or user to make a report on: OWNER_ID
     * VKApi version: V
     * for Celery: CELERY_RESULT_BACKEND, BROKER_URL
* start Redis server: `redis-server`    
* start Celery worker: `celery -A vkdataanalytics worker --beat` 
* start server: `python manage.py runserver`

P.S. I intended to deploy my app to Heroku, 
but to use Redis on Heroku you need to enter your credit card information
(even if you are going to use free mode) :(
  