from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app) # Enable CORS for frontend communication

    # A simple test route to prove the API is working
    @app.route('/api/packages')
    def get_packages():
        # This is placeholder data for now
        # Later, you will query this from your database
        mock_packages = [
            {"id": 1, "name": "Hawaiian Getaway", "description": "A sunny trip to Honolulu."},
            {"id": 2, "name": "Tokyo Adventure", "description": "Explore the vibrant city of Tokyo."},
        ]
        return jsonify(mock_packages)

    return app