from flask import request
from flask_restplus import Resource, fields, Namespace
from sqlalchemy.exc import IntegrityError

from decorator.RoleRequest import login_require
from exceptions import AlreadyExists, NotFoundException, InsertException
from factory.BlFactory import poolBl
from factory.DaoFactory import userDao, poolJoinDao
from publicdata import Role
from utils import JwtUtil
from utils.DateEncoder import DateEncoderUtil
from vo import PoolVO

ns = Namespace('pool', description='关于交友池')

pool_parameters = ns.model('PoolParameters', {
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

login_parser = ns.parser()
login_parser.add_argument('createTime', type=str, help='创建时间', location='form')
# self.createTime = form['createTime']
login_parser.add_argument('city', type=str, help='所在城市', location='form')
# self.city = form['city']
login_parser.add_argument('url', type=str, help='交友池照片', location='form')
# self.url = form['url']
login_parser.add_argument('name', type=str, help='交友池名称', location='form')
# self.name = form['name']
login_parser.add_argument('requirement', type=str, help='加入要求', location='form')
# self.requirement = form['requirement']
login_parser.add_argument('detail', type=str, help='细节', location='form')
# self.detail = form['detail']

get_parser = ns.parser()
get_parser.add_argument('pID', type=str, help='交友池的ID', location='form')

list_parser = ns.parser()
list_parser.add_argument('begin', type=str, help='开始编号', location='form')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Pool(Resource):

    @ns.doc('获取交友池列表')
    @ns.expect(list_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def get(self):
        begin = request.args['begin']
        result = [DateEncoderUtil().changeDate(i) for i in poolBl.get_pool(begin)]
        return result, 200

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取我的交友池列表')
    def patch(self):
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        result = [DateEncoderUtil().changeDate(i) for i in poolBl.get_pool_by_user(username)]
        print(result)
        return result

    @ns.doc('报名进入候选池')
    @ns.expect(get_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
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

    @ns.expect(login_parser)
    @ns.doc('增加交友池')
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
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

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('判断是不是报名了')
    @ns.expect()
    def post(self, id):
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        user = userDao.get_user_by_username(username)
        result = poolJoinDao.getPoolJoin(user.id, id)
        if result:
            return None, 200
        else:
            return None, 404

