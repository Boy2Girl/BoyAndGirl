# -*- coding: utf-8 -*-
from run import db
import traceback


class DaoUtil(object):
    def __init__(self):
        pass

    def insert(self, object):
        try:
            session = db.session
            session.add(object)
            session.commit()
        except:
            traceback.print_exc()


    def delete(self, object):
        try:
            session = db.session
            session.delete(object)
            session.commit()
        except:
            traceback.print_exc()
        finally:
            session.close()

