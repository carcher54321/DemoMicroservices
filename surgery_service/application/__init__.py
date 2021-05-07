import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        # Register blueprints
        from .surgery_api import surgery_api_blueprint
        app.register_blueprint(surgery_api_blueprint, url_prefix='/api/surgery')
        return app
