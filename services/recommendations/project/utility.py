from project.api.models import Match, Hero, MatchHero, WinRates
from project import db
from project.serializer import comp_serialize

def add_hero(id, name):
    hero = Hero(id=id, name=name)
    db.session.add(hero)
    db.session.commit()
    return hero


def add_match(match_id, radiant_win, radiant_team, dire_team):
    match = Match(match_id=match_id,
                  radiant_win=radiant_win,
                  radiant_team=radiant_team,
                  dire_team=dire_team)
    db.session.add(match)
    radiant_team = [x.strip() for x in radiant_team.split(',')]
    dire_team = [x.strip() for x in dire_team.split(',')]
    for hero in radiant_team:
        hero = Hero.query.filter_by(id=hero).first()
        a = MatchHero(hero=hero, match=match, team='radiant', win=radiant_win)
        db.session.add(a)
    for hero in dire_team:
        hero = Hero.query.filter_by(id=hero).first()
        win = False if radiant_win else True
        a = MatchHero(hero=hero, match=match, team='dire', win=win)
        db.session.add(a)
    db.session.commit()
    return match

def add_win_rate(team, win_rate, win_count, lose_count):
    team = comp_serialize(team)
    w = WinRates(team=team)
    w.win_rate = win_rate
    w.win_count = win_count
    w.lose_count = lose_count
    db.session.add(w)
    db.session.commit()
    return w
