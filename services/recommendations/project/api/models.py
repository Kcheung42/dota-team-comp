from sqlalchemy.sql import func
from project import db
from project.serializer import comp_deserialize

class MatchHero(db.Model):
    __tablename__ = 'match_hero'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
    team = db.Column(db.String, nullable=False)
    win = db.Column(db.Boolean, nullable=False)
    match = db.relationship("Match", backref=db.backref('heroes'))
    hero = db.relationship("Hero", backref=db.backref('matches'))


class Match(db.Model):

    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    match_id = db.Column(db.BigInteger, nullable=False)
    radiant_win = db.Column(db.Boolean, nullable=False)
    radiant_team = db.Column(db.String, nullable=False)
    dire_team = db.Column(db.String, nullable=False)

    def __init__(self, match_id, radiant_win, radiant_team, dire_team):
        self.match_id = match_id
        self.radiant_win = radiant_win
        self.radiant_team = radiant_team
        self.dire_team = dire_team

    def to_json(self):
        return {
            'match_id': self.match_id,
            'radiant_win': self.radiant_win,
            'radiant_team': self.radiant_team,
            'dire_team': self.dire_team,
        }

class Hero(db.Model):

    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class WinRates(db.Model):
    __tablename__ = 'win_rates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team = db.Column(db.String, nullable=False)
    win_rate = db.Column(db.Float, nullable=False)
    win_count = db.Column(db.Integer, nullable=False)
    lose_count = db.Column(db.Integer, nullable=False)


    def __init__(self, team):
        self.team = team
        self.win_rate = 0
        self.win_count = 0
        self.lose_count = 0

    def to_json(self):
        return {
            'composition' : comp_deserialize(self.team),
            'win_rate' : self.win_rate,
            'win_count' : self.win_count,
            'lose_count' : self.lose_count,
        }
