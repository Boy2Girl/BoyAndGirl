import datetime
import json

from flask import request
from flask_restplus import Resource, Namespace

from decorator.RoleRequest import login_require
from factory.BlFactory import userInfoBl
from model import UserInfoModel
from publicdata import Role
from utils import DateEncoder
from utils.DateEncoder import DateEncoderUtil
from vo import UserInfoVO

ns = Namespace('user/info', description='关于用户信息')


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class UserInfo(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('填写')
    def put(self):
        userInfoBl.add_user_info(UserInfoVO(form=request.form))
        return None, 200, {}

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('更新')
    def post(self):
        userInfoBl.update_user_info(UserInfoVO(form=request.form))
        return None, 200, {}


@ns.route('/<string:id>')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class UserInfoID(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看')
    @ns.expect()
    def get(self, id):
        result = userInfoBl.get_user_info(id)
        result1 = DateEncoderUtil().changeDate(result)
        print(result1)
        return result1, 200


