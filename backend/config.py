from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os
import redis


load_dotenv()
db = SQLAlchemy()
ma = Marshmallow()
basedir = os.path.abspath(os.path.dirname(__file__))


class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    basedir, "CryptoDB.db"
)

    SESSION_COOKIE_SECURE = True
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mailzaaplikaciju21@gmail.com'
    MAIL_PASSWORD = 'mailzaaplikaciju21'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True