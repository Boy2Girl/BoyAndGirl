from exceptions import NotFoundException
from factory import DaoFactory
from factory.DaoFactory import userDao
from utils.converter import UserInfoConverter, UserListConverter
from vo import UserInfoVO


class UserInfoBl(object):
    def __init__(self):
        self.user_info_dao = DaoFactory.userInfoDao

    """这里注意是要审核之后才能添加进去"""

    def add_user_info(self, user_info: UserInfoVO, username):
        user = userDao.get_user_by_username(username)
        user_info.id = user.id
        self.user_info_dao.insert(UserInfoConverter().toModel(user_info))

    def update_user_info(self, user_info: UserInfoVO):
        self.user_info_dao.update_user_info(UserInfoConverter().toModel(user_info))

    """获取用户的审核通过的信息，找不到就是还没有实名认证，这里的接口改了一定要注意"""

    def get_user_info(self, user_id, is_stable):
        model = self.user_info_dao.get_user_info(user_id, is_stable)
        if not model:
            raise NotFoundException
        return UserInfoConverter().toVO(model)

    def get_un_checking_list(self):
        return self.user_info_dao.get_un_checking_list()

    def check_user_info(self, userID, result):
        return self.user_info_dao.check_user_info(userID, result)

    def get_all_user(self):
        model = self.user_info_dao.get_all()
        return [UserListConverter().toVO(i) for i in model]
