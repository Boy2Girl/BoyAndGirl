# -*- coding: utf-8 -*-
from app import session
from app.exceptions.UsernameNotFoundException import UsernameNotFoundException
from app.model.User import User


class UserDao(object):
    def __init__(self):
        pass

    def insert_user(self, user):
        try:
            session.add(user)
            session.commit()
        except:
            raise SystemError()
        finally:
            session.close()

    def get_user_by_username(self, username):
        try:
            user = session.query(User).filter(User.userName == username).one()
            if not user:
                raise UsernameNotFoundException()
            return user
        except:
            raise SystemError()
