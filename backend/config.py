# backend/config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///travel.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
