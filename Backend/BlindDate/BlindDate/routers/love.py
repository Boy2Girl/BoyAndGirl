from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from factory.BlFactory import poolBl, userInfoBl
from model import PoolModel
from publicdata import Role
from utils import JwtUtil

ns = Namespace('pool/love', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Love(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看全部异性')
    @ns.expect(login_parameters)
    def get(self):
        begin = request.form['begin']
        poolID = request.form['poolID']
        return None

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('对某个异性产生好感')
    @ns.expect(login_parameters)
    def post(self):
        uID = request.form['uID']
        poolID = request.form['poolID']
        username = JwtUtil.JwtUtil.get_token_username(request.headers.get("token"))
        return poolBl.love_some_one(uID, username, poolID)

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('增加交友池')
    def put(self):
        poolID = request.form['poolID']
        createTime = request.form['createTime']
        city = request.form['city']
        realRequired = request.form['realRequired']
        initChance = request.form['initChance']
        removeTime = request.form['removeTime']
        baseCharge = request.form['baseCharge']
        boyBegin = request.form['boyBegin']
        girlBegin = request.form['girlBegin']
        ageIncrement = request.form['ageIncrement']
        sexIncrement = request.form['sexIncrement']
        requirement = request.form['requirementD']

        return poolBl.add_pool(PoolModel(poolID, createTime, city, realRequired, initChance, removeTime,
                                  baseCharge,boyBegin,girlBegin,ageIncrement,sexIncrement,requirement))


@ns.route('/{string:id}')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class LoveID(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看')
    @ns.expect()
    def get(self, id):
        return userInfoBl.get_user_info(id)
