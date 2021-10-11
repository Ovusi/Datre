from flask import render_template, request, redirect, url_for, flash, Blueprint
from logic.admin import *

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route("/<admin>")
def my_admin():
    return render_template("")
