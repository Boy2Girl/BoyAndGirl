from exceptions import NotFoundException
from factory import DaoFactory
from factory.DaoFactory import userDao
from utils.JwtUtil import JwtUtil
from model import ActivityModel, ActivityJoinModel
from utils.converter import ActivityConverter
from vo import ActivityVO


class ActivityBl(object):
    def __init__(self):
        self.activity_dao = DaoFactory.activityDao
        self.activity_join_dao = DaoFactory.activityJoinDao

    def add_activity(self, activity: ActivityVO):
        return self.activity_dao.insert(ActivityConverter().toModel(activity))

    def get_activity_by_id(self, activity_id):
        return ActivityConverter().toVO(self.activity_dao.get_activity(activity_id))

    def get_activity_by_user(self, user_id):
        return self.activity_dao.get_activity_by_user(user_id)

    def get_activity(self, begin, is_old):
        return [ActivityConverter().toVO(i) for i in self.activity_dao.get_activity_list(begin, is_old)]

    def join_activity(self, username, activity_id):
        """还要检查是不是已经报名了"""
        user = userDao.get_user_by_username(username)
        if not user:
            raise NotFoundException
        self.activity_join_dao.getActivityJoin(user.id, activity_id)
        return self.activity_join_dao.insert(ActivityJoinModel(user.id, activity_id))



