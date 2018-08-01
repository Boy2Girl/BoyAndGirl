from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from publicdata import Role
from utils import JwtUtil

ns = Namespace('check', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Check(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看产生好感的全部异性')
    @ns.expect(login_parameters)
    def post(self):
        try:
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            return username, 200
        except:
            return None, 403

