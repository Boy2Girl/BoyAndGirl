from dao.UserDao import UserDao
from exceptions import PasswordWrongException
from exceptions import NotFoundException
from exceptions import UserAlreadyExists
from factory import DaoFactory
from utils.JwtUtil import JwtUtil
from model import UserModel


class UserBl(object):
    def __init__(self):
        self.user_dao: UserDao = DaoFactory.userDao

    def sign_up(self, user: UserModel):
        result = self.user_dao.get_user_by_username(user.username)
        if result:
            raise UserAlreadyExists
        else:
            self.user_dao.insert(user)
            token = JwtUtil.create_token(user.username)
            return token

    def sign_in(self, user: UserModel):
        try:
            result: UserModel = self.user_dao.get_user_by_username(user.username)
            if result.password == user.password:
                """成功登录"""
                token = JwtUtil.create_token(user.username)
                return token
            else:
                raise PasswordWrongException
        except:
            raise NotFoundException
