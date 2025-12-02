# Makefile for common development tasks

.PHONY: help install run test clean docker-up docker-down lint format

help:
	@echo "Big Data Backend Development Commands"
	@echo "===================================="
	@echo "make install          - Install Python dependencies"
	@echo "make run              - Run FastAPI server"
	@echo "make worker           - Run Celery worker"
	@echo "make test             - Run tests"
	@echo "make lint             - Run flake8"
	@echo "make format           - Format code with black"
	@echo "make type-check       - Check types with mypy"
	@echo "make docker-up        - Start Docker Compose services"
	@echo "make docker-down      - Stop Docker Compose services"
	@echo "make docker-logs      - Show Docker Compose logs"
	@echo "make clean            - Clean up temporary files"

install:
	pip install -r requirements.txt

run:
	python -m app.main

worker:
	celery -A app.workers.celery_app worker --loglevel=info

test:
	pytest -v

lint:
	flake8 app tests

format:
	black app tests

type-check:
	mypy app

docker-up:
	docker-compose -f infrastructure/docker/docker-compose.yml up -d

docker-down:
	docker-compose -f infrastructure/docker/docker-compose.yml down

docker-logs:
	docker-compose -f infrastructure/docker/docker-compose.yml logs -f

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
