import bcrypt
import sqlalchemy
from flask import Flask, jsonify, request, abort, session, Response
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_session import Session
from werkzeug.utils import redirect
import random
import _thread
from random import randint
import requests
import string
import sqlite3
from time import sleep
import json
from sha3 import keccak_256
from model.transaction_state import TransactionState
from sqlalchemy import engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from config import os

from model.user import User, UserSchema
from model.transaction import Transaction, TransactionSchema
from model.payment_card import PaymentCard, PaymentCardSchema
from model.crypto_currency import CryptoCurrency, CryptoCurrencySchema
from model.crypto_account import CryptoAccount, CryptoAccountSchema


from config import db, ma, ApplicationConfig, SQLAlchemy

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
CORS(app)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     basedir, "CryptoDB.db"
# )
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.config["SESSION_TYPE"] = redis
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_REDIS"] = redis.from_url("redis://127.0.0.1:6379")

bcrypt = Bcrypt(app)
mail = Mail(app)
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


@app.route("/createCrypto_Account", methods=["POST"])
def create_crypto_account():
    amount = request.json["amount"]
    user_id = request.json["user_id"]
    user = User.query.get(user_id)
    crypto_account = CryptoAccount(amount=amount, crypto_currencies=[], user_id=user_id, user=user)
    db.session.add(crypto_account)
    db.session.commit()
    return "crypto_account created", 200


@app.route("/depositPayment_Card", methods=["PATCH"])#Da li ovo uopste treba???
def deposit_payment_card():
    amount = request.json["amount"]
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    payment_card = user.payment_card
    payment_card.amount += amount
    db.session.commit()

    return Response(status=200)


@app.route("/depositCrypto_Account", methods=["PATCH"])#
def deposit():
    amount = request.json["amount"]
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    payment_card = user.payment_card
    crypto_account = user.crypto_account
    payment_card.amount -= amount
    crypto_account.amount += amount
    db.session.commit()

    return Response(status=200)

#
# @app.route("/createCrypto_Currency", methods=["POST"])
# def create_crypto_currency():
#     amount = request.json["amount"]
#     name = request.json["name"]
#     account_id = request.json["account_id"]
#     crypto_account = CryptoAccount.query.get(account_id)
#     crypto_currency = CryptoCurrency(amount=amount, name=name, account_id=account_id, account=crypto_account)
#     db.session.add(crypto_currency)
#     db.session.commit()
#     return "crypto_currency created", 200


def send_mail(user):
    letters = string.ascii_letters
    user.otp = ''.join(random.choice(letters) for i in range(5))
    msg = Message(subject="Verification Code", sender="mailzaaplikaciju21@gmail.com", recipients=[user.email])
    msg.body = "Email Verification code = " + user.otp
    mail.send(msg)


def user_exists(email):
    user_exist = User.query.filter_by(email=email).first() is None
    if user_exist is None:
        return False
    else:
        return True


def update_crypto_currency(name, amount, crypto_currencies):
    crypto_currency = next(filter(lambda x: x.name == name, crypto_currencies), None)
    crypto_currency.amount += amount
    db.session.commit()
    return


def create_crypto_currency(name, amount, crypto_account):
    crypto_currency = CryptoCurrency(amount=amount, name=name, account_id=crypto_account.id)
    db.session.add(crypto_currency)
    db.session.commit()
    return


@app.route("/showCrypto_symbols")
def get_crypto_value():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    # parameters = {"start": 1, "limit": 5000}
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "4ceb685b-2766-45cc-8127-147c64386639"}
    sess = requests.Session()
    sess.headers.update(headers)
    response = sess.get(url)
    json_response = response.json()
    crypto_value_list = []
    for crypto in json_response["data"]:
        name = str(crypto["name"])
        symbol = str(crypto["symbol"])
        value = crypto["quote"]["USD"]["price"]
        crypto_value_list.append({"name": name, "symbol": symbol, "value": value})
    crypto_value_list = json.dumps(crypto_value_list)
    return crypto_value_list


@app.route("/showCrypto")
def get_all_crypto_currencies():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
    #parameters = {"start": 1, "limit": 5000}
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "4ceb685b-2766-45cc-8127-147c64386639"}
    sess = requests.Session()
    sess.headers.update(headers)
    response = sess.get(url)
    json_response = response.json()
    crypto_list = []
    for i in range(len(json_response["data"])):
        crypto_list.append(str(json_response["data"][i]["symbol"]))
    crypto_list = json.dumps(crypto_list)
    return crypto_list


@app.route("/exchange")
def exchange():
    sell = request.json["sell"]
    buy = request.json["buy"]
    amount = request.json["amount"]

    if buy == "USD":
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        parameters = {"symbol": sell, "convert": buy}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "4ceb685b-2766-45cc-8127-147c64386639"}
        sess = requests.Session()
        sess.headers.update(headers)
        response = sess.get(url, params=parameters)
        price = response.json()["data"][sell]["quote"][buy]["price"]
    else:
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        parameters = {"symbol": buy, "convert": sell}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "4ceb685b-2766-45cc-8127-147c64386639"}
        sess = requests.Session()
        sess.headers.update(headers)
        response = sess.get(url, params=parameters)
        price = response.json()["data"][buy]["quote"][sell]["price"]

    user_id = session.get("user_id")
    user = User.query.get(user_id)
    crypto_account = user.crypto_account
    sum_to_pay = price * amount

    if sell == "USD":
        if sum_to_pay > crypto_account.amount:
            return {"error": "you don't have enough money"}, 400
        crypto_account.amount -= sum_to_pay
        crypto_currencies = crypto_account.crypto_currencies
        iterator = filter(lambda x: x.name == buy, crypto_currencies)
        crypto_currencies = list(iterator)  # da bi vratio listu ovo ogre je iterator
        if crypto_currencies == []:
            create_crypto_currency(buy, amount, crypto_account)
        else:
            update_crypto_currency(buy, amount, crypto_currencies)
    elif buy == "USD":
        crypto_currencies = crypto_account.crypto_currencies
        crypto_currency = next(filter(lambda x: x.name == sell, crypto_currencies), None)
        if sum_to_pay > crypto_currency.amount:
            return {"error": "you don't have enough crypto currency"}, 400
        crypto_currency.amount -= sum_to_pay
        crypto_account.amount += amount
        db.session.commit()

    else:
        crypto_currencies = crypto_account.crypto_currencies
        crypto_currency = next(filter(lambda x: x.name == sell, crypto_currencies), None)
        if sum_to_pay > crypto_currency.amount:
            return {"error": "you don't have enough crypto currency"}, 400
        crypto_currency.amount -= sum_to_pay
        crypto_currencies = crypto_account.crypto_currencies
        iterator = filter(lambda x: x.name == buy, crypto_currencies)
        crypto_currencies = list(iterator)  # da bi vratio listu ovo ogre je iterator
        if crypto_currencies == []:
            create_crypto_currency(buy, amount, crypto_account)
        else:
            update_crypto_currency(buy, amount, crypto_currencies)

    return Response(status=200)


def mining(transaction_id):
    sleep(5*60)
    basedir = os.path.abspath(os.path.dirname(__file__))
    engine = sqlalchemy.create_engine("sqlite:///" + os.path.join(
    basedir, "CryptoDB.db"))
    local_session = sqlalchemy.orm.Session(bind=engine)
    transaction = local_session.query(Transaction).get(transaction_id)
    transaction.state = TransactionState.DONE.value
    local_session.commit()


@app.route("/updateTransactionState", methods=["PATCH"])
def update_transaction_state():
    transaction_id = request.json["transaction_id"]
    state = request.json["state"]
    transaction = Transaction.query.get(transaction_id)
    if TransactionState[state].value == "IN_PROGRESS":
        transaction.state = TransactionState.IN_PROGRESS.value
        db.session.commit()
        _thread.start_new_thread(mining, (transaction_id,))
    else:
        transaction.state = TransactionState.REJECTED.value
        db.session.commit()

    return Response(status=200)


@app.route("/createTransaction", methods=["POST"])
def create_transaction():
    recipient_email = request.json["recipient_email"]
    amount = request.json["amount"]
    if user_exists(recipient_email) is True:
        user_id = session.get("user_id")
        user = User.query.get(user_id)
        keccak = keccak_256()
        generated_string = "" + user.email + recipient_email + str(amount) + str(randint(0, 1000))
        keccak.update(generated_string.encode())

        transaction = Transaction(hashID=keccak.hexdigest(), sender=user.email, recipient=recipient_email, amount=amount, user_id=user_id, user=user)
        db.session.add(transaction)
        db.session.commit()
        return Response(status=200)
    else:
        return "User with that email doesn't exist", 400


@app.route("/filterTransaction")
def filter_transaction():
    filter_by = request.json["filter_by"]
    value = request.json["value"]
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    all_transactions = user.transactions

    all_transactions = filter(lambda x: getattr(x, filter_by) == value, all_transactions)

    schema = TransactionSchema(many=True)  # ako vracam vise
    results = schema.dump(all_transactions)
    return jsonify(results), 200


@app.route("/sortTransactions")
def sort_function():
    sort_by = request.json["sort_by"]
    sort_type = request.json["sort_type"]

    user_id = session.get("user_id")
    user = User.query.get(user_id)
    all_transactions = user.transactions
    if sort_type == "Asc":
        all_transactions.sort(key=lambda x: getattr(x, sort_by))
    else:
        all_transactions.sort(key=lambda x: getattr(x, sort_by), reverse=True)

    schema = TransactionSchema(many=True)  # ako vracam vise
    results = schema.dump(all_transactions)
    return jsonify(results), 200


@app.route("/getTransactions")
def get_transactions():
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    all_transactions = user.transactions
    schema = TransactionSchema(many=True)# ako vracam vise
    results = schema.dump(all_transactions)
    return jsonify(results)


@app.route("/getCrypto") #pregled stanja
def get_crypto():
    user_id = session.get("user_id")
    crypto_account = CryptoAccount.query.filter_by(user_id=user_id).first()
    all_crypto_currencies = crypto_account.crypto_currencies
    schema = CryptoCurrencySchema(many=True)
    results = schema.dump(all_crypto_currencies)
    return jsonify(results)


@app.route("/validateOTP", methods=["PATCH"])
def verification_with_otp():
    user_otp = request.json["otp"]
    user_id = session.get("user_id")
    user = User.query.get(user_id)

    if user_otp == user.otp:
        user.otp = "0"  # oznaka da je validiran
        db.session.commit()
        return {"massage": "Account Verification Successful!"}
    else:
        return {"massage": "Wrong OTP!"}


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
        return jsonify({"error": "User with that email already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    user = User(name, lname, address, hashed_password, email, phone, country, city)

    send_mail(user)

    db.session.add(user)
    db.session.commit()

    return Response(status=200)


@app.route("/login", methods=["POST"])
def login_user():
    password = request.json["password"]
    email = request.json["email"]

    user = User.query.filter_by(email=email).first() 
    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
         return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id #on je pravio neki hex za id

    return user_schema.jsonify(user)


@app.route("/logout", methods = ["POST"])
def logout_user():
    session.pop("user_id")
    return "200"


@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error" : "Unauthorized"}), 401

    user = User.query.filter_by(id=user_id).first()
    return user_schema.jsonify(user)
    

@app.route("/updateUser", methods=["PUT"])#put ili patch
def update_user():
    user_id = session.get("user_id")
    user = User.query.get(user_id)

    user.first_name = request.json["name"]
    user.last_name = request.json["lname"]
    user.address = request.json["address"]
    user.password = request.json["password"]
    user.email = request.json["email"]
    user.phone = request.json["phoneNum"]
    user.country = request.json["country"]
    user.city = request.json["city"]


    email_adress_exists = User.query.filter_by(email=user.email).count() #true ako postoji taj User
    if email_adress_exists > 1:
        return jsonify({"error": "User with that email already exists"}), 409

    user.password = bcrypt.generate_password_hash(user.password)

    db.session.commit()
    return redirect("/@me")



if __name__ == "__main__":
    app.run(debug=True)
