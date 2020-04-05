FROM python:3.8

RUN apt-get update && apt-get install -y gettext curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

RUN pip install pipenv
COPY Pipfile* /app/
RUN cd /app && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

WORKDIR /app

COPY yarn.lock /app
COPY package.json /app
RUN npm run yarn-install

COPY locale /app/locale
RUN django-admin compilemessages

COPY . /app

CMD gunicorn --bind 0.0.0.0:8080 coco_helvetica_gazette.wsgi
