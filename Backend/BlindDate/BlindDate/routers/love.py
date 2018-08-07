from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from exceptions import AlreadyExists, InsertException
from factory.BlFactory import poolBl, userInfoBl
from model import PoolModel
from publicdata import Role
from utils import JwtUtil

ns = Namespace('pool/love', description='关于用户')

# login_parameters = ns.model('LoginParameters', {
#     'username': fields.String(required=True, description='用户名'),
#     'password': fields.String(required=True, description='密码')
# })

list_parser = ns.parser()
list_parser.add_argument('begin', type=str, help='开始编号', location='form')
list_parser.add_argument('poolID', type=str, help='交友池编号', location='form')
list_parser.add_argument('truth', type=str, help='是否是真爱', location='form')

put_parser = ns.parser()
put_parser.add_argument('begin', type=str, help='开始编号', location='form')
put_parser.add_argument('poolID', type=str, help='交友池编号', location='form')
# put_parser.add_argument('truth', type=str, help='是否是真爱', location='form')



@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Love(Resource):

    @ns.doc('查看产生好感的全部异性')
    @ns.expect(list_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def post(self):
        poolID = request.form['poolID']
        truth = request.form['truth'] == 'True'
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        if not truth:
            return poolBl.get_love(username, poolID)
        else:
            return poolBl.get_true_love(username, poolID)

    @ns.doc('对某个异性产生好感')
    @ns.expect(put_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def put(self):
        try:
            uID = request.form['uID']
            poolID = request.form['poolID']
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            return poolBl.love_some_one(uID, username, poolID)
        except AlreadyExists:
            return None, 403
        except InsertException:
            """用户或者候选池不存在"""
            return None, 404
