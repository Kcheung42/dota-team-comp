from flask.cli import FlaskGroup
from project import create_app, db
import sys
import unittest

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


import requests
from project.api.models import Match, Hero

def fetch_heroes():
    response = requests.get('https://api.opendota.com/api/heroes/?api_key=6ac234f2-0bfb-425e-abb1-8fe2fcf1d508')
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
    response = requests.get('https://api.opendota.com/api/publicMatches?api_key=6ac234f2-0bfb-425e-abb1-8fe2fcf1d508')
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
                print("match:{} Successfully Added".format(d), flush=True)




@cli.command('seed_db')
def seed_db():
    """Seeds to the database"""
    fetch_heroes()
    fetch_matches()


if __name__ == '__main__':
    cli()
