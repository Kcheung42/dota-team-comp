from project.serializer import comp_serialize
from project import db
from project.api.models import Hero, WinRates


def combinations(n, heroes, result, cur_team, cur_idx):
    if n == 0:
        team = comp_serialize(cur_team)
        existing_combo = WinRates.query.filter_by(team=team).first()
        if existing_combo is None:
            db.session.add(WinRates(team=team))
            print("Team Comp#:{}".format(int(team,2)))
            return 1
        else:
            print(f'Already in Database:{cur_team}')
            return 0
    else:
        r = 0
        if len(cur_team) > 0:
            team = comp_serialize(cur_team)
            existing_combo = WinRates.query.filter_by(team=team).first()
            if existing_combo is None:
                db.session.add(WinRates(team=team))
                print("Team Comp#:{}".format(int(team,2)))
                r += 1
            else:
                print(f'Already in Database:{cur_team}')
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

    # for production:
    # heroes_id = [h.id for h in heroes]
    # print("Calculating combinaations for {} heroes ...".format(len(heroes_id)))
    # calc_combinations(batch)

    # for development
    hero_batches = [range(i,i+19)for i in range(1,130,20)]
    count = 0
    for batch in hero_batches:
        count += calc_combinations(batch)
    print("combinations:{} Successfully Added".format(count))
