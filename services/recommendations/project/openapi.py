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
                new_hero = Hero(id=hero_id, name=d['localized_name'],)
                db.session.add(new_hero)
                db.session.commit()
                print("hero:{} Successfully Added".format(hero_id), flush=True)

def most_recent_match_id():
    endpoint = '/explorer'
    sql ='sql=select%20*%20from%20public_matches%20order%20by%20start_time%20desc%20limit%201'
    url = f'{base_url}{endpoint}?sql={sql}'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data[0]['match_id']

def fetch_matches():
    latest_match_id = most_recent_match_id()
    # latest_match_id = 4982101905
    print(f'latest_match_id:{latest_match_id}')
    endpoint = '/publicMatches'
    url = f'{base_url}{endpoint}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print("data:{}".format(data), flush=True)
        for d in data:
            match_id = d['match_id']
            if d['radiant_win']:
                winning_team = 'radiant'
            else:
                winning_team = 'dire'
            match = Match.query.filter_by(match_id=match_id).first()
            if not match:
                match = Match(match_id=d['match_id'],
                              radiant_win=d['radiant_win'],
                              radiant_team=d['radiant_team'],
                              dire_team=d['dire_team']
                              )
                db.session.add(match)
                radiant_team = [x.strip() for x in d['radiant_team'].split(',')]
                dire_team = [x.strip() for x in d['dire_team'].split(',')]
                for hero in radiant_team:
                    hero = Hero.query.filter_by(id=hero).first()
                    win = match.radiant_win
                    a = MatchHero(hero=hero, match=match, team='radiant', win=win)
                    db.session.add(a)
                for hero in dire_team:
                    hero = Hero.query.filter_by(id=hero).first()
                    win = False if match.radiant_win else True
                    a = MatchHero(hero=hero, match=match, team='dire', win=win)
                    db.session.add(a)
                db.session.commit()
                print("match:{} Successfully Added".format(match.match_id), flush=True)
