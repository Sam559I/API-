from flask import Blueprint, jsonify, request
from src.Models.user import User, Event
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.app import db, jwt

# Define the blueprint
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
event_schema = EventSchema()
events_schema = EventSchema(many=True)

# Routes


@user_bp.route("/", methods=["GET"])
def get_users():
    """
    Get all users.
    """
    users = User.query.all()
    return jsonify(users_schema.dump(users))


@user_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user.
    """
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    if not username or not email or not password:
        return jsonify({"msg": "Missing parameters"}), 400

    if (
        User.query.filter_by(username=username).first()
        or User.query.filter_by(email=email).first()
    ):
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=username, email=email)
    new_user.password = password

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201


@user_bp.route("/login", methods=["POST"])
def login():
    """
    Login a user and return an access token.
    """
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.verify_password(password):
        access_token = create_access_token(identity=user.user_id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401
