# from config import db, ma
# from flask_marshmallow import fields, Schema


# class CryptoCurrency(db.Model):
#     __tablename__ = "crypto_currency"
#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.Integer)
#     name = db.Column(db.String(32))
#     account_id = db.Column(db.Integer, db.ForeignKey("crypto_account.id"))


# class CryptoAccount(db.Model):
#     __tablename__ = "crypto_account"
#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.Integer)
#     crypto_currencies = db.relationship(
#         "CryptoCurrency", backref="account"
#     )  # one to many
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     def __init__(self):
#         self.crypto_currencies = []


# class PaymentCard(db.Model):
#     __tablename__ = "payment_card"
#     id = db.Column(db.Integer, primary_key=True)
#     card_number = db.Column(db.String(50))
#     cvv = db.Column(db.String(50))
#     expiration_date = db.Column(db.DateTime)
#     user_name = db.Column(db.String(50))
#     money_amount = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     def __init__(
#         self, card_number, cvv, expiration_date, user_name, money_amount, user_id
#     ):
#         self.card_number = card_number
#         self.cvv = cvv
#         self.expiration_date = expiration_date
#         self.user_name = user_name
#         self.money_amount = money_amount


# class Transaction(db.Model):
#     __tablename__ = "transaction"
#     hashID = db.Column(db.String(256), primary_key=True)
#     sender = db.Column(db.String(50))
#     recipient = db.Column(db.String(50))
#     state = db.Column(db.String(50))
#     amount = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     def __init__(self, sender, recipient, state, amount):
#         self.sender = sender
#         self.recipient = recipient
#         self.state = str(state)
#         self.amount = amount


# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(32))
#     last_name = db.Column(db.String(32))
#     address = db.Column(db.String(50))
#     password = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     phone = db.Column(db.String(50))
#     country = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     crypto_account = db.relationship(
#         "CryptoAccount", backref="user", uselist=False
#     )  # one to one
#     payment_card = db.relationship("PaymentCard", backref="user", uselist=False)
#     transations = db.relationship("Transaction", backref="user")

#     def __init__(
#         self, first_name, last_name, address, password, email, phone, country, city
#     ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.password = password
#         self.email = email
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.payment_card = None
#         self.transations = None
#         self.crypto_account = None
