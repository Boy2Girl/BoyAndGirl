import datetime
import json

from flask import request
from flask_restplus import Resource, Namespace

from decorator.RoleRequest import login_require
from exceptions import NotFoundException, AlreadyExists, InsertException
from factory.BlFactory import userInfoBl
from publicdata import Role
from utils.DateEncoder import DateEncoderUtil
from vo import UserInfoVO

ns = Namespace('user/info', description='关于用户信息(增加，获取，更新用户信息)')

login_parser = ns.parser()
login_parser.add_argument('id', type=str, help='用户ID', location='form')
# self.id = form['id']
login_parser.add_argument('phone', type=str, help='用户电话', location='form')
#         self.phone = form['phone']
login_parser.add_argument('email', type=str, help='邮箱', location='form')
#         self.email = form['email']
login_parser.add_argument('nickname', type=str, help='昵称', location='form')
#         self.name = form['nickname']
login_parser.add_argument('name', type=str, help='姓名', location='form')
#         self.realName = form['name']
login_parser.add_argument('gender', type=str, help='性别', location='form')
#         self.gender = form['gender']
login_parser.add_argument('birthDate', type=str, help='出生日期', location='form')
#         self.bornDate = form['birthDate']  # 出生日期
login_parser.add_argument('marriage', type=str, help='婚姻状况', location='form')
#         self.marriage = form['marriage']  # 婚姻状况
login_parser.add_argument('friend', type=str, help='交友要求', location='form')
#         self.friend = form['friend']  # 交友要求
login_parser.add_argument('hometown', type=str, help='家乡', location='form')
#         self.hometown = form['hometown']
login_parser.add_argument('corporation', type=str, help='公司', location='form')
#         self.company = form['corporation']
login_parser.add_argument('live', type=str, help='居住地', location='form')
#         self.livingPlace = form['live']
login_parser.add_argument('career', type=str, help='职位', location='form')
#         self.job = form['career']
login_parser.add_argument('house_state', type=str, help='房屋情况', location='form')
#         self.housingCondition = form['house_state']
login_parser.add_argument('family_state', type=str, help='家庭情况', location='form')
#         self.economyCondition = form['family_state']
login_parser.add_argument('city', type=str, help='城市', location='form')
#         self.city = form['city']
login_parser.add_argument('p_height', type=int, help='身高', location='form')
#         self.p_height = form['p_height']
login_parser.add_argument('studyState', type=str, help='学历', location='form')
#         self.studyState = form['studyState']
login_parser.add_argument('collageSchool', type=str, help='大学学校', location='form')
#         self.collageSchool = form['collageSchool']
login_parser.add_argument('masterSchool', type=str, help='硕士学校', location='form')
#         self.masterSchool = form['masterSchool']
login_parser.add_argument('doctorSchool', type=str, help='博士学校', location='form')
#         self.doctorSchool = form['doctorSchool']
login_parser.add_argument('education', type=str, help='学院', location='form')
#         self.education = form['education']
login_parser.add_argument('major', type=str, help='专业', location='form')
#         self.major = form['major']
login_parser.add_argument('about_you', type=str, help='对另一半的要求', location='form')
#         self.about_you = form['about_you']
login_parser.add_argument('about_me', type=str, help='对自己的要求', location='form')
#         self.about_me = form['about_me']
login_parser.add_argument('avatarUrl', type=str, help='头像地址', location='form')
#         self.avatar = form['avatarUrl']
login_parser.add_argument('personUrl', type=str, help='身份证照片地址', location='form')
#         self.personUrl = form['personUrl']
login_parser.add_argument('studentUrl', type=str, help='学生证地址', location='form')
#         self.studentUrl = form['studentUrl']
login_parser.add_argument('graduateUrl', type=str, help='毕业证地址', location='form')
#         self.graduateUrl = form['graduateUrl']
login_parser.add_argument('otherUrl', type=str, help='其他身份的地址', location='form')
#         self.otherUrl = form['otherUrl']
login_parser.add_argument('qq', type=str, help='qq号', location='form')
#         self.qq = form['qq']
login_parser.add_argument('wechat', type=str, help='微信号', location='form')
#         self.wechat = form['wechat']
login_parser.add_argument('income', type=str, help='收入', location='form')
#         self.income = form['income']
login_parser.add_argument('corporation_type', type=str, help='公司类型', location='form')
#         self.corporation_type = form['corporation_type']
login_parser.add_argument('work_state', type=str, help='工作状态', location='form')
#         self.work_state = form['work_state']


end_parser = ns.parser()
end_parser.add_argument('isChecked', type=bool, help='是否实名认证过的', location='args')

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, '没有找到用户信息')
@ns.response(403, 'access denied')
@ns.response(500, '内部错误')
class UserInfo(Resource):

    # @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('填写')
    @ns.expect(login_parser)
    def put(self):
        try:
            for i in request.form:
                print(i)
            userInfoBl.add_user_info(UserInfoVO(form=request.form))
            return None, 200, {}
        except InsertException:
            return None, 500

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('更新')
    def post(self):
        try:
            userInfoBl.update_user_info(UserInfoVO(form=request.form))
            return None, 200, {}
        except AlreadyExists:
            return None, 403
        except NotFoundException:
            return None, 404

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('获取没有实名认证过的用户信息列表')
    def get(self):
        try:
            return userInfoBl.get_un_checking_list(), 200, {}
        except AlreadyExists:
            return None, 403

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('审批一个用户的用户信息提交')
    def patch(self):
        try:
            userID = request.form['userID']
            isPass = request.form['isPass'] == 'True'
            userInfoBl.check_user_info(userID, isPass)
            return None, 200
        except AlreadyExists:
            return None, 403




@ns.route('/<string:id>')
@ns.response(200, '返回用户信息，格式和参数相同')
@ns.response(404, '没有找到该用户信息')
class UserInfoID(Resource):

    @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看')
    @ns.expect()
    def get(self, id):
        try:
            is_check = request.args['isChecked'] == 'True'
            result = userInfoBl.get_user_info(id, is_check)
            result1 = DateEncoderUtil().changeDate(result)
            return result1, 200
        except NotFoundException:
            return None, 404


