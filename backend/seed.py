from app import create_app
from app.extensions import db
from app.models import User, TravelPackage, Booking
import click
from flask.cli import with_appcontext

# Use the app factory to create an app instance
app = create_app()

@click.command(name='seed')
@with_appcontext
def seed():
    """Seeds the database with initial data."""
    
    # Optional: Clear out existing data
    # This is destructive and should only be used in development.
    # To run this, uncomment the next three lines.
    # print("Deleting all data...")
    # db.session.remove()
    # db.drop_all()
    # db.create_all()

    print("Seeding database...")

    # Create a user
    user1 = User(username='testuser', password='password123') # Note: In a real app, you'd hash this password!

    # Create some travel packages
    package1 = TravelPackage(
        title='Hawaiian Paradise',
        description='A 7-day trip to the beautiful islands of Hawaii.',
        price=2500.00
    )
    package2 = TravelPackage(
        title='Parisian Adventure',
        description='Explore the city of lights with a 5-day guided tour.',
        price=1800.00
    )

    # Add the objects to the database session
    db.session.add(user1)
    db.session.add(package1)
    db.session.add(package2)

    # Commit the session to save the changes
    db.session.commit()

    print("Database seeded successfully!")