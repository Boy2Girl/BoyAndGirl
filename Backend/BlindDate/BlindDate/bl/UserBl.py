from dao.UserDao import UserDao
from exceptions import AlreadyExists
from exceptions import NotFoundException
from exceptions import PasswordWrongException
from factory import DaoFactory
from model import UserModel
from utils.JwtUtil import JwtUtil
from utils.converter import UserConverter
from vo import UserVO


class UserBl(object):
    def __init__(self):
        self.user_dao: UserDao = DaoFactory.userDao

    def sign_up(self, user: UserVO):
        result = self.user_dao.get_user_by_username(user.username)
        if result:
            raise AlreadyExists
        else:
            print(user.__dict__)
            self.user_dao.insert(UserConverter().toModel(user))
            token = JwtUtil.create_token(user.username)
            return token

    def sign_in(self, user: UserVO):
        result: UserModel = self.user_dao.get_user_by_username(user.username)
        if not result:
            raise NotFoundException
        if result.password == user.password:
            """成功登录"""
            token = JwtUtil.create_token(user.username)
            return token, result.id
        else:
            raise PasswordWrongException

    def get_all_user(self):
        model = self.user_dao.get_all_user()
        return [UserConverter().toVO(i).serialize() for i in model]
