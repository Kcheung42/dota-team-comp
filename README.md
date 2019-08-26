# Dota Team Composition

## Technologies Used

#### Backend
* Flask


#### Frontend
* ReactJs

#### Devops
* Docker
* Docker-machine
* Amazon AWS EC2


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

2. Build and run container
```
make docker-build-up-dev
```
3. Run Initial scripts
```
docker-compose -f docker-compose-prod.yml exec [container name] python manage.py [cli]
```


# Visit:
### Application
* http://ec2-100-25-246-192.compute-1.amazonaws.com/

### API
* http://ec2-100-25-246-192.compute-1.amazonaws.com/users
* http://ec2-100-25-246-192.compute-1.amazonaws.com/heroes
* http://ec2-100-25-246-192.compute-1.amazonaws.com/matches
