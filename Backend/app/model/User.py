# -*- coding: utf-8 -*-
from run import db
from sqlalchemy import Column, Integer, CHAR, VARCHAR


class User(db.Model):
    print("init")
    __tablename__ = "User"
    userName = db.Column(VARCHAR(20), primary_key=True)
    passWord = db.Column(VARCHAR(20))
    email = db.Column(VARCHAR(30))