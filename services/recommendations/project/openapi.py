import requests
from project.api.models import Match, Hero, MatchHero
from project import db

base_url = 'https://api.opendota.com/api'
api_key = '6ac234f2-0bfb-425e-abb1-8fe2fcf1d508'

# TODO
# make asynchronous api calls
# https://www.terriblecode.com/blog/asynchronous-http-requests-in-python/

def fetch_heroes():
    endpoint = '/heroes'
    url = f'{base_url}{endpoint}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for d in data:
            hero_id = d['id']
            hero = Hero.query.filter_by(id=hero_id).first()
            if not hero:
                db.session.add(
                    Hero(
                        id=hero_id,
                        name=d['localized_name'],
                        )
                )
                db.session.commit()
                print("hero:{} Successfully Added".format(d), flush=True)


def fetch_matches():
    endpoint = '/publicMatches'
    url = f'{base_url}{endpoint}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print("data:{}".format(data), flush=True)
        for d in data:
            match_id = d['match_id']
            match = Match.query.filter_by(match_id=match_id).first()
            if not match:
                db.session.add(
                    Match(
                        match_id=d['match_id'],
                        radiant_win=d['radiant_win'],
                        radiant_team=d['radiant_team'],
                        dire_team=d['dire_team']
                        )
                    )
                db.session.commit()
                match = Match.query.filter_by(match_id=match_id).first()
                radiant_team = [x.strip() for x in d['radiant_team'].split(',')]
                dire_team = [x.strip() for x in d['dire_team'].split(',')]
                for hero in radiant_team:
                    hero = Hero.query.filter_by(id=hero).first()
                    a = MatchHero(hero=hero, match=match, team='radiant')
                    db.session.add(a)
                    db.session.commit()
                for hero in dire_team:
                    hero = Hero.query.filter_by(id=hero).first()
                    a = MatchHero(hero=hero, match=match, team='dire')
                    db.session.add(a)
                    db.session.commit()
                for assoc in match.heroes:
                    print(assoc.hero)
                print ("direteam{}".format(dire_team))
                print ("radiant{}".format(radiant_team))
                print("match heroes:{}".format(match.heroes))
                print("match:{} Successfully Added".format(match), flush=True)



                # match = Match.query.filter_by(match_id=match_id).first()
                # radiant_team = [x.strip() for x in d['radiant_team'].split(',')]
                # dire_team = [x.strip() for x in d['dire_team'].split(',')]
                # heroes = radiant_team + dire_team
                # TODO not sure if accessing he
