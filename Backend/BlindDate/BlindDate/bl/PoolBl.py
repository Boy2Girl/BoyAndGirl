from exceptions import NotFoundException
from factory import DaoFactory
from model import PoolJoinModel, LoveRelationModel
from utils.JwtUtil import JwtUtil


class PoolBl(object):
    def __init__(self):
        self.pool_dao = DaoFactory.poolDao
        self.love_relation_dao = DaoFactory.loveRelationDao
        self.pool_join_dao = DaoFactory.poolJoinDao

    def add_pool(self, pool):
        self.pool_dao.insert(pool)

    def get_pool_by_id(self, pool_id):
        return self.pool_dao.get_pool(pool_id)

    def get_pool(self):
        return self.pool_dao.get_pool_list()

    def get_pool_by_user(self, user_id):
        return self.pool_dao.get_pool_by_user(user_id)

    def join_pool(self, pool_join: PoolJoinModel):
        self.pool_join_dao.insert(pool_join)

    def love_some_one(self, love_relation: LoveRelationModel):
        self.love_relation_dao.insert(love_relation)

    def get_love(self, user_id):
        return self.love_relation_dao.get_true_love(user_id)

    def get_true_love(self, user_id):
        return self.get_true_love(user_id)

