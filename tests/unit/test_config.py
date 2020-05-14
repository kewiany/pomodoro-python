from app.config import app_config


def test_development_config(test_app):
    test_app.config.from_object(app_config['development'])
    assert not test_app.config['TESTING']


def test_testing_config(test_app):
    test_app.config.from_object(app_config['testing'])
    assert test_app.config['TESTING']
    assert not test_app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
