from config import db, ma
from marshmallow import Schema, fields

# class User(db.Model):
#     __tablename__ = 'user'
#     person_id = db.Column(db.Integer, primary_key=True)
#     lname = db.Column(db.String(32), index=True)
#     fname = db.Column(db.String(32))
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     def __init__(self, lastName, firstName):
#         self.lname = lastName
#         self.fname = firstName

#         def __repr__(self):
#             return '<User %r>' % self.fname

# class UserSchema(Schema):
#     person_id = fields.Number()
#     lname = fields.Str()
#     fname = fields.Str()
#     timestamp = fields.Date()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
