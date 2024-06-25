import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql+psycopg2://event_dev:event123@localhost:5432/event_management")

db = SQLAlchemy(app)
print(vars(db))

@app.route('/')
def index():
    return "Hello World"
