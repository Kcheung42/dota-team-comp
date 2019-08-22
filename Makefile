docker-build:
	docker-compose -f docker-compose-prod.yml build

docker-build-dev:
	docker-compose -f docker-compose.yml build

docker-up-background:
	docker-compose -f docker-compose-prod.yml up -d

docker-up-dev-background:
	docker-compose -f docker-compose.yml up -d

docker-up:
	docker-compose -f docker-compose-prod.yml up

docker-up-dev:
	docker-compose -f docker-compose.yml up

docker-build-up:
	docker-compose -f docker-compose-prod.yml up --build -d

docker-build-up-dev:
	docker-compose -f docker-compose.yml up --build -d
