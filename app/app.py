import os

from flask import Flask, Blueprint, current_app, send_file, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate

from .config import Config
from .models import db

blueprint = Blueprint("root", __name__)


def init_base_app() -> Flask:
    app: Flask = Flask(__name__, static_folder="../dist/static")
    # Config the app
    app.config.from_object(Config)
    # app.debug = True
    app.logger.info(">>> ENV: {}".format(Config.FLASK_ENV))

    # Setup DB
    db.init_app(app)

    return app


def create_app() -> Flask:
    from .api import api_bp  # to avoid circular imports
    from .admin import admin_bp, admin, login_manager, basic_auth

    # Setup Blueprints etc...
    app: Flask = init_base_app()
    app.register_blueprint(blueprint)

    # admin stuff
    app.register_blueprint(admin_bp)
    admin.init_app(app)
    basic_auth.init_app(app)
    login_manager.init_app(app)

    # Setup Models
    Migrate(app, db, directory=os.path.join("app", "migrations"))

    # Setup the API
    app.register_blueprint(api_bp)
    CORS(app)

    app.logger.info(">>> Up and running.")

    return app


# Load the root Vue.js index.html file which is built in the /dist dir
@blueprint.route("/")
def index_client():
    dist_dir = current_app.config["DIST_DIR"]
    entry = os.path.join(dist_dir, "index.html")
    return send_file(entry)


# Load any other static distribution files
@blueprint.route("/<path:path>")
def send_js(path):
    return send_from_directory(current_app.config["DIST_DIR"], path)
