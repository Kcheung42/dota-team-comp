import json
import unittest

from project.tests.base import BaseTestCase
from project.api.models import Match, Hero, MatchHero
from project import db
from project.utility import *

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
        add_win_rate([1,2,3], .1, 1, 10)
        add_win_rate([1,2,4], .2, 2, 10)
        add_win_rate([1,2,5], .3, 3, 10)
        add_win_rate([1,2,6], .4, 4, 10)
        add_win_rate([1,2,7], .5, 5, 10)
        add_win_rate([1,2,8], .6, 6, 10)
        with self.client:
            response = self.client.get('/api/recommendations?ID=1,2')
            data = json.loads(response.data.decode())['data']
            self.assertEqual(list(map(lambda x: x['id'], data['heroes'])), [8, 7, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()
