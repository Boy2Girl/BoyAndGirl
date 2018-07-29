from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException
from run import session,db
from model import UserModel, UserInfoModel
import traceback


class UserInfoDao(DaoUtil):

    def get_user_info(self, user_id):
        try:
            user_info = session.query(UserInfoModel).filter(UserInfoModel.userID == user_id).first()
            return user_info
        except:
            traceback.print_exc()
            raise SystemError

    def update_user_info(self, userInfoModel: UserInfoModel):
        try:
            user_info: UserInfoModel = session.query(UserInfoModel).filter(UserInfoModel.userID == userInfoModel.userID).first()
            """先设置成删除然后去增加的，后面再修改"""
            session.delete(user_info)
            session.add(userInfoModel)
            session.commit()
        except:
            traceback.print_exc()
            raise SystemError



