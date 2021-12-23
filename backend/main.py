import os
from flask import Flask, jsonify, request
from flask_cors import CORS


from model.user import User, UserSchema
from model.transaction import Transaction, TransactionSchema
from model.payment_card import PaymentCard, PaymentCardSchema
from model.crypto_currency import CryptoCurrency, CryptoCurrencySchema
from model.crypto_account import CryptoAccount, CryptoAccountSchema


from config import db, ma

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "CryptoDB.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


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

    user = User(name, lname, address, password, email, phone, country, city)

    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
