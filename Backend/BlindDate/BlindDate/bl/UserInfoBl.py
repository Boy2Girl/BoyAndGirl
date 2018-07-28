from exceptions.UsernameNotFoundException import UsernameNotFoundException
from factory import DaoFactory
from model import UserInfoModel
from utils.JwtUtil import JwtUtil


class UserInfoBl(object):
    def __init__(self):
        self.user_info_dao = DaoFactory.userInfoDao

    def add_user_info(self, user_info:UserInfoModel):
        self.user_info_dao.insert(user_info)

    def get_user_info(self, user_id):
        self.user_info_dao.get_user_info(user_id)

