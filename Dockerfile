FROM python:3.7.8-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

