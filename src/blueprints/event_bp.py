from flask import Blueprint, jsonify, request
from datetime import datetime
from src.app import db, jwt
from src.blueprints.user_bp import Event

event_bp = Blueprint("event_bp", __name__, url_prefix="/events")


# Create (POST)
@event_bp.route("/", methods=["POST"])
def create_event():
    data = request.json
    new_event = Event(
        title=data["title"],
        description=data["description"],
        event_datetime=datetime.strptime(data["event_datetime"], "%Y-%m-%d %H:%M:%S"),
        location=data["location"],
        organizer_id=data["organizer_id"],
        max_capacity=data["max_capacity"],
        status=data.get("status", "upcoming"),
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.__dict__), 201


# Read All (GET)
@event_bp.route("/", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([event.__dict__ for event in events])


# Read One (GET)
@event_bp.route("/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.__dict__)


# Update (PUT)
@event_bp.route("/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.json
    event.title = data.get("title", event.title)
    event.description = data.get("description", event.description)
    event.event_datetime = datetime.strptime(
        data["event_datetime"], "%Y-%m-%d %H:%M:%S"
    )
    event.location = data.get("location", event.location)
    event.organizer_id = data.get("organizer_id", event.organizer_id)
    event.max_capacity = data.get("max_capacity", event.max_capacity)
    event.status = data.get("status", event.status)
    db.session.commit()
    return jsonify(event.__dict__)


# Delete (DELETE)
@event_bp.route("/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"})
