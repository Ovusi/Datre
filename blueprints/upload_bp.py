from flask import render_template, request, redirect, url_for, flash, Blueprint
from logic.file_handler import *

upload_bp = Blueprint('upload_bp', __name__)
