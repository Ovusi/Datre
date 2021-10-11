from flask import render_template, request, redirect, url_for, flash, Blueprint

signup_bp = Blueprint('signup_bp', __name__)


@signup_bp.route("/signup", methods=['POST', 'GET'])
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
                signup(user_name, password, email_address, phone_no, database=db)
            except Exception as e:
                flash(e)
            else:
                return redirect(url_for(''))
        flash(error)
    return render_template("")