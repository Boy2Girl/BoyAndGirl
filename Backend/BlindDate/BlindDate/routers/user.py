from flask import request
from flask_restplus import Resource, fields, Namespace

from exceptions import PasswordWrongException, NotFoundException, AlreadyExists, InsertException
from factory.BlFactory import userBl
from vo import UserVO

ns = Namespace('user', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
    'role': fields.String(required=True, description='角色')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class User(Resource):

    @ns.doc('登录')
    # @ns.expect(login_parameters)
    def post(self):
        try:
            print(request.form)
            token, user_id = userBl.sign_in(UserVO(form=request.form))
            print(token)
            return {'token': token, "id": user_id}, 200
        except PasswordWrongException:
            return None, 403
        except NotFoundException:
            return None, 404

    @ns.doc('注册')
    def put(self):
        try:
            token = userBl.sign_up(UserVO(form=request.form))
            return {'token': token}, 200
        except AlreadyExists:
            return None, 405
