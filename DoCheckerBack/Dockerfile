FROM python:3.9 AS build-stage
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
COPY  requirements.txt /requirements.txt
RUN pip install  -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . /app
