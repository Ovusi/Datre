import pandas as pd
from openpyxl import load_workbook


def xlsx(file):
    workbook = load_workbook(filename=file)
    workbook.sheetnames()
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
        pass
    for col in sheet.iter_cols(min_row=1, max_row=2, min_col=1, max_col=3, values_only=True):
        pass
