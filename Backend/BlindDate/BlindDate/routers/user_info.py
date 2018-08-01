import datetime
import json

from flask import request
from flask_restplus import Resource, Namespace

from decorator.RoleRequest import login_require
from exceptions import NotFoundException, AlreadyExists, InsertException
from factory.BlFactory import userInfoBl
from publicdata import Role
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

    # @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('填写')
    def put(self):
        try:
            for i in request.form:
                print(i)
            userInfoBl.add_user_info(UserInfoVO(form=request.form))
            return None, 200, {}
        except InsertException:
            return None, 404

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('更新')
    def post(self):
        try:
            userInfoBl.update_user_info(UserInfoVO(form=request.form))
            return None, 200, {}
        except AlreadyExists:
            return None, 403
        except NotFoundException:
            return None, 404


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
        try:
            result = userInfoBl.get_user_info(id)
            result1 = DateEncoderUtil().changeDate(result)
            return result1, 200
        except NotFoundException:
            return None, 404


