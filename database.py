from server import db


class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(12))
    phone = db.Column("phone", db.Integer)
