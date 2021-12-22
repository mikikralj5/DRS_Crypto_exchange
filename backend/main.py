from flask import Flask, jsonify, request
from flask_cors import CORS
from model import crypto_currency


from config import db, ma

app = Flask(__name__)
CORS(app)

# db_dir = "../../CryptoDB.db"
# print(f"os.path.abspath(db_dir): {str(os.path.abspath(db_dir))}")
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_dir)


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///C:\\fax\\drs\\DRS_Crypto_exchange\\CryptoDB.db"
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
