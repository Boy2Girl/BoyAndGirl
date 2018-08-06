# -*- coding: utf-8 -*-
import traceback

from dao.DaoUtil import DaoUtil
from model import UserModel
from run import db


class UserDao(DaoUtil):

    def get_user_by_username(self, username):
        try:
            session = db.session
            user = session.query(UserModel).filter(UserModel.username == username).first()
            return user
        except:
            traceback.print_exc()
            raise SystemError

    def get_user_by_id(self, user_id):
        try:
            session = db.session
            user = session.query(UserModel).filter(UserModel.id == user_id).first()
            return user
        except:
            raise SystemError

    def updateUserRole(self, user_id, user_role):
        try:
            session = db.session
            session.query(UserModel).filter(UserModel.id == user_id).update(dict(role=user_role))
            session.commit()
        except:
            raise SystemError

    def get_all_user(self):
        try:
            session = db.session
            user_list = session.query(UserModel).all()
            return user_list
        except:
            raise SystemError
