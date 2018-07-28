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
    userName = db.Column(VARCHAR(20), primary_key=True)
    passWord = db.Column(VARCHAR(20))

    def __init__(self, username,password):
        self.userName = username
        self.passWord = password


db.create_all()
