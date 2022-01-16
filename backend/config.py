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
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/CryptoDB"
    #SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{os.environ['POSTGRES_PASSWORD']}@postgres:5432/{os.environ['POSTGRES_DB']}"
    # MYSQL_DATABASE_USER = 'root'
    # MYSQL_DATABASE_PASSWORD = 'flasktest2021'
    # MYSQL_DATABASE_DB = 'flasktest'
    # MYSQL_DATABASE_HOST = '0.0.0.0'

    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:flasktest2021@0.0.0.0/flasktest'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@db/mysql_db'

    SESSION_COOKIE_SECURE = True
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url("redis://localhost:6379")
    SESSION_REDIS = redis.from_url("redis://redis:6379/0")
    SESSION_COOKIE_SECURE = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mailzaaplikaciju21@gmail.com'
    MAIL_PASSWORD = 'mailzaaplikaciju21'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
