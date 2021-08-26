from flask import Flask, render_template, request, redirect, url_for, flash

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


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        user_name = request.form[""]
        password = request.form[""]
        error = None

        if not user_name:
            error = 'User name is required'
        elif not password:
            error = 'Password name is required'

        if error is None:
            try:
                login(user_name, password)
            except Exception as e:
                flash(e)
            else:
                return redirect(url_for(''))
        flash(error)
    return render_template("")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user_name = request.form[""]
        password = request.form[""]
        email_address = request.form[""]
        phone_no = request.form[""]
        error = None

        if not user_name:
            error = 'User name is required'
        elif not password:
            error = 'Password name is required'
        elif not email_address:
            error = 'Email is required'
        elif not phone_no:
            error = 'Phone Number is required'

        if error is None:
            try:
                signup(user_name, password, email_address, phone_no)
            except Exception as e:
                flash(e)
            else:
                return redirect(url_for(''))
        flash(error)
    return render_template("")


@app.route("/<user>/xlsx_csv", methods=['POST', 'GET'])
def upload_xlsx_csv():
    file = request.files['']
    if not file:
        flash('No file selected')
    else:
        try:
            upload(file=file)
        except Exception as e:
            flash(e)
        else:
            flash("File uploaded successfully")
            return redirect(url_for(""))
    return render_template("")


@app.route("/<user>")
def user():
    return render_template("")


@app.route("/<admin>")
def my_admin():
    return render_template("")


if __name__ == '__main__':
    app.run(debug=False)
