from flask import Flask
import os
from extensions import db, migrate, jwt, ma
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    @app.route("/")
    def index():
        return "Welcome to the API!"

    # Register blueprints
    from src.blueprints.user_bp import user_bp
    from src.blueprints.event_bp import event_bp
    from src.blueprints.attendee_bp import attendee_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(attendee_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
