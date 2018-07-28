from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from run import session,db
from model import UserModel, UserInfoModel
import traceback


class UserInfoDao(DaoUtil):

    def get_user_info(self, user_id):
        try:
            user_info = session.query(UserInfoModel).filter(UserInfoModel.userID == user_id)
            if not user_info:
                raise NotFoundException
            return user_info
        except:
            raise SystemError


