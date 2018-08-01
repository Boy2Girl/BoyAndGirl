from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from exceptions import AlreadyExists, InsertException
from factory.BlFactory import postsBl, userInfoBl
from model import PoolModel
from publicdata import Role
from utils import JwtUtil
from utils.DateEncoder import DateEncoderUtil

ns = Namespace('posts', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Posts(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('应征某个发帖')
    @ns.expect(login_parameters)
    def post(self):
        try:
            postsID = request.form['postsID']
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            return postsBl.recruit_someone(username, postsID), 200
        except AlreadyExists:
            return None, 405
        except InsertException:
            return None, 404

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('我的应征')
    @ns.expect()
    def patch(self):
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        return [DateEncoderUtil().changeDate(i) for i in postsBl.get_my_posts(username)], 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取全部应征')
    @ns.expect()
    def get(self):
        # username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        return [DateEncoderUtil().changeDate(i) for i in postsBl.get_all()], 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取全部应征')
    @ns.expect()
    def delete(self):
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        return [DateEncoderUtil().changeDate(i) for i in postsBl.get_my(username)], 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('创建一个发帖应征')
    @ns.expect(login_parameters)
    def put(self):
        try:
            endTime = request.form['endTime']
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            return postsBl.add_posts(username, endTime)
        except AlreadyExists:
            return None, 403
        except InsertException:
            """用户或者候选池不存在"""
            return None, 404
