# pull official base image
FROM python:3.8.1-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP pomodoro-python/app/__init__.py
ENV FLASK_ENV production

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run server
CMD gunicorn --bind 0.0.0.0:$PORT app:app
