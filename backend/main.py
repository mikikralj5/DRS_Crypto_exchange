import bcrypt
from flask import Flask, jsonify, request, abort, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_session import Session
from werkzeug.utils import redirect
import  random
import  string


from model.user import User, UserSchema
from model.transaction import Transaction, TransactionSchema
from model.payment_card import PaymentCard, PaymentCardSchema
from model.crypto_currency import CryptoCurrency, CryptoCurrencySchema
from model.crypto_account import CryptoAccount, CryptoAccountSchema


from config import db, ma, ApplicationConfig

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


@app.route("/createCrypto_Currency", methods=["POST"])
def create_crypto_currency():
    amount = request.json["amount"]
    name = request.json["name"]
    account_id = request.json["account_id"]
    crypto_account = CryptoAccount.query.get(account_id)
    crypto_currency = CryptoCurrency(amount=amount, name=name, account_id=account_id, account=crypto_account)
    db.session.add(crypto_currency)
    db.session.commit()
    return "crypto_currency created", 200


def send_mail(user):
    letters = string.ascii_letters
    user.otp = ''.join(random.choice(letters) for i in range(5))
    msg = Message(subject="Verification Code", sender="mailzaaplikaciju21@gmail.com", recipients=[user.email])
    msg.body = "OTP = " + user.otp
    mail.send(msg)


# @app.route("/createTransaction")
# def create_transaction():


@app.route("/sortTransactions")
def sort_function():
    sort_by = request.json["sort_by"]#recipient,state,amount
    sort_type = request.json["sort_type"]

    user_id = session.get("user_id")
    user = User.query.get(user_id)
    all_transactions = user.transactions

    if sort_type == "Asc":
        all_transactions.sort(key=sort_by)
    else:
        all_transactions.sort(key=sort_by, reversed=True)



@app.route("/getTransactions")
def get_transactions():
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    all_transactions = user.transactions
    schema = TransactionSchema(many=True)# ako vracam vise
    results = schema.dump(all_transactions)
    return jsonify(results)


@app.route("/getCrypto")#pregled stanja
def get_crypto():
    user_id = session.get("user_id")
    crypto_account = CryptoAccount.query.filter_by(user_id=user_id).first()
    all_crypto_currencies = crypto_account.crypto_currencies
    schema = CryptoCurrencySchema(many=True)
    results = schema.dump(all_crypto_currencies)
    return jsonify(results)


@app.route("/validateOTP", methods=["PUT"])
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
        return jsonify({"error": "User with that email already exists"}, 409)

    hashed_password = bcrypt.generate_password_hash(password)
    user = User(name, lname, address, hashed_password, email, phone, country, city)

    send_mail(user)

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


@app.route("/logout")
def logout_user():
    session.pop("user_id")
    return "Succesfuly loged out", 200


@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error" : "Unauthorized"}, 401)

    user = User.query.filter_by(id=user_id).first()
    return user_schema.jsonify(user)
    

@app.route("/updateUser", methods=["PUT"]) #kako je ovo put
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
        return jsonify({"error" : "User with that email alredy exists"}, 409)

    user.password = bcrypt.generate_password_hash(user.password)

    db.session.commit()
    return redirect("/@me")



if __name__ == "__main__":
    app.run(debug=True)
