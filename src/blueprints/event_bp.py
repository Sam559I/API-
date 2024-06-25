from flask import Blueprint, jsonify, request
from datetime import datetime
from .. import db
from ..models import Event

event_bp = Blueprint("event_bp", __name__, url_prefix="/events")


@event_bp.route("/", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([event.__dict__ for event in events])


@event_bp.route("/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.__dict__)


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

