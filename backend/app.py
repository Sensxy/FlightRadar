# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, get_jwt_identity

from config import Config
from extensions import db, bcrypt, jwt
from models import Package
from auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

    # Initialize extensions from extensions.py
    db.init_app(app)
    Migrate(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    CORS(app, supports_credentials=True)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # --- THIS SECTION IS TEMPORARILY DISABLED ---
    # @app.route('/api/my-bookings')
    # @jwt_required()
    # def my_bookings():
    #     current_user_id = get_jwt_identity()
    #     mock_bookings = [
    #         {"id": 1, "package_name": "Parisian Dream", "user_id": current_user_id},
    #         {"id": 2, "package_name": "Roman Holiday", "user_id": current_user_id},
    #     ]
    #     return jsonify(mock_bookings)

    @app.route('/api/packages')
    def get_packages():
        search_term = request.args.get('search', '')
        query = Package.query
        if search_term:
            query = query.filter(Package.name.ilike(f'%{search_term}%'))
        packages = query.all()
        results = [
            {"id": pkg.id, "name": pkg.name, "description": pkg.description}
            for pkg in packages
        ]
        return jsonify(results)

    return app