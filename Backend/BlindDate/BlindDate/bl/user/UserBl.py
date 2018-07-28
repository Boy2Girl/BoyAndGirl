from exceptions.UsernameNotFoundException import UsernameNotFoundException
from factory import DaoFactory
from utils.JwtUtil import JwtUtil
from model import UserModel


class UserBl(object):
    def __init__(self):
        self.user_dao = DaoFactory.userDao

    def save_user(self, user: UserModel):
        self.user_dao.insert_user(user)
        token = JwtUtil.create_token(user.username)
        return token

    def check_user(self, user: UserModel):
        try:
            self.user_dao.get_user_by_username(user.username)
            return "success"
        except:
            return "not found"
