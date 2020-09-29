from flask import Blueprint, redirect, abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_basicauth import BasicAuth

from .models import db, User


admin_bp = Blueprint("app.admin.admin_bp", __name__)
admin = Admin()
basic_auth = BasicAuth()
login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get("Authorization")
    if token:
        user = User.verify_auth_token(token.encode("ASCII"))
        return user
    else:
        return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    # this should return a response for the frontend to redirect to /login
    # with open("tmp.txt", "w") as file:
    #     from flask import request
    #     file.write(str(request.headers))
    abort(401, "Unauthorized")


@admin_bp.route("/admin/login")
@basic_auth.required
def secret_view():
    return redirect("/admin")


# Setup a backend Admin
# First override accessibility
class ProtectedModelView(ModelView):
    def is_accessible(self):
        # return current_user.is_authenticated
        return basic_auth.authenticate()

    # TODO: I think this is broken
    def inaccessible_callback(self, name, **kwargs):
        return redirect("/admin/login")


class UserModelView(ProtectedModelView):
    column_searchable_list = ["email", "first_name", "last_name"]


admin.add_view(UserModelView(User, db.session))
