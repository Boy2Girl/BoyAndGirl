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
login_parser = ns.parser()
login_parser.add_argument('url', type=str, help='活动的照片', location='form')
        # self.url = form['url']
login_parser.add_argument('name', type=str, help="活动名称", location='form')
        # self.name = form['name']
login_parser.add_argument('location', type=str, help='活动地点', location='form')
        # self.location = form['location']
login_parser.add_argument('registerBeginTime', type=str, help='注册开始时间', location='form')
        # self.registerBeginTime = form['registerBeginTime']
login_parser.add_argument('registerEndTime', type=str, help='注册结束时间', location='form')
        # self.registerEndTime = form['registerEndTime']
login_parser.add_argument('selectBeginTime', type=str, help='互选开始时间', location='form')
        # self.selectBeginTime = form['selectBeginTime']
login_parser.add_argument('selectEndTime', type=str, help='互选结束时间', location='form')
        # self.selectEndTime = form['selectEndTime']
login_parser.add_argument('chargeRule', type=str, help='收费标准', location='form')
        # self.chargeRule = form['chargeRule']
login_parser.add_argument('boyBeginAge', type=str, help='男生收费开始年龄', location='form')
        # self.boyBeginAge = form['boyBeginAge']
login_parser.add_argument('girlBeginAge', type=str, help='女生收费开始年龄', location='form')
        # self.girlBeginAge = form['girlBeginAge']
login_parser.add_argument('increment', type=str, help='每增一岁递增收费', location='form')
        # self.increment = form['increment']
login_parser.add_argument('wechat', type=str, help='活动负责人微信号', location='form')
        # self.wechat = form['wechat']
login_parser.add_argument('activityBeginTime', type=str, help='活动开始时间', location='form')
        # self.activityBeginTime = form['activityBeginTime']
login_parser.add_argument('activityEndTime', type=str, help='活动结束时间', location='form')
        # self.activityEndTime = form['activityEndTime']
login_parser.add_argument('detail', type=str, help='活动详情', location='form')
        # self.detail = form['detail']

get_parser = ns.parser()
get_parser.add_argument('aID', type=str, help='活动的ID', location='form')

list_parser = ns.parser()
list_parser.add_argument('begin', type=str, help='开始编号', location='form')
list_parser.add_argument('isCurrent', type=str, help='是否是当前活动（或者历史活动）', location='form')

my_list_parser = ns.parser()
my_list_parser.add_argument('begin', type=str, help='开始编号', location='form')
my_list_parser.add_argument('isCurrent', type=str, help='是否是当前活动（或者历史活动）', location='form')
my_list_parser.add_argument('userID', type=str, help='用户的ID', location='form')

activity_bl = BlFactory.activityBl


@ns.route('')
@ns.response(200, 'OK，若返回活动或者活动列表，格式和参数相同')
@ns.response(404, '没有找到活动')
@ns.response(403, 'access denied')
@ns.response(405, '已经存在')
@ns.response(500, '内部错误')
class Activity(Resource):


    @ns.doc('增加活动')
    @ns.expect(login_parser)
    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    def put(self):
        try:
            result = activity_bl.add_activity(ActivityVO(form=request.form))
            return result, 200
        except InsertException:
            return None, 500


    @ns.doc('报名参加活动')
    @ns.expect(get_parser)
    # @ns.marshal_with(activity_post_parameters, as_list=True, code=200)
    @login_require(Role.USER)
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


    @ns.doc('取消报名活动')
    @ns.expect(get_parser)
    @login_require(Role.USER)
    def delete(self):
        aID = request.form['aID']
        try:
            activity_bl.leave_activity(JwtUtil.get_token_username(flask.request.headers.get("token")), aID)
            return None, 200
        except NotFoundException:
            return {"error": "can not find user or activity"}, 404
        except InsertException:
            return {"error": "system is error"}, 500
        except AlreadyExists:
            return {"error": "already exists"}, 405

    @ns.doc('获取活动列表')
    @ns.expect(list_parser)
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

    @ns.doc('获取我的活动列表')
    @ns.expect(my_list_parser)
    def fetch(self):
        begin = request.args['begin']
        is_current = request.args['isCurrent']
        user_id = request.args['userId']
        try:
            activity_list = activity_bl.get_activity_by_id(begin, not is_current, user_id)
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
    @ns.param(name="aID", description="活动的ID", _in="path")
    def get(self, aID):
        try:
            activity = activity_bl.get_activity_by_id(aID)
            return DateEncoderUtil().changeDate(activity), 200
        except NotFoundException:
            return {"error": "can not find the activity"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500

    @ns.doc('检查有没有报名活动')
    @ns.param(name="aID", description="活动的ID", _in="path")
    def post(self):
        try:
            aID = request.form['aID']
            username = JwtUtil.get_token_username(flask.request.headers.get("token"))
            activity = activity_bl.check_register(username, aID)
            return None, 200
        except NotFoundException:
            return {"error": "can not find the activity"}, 404
        except SystemErrorException:
            return {"error": "system is error"}, 500

