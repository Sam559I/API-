from flask import Blueprint, jsonify, request
from datetime import datetime
from src.app import db
from src.blueprints.user_bp import Event, EventSchema

event_bp = Blueprint("event_bp", __name__, url_prefix="/events")

event_schema = EventSchema()
events_schema = EventSchema(many=True)


# Create (POST)
@event_bp.route("/", methods=["POST"])
def create_event():
    data = request.json

    # Check if 'event_datetime' is present in the data
    if "event_datetime" not in data:
        return jsonify({"error": "'event_datetime' field is required"}), 400

    try:
        new_event = Event(
            title=data["title"],
            description=data["description"],
            event_datetime=datetime.strptime(
                data["event_datetime"], "%Y-%m-%d %H:%M:%S"
            ),
            location=data["location"],
            organizer_id=data["organizer_id"],
            max_capacity=data["max_capacity"],
            status=data.get("status", "upcoming"),
        )
        db.session.add(new_event)
        db.session.commit()
        # Serialize the new_event object using EventSchema
        result = event_schema.dump(new_event)
        return jsonify(result), 201
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Read All (GET)
@event_bp.route("/", methods=["GET"])
def list_events():
    events = Event.query.all()
    result = events_schema.dump(events)
    return jsonify(result)


# Read One (GET)
@event_bp.route("/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    result = event_schema.dump(event)
    return jsonify(result)


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
    result = event_schema.dump(event)
    return jsonify(result)


# Delete (DELETE)
@event_bp.route("/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"})
