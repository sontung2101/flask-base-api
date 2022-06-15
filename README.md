# Flask API Source

Flask API Source template components

## Directory Structure

```
├── apps
│   ├── __init__.py
│   ├── routers.py
│   ├── healths
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routers.py
├── config
│   ├── __init__.py
│   ├── default.py
│   ├── development.py
│   ├── production.py
│   ├── staging.py
├── helpers
│   ├── __init__.py
│   ├── middlewares.py
│   ├── response.py
│   ├── encoder.py
│   ├── exception.py
├── utils
│   ├── __init__.py
├── .gitignore
├── __init__.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── supervisord.conf
```

## Contribution Guide

`ToDo`

## Getting Started

```bash
$ virtualenv venv

# Unix
$ source venv/bin/activate
or
# Windows
$ source venv/Scripts/activate

$ pip install -r requirements.txt

$ python main.py

```

## Run Development Local

```bash
# Insert local env to `configs.local.py`
$ touch configs/local.py 

$ python main.py
```

## Run Development in Docker

- Create `.env` file and insert `.env` to .env (view `.env.example`)

```bash
$ docker-compose up -d --build
```

