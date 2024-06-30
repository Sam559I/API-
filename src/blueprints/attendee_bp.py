from flask import Blueprint, jsonify, request
from src.app import db
from src.Models.user import Attendee, AttendeeSchema

attendee_bp = Blueprint("attendee_bp", __name__, url_prefix="/attendees")
attendee_schema = AttendeeSchema()
attendees_schema = AttendeeSchema(many=True)


# Create (POST)
@attendee_bp.route("/", methods=["POST"])
def create_attendee():
    data = request.json
    if "name" not in data or "contact_details" not in data:
        return jsonify({"error": "Name and contact_details are required"}), 400

    new_attendee = Attendee(
        event_id=data["event_id"],
        user_id=data["user_id"],
        status="registered",
        name=data["name"],
        contact_details=data["contact_details"],
    )
    db.session.add(new_attendee)
    db.session.commit()

    # Convert SQLAlchemy object to dictionary using schema
    result = attendee_schema.dump(new_attendee)
    return jsonify(result), 201


# Read All (GET)
@attendee_bp.route("/", methods=["GET"])
def get_attendees():
    attendees = Attendee.query.all()
    # Serialize list of objects to JSON
    result = attendees_schema.dump(attendees)
    return jsonify(result)


# Read One (GET)
@attendee_bp.route("/<int:attendee_id>", methods=["GET"])
def get_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    # Serialize single object to JSON
    result = attendee_schema.dump(attendee)
    return jsonify(result)


# Update (PUT)
@attendee_bp.route("/<int:attendee_id>", methods=["PUT"])
def update_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    data = request.json
    attendee.event_id = data.get("event_id", attendee.event_id)
    attendee.user_id = data.get("user_id", attendee.user_id)
    db.session.commit()
    # Serialize updated object to JSON
    result = attendee_schema.dump(attendee)
    return jsonify(result)


# Delete (DELETE)
@attendee_bp.route("/<int:attendee_id>", methods=["DELETE"])
def delete_attendee(attendee_id):
    attendee = Attendee.query.get_or_404(attendee_id)
    db.session.delete(attendee)
    db.session.commit()
    return jsonify({"message": "Attendee deleted successfully"})
