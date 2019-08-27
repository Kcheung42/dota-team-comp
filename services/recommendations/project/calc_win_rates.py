from project.api.models import Hero, Match, MatchHero, WinRates
from project.serializer import comp_deserialize
from project import db
from sqlalchemy import or_, func, update


def _find_matches_wins(heroes_id, is_winner):
    """Given a list of hero ids and a win or lose boolean
    find matches matching conditions:
    1.All heroes on the same team
    2.Game is a win or not
    """
    clauses = [MatchHero.hero_id==i for i in heroes_id]
    q = db.session.query(
        MatchHero.match_id,func.count(MatchHero.id)).\
        join(Match).\
        filter(or_(*clauses)).\
                    group_by(MatchHero.match_id, MatchHero.team).\
                    filter(MatchHero.win==is_winner).\
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
    result['win_rate'] = 0.0

    if(win_count + lose_count > 0):
        result['win_rate'] = win_count / (win_count + lose_count)
    return result


def team_to_skip(team, to_skip):
    for t in to_skip:
        if team & t == t:
            return True
    False


def calc_win_rates():
    """For each Combination in the WinRates table,
    Calculate the winarates.
    """
    table = WinRates.query.all()
    to_skip = []
    for t in table:
        if not team_to_skip(int(t.team,2), to_skip):
            team = (comp_deserialize(t.team))
            result = _calc_win_rate(team)
            t.win_rate = result['win_rate']
            t.win_count = result['win_count']
            t.lose_count = result['lose_count']
            if result['win_count'] + result['lose_count'] == 0:
                to_skip.append(int(t.team,2))
            db.session.commit()
            print(f"comb#={team} win={result['win_count']} loss={result['lose_count']} winrate={result['win_rate']}")

# Runnin Times
# 1-20 Heroes Combinations: 1663 Combinations
# 2792.7711927890778 seconds
