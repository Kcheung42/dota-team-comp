from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero, Match, MatchHero, WinRates
import json
import random
from sqlalchemy import or_, func, create_engine
import os


recommend_blueprint = Blueprint('recommendations', __name__)
api = Api(recommend_blueprint)


class RecommendationsPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

class Recommendations(Resource):

    # TODO To Remove
    def Rand(self, start, end, num):
        res = []
        random_v = random.sample(range(start, end), num)
        # random_v = range(1,5)
        for r in random_v:
            h = Hero.query.filter_by(id=r).first()
            res.append(h)
        return res

    # TODO To Remove
    # WISH: dynamically construct queries as I could in functional
    # Programming
    def _find_matches_wins(self, heroes_id, win):
        clauses = [MatchHero.hero_id==i for i in heroes_id]
        print(f'clauses:{clauses}')
        q = db.session.query(
            MatchHero.match_id,func.count(MatchHero.id)).\
            join(Match).\
            filter(or_(*clauses)).\
                       group_by(MatchHero.match_id, MatchHero.team).\
                       filter(MatchHero.win==win).\
                       having(func.count(MatchHero.id)==len(heroes_id))

        # print(f'q:{q}')
        matches = list(map(lambda x: x[0], q))
        return matches

    # TODO To Remove
    def _calc_win_rate(self, heroes_id):
        winning_matches = self._find_matches_wins(heroes_id, True)
        losing_matches = self._find_matches_wins(heroes_id, False)
        win_count = len(winning_matches)
        lose_count = len(losing_matches)

        result = dict()
        result['win_count'] = win_count
        result['lose_count'] = lose_count
        result['win_rate'] = 0

        if(win_count + lose_count > 0):
            result['win_rate'] = win_count / (win_count + lose_count)
        return result



    def get(self):
        heroes_id = request.args.get('ID').split(',')
        print("\nDEBUGGING **********************************")

        print(f'heroes:{heroes_id}')
        winning_matches = self._find_matches_wins(heroes_id, True)
        losing_matches = self._find_matches_wins(heroes_id, False)
        win_rate = self._calc_win_rate(heroes_id)['win_rate']

        print(f'winning:{winning_matches}')
        print(f'Losing:{losing_matches}')
        print(f'win_rate:{win_rate}')
        "{0:b}".format(2**129|1)

        # print("==================================================")
        # engine = create_engine(os.environ['DATABASE_TEST_URL'])
        # conn = engine.connect()
        # e_str = "select match_id,count(id) from match_hero where (hero_id=1 or hero_id=2)  group by match_id,team having count(id)=2"
        # # print(Match.query.filter_by(id=27).first().to_json())
        # print(conn.execute(e_str).fetchall())
        # print("==================================================")

        heroes = self.Rand(1, 100, 5)
        response_object = {
            'status' : 'success',
            'data' : {
                'heroes' : [h.to_json() for h in heroes],
                'params' : heroes_id
            }
        }
        return response_object, 200


class RecommendationsWinRates(Resource):
    def get(self):
        win_rates = WinRates.query.order_by(WinRates.id).all()
        win_rates = list(filter(lambda x: (x.win_count + x.lose_count) != 0, win_rates))
        response_object = {
            'status' : 'success',
            'data' : {
                'count' : len(win_rates),
                'win_rates' : [each.to_json() for each in win_rates],
            }
        }
        return response_object, 200


api.add_resource(Recommendations, '/api/recommendations')
api.add_resource(RecommendationsWinRates, '/api/win_rates')
api.add_resource(RecommendationsPing, '/api/ping')


