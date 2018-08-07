from exceptions import NotFoundException
from factory import DaoFactory
from factory.DaoFactory import userDao
from utils.JwtUtil import JwtUtil
from model import ActivityModel, ActivityJoinModel, PostsModel, RecruitModel
from utils.converter import ActivityConverter, RecruitListConverter, PostsListConverter
from vo import ActivityVO


class PostsBl(object):
    def __init__(self):
        self.posts_dao = DaoFactory.postsDao
        self.recruit_dao = DaoFactory.recruitDao
        self.user_info_dao = DaoFactory.userInfoDao

    def add_posts(self, username, endTime):
        user = userDao.get_user_by_username(username)
        self.posts_dao.get_posts_by_user(user.id)
        return self.posts_dao.insert(PostsModel(user.id, endTime))

    def recruit_someone(self, username, postsID):
        user = userDao.get_user_by_username(username)
        self.recruit_dao.get_recruit(user.id, postsID)
        return self.recruit_dao.insert(RecruitModel(user.id, postsID, False))

    def get_my_posts(self, username):
        user = userDao.get_user_by_username(username)
        posts = self.posts_dao.get_posts_by_user_id(user.id)
        return [PostsListConverter().toVO(i, self.user_info_dao.get_user_info(i.userID)) for i in posts]

    def get_all(self):
        posts = self.posts_dao.get_all()
        return [PostsListConverter().toVO(i, self.user_info_dao.get_user_info(i.userID, True)) for i in posts]

    def get_my(self, username):
        user = userDao.get_user_by_username(username)
        posts = self.posts_dao.get_my(user.id)
        return [PostsListConverter().toVO(i, self.user_info_dao.get_user_info(i.userID)) for i in posts]
