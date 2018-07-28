# -*- coding: utf-8 -*-
from run import session,db
from exceptions import UsernameNotFoundException
from model import UserModel
import traceback


class DaoUtil(object):
    def __init__(self):
        pass

    def insert(self, object):
        try:
            session.add(object)
            session.commit()
        except:
            traceback.print_exc()
        finally:
            session.close()

    def delete(self, object):
        try:
            session.delete(object)
            session.commit()
        except:
            traceback.print_exc()
        finally:
            session.close()

