from app.factory import BlFactory, DataFactory
from app.utils.JwtUtil import JwtUtil


class UserBl(object):
    def __init__(self):
        self.user_data = DataFactory.userData

    def save_user(self, user):
        self.user_data.save_user(user)
        token = JwtUtil.create_token(user.userName)
        return token
