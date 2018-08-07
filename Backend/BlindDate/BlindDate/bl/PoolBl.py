from exceptions import NotFoundException, AlreadyExists
from factory import DaoFactory
from factory.DaoFactory import userDao
from model import PoolJoinModel, LoveRelationModel
from utils.JwtUtil import JwtUtil
from utils.converter import PoolConverter, PoolListConverter
from vo import PoolVO


class PoolBl(object):
    def __init__(self):
        self.pool_dao = DaoFactory.poolDao
        self.love_relation_dao = DaoFactory.loveRelationDao
        self.pool_join_dao = DaoFactory.poolJoinDao

    """暂时不检查重复插入的问题，所有的都允许插入"""
    def add_pool(self, pool: PoolVO):
        poolModel = PoolConverter().toModel(pool)
        return self.pool_dao.insert(poolModel)

    def get_pool_by_id(self, pool_id):
        return PoolConverter().toVO(self.pool_dao.get_pool(pool_id))

    def get_pool(self, begin):
        return [PoolListConverter().toVO(i) for i in self.pool_dao.get_pool_list(begin)]

    def get_pool_by_user(self, username):
        user = userDao.get_user_by_username(username)
        print("get my")
        return [PoolListConverter().toVO(i) for i in self.pool_dao.get_pool_by_user(user.id)]

    def join_pool(self, pID, username):
        """ 先检查有没有参加过　"""
        print(str(pID)+" "+str(username))
        user = userDao.get_user_by_username(username)
        result = self.pool_join_dao.getPoolJoin(user.id, pID)
        print(result)
        if result:
            raise AlreadyExists
        self.pool_join_dao.insert(PoolJoinModel(pID, user.id))

    def love_some_one(self, uID, username, poolID):
        """还是要看是不是已经关注过了，在这个互选池中"""
        """ todo: 还要做异性的检查... """
        user = userDao.get_user_by_username(username)
        try:
            self.love_relation_dao.get_relation(user.id, uID, poolID)
        except AlreadyExists:
            raise AlreadyExists
        self.love_relation_dao.insert(LoveRelationModel(user.id, uID, poolID))

    def get_love(self, username, pool_id):
        user = userDao.get_user_by_username(username)
        return self.love_relation_dao.get_your_love(user.id, pool_id)

    def get_true_love(self, username, pool_id):
        user = userDao.get_user_by_username(username)
        return self.love_relation_dao.get_true_love(user.id, pool_id)

    def check_register(self, username, pID):
        print(str(pID) + " " + str(username))
        user = userDao.get_user_by_username(username)
        print(str(pID) + " " + str(user.id))
        result = self.pool_join_dao.getPoolJoin(user.id, pID)
        print(result)
        if not result:
            raise NotFoundException
        return result

    def get_people_in_pool(self, pID):
        # print(str(pID) + " " + str(username))
        # user = userDao.get_user_by_username(username)
        # print(str(pID) + " " + str(user.id))
        # result = self.pool_join_dao.getPoolJoin(user.id, pID)
        # print(result)
        # if not result:
        #     raise NotFoundException
        # return result
        pass

