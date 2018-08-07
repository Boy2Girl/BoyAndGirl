# -*- coding: utf-8 -*-


class UserVO:

    def __init__(self, *args, **kwargs):
        if not args:
            self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        # self.id = form['id']
        self.username = form['username']
        self.password = form['password']
        self.role = form['role']

    def serialize(self):
        return {
            # 'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }


class UserInfoVO:

    def __init__(self, *args, **kwargs):
        if not args:
            self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.id = form['id']
        self.phone = form['phone']
        self.email = form['email']
        self.name = form['nickname']
        self.realName = form['name']
        self.gender = form['gender']
        self.bornDate = form['birthDate']  # 出生日期
        self.marriage = form['marriage']  # 婚姻状况
        self.friend = form['friend']  # 交友要求
        self.hometown = form['hometown']
        self.company = form['corporation']
        self.livingPlace = form['live']
        self.job = form['career']
        self.housingCondition = form['house_state']
        self.economyCondition = form['family_state']
        self.city = form['city']
        self.p_height = form['p_height']
        self.studyState = form['studyState']
        self.collageSchool = form['collageSchool']
        self.masterSchool = form['masterSchool']
        self.doctorSchool = form['doctorSchool']
        self.education = form['education']
        self.major = form['major']
        self.about_you = form['about_you']
        self.about_me = form['about_me']
        self.avatar = form['avatarUrl']
        self.personUrl = form['personUrl']
        self.studentUrl = form['studentUrl']
        self.graduateUrl = form['graduateUrl']
        self.otherUrl = form['otherUrl']
        self.qq = form['qq']
        self.wechat = form['wechat']
        self.income = form['income']
        self.corporation_type = form['corporation_type']
        self.work_state = form['work_state']


class ActivityVO:

    def __init__(self, *args, **kwargs):
        if not args:
            if kwargs:
                self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.url = form['url']
        self.name = form['name']
        self.location = form['location']
        self.registerBeginTime = form['registerBeginTime']
        self.registerEndTime = form['registerEndTime']
        self.selectBeginTime = form['selectBeginTime']
        self.selectEndTime = form['selectEndTime']
        self.chargeRule = form['chargeRule']
        self.boyBeginAge = form['boyBeginAge']
        self.girlBeginAge = form['girlBeginAge']
        self.increment = form['increment']
        self.wechat = form['wechat']
        """新增的在下面，并且删掉了一些"""
        self.activityBeginTime = form['activityBeginTime']
        self.activityEndTime = form['activityEndTime']
        self.detail = form['detail']


class PoolVO:

    def __init__(self, *args, **kwargs):
        if not args:
            if kwargs:
                self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.id = 0
        self.createTime = form['createTime']
        self.city = form['city']
        self.url = form['url']
        self.name = form['name']
        # self.realRequired = form['realRequired'] == 'True'
        # self.initChance = form['initChance']
        # self.removeTime = form['removeTime']
        # self.baseCharge = form['baseCharge']
        # self.boyBegin = form['boyBegin']
        # self.girlBegin = form['girlBegin']
        # self.ageIncrement = form['ageIncrement']
        # self.sexIncrement = form['sexIncrement']
        self.requirement = form['requirement']
        self.detail = form['detail']


class ActivityListVO:
    def __init__(self):
        pass


class PoolListVO:
    def __init__(self):
        pass


class PostListVo:
    def __init__(self):
        pass


class RecruitVo:
    def __init__(self):
        pass


class UserListVO:
    def __init__(self):
        pass
