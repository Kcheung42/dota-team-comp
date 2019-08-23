from project.serializer import comp_serialize
from project import db
from project.api.models import Hero, WinRates


def combinations(n, heroes, result, cur_team, cur_idx):
    if n == 0:
        team = comp_serialize(cur_team)
        print("Team Comp#:{}".format(team))
        result.append(team)
        return
    else:
        if len(cur_team) > 0:
            team = comp_serialize(cur_team)
            print("Team Comp#:{}".format(team))
            result.append(team)
        count = 1
        for i in range(cur_idx, len(heroes)):
            combinations(n-1, heroes, result, cur_team+[heroes[i]], cur_idx + count)
            count += 1
        return


def calc_combinations(sample):
    results = []
    combinations(5, sample, results, [], 0)
    return results


def store_compositions():
    heroes = Hero.query.all()
    heroes_id = [h.id for h in heroes]
    heroes_id = range(1,11)
    compositions = calc_combinations(heroes_id)
    i = 0
    for c in compositions:
        i += 1
        db.session.add(
            WinRates(team=c))
        print("Seeding team composition#:{}".format(i))
    db.session.commit()
    print("combinations:{} Successfully Added".format(len(compositions)))
