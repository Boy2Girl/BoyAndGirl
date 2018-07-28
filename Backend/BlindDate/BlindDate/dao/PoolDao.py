from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from run import session,db
from model import UserModel, PoolModel, PoolJoinModel
import traceback


class PoolDao(DaoUtil):

    def get_pool_list(self):
        try:
            pools = session.query(PoolModel)
            return pools
        except:
            raise SystemError

    def get_pool(self, pool_id):
        try:
            pool = session.query(PoolModel).filter(PoolModel.poolID == pool_id)
            if not pool:
                raise NotFoundException
            return pool
        except:
            raise SystemError

    def get_pool_by_user(self, user_id):
        try:
            pools = session.query(PoolModel).join(PoolJoinModel).filter(PoolJoinModel.userID == user_id)
            return pool
        except:
            raise SystemError

