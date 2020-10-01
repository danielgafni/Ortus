from flask import request, abort
from flask_restx import Resource, marshal_with, fields
from flask_cors import cross_origin
from . import api_rest
from app.models import User, db


marshall_fields = {
    "id": fields.Integer,
    "created_at": fields.DateTime,
    "update_ad": fields.DateTime,
    "uuid": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "wants_news": fields.Boolean,
}


@api_rest.route("/users", methods=["POST"])
@cross_origin()
class UserAPI(Resource):
    @marshal_with(marshall_fields, envelope="resource")
    def post(self):
        email = request.json["email"]
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        password = request.json["password"]
        wants_news = request.json["wants_news"]

        if not all([email, first_name, last_name, password]):
            abort(
                400,
                f"Invalid data: {(email, first_name, last_name, password, wants_news)}",
            )
        if User.query.filter_by(email=email).first() is not None:
            abort(409, f"This user already exists: {email}")

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            wants_news=wants_news,
        )
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            abort(500, f"Database Error: {e}")

        return user, 201
