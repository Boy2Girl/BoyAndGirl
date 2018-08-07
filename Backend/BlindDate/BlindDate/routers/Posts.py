from flask import request
from flask_restplus import Resource, Namespace

from decorator.RoleRequest import login_require
from exceptions import AlreadyExists, InsertException
from factory.BlFactory import postsBl
from publicdata import Role
from utils import JwtUtil
from utils.DateEncoder import DateEncoderUtil

ns = Namespace('posts', description='关于发帖')

get_parser = ns.parser()
get_parser.add_argument('postsID', type=str, help='帖子id', location='form')

list_parser = ns.parser()
list_parser.add_argument('userId', type=str, help='用户id', location='form')

end_parser = ns.parser()
end_parser.add_argument('endTime', type=str, help='结束时间', location='form')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Posts(Resource):

    @ns.doc('应征某个发帖')
    @ns.expect(get_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def post(self):
        try:
            userID = request.form['postsID']
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            return postsBl.recruit_someone(username, userID), 200
        except AlreadyExists:
            return None, 405
        except InsertException:
            return None, 404
        except SystemError:
            return None, 500

    @ns.doc('我的应征')
    @ns.expect(list_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def fetch(self):
        try:
            user_id = request.form['userId']
            return postsBl.get_my_posts(user_id), 200
        except SystemError:
            return None, 500

    @ns.doc('创建一个发帖应征')
    @ns.expect(end_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
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
        except SystemError:
            return None, 500

    @ns.doc('获得发帖应征')
    @ns.expect(list_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def get(self):
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        type = request.args['type']
        if type == 'all':
            id = request.args['id']
            return [DateEncoderUtil().changeDate(i) for i in postsBl.get_all()], 200
        elif type == 'myPost':
            id = request.args['id']
            return [DateEncoderUtil().changeDate(i) for i in postsBl.get_my_posts(username)], 200
        elif type == 'postMy':
            id = request.args['id']
            return [DateEncoderUtil().changeDate(i) for i in postsBl.get_my(username)], 200
