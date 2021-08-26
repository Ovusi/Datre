from flask import Flask, render_template, request

from logic.file_handler import *
from logic.users import *
from logic.admin import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx', 'csv']

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    user_name = request.form[""]
    password = request.form[""]
    return render_template("")


@app.route("/signup")
def signup():
    user_name = request.form[""]
    password = request.form[""]
    email_address = request.form[""]
    phone_no = request.form[""]
    return render_template("")


@app.route("/<user>")
def user():
    return render_template("")


@app.route("/<user>/xlsx_csv", methods=['POST'])
def upload_xlsx_csv():
    file = request.files['']
    if file is None:
        return ''
    else:
        upload(extension=app.config['UPLOAD_EXTENSIONS'], file=file)
        return render_template("")


if __name__ == '__main__':
    app.run(debug=False)
