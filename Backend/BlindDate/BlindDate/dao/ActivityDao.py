# -*- coding: utf-8 -*-
from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from run import session
from model import ActivityModel, ActivityJoinModel
import traceback
import datetime


class ActivityDao(DaoUtil):

    """根据ID查询"""
    def get_activity(self, activity_id):
        try:
            activity = session.query(ActivityModel).filter(ActivityModel.activityID == activity_id)
            if not activity:
                raise NotFoundException
            return activity
        except:
            traceback.print_exc()

    """获取活动列表"""
    def get_activity_list(self, begin, is_old):
        try:
            activity_list = []
            if is_old:
                activity_list = session.query(ActivityModel).filter(ActivityModel.selectEndTime < datetime.datetime.now())
            else:
                activity_list = session.query(ActivityModel).filter(ActivityModel.selectEndTime <= datetime.datetime.now())
            result = []
            for i in range(8):
                try:
                    result.append(activity_list[begin+i])
                except:
                    pass
            return result
        except:
            raise SystemError

    """获取用户参加过的活动"""
    def get_activity_by_user(self, userID):
        try:
            activity = session.query(ActivityModel).join(ActivityJoinModel).filter(ActivityJoinModel.userID == userID)
            return activity
        except:
            raise SystemError




