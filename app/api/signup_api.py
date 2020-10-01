from sqlalchemy.exc import IntegrityError
from flask import request
from flask_cors import cross_origin
from flask_restx import Resource, abort, marshal_with, fields
from . import api_rest
from app.models import Signup, db


marshall_fields = {
    "id": fields.Integer,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
    "email": fields.String,
}


@api_rest.route("/signups", methods=["POST"])
@cross_origin
class SignupAPI(Resource):
    @marshal_with(marshall_fields, envelope="resource")
    def post(self):
        """
        Process the email submitted for signup.py.
        """
        email = request.json["email"]
        if not email:
            abort(400, f"Please provide email. Received: {email}")
        new_signup = Signup(email=email)
        try:
            db.session.add(new_signup)
            db.session.commit()
        except IntegrityError:
            return new_signup, 200
        except Exception as e:
            abort(500, f"Database Error: {e}")

        return new_signup, 201
