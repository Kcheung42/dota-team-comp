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

1. Point environment to 


To get ip of docker-machine instance
```
docker-machine ip [docker-machine name]
```

```
eval $(docker-machine env -dota)
export 
export REACT_APP_HERO_SERVICE_URL=[ip address of amazon docker-machine instance]
export REACT_APP_HERO_SERVICE_URL=[ip address of amazon docker-machine instance]
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


# Visit:
### Application
* http://ec2-3-208-87-9.compute-1.amazonaws.com/

### API
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/users
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/heroes
* http://ec2-3-208-87-9.compute-1.amazonaws.com/api/matches
