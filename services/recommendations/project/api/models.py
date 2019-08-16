from sqlalchemy.sql import func
from project import db


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
            'dire_team': self.dire_team
        }
