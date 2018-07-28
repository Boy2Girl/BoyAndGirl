from dao.DaoUtil import DaoUtil
from run import session,db
from model import UserModel, WatchInfoModel
import traceback


class WatchInfoDao(DaoUtil):

    def get_watch_info(self, activity_id):
        try:
            watch_info = session.query(WatchInfoModel.times).filter(WatchInfoModel.activityID == activity_id)
            return watch_info
        except:
            raise SystemError

    def add_watch_info(self, activity_id):
        try:
            session.query(WatchInfoModel.times).filter(WatchInfoModel.activityID == activity_id).\
                update({WatchInfoModel.times: WatchInfoModel.times+1})
            return "success"
        except:
            raise SystemError
