from flask import render_template, request, redirect, url_for, flash, Blueprint

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/<user>")
def user():
    return render_template("")
