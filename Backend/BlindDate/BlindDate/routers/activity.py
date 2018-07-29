import flask
from flask import request
from flask_restplus import Resource, fields, Namespace

from decorator.RoleRequest import login_require
from exceptions import NotFoundException, SystemErrorException
from factory import BlFactory
from publicdata import Role
from utils.JwtUtil import JwtUtil

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

activity_bl = BlFactory.activity_bl


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'activity not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Activity(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER)
    @ns.doc('增加活动')
    @ns.expect(activity_put_parameters)
    def put(self):
        activity = {}
        activity.activityName = request.data['activityName']
        activity.location = request.data['location']
        activity.registerBeginTime = request.data['registerBeginTime']
        activity.registerEndTime = request.data['registerEndTime']
        activity.selectBeginTime = request.data['selectBeginTime']
        activity.selectEndTime = request.data['selectEndTime']
        activity.chargeRule = request.data['chargeRule']
        activity.boyBeginAge = request.data['boyBeginAge']
        activity.girlBeginAge = request.data['girlBeginAge']
        activity.increment = request.data['increment']
        activity.wechat = request.data['wechat']
        activity.realName = request.data['realName']
        try:
            activity_bl.add_activity(activity)
        except SystemErrorException:
            return {"error": "system is error"}, 500
        return {"success": "success"}, 201

    @login_require(Role.USER)
    @ns.doc('报名参加活动')
    @ns.expect(activity_post_parameters)
    def post(self):
        aID = request.data['aID']
        try:
            activity_bl.join_activity(JwtUtil.get_token_username(flask.request.headers.get("token")), aID)
        except NotFoundException:
            return {"error": "can not find user or activity"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500
        return {'success': 'success'}, 200

    @ns.doc('获取活动列表')
    @ns.expect(activity_get_parameters)
    def get(self):
        begin = request.data['begin']
        is_current = request.data['isCurrent']
        try:
            activity_list = activity_bl.get_activity(begin, is_current)
        except NotFoundException:
            return {"error": "can not find the page"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500
        return {"list": activity_list}, 200


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
        except NotFoundException:
            return {"error": "can not find the activity"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500
        return {"activity": activity}, 200
