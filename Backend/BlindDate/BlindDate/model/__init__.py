# -*- coding: utf-8 -*-
from run import db
from sqlalchemy import VARCHAR


class TestModel(db.Model):
    __tablename__ = "Test"
    userName = db.Column(VARCHAR(20), primary_key=True)

    def __init__(self, username):
        self.userName = username


class UserModel(db.Model):
    __tablename__ = "User"
    username = db.Column(VARCHAR(20), primary_key=True)
    password = db.Column(VARCHAR(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password


db.create_all()
