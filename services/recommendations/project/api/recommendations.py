from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero, Match, MatchHero
import json
import random


recommend_blueprint = Blueprint('recommendations', __name__)
api = Api(recommend_blueprint)

class Recommendations(Resource):

    def Rand(self, start, end, num):
        res = []
        random_v = random.sample(range(100), 5)
        for r in random_v:
            h = Hero.query.filter_by(id=r).first()
            res.append(h)
        return res

    def get(self):
        Id = request.args.get('ID')
        heroes = self.Rand(0,100,5)
        response_object = {
            'status' : 'success',
            'data' : {
                'heroes' : [hero.to_json() for hero in heroes],
                'param' : Id
            }
        }
        return response_object, 200


api.add_resource(Recommendations, '/api/recommendations')
