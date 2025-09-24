# backend/run.py
from app import create_app
from extensions import db
from models import Package, User, Booking

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Package': Package,
        'Booking': Booking
    }

if __name__ == '__main__':
    app.run(debug=True)