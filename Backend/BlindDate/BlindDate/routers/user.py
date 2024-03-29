import flask
from flask import request
from flask_restplus import Resource, fields, Namespace

from exceptions import PasswordWrongException, NotFoundException, AlreadyExists
from factory.BlFactory import userBl
from utils.JwtUtil import JwtUtil
from vo import UserVO


ns = Namespace('user', description='关于用户（登录注册）')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码'),
    'role': fields.String(required=True, description='角色')
})

login_parser = ns.parser()
login_parser.add_argument('username', type=str, help='用户名', location='form')
login_parser.add_argument('password', type=str, help='密码', location='form')
login_parser.add_argument('role', type=str, help='角色', location='form')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, '没有找到用户名或者密码')
@ns.response(403, '用户名或者密码不正确')
@ns.response(500, '内部错误')
class User(Resource):

    @ns.doc(decription="登录")
    @ns.expect(login_parser)
    def post(self):
        try:
            print(request.form)
            token, user_id = userBl.sign_in(UserVO(form=request.form))
            print(token)
            return {'token': token, "id": user_id}, 200
        except PasswordWrongException:
            return {'error': 'wrong password'}, 403
        except NotFoundException:
            return {'error': 'user not found'}, 404

    # @ns.marshal_with(login_parameters)
    @ns.doc('注册')
    @ns.expect(login_parser)
    def put(self):
        try:
            token = userBl.sign_up(UserVO(form=request.form))
            return {'token': token}, 200
        except AlreadyExists:
            return None, 405

    @ns.doc('获取用户列表')
    def get(self):
        try:
            return userBl.get_all_user(), 200
        except AlreadyExists:
            return None, 405


@ns.route('/<string:aID>')
@ns.response(200, 'OK')
@ns.response(404, '没有找到用户名或者密码')
@ns.response(403, '用户名或者密码不正确')
@ns.response(500, '内部错误')
class User(Resource):
    @ns.doc('获取access_token 和 open_id')
    def get(self, code):
        try:
            username = JwtUtil.get_token_username(flask.request.headers.get("token"))
        except:
            return "token_error", 403
        print("here")
        try:
            return userBl.get_open_id(code, username)
        except NotFoundException:
            return None, 404

# print(requests.get("http://www.injusalon.com:5000/api/user").content)