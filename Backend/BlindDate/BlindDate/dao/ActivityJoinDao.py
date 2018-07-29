from dao.DaoUtil import DaoUtil
from exceptions import AlreadyExists
from model import ActivityJoinModel
from run import session,db


class ActivityJoinDao(DaoUtil):

    def getActivityJoin(self, user_id, activity_id):
        try:
            join = session.query(ActivityJoinModel).filter(ActivityJoinModel.userID == user_id). \
                filter(ActivityJoinModel.activityID == activity_id).first()
            if join:
                raise AlreadyExists
        except AlreadyExists:
            raise AlreadyExists
        except:
            raise SystemError

    pass
