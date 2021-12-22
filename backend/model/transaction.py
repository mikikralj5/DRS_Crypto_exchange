# from config import db, ma
# from marshmallow import Schema, fields


# class Transaction(db.Model):
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


# class TransactionSchema(ma.Schema):
#     hashID = fields.Str()
#     sender = fields.Str()
#     recipient = fields.Str()
#     state = fields.Str()
#     amount = fields.Number()
