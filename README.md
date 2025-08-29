Travel Booking Agency 
This is the backend REST API for a full-stack travel booking application. It is built with Python and Flask and is responsible for managing users, travel packages, and bookings.

Tech Stack (Backend)
Framework: Flask

Database ORM: Flask-SQLAlchemy

Database Migrations: Flask-Migrate

Authentication: Flask-JWT-Extended

Database: SQLite (for development)

Getting Started

Follow these instructions to get the backend server running on your local machine.

Prerequisites
Python 3.10+

Pip

Setup and Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Navigate to the backend directory:

Bash

cd backend
Create and activate a virtual environment:

Bash

python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Create and seed the database:
This command will create the database file and populate it with initial sample data.

Bash

# (Optional) If you have a .flaskenv file, this will be read automatically
# export FLASK_APP="manage.py"

flask db upgrade
flask seed
Run the development server:

Bash

flask run
The API is now running and available at http://127.0.0.1:5000.

Available API Endpoints
Use a tool like Thunder Client or Postman to test the following endpoints.

Method	Endpoint	Description
GET	/packages/	Retrieves a list of all travel packages.
POST	/packages/	Creates a new travel package.
POST	/auth/register	(To be implemented) Creates a new user.
POST	/auth/login	(To be implemented) Logs in a user.
This version is concise, accurate to your current progress, and gives anyone (including your future self) a clear and simple path to get the backend running. You can expand it with the frontend and Docker details as you build them out.
