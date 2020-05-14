import os

from flask import Flask

from app.config import app_config


def create_app(config_object=None):
    app = Flask(__name__)
    if config_object == None:
        app.config.from_object(app_config[os.environ.get('FLASK_ENV')])
    else:
        app.config.from_object(config_object)
    return app
