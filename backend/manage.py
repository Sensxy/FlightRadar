from app import create_app
from seed import seed # Import the seed command from your seed.py file

# Create an app instance using the factory
app = create_app()

# Add the seed command to the Flask CLI
app.cli.add_command(seed)

# You can add other commands here as your app grows