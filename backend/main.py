import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


from config import db, ma

app = Flask(__name__)
CORS(app)

db_dir = "../../CryptoDB.db"
# print(f"os.path.abspath(db_dir): {str(os.path.abspath(db_dir))}")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_dir)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma.init_app(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True)
