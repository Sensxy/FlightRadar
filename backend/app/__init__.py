from flask import Flask
from config import Config
from .extensions import db, jwt, migrate

def create_app(config_class=Config):
    """
    Application factory function.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app object
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes *inside* the factory
    # This avoids circular imports
    with app.app_context():
        from . import models
        from .routes import register_routes
        register_routes(app)

    return app