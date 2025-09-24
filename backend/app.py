# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

from config import Config
from models import db, Package, bcrypt # <-- Import bcrypt
from auth import auth_bp # <-- Import the auth blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Add a secret key for JWT
    # In a real app, this should be in your .env file!
    app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me" 

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    bcrypt.init_app(app) # <-- Initialize bcrypt
    jwt = JWTManager(app) # <-- Initialize JWTManager

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth') # <-- Register the auth routes

    @app.route('/api/my-bookings')
    @jwt_required() # This decorator protects the route
    def my_bookings():
    # Get the user's ID from the JWT
        current_user_id = get_jwt_identity()

    # In a real app, you would query the Booking model here.
    # For now, we'll return some mock data.
        mock_bookings = [
            {"id": 1, "package_name": "Parisian Dream"},
            {"id": 2, "package_name": "Roman Holiday"},
        ]

        return jsonify(mock_bookings)

    @app.route('/api/packages')
    def get_packages():
        # Query the database for all packages
        packages = Package.query.all()
        
        # This part creates the 'results' variable
        results = [
            {
                "id": pkg.id,
                "name": pkg.name,
                "description": pkg.description
            } 
            for pkg in packages
        ]
        
        return jsonify(results)

    return app