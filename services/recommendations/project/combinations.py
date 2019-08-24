from project.serializer import comp_serialize
from project import db
from project.api.models import Hero, WinRates


def combinations(n, heroes, result, cur_team, cur_idx):
    if n == 0:
        team = comp_serialize(cur_team)
        existing_combo = WinRates.query.filter_by(team=team).first()
        if existing_combo is None:
            db.session.add(WinRates(team=team))
            # print("Team Comp#:{}".format(team))
            result.append(team)
            return 1
        else:
            return 0
    else:
        r = 0
        if len(cur_team) > 0:
            team = comp_serialize(cur_team)
            existing_combo = WinRates.query.filter_by(team=team).first()
            if existing_combo is None:
                db.session.add(WinRates(team=team))
                # print("Team Comp#:{}".format(team))
                result.append(team)
                r += 1
        count = 1
        for i in range(cur_idx, len(heroes)):
            r += combinations(n-1, heroes, result, cur_team+[heroes[i]], cur_idx + count)
            count += 1
        return r


def calc_combinations(sample):
    results = []
    count = combinations(5, sample, results, [], 0)
    db.session.commit()
    return count


def store_compositions():
    heroes = Hero.query.all()
    # heroes_id = [h.id for h in heroes]
    heroes_id = range(1,20)
    print("Calculating combinaations for {} heroes ...".format(len(heroes_id)))
    count = calc_combinations(heroes_id)
    print("combinations:{} Successfully Added".format(count))
