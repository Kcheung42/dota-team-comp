import requests
from project.api.models import Match, Hero, MatchHero
from project import db
from project.utility import add_hero, add_match

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
            fetch_images(d['name'].replace('npc_dota_hero_', ''), d['id'], '_sb.png')
            fetch_images(d['name'].replace('npc_dota_hero_', ''), d['id'], '_full.png')
            hero_id = d['id']
            hero = Hero.query.filter_by(id=hero_id).first()
            if not hero:
                add_hero(hero_id, d['localized_name'])
                # new_hero = Hero(id=hero_id, name=d['localized_name'],)
                # db.session.add(new_hero)
                # db.session.commit()
                print("hero:{} Successfully Added".format(hero_id), flush=True)

# TODO Not working
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
            match = Match.query.filter_by(match_id=match_id).first()
            if not match:
                match = add_match(d['match_id'], d['radiant_win'], d['radiant_team'], d['dire_team'])
                db.session.commit()
                print("match:{} Successfully Added".format(match.match_id), flush=True)


def fetch_images(hero_name, id, suffix):
    url = 'http://cdn.dota2.com/apps/dota2/images/heroes/'
    final_url = url + hero_name + suffix
    image_data = requests.get(final_url).content

    file_dir = 'project/assets/'
    file_name = str(id) + suffix
    file_path = file_dir + file_name
    print(f'image downloaded:{file_path}')
    with open(file_path, 'wb') as handler:
        handler.write(image_data)
