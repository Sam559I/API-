from functools import wraps
from flask import abort
from flask_jwt_extended import get_jwt_identity
from src.Models.user import User

# from src.app import db


def authorize(user_id=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Getting the user ID from the JWT token
            jwt_user_id = get_jwt_identity()

            # Selecting the user from the database using the user ID from the JWT token
            user = User.query.get(jwt_user_id)

            if not (user.is_admin or (user_id and jwt_user_id == user_id)):
                abort(401)

            return func(user, *args, **kwargs)

        return wrapper

    return decorator
