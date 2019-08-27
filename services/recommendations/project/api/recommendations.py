from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero, Match, MatchHero, WinRates
from project.serializer import comp_serialize
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
    # TODO To Remove once fully db fully populated
    def Rand(self, num):
        res = []
        heroes = Hero.query.all()
        random_v = random.sample([h.id for h in heroes], num)
        for r in random_v:
            h = Hero.query.get(r)
            res.append(h)
        return res

    def get(self):
        """Given a list of Hero ids, return the top 5 heroes with
        the highest win rate
        """
        response_object = {
            'status' : 'success',
            'data' : {
                'heroes' : [],
                'params' : "",
            }
        }

        params = request.args.get('ID')
        selected_id = [int(x) for x in params.split(',')]
        selected_heroes = [Hero.query.get(x) for x in selected_id]
        hero_list = Hero.query.all()
# TODO use max heap to build top 5 pick
        top_results = []
        for h in hero_list:
            if h not in selected_heroes:
                team = selected_id + [h.id]
                serialize_team = comp_serialize(team)
                w = WinRates.query.filter_by(team=serialize_team).first()
                if w:
                    top_results.append((w.win_rate, h))
                else:
                    top_results.append((0, h))

        if len(top_results) > 0:
            top_results = sorted(top_results, key=lambda x: x[0])
            top_results = top_results[::-1][:5]
            top_results = list(filter(lambda x: x[0] != 0, top_results))
            data = []
            for t in top_results:
                hero_json = t[1].to_json()
                hero_json.update({'win_rate': t[0]})
                data.append(hero_json)
            response_object['data']['heroes'] = data
        else:
            data = []
            top_results = self.Rand(5)
            for t in top_results:
                hero_json = t.to_json()
                hero_json.update({'win_rate': 0})
                data.append(hero_json)
            response_object['data']['heroes'] = data

        return response_object, 200


class RecommendationsWinRates(Resource):
    def get(self):
        response_object = {
            'status' : 'success',
            'data' : {
                'count' : 0,
                'win_rates' : [],
            }
        }
        win_rates = WinRates.query.order_by(WinRates.id).all()
        if win_rates:
            response_object['data']['count'] = len(win_rates)
            response_object['data']['win_rates'] = [each.to_json() for each in win_rates]
        return response_object, 200

class CalculatedWinRates(Resource):
    def get(self):
        response_object = {
            'status' : 'success',
            'data' : {
                'count' : 0,
                'win_rates' : [],
            }
        }
        win_rates = WinRates.query.order_by(WinRates.id).all()
        if win_rates:
            win_rates = list(filter(lambda x: (x.win_count + x.lose_count) != 0, win_rates))
            response_object['data']['count'] = len(win_rates)
            response_object['data']['win_rates'] = [each.to_json() for each in win_rates]
        return response_object, 200


api.add_resource(RecommendationsPing, '/api/ping')
api.add_resource(Recommendations, '/api/recommendations')
api.add_resource(RecommendationsWinRates, '/api/win_rates')
api.add_resource(CalculatedWinRates, '/api/pos_win_rates')


