# from flask_sqlalchemy import SQLAlchemy
from . import db
import requests
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (
    TimedJSONWebSignatureSerializer,
    URLSafeTimedSerializer,
    BadSignature,
    SignatureExpired,
)
from app.config import Config


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    uuid = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    wants_news = db.Column(db.Boolean)
    verified = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=600):
        s = TimedJSONWebSignatureSerializer(Config.SECRET_KEY, expires_in=expiration)
        return s.dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(Config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data["id"])
        return user

    def set_verified(self):
        self.verified = True
        db.session.commit()

    def generate_verification_token(self):
        s = URLSafeTimedSerializer(Config.SECRET_VALIDATION_KEY)
        return s.dumps({"id": self.id})

    @staticmethod
    def verify_verification_token(token):
        s = URLSafeTimedSerializer(Config.SECRET_VALIDATION_KEY)
        try:
            data = s.loads(token)
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data["id"])
        return user

    def send_email_verification_token(self):
        return requests.post(
            f"https://api.mailgun.net/v3/{Config.MAILGUN_DOMAIN_NAME}/messages",
            auth=("api", Config.MAILGUN_API_KEY),
            data={
                "from": f"Ortus <mailgun@{Config.MAILGUN_DOMAIN_NAME}>",
                "to": [self.email],
                "subject": "Ortus account verification",
                "text": f"Please verify your account by visiting this link:\n\n"
                f"{Config.VUE_APP_BASE}:{Config.APP_UI_PORT}/account/verify/?token={self.generate_verification_token()}",
            },
        )
