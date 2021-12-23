import bcrypt
import redis
from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, jsonify, request, abort, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session


from model.user import User, UserSchema
from model.transaction import Transaction, TransactionSchema
from model.payment_card import PaymentCard, PaymentCardSchema
from model.crypto_currency import CryptoCurrency, CryptoCurrencySchema
from model.crypto_account import CryptoAccount, CryptoAccountSchema
#pip install requirements

from config import db, ma

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "CryptoDB.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SESSION_TYPE"] = redis
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_REDIS"] = redis.from_url("redis://127.0.0.1:6379")

bcrypt = Bcrypt(app)
server_session = Session(app) #enabeld server side seesion sve je na serveru sem session id 
db.init_app(app)
ma.init_app(app)

user_schema = UserSchema()




@app.route("/", methods=["GET"])
def index():
    return jsonify({"hello": "world"})


@app.route("/create")
def create():
    db.create_all()
    return "All tables created"


@app.route("/registerUser", methods=["POST"])
def register_user():
    name = request.json["name"]
    lname = request.json["lname"]
    address = request.json["address"]
    password = request.json["password"]
    email = request.json["email"]
    phone = request.json["phoneNum"]
    country = request.json["country"]
    city = request.json["city"]

    user_exists = User.query.filter_by(email=email).first() is not None #true ako postoji taj User
    if user_exists == True:
        return jsonify({"error" : "User with that email alredy exists"}, 409)

    hashed_password = bcrypt.generate_password_hash(password)
    user = User(name, lname, address, hashed_password, email, phone, country, city)

    db.session.add(user)
    db.session.commit()
    return {"hello": "worlds"}



@app.route("/login", methods=["POST"])
def login_user():
    password = request.json["password"]
    email = request.json["email"]

    user = User.query.filter_by(email=email).first() 
    if user == None:
        return jsonify({"error" : "Unauthorized"}, 401)

    if not bcrypt.check_password_hash(user.password, password):
         return jsonify({"error" : "Unauthorized"}, 401)

    session["user_id"] = user.id #on je pravio neki hex za id

    return user_schema.jsonify(user)



@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error" : "Unauthorized"}, 401)

    user = User.query.filter_by(id=user_id).first()
    return user_schema.jsonify(user)
    

if __name__ == "__main__":
    app.run(debug=True)
