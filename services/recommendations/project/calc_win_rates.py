from project.api.models import Hero, Match, MatchHero, WinRates
from project.serializer import comp_deserialize
from project import db
from sqlalchemy import or_, func, update


def _find_matches_wins(heroes_id, win):
    clauses = [MatchHero.hero_id==i for i in heroes_id]
    print(f'clauses:{clauses}')
    q = db.session.query(
        MatchHero.match_id,func.count(MatchHero.id)).\
        join(Match).\
        filter(or_(*clauses)).\
                    group_by(MatchHero.match_id, MatchHero.team).\
                    filter(MatchHero.win==win).\
                    having(func.count(MatchHero.id)==len(heroes_id))
    matches = list(map(lambda x: x[0], q))
    return matches

def _calc_win_rate(heroes_id):
    winning_matches = _find_matches_wins(heroes_id, True)
    losing_matches = _find_matches_wins(heroes_id, False)

    win_count = len(winning_matches)
    lose_count = len(losing_matches)

    result = dict()
    result['win_count'] = win_count
    result['lose_count'] = lose_count
    result['win_rate'] = 0

    if(win_count + lose_count > 0):
        result['win_rate'] = win_count / (win_count + lose_count)
    return result


def calc_win_rates():
    table = WinRates.query.all()
    for t in table:
        result = _calc_win_rate(comp_deserialize(t.team))
        t.win_rate = result['win_rate']
        t.win_count = result['win_count']
        t.lose_count = result['lose_count']
        db.session.commit()

