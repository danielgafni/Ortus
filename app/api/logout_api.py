from flask_login import logout_user, login_required, current_user


from flask_restx import Resource
from . import api_rest


@api_rest.route("/logout", methods=["POST"])
class LogoutAPI(Resource):
    @login_required
    def post(self):
        logout_user()
        return "Logged out", 205
