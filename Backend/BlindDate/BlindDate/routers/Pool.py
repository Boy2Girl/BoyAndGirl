from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from factory.BlFactory import poolBl
from publicdata import Role
from utils import JwtUtil
from vo import PoolVO

ns = Namespace('pool', description='关于用户')

pool_parameters = ns.model('LoginParameters', {
    'poolID': fields.Integer(required=True, description='用户名'),
    'createTime': fields.Date(required=True, description='密码'),
    'city': fields.String(required=True, description='密码'),
    'realRequired': fields.Boolean(required=True, description='密码'),
    'initChance': fields.Integer(required=True, description='密码'),
    'removeTime': fields.Date(required=True, description='密码'),
    'baseCharge': fields.Integer(required=True, description='密码'),
    'boyBegin': fields.Integer(required=True, description='密码'),
    'girlBegin': fields.Integer(required=True, description='密码'),
    'ageIncrement': fields.Float(required=True, description='密码'),
    'sexIncrement': fields.Float(required=True, description='密码'),
    'requirement': fields.Boolean(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Pool(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取交友池列表')
    def get(self):
        begin = request.form['begin']
        return poolBl.get_pool(begin)

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('报名进入候选池')
    @ns.expect(pool_parameters)
    def post(self):
        pID = request.form['pID']
        print(request.headers.get("token"))
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        return poolBl.join_pool(pID, username)

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('增加交友池')
    def put(self):
        poolBl.add_pool(PoolVO(form=request.form))
        return None, 200


@ns.route('/{string:id}')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class PoolID(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看')
    @ns.expect()
    def get(self, id):
        return poolBl.get_pool_by_id(id)
