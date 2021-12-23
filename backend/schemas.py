# from config import ma
# from flask_marshmallow import fields, Schema


# class CryptoCurrencySchema(ma.Schema):
#     id = fields.Number()
#     amount = fields.Number()
#     name = fields.Str()
#     account_id = fields.Number()


# class CryptoAccountSchema(ma.Schema):
#     id = fields.Number()
#     crypto_currencies = fields.List(fields.Nested(CryptoCurrencySchema))


# class PaymentCardSchema(ma.Schema):
#     id = fields.Number()
#     card_number = fields.Str()
#     cvv = fields.Str()
#     expiration_date = fields.Date()
#     user_name = fields.Str()
#     money_amount = fields.Number()


# class TransactionSchema(ma.Schema):
#     hashID = fields.Str()
#     sender = fields.Str()
#     recipient = fields.Str()
#     state = fields.Str()
#     amount = fields.Number()


# class UserSchema(ma.Schema):
#     class meta:
#         fields("id", "first_name", "last_name", "address")
