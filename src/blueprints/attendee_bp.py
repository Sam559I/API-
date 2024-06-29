from flask import Blueprint, jsonify, request
from src.init import db, jwt
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


# Read All (GET)
@attendee_bp.route("/", methods=["GET"])
def get_attendees():
    attendees = Attendee.query.all()
    return jsonify([attendee.__dict__ for attendee in attendees])


# Read One (GET)
@attendee_bp.route("/<int:attendee_id>", methods=["GET"])
def get_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    return jsonify(attendee.__dict__)


# Update (PUT)
@attendee_bp.route("/<int:attendee_id>", methods=["PUT"])
def update_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    data = request.json
    attendee.event_id = data.get("event_id", attendee.event_id)
    attendee.user_id = data.get("user_id", attendee.user_id)
    db.session.commit()
    return jsonify(attendee.__dict__)


# Delete (DELETE)
@attendee_bp.route("/<int:attendee_id>", methods=["DELETE"])
def delete_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    db.session.delete(attendee)
    db.session.commit()
    return jsonify({"message": "Attendee deleted successfully"})
