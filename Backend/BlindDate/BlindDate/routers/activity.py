import flask
from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from exceptions import NotFoundException, SystemErrorException, InsertException, AlreadyExists
from factory import BlFactory
from publicdata import Role
from utils.DateEncoder import DateEncoderUtil
from utils.JwtUtil import JwtUtil
from vo import ActivityVO

ns = Namespace('activity', description='关于活动')

activity_put_parameters = ns.model('ActivityPutParameters', {
    'activityName': fields.String(required=True, description='活动名称'),
    'location': fields.String(required=True, description='密码'),
    'registerBeginTime': fields.Date(required=True, description='注册开始时间'),
    'registerEndTime': fields.Date(required=True, description='注册结束时间'),
    'selectBeginTime': fields.Date(required=True, description='互选开始时间'),
    'selectEndTime': fields.Date(required=True, description='互选结束时间'),
    'chargeRule': fields.String(required=True, description='收费标准'),
    'boyBeginAge': fields.Integer(required=True, description='男生开始收费年龄'),
    'girlBeginAge': fields.Integer(required=True, description='女生开始收费年龄'),
    'increment': fields.Float(required=True, description='根据年龄递增的收费'),
    'wechat': fields.String(required=True, description='发起人微信号'),
    'realName': fields.String(required=True, description='是否需要真实信息')
})
activity_post_parameters = ns.model('ActivityPostParameters', {
    'aID': fields.String(required=True, description='活动的ID')
})
activity_get_parameters = ns.model('ActivityGetParameters', {
    'begin': fields.Integer(required=True, description='开始的编号，分页使用'),
    'isCurrent': fields.Boolean(required=True, description='是否是历史活动')
})

activity_bl = BlFactory.activityBl


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'activity not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Activity(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('增加活动')
    @ns.expect(activity_put_parameters)
    def put(self):
        try:
            result = activity_bl.add_activity(ActivityVO(form=request.form))
            return result, 200
        except InsertException:
            return None, 500

    @login_require(Role.USER)
    @ns.doc('报名参加活动')
    @ns.expect(activity_post_parameters)
    def post(self):
        print(request.form)
        aID = request.form['aID']
        try:
            activity_bl.join_activity(JwtUtil.get_token_username(flask.request.headers.get("token")), aID)
            return None, 200
        except NotFoundException:
            return {"error": "can not find user or activity"}, 404
        except InsertException:
            return {"error": "system is error"}, 500
        except AlreadyExists:
            return {"error": "already exists"}, 405

    @ns.doc('获取活动列表')
    @ns.expect(activity_get_parameters)
    def get(self):
        begin = request.args['begin']
        is_current = request.args['isCurrent']
        try:
            activity_list = activity_bl.get_activity(begin, not is_current)
            return [DateEncoderUtil().changeDate(i) for i in activity_list]
        except NotFoundException:
            return {"error": "can not find the page"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500


@ns.route('/<string:aID>')
@ns.response(200, 'OK')
@ns.response(404, 'activity not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class ActivityAID(Resource):

    @ns.doc('获取某一个特定的活动信息')
    @ns.param(name="aId", description="活动的ID", _in="path")
    def get(self, aID):
        try:
            activity = activity_bl.get_activity_by_id(aID)
            return DateEncoderUtil().changeDate(activity), 200
        except NotFoundException:
            return {"error": "can not find the activity"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500
