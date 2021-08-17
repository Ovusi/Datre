from flask import Flask, render_template, url_for
import database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("index.html")


@app.route("/<user>")
def user():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
