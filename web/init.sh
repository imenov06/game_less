#!/bin/bash

alembic revision --autogenerate
alembic upgrade head
uvicorn main:app --reload --host 0.0.0.0 --port 8000