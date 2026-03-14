.PHONY: up down test-backend

up:
	docker compose up --build

down:
	docker compose down -v

test-backend:
	cd backend && python -m pytest -q
