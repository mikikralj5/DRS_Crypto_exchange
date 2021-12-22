# from config import db, ma
# from marshmallow import Schema, fields


# class PaymentCard(db.Model):
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


# class PaymentCardSchema(ma.Schema):
#     id = fields.Number()
#     card_number = fields.Str()
#     cvv = fields.Str()
#     expiration_date = fields.Date()
#     user_name = fields.Str()
#     money_amount = fields.Number()
