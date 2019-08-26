from flask.cli import FlaskGroup
from project import create_app, db
from project.openapi import *
from project.combinations import store_compositions
from project.calc_win_rates import calc_win_rates
import sys
import unittest

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


import time
# TODO Make calls dependent on the last
@cli.command('seed_db')
def seed_db():
    """Seeds to the database"""
    start = time.time()
    fetch_heroes()
    fetch_matches()
    end = time.time()
    print(f'{end - start} seconds')

@cli.command('combo')
def calc_combinations():
    start = time.time()
    store_compositions()
    end = time.time()
    print(f'{end - start} seconds')

@cli.command('win_rates')
def recalc_win_rates():
    """Warning! Intensive Op: Calculates winrates for all Comp"""
    start = time.time()
    calc_win_rates()
    end = time.time()
    print(f'{end - start} seconds')


if __name__ == '__main__':
    cli()
