import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



# instantiate the db
db = SQLAlchemy()
cors = CORS()

# Update project/__init__.py, removing the route and model
# and adding the Application Factory pattern:

# create multiple instances of this app later
# why?
# 1. Testing You can have instances of the application
# 2. Multiple instances of in the same application process

def create_app(script_info=None):

   # instantiate the app
    app = Flask(__name__)

    api = Api(app)

    # set up config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app)

    #register blueprints
    from project.api.matches import matches_blueprint
    from project.api.heroes import heroes_blueprint
    from project.api.recommendations import recommend_blueprint
    app.register_blueprint(matches_blueprint)
    app.register_blueprint(heroes_blueprint)
    app.register_blueprint(recommend_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app' : app, 'db' : db}

    return app
