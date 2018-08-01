from sqlalchemy.exc import IntegrityError

from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException, AlreadyExists
from run import session,db
from model import UserModel, UserInfoModel
import traceback


class UserInfoDao(DaoUtil):

    def get_user_info(self, user_id):
        try:
            user_info = session.query(UserInfoModel).filter(UserInfoModel.id == user_id).first()
            return user_info
        except NotFoundException:
            raise NotFoundException
        except:
            traceback.print_exc()

    def update_user_info(self, userInfoModel: UserInfoModel):
        try:
            self.session = db.session
            user_info: UserInfoModel = session.query(UserInfoModel).filter(UserInfoModel.userID == userInfoModel.userID).first()
            """先设置成删除然后去增加的，后面再修改"""
            if not user_info:
                raise NotFoundException
            print(user_info.__dict__)
            print(userInfoModel.__dict__)
            self.delete(user_info)
            session.add(userInfoModel)
            session.commit()
        except NotFoundException:
            raise NotFoundException
        except IntegrityError:
            raise AlreadyExists
        finally:
            session.close()

    def get_all(self):
        try:
            user_info = session.query(UserInfoModel).all()
            return user_info
        except:
            traceback.print_exc()



