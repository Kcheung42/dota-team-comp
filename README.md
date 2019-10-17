# Dota Team Composition

## Technologies Used

#### Backend
* Flask (Python)


#### Frontend
* React (Javascript)

#### Devops
* Docker
* Docker-machine
* Amazon AWS EC2

# Development build
1. Point environment to local

```
eval $(docker-machine env -u)
export REACT_APP_HERO_SERVICE_URL=localhost
export REACT_APP_HERO_SERVICE_URL=localhost
```
2. Build and run container in background

```
make docker-build-up-dev
```


# Production build
##### Note: Follow link to set up 


1. Follow steps from https://docs.docker.com/machine/examples/aws/ to:
 > 1. Sign up for AWS and configure credentials
 > 2. Use Machine to create the instance


2. Log into aws docker-machine instance

```
eval $(docker-machine env -dota)
export REACT_APP_HERO_SERVICE_URL=[ip address of amazon docker-machine instance]
```
##### Note: To get ip of docker-machine instance
```
docker-machine ip [docker-machine name]
```

2. Build and run container in background
```
make docker-build-up-dev
```
3. Run Initial scripts
Available scripts:
* seed_db (will fetch hero and match data from opendota api)
* test (run tests)
* combo (calculate team all combinations)
* win_rates (calculate win rates for combinations)
```
docker-compose -f docker-compose-prod.yml exec [container name] python manage.py [cli]
```

4. Log off
```
eval $(docker-machine env -u)
```


# Visit:
### Application
* http://ec2-3-208-87-9.compute-1.amazonaws.com/

### API
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/users
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/heroes
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/matches
