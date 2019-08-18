docker-build:
	docker-compose -f docker-compose-prod.yml build

docker-build-dev:
  docker-compose -f docker-comopse.yml build

docker-up-background:
	docker-compose -f docker-compose-prod.yml up -d

docker-up-background-dev:
	docker-compose -f docker-compose.yml up -d

docker-up:
	docker-compose -f docker-compose-prod.yml up

docker-up-dev:
	docker-compose -f docker-compose.yml up
