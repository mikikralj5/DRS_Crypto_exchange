from config import db, ma
from marshmallow import Schema, fields


class CryptoCurrency(db.Model):
    __tablename__ = "crypto_currency"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    name = db.Column(db.String(32))
    # account_id = db.Column(db.Integer, db.ForeignKey("crypto_account.id"))


class CryptoCurrencySchema(ma.Schema):
    id = fields.Number()
    amount = fields.Number()
    name = fields.Str()
    account_id = fields.Number()
