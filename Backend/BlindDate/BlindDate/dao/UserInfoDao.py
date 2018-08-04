from sqlalchemy.exc import IntegrityError

from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException, AlreadyExists
from run import session,db
from model import UserModel, UserInfoModel, CheckingUserInfoModel
import traceback

from utils.converter import UserInfoConverter


class UserInfoDao(DaoUtil):

    def get_user_info(self, user_id, is_stable):
        try:
            if is_stable:
                user_info = session.query(UserInfoModel).filter(UserInfoModel.id == user_id).first()
            else:
                user_info = session.query(CheckingUserInfoModel).filter(CheckingUserInfoModel.id == user_id).first()
            if not user_info:
                raise NotFoundException
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

    def get_un_checking_list(self):
        user_info = [i[0] for i in session.query(CheckingUserInfoModel.id).all()]
        return user_info

    def check_user_info(self, user_id, result):
        if result:
            """把一个数据库中的数据直接拿到另一个数据库中"""
            user_info = session.query(CheckingUserInfoModel).filter(CheckingUserInfoModel.id == user_id).first()
            if not user_info:
                raise NotFoundException
            current_info = session.query(UserInfoModel).filter(UserInfoModel.id == user_id).first()
            if current_info:
                self.delete(current_info)
            self.insert(UserInfoConverter().mockToReal(user_info))
            self.delete(user_info)
            self.session.commit()
        else:
            session.query(CheckingUserInfoModel).filter(CheckingUserInfoModel.id == user_id)\
                .update(dict(isReject=True))
            # user_info.isRejected = True
            self.session.commit()
        user_info = [i[0] for i in session.query(CheckingUserInfoModel.id).all()]
        return user_info
    def get_all(self):
        try:
            user_info = session.query(UserInfoModel).all()
            return user_info
        except:
            traceback.print_exc()



