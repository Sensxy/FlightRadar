# FlightRadar 

FlightRadar is a full-stack travel booking web application built with a Python/Flask REST API and a React single-page application frontend. It is responsible for managing users, travel packages, and bookings.

## Tech Stack

* **Backend**
    * Framework: **Flask**
    * Database ORM: **Flask-SQLAlchemy**
    * Database Migrations: **Flask-Migrate**
    * Authentication: **Flask-JWT-Extended** & **Flask-Bcrypt**
    * Database: **PostgreSQL**

* **Frontend**
    * Framework: **React** (with Vite)
    * Routing: **React Router**
    * API Communication: **Axios**

## Getting Started

Follow these instructions to get both the backend and frontend servers running on your local machine.

### Prerequisites

* Python 3.10+ & Pip
* Node.js & npm
* PostgreSQL

### 1. Backend Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/Sensxy/FlightRadar.git](https://github.com/Sensxy/FlightRadar.git)
    cd FlightRadar
    ```

2.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

3.  **Create and activate a virtual environment**:
    * On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up the database & environment**:
    * In PostgreSQL, create a new database (e.g., `CREATE DATABASE flightradar;`).
    * In the `backend` folder, create a `.env` file with your database URL:
        `DATABASE_URL="postgresql://postgres:your_password@localhost:5432/flightradar"`
    * In the `backend` folder, create a `.flaskenv` file with the app entry point:
        `FLASK_APP=run.py`

6.  **Create the database tables**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
7.  **(Optional) Seed the database with sample packages**:
    ```bash
    flask shell
    ```
    Then inside the shell, run:
    ```python
    from models import Package, db
    pkg1 = Package(name='Parisian Dream', description='A romantic tour of Paris.')
    pkg2 = Package(name='Roman Holiday', description='Explore the ancient ruins of Rome.')
    db.session.add_all([pkg1, pkg2])
    db.session.commit()
    exit()
    ```
8.  **Run the development server**:
    ```bash
    flask run
    ```
    The API is now running at `http://127.0.0.1:5000`.

### 2. Frontend Setup

1.  **Open a new terminal**.
2.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```
3.  **Install Node.js dependencies**:
    ```bash
    npm install
    ```
4.  **Run the development server**:
    ```bash
    npm run dev
    ```
    The frontend is now running at `http://localhost:5173`.

## Available API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/auth/register` | Creates a new user. | No |
| `POST` | `/api/auth/login` | Logs in a user, returns a JWT. | No |
| `GET` | `/api/packages` | Retrieves packages. Accepts `?search=` query param. | No |
| `POST` | `/api/packages/<id>/book`| Books a package for the authenticated user. | Yes |
| `GET` | `/api/my-bookings` | Gets the authenticated user's bookings. | Yes |
