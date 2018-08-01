from flask import request
from flask_restplus import Resource, fields, Namespace
from sqlalchemy.exc import IntegrityError

from decorator.RoleRequest import login_require
from exceptions import AlreadyExists, NotFoundException, InsertException
from factory.BlFactory import poolBl
from publicdata import Role
from utils import JwtUtil
from utils.DateEncoder import DateEncoderUtil
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
        begin = request.args['begin']
        result = [DateEncoderUtil().changeDate(i) for i in poolBl.get_pool(begin)]
        return result, 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取我的交友池列表')
    def fetch(self):
        begin = request.args['begin']
        user_id = request.args['userId']
        result = [DateEncoderUtil().changeDate(i) for i in poolBl.get_pool_by_user(begin, user_id)]
        return result, 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('报名进入候选池')
    @ns.expect(pool_parameters)
    def post(self):
        try:
            pID = request.form['pID']
            username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
            poolBl.join_pool(pID, username)
            return None, 200
        except AlreadyExists:
            return None, 403
        except InsertException:
            return None, 404

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('增加交友池')
    def put(self):
        try:
            result = poolBl.add_pool(PoolVO(form=request.form))
            return result, 200
        except InsertException:
            return None, 404


@ns.route('/<string:id>')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class PoolID(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看')
    @ns.expect()
    def get(self, id):
        try:
            return DateEncoderUtil().changeDate(poolBl.get_pool_by_id(id)), 200
        except NotFoundException:
            return None, 404
