from factory import DataFactory
from utils.JwtUtil import JwtUtil
from model import UserModel


class UserBl(object):
    def __init__(self):
        self.user_data = DataFactory.userData

    def save_user(self, user: UserModel):
        self.user_data.save_user(user)
        token = JwtUtil.create_token(user.userName)
        return token
