import json

import requests

from dao.UserDao import UserDao
from exceptions import AlreadyExists
from exceptions import NotFoundException
from exceptions import PasswordWrongException
from factory import DaoFactory
from model import UserModel
from utils.JwtUtil import JwtUtil
from utils.converter import UserConverter
from vo import UserVO

appId = 'wxcf058ebab08beee9'
secret = '712f763fd5394d307adb242ca5c158e2'
grant_type = 'authorization_code'
baseUrl = ' https://api.weixin.qq.com/sns/oauth2/access_token'


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

    def get_open_id(self, code, username):
        user = self.user_dao.get_user_by_username(username)
        if not user:
            raise NotFoundException

        if user.openid != None:
            return user.openid

        payload = {'appid': appId, 'secret': secret, 'grant_type': grant_type, 'code': code}
        # payload = {'appid': appId, 'secret': secret, 'grant_type': grant_type, 'code': code}
        # if not user.refresh_token:
        #     if not code:
        #         raise NotFoundException
        #     else:
        #         payload = {'appid': appId, 'secret': secret, 'grant_type': grant_type, 'code': code}
        # else:
        #     payload = {'appid': appId, 'grant_type': 'refresh_token', 'refresh_token': user.refresh_token}

        result = requests.get(baseUrl, params=payload).content
        result_json = json.loads(result)
        try:
            self.user_dao.updateOpenid(user.id, result_json['openid'])
        except KeyError:
            raise NotFoundException

        return result_json['openid']


# UserBl().get_open_id("011Gf3fQ0QImF528JAgQ0npPeQ0Gf3fa", "18851830977")
# DaoFactory.userDao.updateOpenid(1, "111")
#
# user = DaoFactory.userDao.get_user_by_username("13700000126")
# if user.openid != None:
#     print("jjj")