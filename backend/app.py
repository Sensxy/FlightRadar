from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from models import db, Package # Make sure to import Package

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app) # Enable CORS for frontend communication

    @app.route('/api/packages')
    def get_packages():
        # Query the database for all packages
        packages = Package.query.all()
        
        # Convert the list of package objects to a list of dictionaries
        results = [
            {
                "id": pkg.id,
                "name": pkg.name,
                "description": pkg.description
            } 
            for pkg in packages
        ]
        
        return jsonify(results)

    # This line is crucial!
    return app