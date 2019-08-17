from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Hero
from sqlalchemy import exc
import json
import requests


heroes_blueprint = Blueprint('heroe', __name__)
api = Api(heroes_blueprint)

class HeroList(Resource):
    def get(self):
        heroes = Hero.query.all()
        response_object = {
            'status' : 'success',
            'data' : {
                'count' : len(heroes),
                'heroes' : [hero.to_json() for hero in heroes]
            }
        }
        return response_object, 200


api.add_resource(HeroList, '/heroes')
