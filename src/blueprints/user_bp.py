from flask import Blueprint, jsonify, request
from init import db
from models import User

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])
