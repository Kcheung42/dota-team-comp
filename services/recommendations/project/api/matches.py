from flask import Blueprint, request
from flask_restful import Resource, Api
from project import db
from project.api.models import Match
from sqlalchemy import exc
import json


matches_blueprint = Blueprint('matches', __name__)
api = Api(matches_blueprint)


class MatchesPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

class Matches(Resource):
    def get(self, match_id):
        """Get single user details"""
        response_object = {
            'status' : 'fail',
            'message' : 'Match does not exist'
        }
        try:
            m = Match.query.filter_by(match_id=match_id).first()
            if not m:
                return response_object, 404
            else:
                response_object = {
                    'status': 'success',
                    'data': m.to_json()
                }
            return response_object, 200
        except exc.DataError:
            return response_object, 404


class MatchesList(Resource):
    # def post(self):
    #     post_data = request.get_json()
    #     response_object = {
    #         'status' : 'fail',
    #        'message' : 'Invalid payload.'
    #     }
    #     if not post_data:
    #         return response_object, 400

    #     match_id = post_data.get('match_id')
    #     try:
    #         match = Match.query.filter_by(match_id=match_id).first()
    #         if not match:
    #             db.session.add(
    #                 Match(
    #                     match_id=d['match_id'],
    #                     radiant_win=d['radiant_win'],
    #                     radiant_team=d['radiant_team'],
    #                     dire_team=d['dire_team']
    #                     )
    #             )
    #             db.session.commit()
    #             response_object['status'] = 'success'
    #             response_object['message'] = f'Match {match_id} was added!'
    #             return response_object, 201
    #         else:
    #             response_object['message'] = f'Sorry. That match already exists.'
    #             return response_object, 400
    #     except exc.IntegrityError:
    #         db.session.rollback()
    #         return response_object, 400
    #     return response_object, 201

    def get(self):
        """Get all matches"""
        matches = Match.query.all()
        response_object = {
            'status' : 'success',
            'data' : {
                'count' : len(matches),
                'matches': [match.to_json() for match in matches]}
        }
        return response_object, 200

api.add_resource(MatchesPing, '/api/matches/ping')
api.add_resource(MatchesList, '/api/matches')
api.add_resource(Matches, '/api/matches/<match_id>')
