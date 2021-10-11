from flask import render_template, request, redirect, url_for, flash, Blueprint

login_bp = Blueprint('login_bp', __name__)


@login_bp.route("/login", methods=['POST', 'GET'])
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
