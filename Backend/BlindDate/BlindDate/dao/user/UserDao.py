# -*- coding: utf-8 -*-
from run import session,db
from exceptions import UsernameNotFoundException
from model import UserModel
# import traceback


class UserDao(object):
    def __init__(self):
        pass

    def insert_user(self, user):
        try:
            session.add(user)
            session.commit()
        except:
            print("error")
            # traceback.print_exc()
        finally:
            session.close()

    def get_user_by_username(self, username):
        try:
            user = session.query(UserModel).filter(UserModel.userName == username).one()
            if not user:
                raise UsernameNotFoundException()
            return user
        except:
            raise SystemError()
