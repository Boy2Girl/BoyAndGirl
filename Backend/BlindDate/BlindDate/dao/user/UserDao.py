# -*- coding: utf-8 -*-
import traceback

from exceptions import UsernameNotFoundException
from model import UserModel
from run import db


class UserDao(object):
    def __init__(self):
        pass

    def insert_user(self, user):
        try:
            session = db.session()
            session.add(user)
            session.commit()
        except:
            print("error")
            traceback.print_exc()
        finally:
            session.close()

    def get_user_by_username(self, username):
        try:
            session = db.session()
            user = session.query(UserModel).filter(UserModel.username == username).first()
            if not user:
                raise UsernameNotFoundException
            return user
        except:
            traceback.print_exc()
        finally:
            session.close()
