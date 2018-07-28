from exceptions import NotFoundException
from factory import DaoFactory
from utils.JwtUtil import JwtUtil
from model import ActivityModel, ActivityJoinModel


class ActivityBl(object):
    def __init__(self):
        self.activity_dao = DaoFactory.activityDao
        self.activity_join_dao = DaoFactory.ActivityJoinDao

    def add_activity(self, activity: ActivityModel):
        self.activity_dao.insert(activity)

    def get_activity_by_id(self, activity_id):
        return self.activity_dao.get_activity(activity_id)

    def get_activity_by_user(self, user_id):
        return self.activity_dao.get_activity_by_user(user_id)

    def get_activity(self, begin, is_old):
        return self.get_activity(begin, is_old)

    def join_activity(self, activity_join:ActivityJoinModel):
        self.activity_join_dao.insert(activity_join)


