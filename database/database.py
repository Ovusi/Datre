from app import db
from datetime import datetime
import os


class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(32), unique=True)
    email = db.Column("email", db.String(100), unique=True)
    password = db.Column("password", db.String(12))
    phone = db.Column("phone", db.Integer)


class Charts(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime)
    data = db.Column(db.LargeBinary)


if 'database.db' in os.getcwd():
    pass
else:
    db.create_all()
    db.session.commit()
