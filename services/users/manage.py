from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
import sys
import unittest

# Now you can work with the app and db directly
# docker-compose exec users flask shell
# >>> app
# >>> db
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

@cli.command('seed_db')
def seed_db():
    """Seeds to the database"""
    db.session.add(User(username='Joe', email='shmoe@test.com'))
    db.session.add(User(username='Joe2', email='joe@test.com'))
    db.session.commit()


if __name__ == '__main__':
    cli()
