FROM python:3.8

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN cd /app && \
    pip install -r requirements.txt

COPY locale /app/locale
RUN django-admin compilemessages

COPY . /app

CMD gunicorn --bind 0.0.0.0:8080 coco_helvetica_gazette.wsgi
