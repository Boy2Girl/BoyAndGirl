from exceptions import NotFoundException
from factory import DaoFactory
from factory.DaoFactory import userDao
from model import PoolJoinModel, LoveRelationModel
from utils.JwtUtil import JwtUtil
from utils.converter import PoolConverter
from vo import PoolVO


class PoolBl(object):
    def __init__(self):
        self.pool_dao = DaoFactory.poolDao
        self.love_relation_dao = DaoFactory.loveRelationDao
        self.pool_join_dao = DaoFactory.poolJoinDao

    def add_pool(self, pool: PoolVO):
        print(pool.__dict__)
        poolModel = PoolConverter().toModel(pool)
        print(poolModel.__dict__)
        self.pool_dao.insert(poolModel)

    def get_pool_by_id(self, pool_id):
        return self.pool_dao.get_pool(pool_id)

    def get_pool(self, begin):
        return self.pool_dao.get_pool_list(begin)

    def get_pool_by_user(self, user_id):
        return self.pool_dao.get_pool_by_user(user_id)

    def join_pool(self, pID, username):
        userID = userDao.get_user_by_username(username)
        self.pool_join_dao.insert(PoolJoinModel(pID, userID))

    def love_some_one(self, uID, username, poolID):
        userID = userDao.get_user_by_username(username)
        self.love_relation_dao.insert(LoveRelationModel(userID, uID, poolID))

    def get_love(self, user_id):
        return self.love_relation_dao.get_true_love(user_id)

    def get_true_love(self, user_id):
        return self.get_true_love(user_id)

