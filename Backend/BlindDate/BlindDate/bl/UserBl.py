from dao.UserDao import UserDao
from exceptions import PasswordWrongException
from exceptions import NotFoundException
from exceptions import UserAlreadyExists
from factory import DaoFactory
from utils.JwtUtil import JwtUtil
from model import UserModel
from utils.converter import UserConverter
from vo import UserVO


class UserBl(object):
    def __init__(self):
        self.user_dao: UserDao = DaoFactory.userDao

    def sign_up(self, user: UserVO):
        result = self.user_dao.get_user_by_username(user.username)
        if result:
            raise UserAlreadyExists
        else:
            self.user_dao.insert(UserConverter().toModel(user))
            token = JwtUtil.create_token(user.username)
            return token

    def sign_in(self, user: UserVO):
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
