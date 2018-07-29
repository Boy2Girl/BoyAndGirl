# -*- coding: utf-8 -*-
from publicdata import Role
from run import db
from sqlalchemy import VARCHAR, Enum, DATE, Integer, Float, Boolean, DATETIME
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "User"
    id = db.Column(Integer, primary_key=True)
    username = db.Column(VARCHAR(20))
    password = db.Column(VARCHAR(20))
    role = db.Column(db.Enum(Role), default=Role.USER)

    def __init__(self, **kwargs):
        pass


class UserInfoModel(db.Model):
    __tablename__ = "UserInfo"
    id = db.Column(Integer, primary_key=True)
    phone = db.Column(VARCHAR(30))
    email = db.Column(VARCHAR(30))
    name = db.Column(VARCHAR(30))
    realName = db.Column(VARCHAR(30))
    gender = db.Column(VARCHAR(30))
    bornDate = db.Column(DATE)
    detailLocation = db.Column(VARCHAR(100))
    marriage = db.Column(VARCHAR(40))
    friend = db.Column(VARCHAR(100))  # 交友要求
    hometown = db.Column(VARCHAR(100))
    schoolLevel = db.Column(VARCHAR(100))
    company = db.Column(VARCHAR(100))
    livingPlace = db.Column(VARCHAR(100))
    job = db.Column(VARCHAR(100))
    housingCondition = db.Column(VARCHAR(100))
    economyCondition = db.Column(VARCHAR(100))

    def __init__(self, **kwargs):
        pass


class ActivityModel(db.Model):
    __tablename__ = "Activity"
    id = db.Column(Integer, primary_key=True)
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

    def __init__(self, **kwargs):
        pass


class PoolModel(db.Model):
    __tablename__ = "Pool"
    id = db.Column(Integer, primary_key=True)
    createTime = db.Column(DATE)
    city = db.Column(VARCHAR(100))
    realRequired = db.Column(Boolean)
    initChance = db.Column(Integer)
    removeTime = db.Column(DATE)
    baseCharge = db.Column(Float)
    boyBegin = db.Column(Integer)
    girlBegin = db.Column(Integer)
    ageIncrement = db.Column(Float)
    sexIncrement = db.Column(Float)
    requirement = db.Column(VARCHAR(200))

    def __init__(self, **kwargs):
        pass


class ActivityJoinModel(db.Model):
    __tablename__ = "ActivityJoin"
    id = db.Column(Integer, primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.id'))
    activityID = db.Column(Integer, db.ForeignKey('Activity.id'))
    joinTime = db.Column(DATETIME)

    def __init__(self, userID, activityID):
        self.userID = userID
        self.activityID = activityID
        self.joinTime = datetime.now()


class PoolJoinModel(db.Model):
    __tablename__ = "PoolJoin"
    id = db.Column(Integer, primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.id'))
    poolID = db.Column(Integer, db.ForeignKey('Pool.id'))
    joinTime = db.Column(DATETIME)

    def __init__(self, poolID, userID):
        self.poolID = poolID
        self.userID = userID
        self.joinTime = datetime.now()


class LoveRelationModel(db.Model):
    __tablename__ = "LoveRelation"
    id = db.Column(Integer, primary_key=True)
    fromID = db.Column(Integer, db.ForeignKey('User.id'))
    toID = db.Column(Integer, db.ForeignKey('User.id'))
    poolID = db.Column(Integer, db.ForeignKey('Pool.id'))
    loveTime = db.Column(DATETIME)

    def __init__(self, fromID, toID, poolID):
        self.fromID = fromID
        self.toID = toID
        self.poolID = poolID
        self.loveTime = datetime.now()


class WatchInfoModel(db.Model):
    __tablename__ = "WatchInfo"
    id = db.Column(Integer, primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.id'))
    times = db.Column(Integer)
    watchTime = db.Column(DATETIME)


db.create_all()
