# backend/app/routes/packages.py
from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import TravelPackage

packages_bp = Blueprint("packages", __name__)

# GET all packages
@packages_bp.route("/", methods=["GET"])
def get_packages():
    packages = TravelPackage.query.all()
    # This list comprehension is a more concise way to write the loop
    packages_list = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": p.price
        } 
        for p in packages
    ]
    return jsonify(packages_list)

# POST create new package
@packages_bp.route("/", methods=["POST"])
def create_package():
    data = request.get_json()
    # Ensure you are using 'title' to match the model
    if 'title' not in data or 'price' not in data:
        return jsonify({"error": "Missing title or price"}), 400
        
    package = TravelPackage(
        title=data["title"],  # <--- CORRECTED LINE
        description=data.get("description", ""),
        price=data["price"]
    )
    db.session.add(package)
    db.session.commit()
    return jsonify({"message": "Package created", "id": package.id}), 201