# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime


class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    email = db.Column(
        db.String(128), index=True, unique=True
    )  # Let the db enforce uniquness
