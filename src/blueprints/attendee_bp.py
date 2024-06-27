from flask import Blueprint, jsonify, request
from src.app import db, jwt
from src.Models.user import Attendee

attendee_bp = Blueprint("attendee_bp", __name__, url_prefix="/attendees")


# Create (POST)
@attendee_bp.route("/", methods=["POST"])
def create_attendee():
    data = request.json
    new_attendee = Attendee(event_id=data["event_id"], user_id=data["user_id"])
    db.session.add(new_attendee)
    db.session.commit()
    return jsonify(new_attendee.__dict__), 201
