from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
import os

db = SQLAlchemy(app)

def create_app(config_class=Init):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    Migrate(app, db)

    @app.route("/")
    def hello():
        return "1 Test page!"

    return app


app = create_app()
