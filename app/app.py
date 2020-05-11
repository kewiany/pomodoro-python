import os

from flask import Flask

from app.config import app_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config[os.environ.get('FLASK_ENV')])
    return app
