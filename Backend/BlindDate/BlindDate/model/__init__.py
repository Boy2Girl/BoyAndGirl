# -*- coding: utf-8 -*-
from run import db
from sqlalchemy import VARCHAR,Boolean,DATE,DATETIME,Integer,Float


class UserModel(db.Model):
    __tablename__ = "User"
    userID = db.Column(VARCHAR(20), primary_key=True)
    username = db.Column(VARCHAR(100))
    password = db.Column(VARCHAR(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserInfoModel(db.Model):
    __tablename__ = "UserInfo"
    userID = db.Column(VARCHAR(20), primary_key=True)
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


class ActivityModel(db.Model):
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
    realName = db.Column(Boolean) # 是否需要真实信息


class PoolModel(db.Model):
    __tablename__ = "Pool"
    poolID = db.Column(VARCHAR(20), primary_key=True)
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


class ActivityJoinModel(db.Model):
    __tablename__ = "ActivityJoin"
    joinID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(VARCHAR(20), db.ForeignKey('User.userID'))
    activityID = db.Column(VARCHAR(20), db.ForeignKey('Activity.activityID'))
    joinTime = db.Column(DATETIME)


class PoolJoinModel(db.Model):
    __tablename__ = "PoolJoin"
    joinID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(VARCHAR(20), db.ForeignKey('User.userID'))
    poolID = db.Column(VARCHAR(20), db.ForeignKey('Pool.poolID'))
    joinTime = db.Column(DATETIME)


class LoveRelationModel(db.Model):
    __tablename__ = "LoveRelation"
    loveID = db.Column(VARCHAR(20), primary_key=True)
    fromID = db.Column(VARCHAR(20), db.ForeignKey('User.userID'))
    toID = db.Column(VARCHAR(20), db.ForeignKey('User.userID'))
    poolID = db.Column(VARCHAR(20), db.ForeignKey('Pool.poolID'))
    loveTime = db.Column(DATETIME)


class WatchInfoModel(db.Model):
    __tablename__ = "LoveRelation"
    activityID = db.Column(VARCHAR(20), primary_key=True)
    userID = db.Column(VARCHAR(20), db.ForeignKey('User.userID'))
    times = db.Column(Integer)
    watchTime = db.Column(DATETIME)


db.create_all()
