# syntax=docker/dockerfile:1
FROM python:3-alpine
LABEL maintainer truc0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN apk update && apk add uwsgi-python3
RUN pip install -U pip && pip install -r requirements.txt
RUN chmod +x /code/docker-entrypoint.sh
