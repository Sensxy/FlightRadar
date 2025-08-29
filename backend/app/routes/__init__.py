from .auth import auth_bp
from .packages import packages_bp
from .bookings import bookings_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(packages_bp, url_prefix="/packages")
    app.register_blueprint(bookings_bp, url_prefix="/bookings")
