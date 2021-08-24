import pandas as pd
from flask_admin import Admin
from flask_login import LoginManager, UserMixin
from database import *
from openpyxl import load_workbook
from server import db


def xlsx(file):
    workbook = load_workbook(filename=file)
    workbook.sheetnames()
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
        pass
    for col in sheet.iter_cols(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
        pass


def csv(file):
    pass


def upload(extension, file):
    new_file = Charts(name=file.filename, data=file.read())
    if new_file != '':
        file_ext = os.path.splitext(new_file)[1]
        if file_ext not in extension:
            return ''
        else:
            db.session.add(new_file)
            db.session.commit()


def download():
    pass
