FROM python:3.11.9-slim

RUN mkdir app/
WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /app/*.sh