# -*- coding: utf-8 -*-
from model import UserModel, UserInfoModel
from publicdata import Role
from run import db
from sqlalchemy import VARCHAR, DATE, Integer, Float, Boolean, DATETIME
from datetime import datetime


class UserVO:
    __tablename__ = "User"
    userID = db.Column(Integer, primary_key=True)
    username = db.Column(VARCHAR(20))
    password = db.Column(VARCHAR(20))
    role = db.Column(db.Enum(Role), default=Role.USER)

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
        self.userID = form['userID']
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
    __tablename__ = "Activity"
    activityID = db.Column(VARCHAR(20), primary_key=True)
    location = db.Column(VARCHAR(30))
    registerBeginTime = db.Column(DATE)
    registerEndTime = db.Column(DATE)
    selectBeginTime = db.Column(DATE)
    selectEndTime = db.Column(DATE)
    chargeRule = db.Column(VARCHAR(100))
    boyBeginAge = db.Column(Integer)
    girlBeginAge = db.Column(Integer)
    increment = db.Column(Float)
    wechat = db.Column(VARCHAR(100))
    realName = db.Column(Boolean)  # 是否需要真实信息


class PoolVO:

    def __init__(self, *args, **kwargs):
        if not args:
            self.__init__from_form(kwargs)

    def __init__from_form(self, form_dict):
        form = form_dict['form']
        self.poolID = form['poolID']
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


class ActivityJoinVO:
    __tablename__ = "ActivityJoin"
    joinID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.userID'))
    activityID = db.Column(VARCHAR(20), db.ForeignKey('Activity.activityID'))
    joinTime = db.Column(DATETIME)


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
