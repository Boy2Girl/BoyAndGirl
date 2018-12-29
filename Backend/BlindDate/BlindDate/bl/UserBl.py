from dao.UserDao import UserDao
from exceptions import AlreadyExists
from exceptions import NotFoundException
from exceptions import PasswordWrongException
from factory import DaoFactory
from model import UserModel
from utils.JwtUtil import JwtUtil
from utils.converter import UserConverter
from vo import UserVO
import requests
import json

appId = ''
secret = ''
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
        payload = {}
        user = UserDao.get_user_by_username(username)
        if not user:
            raise NotFoundException

        if not user.refresh_token:
            if not code:
                raise NotFoundException
            else:
                payload = {'appid': appId, 'secret': secret, 'grant_type': grant_type, 'code': code}
        else:
            payload = {'appid': appId, 'grant_type': 'refresh_token', 'refresh_token': user.refresh_token}

        result = requests.get(baseUrl, params=payload).content
        result_json = json.load(result)
        if not result_json['openid']:
            raise NotFoundException
        else:
            UserDao.updateUserRefreshToken(user.id, result_json['refresh_token'])
        return result_json['openid']



