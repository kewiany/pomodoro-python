from app.app import create_app

__version__ = "0.0.0"

app = create_app()

from app import views
