from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from factory.BlFactory import user_bl
from model import UserModel
from publicdata import Role, role_dict

ns = Namespace('user', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class User(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER)
    @ns.doc('登录')
    @ns.expect(login_parameters)
    def post(self):
        username = request.form['username']
        password = request.form['password']
        return 200, {}

    @ns.doc('注册')
    def put(self):
        # TestModel("law")
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        token = user_bl.sign_up(UserModel(username, password, role_dict[role]))
        return {'token': token}, 200
