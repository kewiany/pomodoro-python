import os


class BaseConfig(object):
    TESTING = False
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
