from flask import request, jsonify, make_response
from flask_login import login_user, current_user, logout_user


from flask_restx import Resource, abort
from . import api_rest
from app.models import User


@api_rest.route("/login", methods=["POST"])
class LoginAPI(Resource):
    def post(self):
        # If, for some reason a user is logged in... we should actually login the new user.
        # This is an edge case if someone leaves it open on laptop or public computer
        if current_user.is_authenticated:
            logout_user()

        try:
            email = request.json["email"]
            password = request.json["password"]
            # remember_me = request.json["remember_me"]
        except (KeyError, TypeError):
            abort(400, "Invalid data")

        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            abort(401, "Unauthorized: Incorrect email and/or password.")

        login_user(user)
        token = user.generate_auth_token().decode("ASCII")
        return make_response(
            jsonify(
                {
                    "token": token,
                    # "next_page": next_page,
                    "is_verified": user.verified,
                }
            ),
            201,
        )
