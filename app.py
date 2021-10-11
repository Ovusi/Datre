from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from blueprints import user_bp, admin_bp, upload_bp, login_bp, signup_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///models/models.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx', 'csv']

db = SQLAlchemy(app)

app.register_blueprint(user_bp.user_bp, url_prefix='/users')
app.register_blueprint(admin_bp.admin_bp, url_prefix='/admin')
app.register_blueprint(upload_bp.upload_bp, url_prefix='/upload')
app.register_blueprint(login_bp.login_bp, url_prefix='/login')
app.register_blueprint(signup_bp.signup_bp, url_prefix='/signup')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
