import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Register blueprints
    from .blueprints.user_bp import user_bp
    from .blueprints.event_bp import event_bp
    from .blueprints.attendee_bp import attendee_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(event_bp, url_prefix="/api/events")
    app.register_blueprint(attendee_bp, url_prefix="/api/attendees")

    return app
