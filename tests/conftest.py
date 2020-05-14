import pytest

from app.app import create_app
from app.config import app_config


@pytest.fixture(scope='module')
def test_app():
    app = create_app(app_config['testing'])
    with app.app_context():
        yield app
