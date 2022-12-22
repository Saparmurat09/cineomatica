FROM python:3.10.6


ENV PYTHON_VERSION=3.10.6
ENV PYTHONBUFFERED 1

RUN mkdir /cineomatica

WORKDIR /cineomatica

ADD . /cineomatica

RUN pip install -r requirements.txt



