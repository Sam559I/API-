from os import environ
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
