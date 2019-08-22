from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero, Match, MatchHero
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

    def Rand(self, start, end, num):
        res = []
        # random_v = random.sample(range(start, end), num)
        random_v = range(1,5)
        for r in random_v:
            h = Hero.query.filter_by(id=r).first()
            res.append(h)
        return res

    # WISH: dynamically construct queries as I could in functional
    # Programming
    def _find_matches_wins(self, heroes_id, win):
        # heroes_id = [h.id for h in heroes]
        clauses = [MatchHero.hero_id==i for i in heroes_id]
        print(f'clauses:{clauses}')
        q = db.session.query(
            MatchHero.match_id,func.count(MatchHero.id)).\
            join(Match).\
            filter(or_(*clauses)).\
                       group_by(MatchHero.match_id, MatchHero.team).\
                       filter(Match.radiant_win==MatchHero.team).\
                       having(func.count(MatchHero.id)==2)
        # if win = True:
        #     q = q.filter(Match.radiant_win==MatchHero.team)
        # else:
        #     q = q.filter(match.radiant_win==)


        # print(f'q:{q}')
        matches = list(map(lambda x: x[0], q))
        return matches

    def get(self):
        heroes_id = request.args.get('ID').split(',')
        print("\nDEBUGGING **********************************")

        winning_matches = self._find_matches_wins(heroes_id, False)
        losing_matches = self._find_matches_wins(heroes_id, True)

        print(f'winning:{winning_matches}')
        print(f'Losing:{losing_matches}')

        # print("==================================================")
        # engine = create_engine(os.environ['DATABASE_TEST_URL'])
        # conn = engine.connect()
        # e_str = "select match_id,count(id) from match_hero where (hero_id=1 or hero_id=2)  group by match_id,team having count(id)=2"
        # # print(Match.query.filter_by(id=27).first().to_json())
        # print(conn.execute(e_str).fetchall())
        # print("==================================================")

        response_object = {
            'status' : 'success',
            'data' : {
                'heroes' : [],
                'params' : heroes_id
            }
        }
        return response_object, 200


api.add_resource(Recommendations, '/api/recommendations')
api.add_resource(RecommendationsPing, '/api/ping')


