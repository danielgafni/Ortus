from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    passwords = db.relationship('Password', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f"User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encrypted_password = db.Column(db.String(140), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, **kwargs):
    #     super(Password, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Encrypted password {self.encrypted_password}>"
