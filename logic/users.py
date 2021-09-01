from flask_login import LoginManager, UserMixin
from database.database import *


""" This module contains user related functions.
    login(), logout(), signup() etc."""


def login(usr, password):
    pass


def logout():
    pass


def signup(usr, password, email, phone, database):
    new_user = Users(usr, password, email, phone)
    database.session.add(new_user)
    database.session.commit()
