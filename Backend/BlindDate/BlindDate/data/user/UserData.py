# -*- coding: utf-8 -*-
from factory import DaoFactory


class UserData(object):
    def __init__(self):
        self.user_dao = DaoFactory.userDao

    def save_user(self, user):
        self.user_dao.insert_user(user)
