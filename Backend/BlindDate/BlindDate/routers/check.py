import traceback

from flask import request
from flask_restplus import Resource, Namespace

from decorator.RoleRequest import login_require
from exceptions import NotFoundException
from factory import DaoFactory
from publicdata import Role
from utils import JwtUtil

ns = Namespace('check', description='检查用户登录状态')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Check(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看用户是否实名登录以及返回用户的角色信息身份')
    def post(self):
        try:
            userDao = DaoFactory.userDao
            userInfoDao = DaoFactory.userInfoDao
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            user = userDao.get_user_by_username(username)
            try:
                userInfoDao.get_user_info(user.id, True)
                isReal = True
            except NotFoundException:
                isReal = False
            return {'role': str(user.role).split('.')[1], 'isReal': isReal}, 200
        except:
            return None, 403

    @login_require(Role.ADMIN)
    @ns.doc('更新用户的权限')
    def patch(self):
        try:
            userID = request.form['userID']
            increase = request.form['increase'] == 'true'
            userDao = DaoFactory.userDao
            user = userDao.get_user_by_id(userID)
            print(user.role)
            print(increase)
            if not user:
                return None, 404
            if user.role == Role.USER and increase:
                userDao.updateUserRole(userID, Role.PUBLISHER)
            elif user.role == Role.PUBLISHER and not increase:
                userDao.updateUserRole(userID, Role.USER)
            else:
                return None, 403
            return None, 200
        except:
            traceback.print_exc()
            return None, 403
