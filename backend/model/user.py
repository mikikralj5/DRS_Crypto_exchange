from email.policy import default
from .crypto_account import CryptoAccountSchema
from .payment_card import PaymentCardSchema
from .transaction import TransactionSchema
from config import db, ma
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(320))
    last_name = db.Column(db.String(320))
    address = db.Column(db.String(500))
    password = db.Column(db.String(500))
    email = db.Column(db.String(500))
    phone = db.Column(db.String(500))
    country = db.Column(db.String(500))
    city = db.Column(db.String(500))
    verified = db.Column(db.String(20), default="false")
    crypto_account = db.relationship(
        "CryptoAccount", backref="user", uselist=False
    )  # one to one
    payment_card = db.relationship("PaymentCard", backref="user", uselist=False)
    transactions = db.relationship("Transaction", backref="user")

    def __init__(
        self, first_name, last_name, address, password, email, phone, country, city
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.password = password
        self.email = email
        self.phone = phone
        self.country = country
        self.city = city


class UserSchema(ma.Schema):
    id = fields.Number()
    first_name = fields.Str()
    last_name = fields.Str()
    address = fields.Str()
    password = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    country = fields.Str()
    city = fields.Str()
    verified = fields.Str()
    crypto_account = fields.Nested(CryptoAccountSchema)
    payment_card = fields.Nested(PaymentCardSchema)
    transactions = fields.List(fields.Nested(TransactionSchema))
