# Coco Helvetica Gazette

Django 3 project running on python 3.8 with Pipenv

## Requirement

- Python 3
- pip3
- pipenv


See [this documentation](https://pipenv-fork.readthedocs.io/en/latest/install.html) to install pipenv

OR:

Docker

## Running with Docker

```
docker build -t coco .
docker run -it -p 8000:80 --name coco coco python manage.py runserver
```

To run the migrations:

```
docker exec -it coco python manage.py migrate
```

Then open this link in your browser to see the project in action [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Unfortunately, this breaks django live reload, so you have to kill and start the server process for your changes outside the container to take effect.

## Setup your project without Docker
Clone the repository

    git@github.com:antoinealb/coco-helvetica-gazette.git

Go into the `django` folder

    cd coco-helvetica-gazette/django

Create a virtual environment
    python3 -m venv env

Activate it (needed every time you create a shell)
    source env/bin/activate  # for bash users
    source env/bin/activate.fish  # for fish users

Install python dependencies

    pip install -r requirements.txt

Run the migrations

    python manage.py migrate

Run the python dev server

    python manage.py runserver

Then open this link in your browser to see the project in action [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


# Deploying on Google App Engine

## Registering application secrets

Create a file named `credentials.yaml` with the following content:

```yml
env_variables:
  DJANGO_SECRET_KEY:
  DJANGO_DB_HOST:
  DJANGO_DB_NAME:
  DJANGO_DB_USER:
  DJANGO_DB_PASSWORD:
  # Optional, for telegram bot notifications
  TELEGRAM_CHAT_ID:
  TELEGRAM_API_KEY:
```

and fill in the values with the chosen secrets.

## Deploy application to AppEngine

```python
# Compiles translations
python manage.py compilemessages

# Copies static files (.js and .css)
python manage.py collectstatic

# Send the app to AppEngine
gcloud app deploy
```
