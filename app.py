from flask import Flask, render_template, request, redirect, url_for, flash


from controllers.file_handler import *
from controllers.users import *
from controllers.admin import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///models/models.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx', 'csv']

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
