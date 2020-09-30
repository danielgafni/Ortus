""" API Blueprint Application """

from flask import Blueprint
from flask_restx import Api
from app.config import Config


api_bp = Blueprint("api_bp", __name__, url_prefix="/api")
api_rest: Api = Api(api_bp)


@api_bp.after_request
def add_header(response):
    # response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Origin"] = "*" #Config.UI_BASE
    return response


from .user_api import UserAPI
from .login_api import LoginAPI
from .logout_api import LogoutAPI
from .signup_api import SignupAPI
