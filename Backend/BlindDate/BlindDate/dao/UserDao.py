# -*- coding: utf-8 -*-
from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from model import UserModel
from run import db
import traceback


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
            user = session.query(UserModel).filter(UserModel.id == user_id)
            if not user:
                raise NotFoundException
            return user
        except:
            raise SystemError
        finally:
            session.close()
