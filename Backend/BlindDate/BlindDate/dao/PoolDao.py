from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from run import session,db
from model import UserModel, PoolModel, PoolJoinModel


class PoolDao(DaoUtil):

    def get_pool_list(self, begin):
        try:
            pools = session.query(PoolModel).all()
            return pools
        except:
            raise SystemError

    def get_pool(self, pool_id):
        try:
            pool = session.query(PoolModel).filter(PoolModel.id == pool_id).first()
            if not pool:
                raise NotFoundException
            return pool
        except NotFoundException:
            raise NotFoundException
        except:
            raise SystemError


    def get_pool_by_user(self, user_id):
        try:
            pools = session.query(PoolModel).join(PoolJoinModel).filter(PoolJoinModel.userID == user_id)
            return pools
        except:
            raise SystemError

