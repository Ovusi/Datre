from flask import render_template, request, redirect, url_for, flash, Blueprint

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route("/<admin>")
def my_admin():
    return render_template("")
