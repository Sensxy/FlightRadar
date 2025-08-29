# backend/app/routes/bookings.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Booking, TravelPackage, User

bookings_bp = Blueprint("bookings", __name__)

# GET my bookings
@bookings_bp.route("/", methods=["GET"])
@jwt_required()
def get_my_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": b.id,
        "package_id": b.package_id,
        "date": b.date.isoformat()
    } for b in bookings])

# POST create booking
@bookings_bp.route("/", methods=["POST"])
@jwt_required()
def create_booking():
    data = request.get_json()
    user_id = get_jwt_identity()
    package_id = data.get("package_id")

    # Ensure package exists
    package = TravelPackage.query.get(package_id)
    if not package:
        return jsonify({"error": "Package not found"}), 404

    booking = Booking(user_id=user_id, package_id=package_id)
    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Booking created", "id": booking.id}), 201
