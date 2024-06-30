# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.extensions import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=True)
    events = db.relationship("Event", backref="organizer", lazy=True)
    attendees = db.relationship("Attendee", backref="user", lazy=True)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Event(db.Model):
    __tablename__ = "events"
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    attendees = db.relationship("Attendee", backref="event", lazy=True)


class Attendee(db.Model):
    __tablename__ = "attendees"
    attendee_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.event_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    contact_details = db.Column(db.String(255), nullable=False)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash",)


class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True


class AttendeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Attendee
        load_instance = True
