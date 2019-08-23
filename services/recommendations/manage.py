from flask.cli import FlaskGroup
from project import create_app, db
from project.openapi import *
from project.combinations import store_compositions
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


# TODO Make calls dependent on the last
@cli.command('seed_db')
def seed_db():
    """Seeds to the database"""
    fetch_heroes()
    fetch_matches()
    store_compositions()


if __name__ == '__main__':
    cli()
