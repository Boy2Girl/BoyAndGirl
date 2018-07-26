# -*- coding: utf-8 -*-
from app import Base
from sqlalchemy import Column, Integer, CHAR, VARCHAR


class User(Base):
    __tablename__ = "User"
    userName = Column(VARCHAR(20), primary_key=True)
    passWord = Column(VARCHAR(20))
    email = Column(VARCHAR(30))
