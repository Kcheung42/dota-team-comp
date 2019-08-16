import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy



# instantiate the db
db = SQLAlchemy()

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

    #register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app' : app, 'db' : db}

    return app
