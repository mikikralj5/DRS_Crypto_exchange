from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os
import redis
from flaskext.mysql import MySQL


load_dotenv()
mysql = MySQL()
db = SQLAlchemy()
ma = Marshmallow()
basedir = os.path.abspath(os.path.dirname(__file__))


class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    #     basedir, "CryptoDB.db"
    # )

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@db/mysql_db'
    ISOLATION_LEVEL = "READ UNCOMMITTED"
    SESSION_COOKIE_SECURE = True
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

    #SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    SESSION_REDIS = redis.from_url("redis://redis:6379/0")
    #SESSION_REDIS = redis.from_url("redis://localhost:6379")
    #SESSION_REDIS = redis.from_url("redis://redis:6379")
