from dao.DaoUtil import DaoUtil
from exceptions import AlreadyExists
from run import session,db
from model import UserModel, PoolJoinModel
import traceback


class PoolJoinDao(DaoUtil):

    def getPoolJoin(self, user_id, pool_id):
        try:
            join = session.query(PoolJoinModel).filter(PoolJoinModel.userID == user_id).\
                filter(PoolJoinModel.poolID == pool_id).first()
            print(join)
            return join
        except AlreadyExists:
            raise AlreadyExists
        except:
            raise SystemError
        finally:
            session.close()
