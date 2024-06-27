from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

db = SQLAlchemy(app)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

# Register blueprints
from src.blueprints.user_bp import user_bp
from src.blueprints.event_bp import event_bp

app.register_blueprint(user_bp)
app.register_blueprint(event_bp)


@app.route("/")
def index():
    return "Welcome to the API!"
