import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import User, CryptoAccount, CryptoCurrency, PaymentCard, Transaction


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


@app.route("/", methods=["GET"])
def index():
    return jsonify({"hello": "world"})


@app.route("/create")
def create():
    db.create_all()
    return "All tables created"


if __name__ == "__main__":
    app.run(debug=True)
