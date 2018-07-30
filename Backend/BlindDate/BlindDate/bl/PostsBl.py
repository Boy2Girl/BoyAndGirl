from exceptions import NotFoundException
from factory import DaoFactory
from factory.DaoFactory import userDao
from utils.JwtUtil import JwtUtil
from model import ActivityModel, ActivityJoinModel, PostsModel, RecruitModel
from utils.converter import ActivityConverter
from vo import ActivityVO


class PostsBl(object):
    def __init__(self):
        self.posts_dao = DaoFactory.postsDao
        self.recruit_dao = DaoFactory.recruitDao

    def add_posts(self, username, endTime):
        user = userDao.get_user_by_username(username)
        self.posts_dao.get_posts_by_user(user.id)
        return self.posts_dao.insert(PostsModel(user.id, endTime))

    def recruit_someone(self, username, postsID):
        user = userDao.get_user_by_username(username)
        self.recruit_dao.get_recruit(user.id, postsID)
        return self.recruit_dao.insert(RecruitModel(user.id, postsID, False))





