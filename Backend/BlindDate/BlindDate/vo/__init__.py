# -*- coding: utf-8 -*-
from run import db
from sqlalchemy import VARCHAR, DATE, Integer, Float, Boolean, DATETIME
from datetime import datetime


class UserVO:

    def __init__(self, *args, **kwargs):
        if not args:
            self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.username = form['username']
        self.password = form['password']
        self.role = form['role']


class UserInfoVO:

    def __init__(self, *args, **kwargs):
        if not args:
            self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.id = form['id']
        self.phone = form['phone']
        self.email = form['email']
        self.name = form['name']
        self.realName = form['realName']
        self.gender = form['gender']
        self.bornDate = form['bornDate']
        self.detailLocation = form['detailLocation']
        self.marriage = form['marriage']
        self.friend = form['friend']  # 交友要求
        self.hometown = form['hometown']
        self.schoolLevel = form['schoolLevel']
        self.company = form['company']
        self.livingPlace = form['livingPlace']
        self.job = form['job']
        self.housingCondition = form['housingCondition']
        self.economyCondition = form['economyCondition']


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
        self.realRequired = form['realRequired'] == 'True'
        self.initChance = form['initChance']
        self.removeTime = form['removeTime']
        self.baseCharge = form['baseCharge']
        self.boyBegin = form['boyBegin']
        self.girlBegin = form['girlBegin']
        self.ageIncrement = form['ageIncrement']
        self.sexIncrement = form['sexIncrement']
        self.requirement = form['requirement']


class ActivityListVO:
    def __init__(self):
        pass


class PoolJoinVO:
    __tablename__ = "PoolJoin"
    joinID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.userID'))
    poolID = db.Column(VARCHAR(20), db.ForeignKey('Pool.poolID'))
    joinTime = db.Column(DATETIME)

    def __init__(self, poolID, userID):
        self.poolID = poolID
        self.userID = userID
        self.joinTime = datetime.now()


class LoveRelationVO:
    __tablename__ = "LoveRelation"
    loveID = db.Column(VARCHAR(20), primary_key=True)
    fromID = db.Column(Integer, db.ForeignKey('User.userID'))
    toID = db.Column(Integer, db.ForeignKey('User.userID'))
    poolID = db.Column(VARCHAR(20), db.ForeignKey('Pool.poolID'))
    loveTime = db.Column(DATETIME)

    def __init__(self, fromID, toID, poolID):
        self.fromID = fromID
        self.toID = toID
        self.poolID = poolID
        self.loveTime = datetime.now()


class WatchInfoVO:
    __tablename__ = "WatchInfo"
    activityID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.userID'))
    times = db.Column(Integer)
    watchTime = db.Column(DATETIME)


db.create_all()
