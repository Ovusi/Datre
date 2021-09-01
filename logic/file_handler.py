from database.database import *
import json
import pandas as pd


""" This module contains functions for file handling and manipulation.
    """


def xlsx(file):
    # read the data from the xlsx file and convert to dict.
    # get the values of the dict and parse.
    data = pd.read_excel(file)
    result = data.to_dict(orient="values")
    parsed = json.loads(result)
    return json.dumps(parsed)


def csv(file):
    # read the data from the csv file and convert to dict.
    # get the values of the dict and parse.
    data = pd.read_csv(file)
    result = data.to_dict(orient="values")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=1)


def upload(file, database):
    new_file = Charts(name=file.filename, data=file.read())
    database.session.add(new_file)
    database.session.commit()


def download():
    pass
