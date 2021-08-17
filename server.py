from flask import Flask, render_template, url_for
from database import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("")


@app.route("/login")
def login():
    return render_template("")


@app.route("/signup")
def signup():
    return render_template("")


@app.route("/<user>")
def user():
    return render_template("")


@app.route("/<user>/xlsx_csv")
def xlsx_csv():
    return render_template("")


if __name__ == '__main__':
    app.run(debug=False)