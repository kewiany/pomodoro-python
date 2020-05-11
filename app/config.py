import os


class BaseConfig(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
}
