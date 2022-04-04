FROM python:3.9 AS build-stage
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install  -r requirements.txt

