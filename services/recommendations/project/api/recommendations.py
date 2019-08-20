from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero, Match, MatchHero
import json


recommend_blueprint = Blueprint('recommendations', __name__)
api = Api(recommend_blueprint)

class Recommendations(Resource):
    def get(self):
        response_object = {
            'status' : 'success',
            'data' : {
                'heroes' : [1, 2 , 3, 4]
            }
        }
        return response_object, 200


api.add_resource(Recommendations, '/api/recommendations')
