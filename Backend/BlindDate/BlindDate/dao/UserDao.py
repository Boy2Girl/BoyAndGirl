# -*- coding: utf-8 -*-
<<<<<<< HEAD:Backend/BlindDate/BlindDate/dao/UserDao.py
from dao.DaoUtil import DaoUtil
from run import session,db
from exceptions import NotFoundException
=======
import traceback

from exceptions import UsernameNotFoundException
>>>>>>> 835291a3b8298c8d3bfaa030458bd7c5a1e33caa:Backend/BlindDate/BlindDate/dao/user/UserDao.py
from model import UserModel
from run import db


class UserDao(DaoUtil):

    def get_user_by_username(self, username):
        try:
<<<<<<< HEAD:Backend/BlindDate/BlindDate/dao/UserDao.py
            user = session.query(UserModel).filter(UserModel.username == username)
            if not user:
                raise NotFoundException
            return user
=======
            session = db.session()
            session.add(user)
            session.commit()
>>>>>>> 835291a3b8298c8d3bfaa030458bd7c5a1e33caa:Backend/BlindDate/BlindDate/dao/user/UserDao.py
        except:
            traceback.print_exc()

    def get_user_by_id(self, user_id):
        try:
<<<<<<< HEAD:Backend/BlindDate/BlindDate/dao/UserDao.py
            user = session.query(UserModel).filter(UserModel.userID == user_id)
            if not user:
                raise NotFoundException
=======
            session = db.session()
            user = session.query(UserModel).filter(UserModel.username == username).first()
            if not user:
                raise UsernameNotFoundException
>>>>>>> 835291a3b8298c8d3bfaa030458bd7c5a1e33caa:Backend/BlindDate/BlindDate/dao/user/UserDao.py
            return user
        except:
            traceback.print_exc()
        finally:
            session.close()
