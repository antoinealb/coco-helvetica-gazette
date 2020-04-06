FROM python:3.8

RUN apt-get update && apt-get install -y gettext

RUN pip install pipenv
COPY Pipfile* /app/
RUN cd /app && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

WORKDIR /app

COPY locale /app/locale
RUN django-admin compilemessages

COPY . /app

CMD gunicorn --bind 0.0.0.0:8080 coco_helvetica_gazette.wsgi
