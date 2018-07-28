# -*- coding: utf-8 -*-
from dao.DaoUtil import DaoUtil
from run import session,db
from exceptions import NotFoundException
from model import UserModel
import traceback


class UserDao(DaoUtil):

    def get_user_by_username(self, username):
        try:
            user = session.query(UserModel).filter(UserModel.username == username)
            if not user:
                raise NotFoundException
            return user
        except:
            traceback.print_exc()

    def get_user_by_id(self, user_id):
        try:
            user = session.query(UserModel).filter(UserModel.userID == user_id)
            if not user:
                raise NotFoundException
            return user
        except:
            traceback.print_exc()
