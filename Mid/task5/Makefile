.PHONY: run test clean

run:
	docker-compose up --build

test:
	pip install requests pytest
	pytest test_compose.py

clean:
	docker-compose down -v