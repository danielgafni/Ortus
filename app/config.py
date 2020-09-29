import os
from dotenv import load_dotenv, find_dotenv


class Config:
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, "dist")

    load_dotenv(
        find_dotenv(".env.local")
    )

    FLASK_ENV = os.getenv("FLASK_ENV")
    assert FLASK_ENV, "FLASK_ENV should be set"

    load_dotenv()  # default application settings
    load_dotenv(
        find_dotenv(f".env.{FLASK_ENV.lower()}")
    )  # load environment specific config

    SECRET_KEY = os.getenv("SECRET_KEY", "super-mega-secret-key")
    SECRET_VALIDATION_KEY = os.getenv("SECRET_VALIDATION_KEY", "super-mega-secret-validation-key")

    API_BASE = os.getenv("VUE_APP_API_BASE")
    UI_BASE = os.getenv("VUE_APP_UI_BASE")

    if FLASK_ENV == "testing":
        sqlite = "sqlite:///" + os.path.join(ROOT_DIR, "tests", "db.sqlite")
    else:
        sqlite = "sqlite:///" + os.path.join(ROOT_DIR, "app", "db.sqlite")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", sqlite)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Basic Auth for Flask Admin
    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

    # MailGun
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    MAILGUN_DOMAIN_NAME = os.getenv("MAILGUN_DOMAIN_NAME")
