from flask_sqlalchemy import SQLAlchemy
from index import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password")

