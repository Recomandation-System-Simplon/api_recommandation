# syntax=docker/dockerfile:1
FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:ubuntugis/ppa -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y build-essential libssl-dev libffi-dev python3.9-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.9-venv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m venv /venv
ENV PATH=/venv/bin:$PATH

# Get and install packages needed for api-recommandation 
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt


ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000


# Copy in the application code from your work station at the current directory
# over to the working directory.
COPY . .

RUN chmod 755 app-entrypoint.sh

ENTRYPOINT ["/app/app-entrypoint.sh", "db"]
