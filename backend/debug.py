# backend/debug.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

app = Flask(__name__)
# Use a simple, hardcoded secret key for this test
app.config["JWT_SECRET_KEY"] = "this-is-a-test"

# Use the simplest possible CORS and JWT setup
CORS(app)
jwt = JWTManager(app)

# A simple, unprotected route to get a token
@app.route("/login_test", methods=["POST"])
def login_test():
    # We don't need a password; just create a token for a test user
    access_token = create_access_token(identity="test_user")
    return jsonify(access_token=access_token)

# The protected route we want to test
@app.route("/protected_test")
@jwt_required()
def protected_test():
    return jsonify(message="SUCCESS: If you see this, the test worked!")

# Allows us to run this file directly
if __name__ == "__main__":
    # Run on port 5001 to avoid conflicting with your main app
    app.run(port=5001, debug=True)