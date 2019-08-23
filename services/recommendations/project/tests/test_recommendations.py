import json
import unittest

from project.tests.base import BaseTestCase
from project.api.models import Match, Hero, MatchHero
from project import db

def add_hero(id, name):
    hero = Hero(id=id, name=name)
    db.session.add(hero)
    db.session.commit()
    return hero


def add_match(match_id, radiant_win, radiant_team, dire_team):
    match = Match(match_id=match_id,
                  radiant_win=radiant_win,
                  radiant_team=radiant_team,
                  dire_team=dire_team)
    db.session.add(match)
    radiant_team = [x.strip() for x in radiant_team.split(',')]
    dire_team = [x.strip() for x in dire_team.split(',')]
    for hero in radiant_team:
        hero = Hero.query.filter_by(id=hero).first()
        a = MatchHero(hero=hero, match=match, team='radiant', win=radiant_win)
        db.session.add(a)
    for hero in dire_team:
        hero = Hero.query.filter_by(id=hero).first()
        win = False if radiant_win else True
        a = MatchHero(hero=hero, match=match, team='dire', win=win)
        db.session.add(a)
    db.session.commit()



class Test(BaseTestCase):
    """Tests for the Recommendations Service."""

    def test_sanity(self):
        """Ensure the/ping route behaves correctly"""
        with self.client:
            response = self.client.get('/api/ping')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pong!', data['message'])
            self.assertIn('success', data['status'])

    def test_recommend_one_input(self):
        for i in range(1,11):
            add_hero(i, 'blahblahHero' + str(i))
        add_match('1', True , '1,2', '3,4') # on winning team
        add_match('2', False, '1,5', '3,2') # not same team
        add_match('3', False, '3,5', '1,2') # on winning team
        add_match('4', True, '1,2', '5,3') # on winning team
        add_match('5', False, '1,2', '5,3') # on losing team
        add_match('6', True, '1,3,2', '5,3') # on winning team
        def test_one_input(self):
            with self.client:
                response = self.client.get('/api/recommendations?ID=1')
                data = json.loads(response.data.decode())['data']
                print(f'data:{data}')
                self.assertEqual(data['heroes'], [])
                self.assertEqual(data['params'], ['1'])

        def test_recommend_multipleinput(self):
            with self.client:
                response = self.client.get('/api/recommendations?ID=1,2')
                data = json.loads(response.data.decode())['data']
                print(f'data:{data}')
                self.assertEqual(data['heroes'], [])
                self.assertEqual(data['params'], ['1', '2'])


if __name__ == '__main__':
    unittest.main()
