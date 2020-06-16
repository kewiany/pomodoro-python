import os


class BaseConfig(object):
    TESTING = False
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProductionConfig(BaseConfig):
    ENV = 'production'


class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    DEBUG = True


app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
