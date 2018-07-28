# -*- coding: utf-8 -*-
from publicdata import Role
from run import db
from sqlalchemy import VARCHAR, Enum


class TestModel(db.Model):
    __tablename__ = "Test"
    userName = db.Column(VARCHAR(20), primary_key=True)

    def __init__(self, username):
        self.userName = username


class UserModel(db.Model):
    __tablename__ = "User"
    username = db.Column(VARCHAR(20), primary_key=True)
    password = db.Column(VARCHAR(20))
    role = db.Column(db.Enum(Role), default=Role.USER)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


db.create_all()
