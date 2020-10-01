from flask_login import logout_user, login_required, current_user
from flask_cors import cross_origin
from flask_restx import Resource
from . import api_rest


@api_rest.route("/logout", methods=["POST"])
# @cross_origin()
class LogoutAPI(Resource):
    @login_required
    def post(self):
        logout_user()
        return "Logged out", 205
