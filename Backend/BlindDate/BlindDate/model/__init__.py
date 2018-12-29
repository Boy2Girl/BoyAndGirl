# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import VARCHAR, DATE, Integer, Float, Boolean, DATETIME
from sqlalchemy.dialects.mysql import LONGBLOB

from publicdata import Role
from run import db


class UserModel(db.Model):
    __tablename__ = "User"
    id = db.Column(Integer, primary_key=True)
    username = db.Column(VARCHAR(20))
    password = db.Column(VARCHAR(20))
    role = db.Column(db.Enum(Role), default=Role.USER)
    refresh_token = db.Column(VARCHAR(100))

    def __init__(self, **kwargs):
        pass


class UserInfoModel(db.Model):
    __tablename__ = "UserInfo"
    id = db.Column(Integer, primary_key=True)
    phone = db.Column(VARCHAR(100))
    email = db.Column(VARCHAR(100))
    name = db.Column(VARCHAR(100))
    realName = db.Column(VARCHAR(100))
    gender = db.Column(VARCHAR(100))
    bornDate = db.Column(DATE)  # 出生日期
    marriage = db.Column(VARCHAR(100))  # 婚姻状况
    friend = db.Column(VARCHAR(100))  # 交友要求
    hometown = db.Column(VARCHAR(100))
    company = db.Column(VARCHAR(100))
    livingPlace = db.Column(VARCHAR(100))
    job = db.Column(VARCHAR(100))
    housingCondition = db.Column(VARCHAR(100))
    economyCondition = db.Column(VARCHAR(100))
    city = db.Column(VARCHAR(100))
    p_height = db.Column(Integer)
    studyState = db.Column(VARCHAR(100))
    collageSchool = db.Column(VARCHAR(100))
    masterSchool = db.Column(VARCHAR(100))
    doctorSchool = db.Column(VARCHAR(100))
    education = db.Column(VARCHAR(100))
    major = db.Column(VARCHAR(100))
    about_you = db.Column(VARCHAR(100))
    about_me = db.Column(VARCHAR(100))
    avatar = db.Column(VARCHAR(100))
    personUrl = db.Column(VARCHAR(100))
    studentUrl = db.Column(VARCHAR(100))
    graduateUrl = db.Column(VARCHAR(100))
    otherUrl = db.Column(VARCHAR(100))
    qq = db.Column(VARCHAR(100))
    wechat = db.Column(VARCHAR(100))
    income = db.Column(VARCHAR(100))
    corporation_type = db.Column(VARCHAR(100))
    work_state = db.Column(VARCHAR(100))

    def __init__(self, **kwargs):
        pass


class WechatInfoModel(db.Model):
    __tablename__ = "UserInfo"
    id = db.Column(Integer, primary_key=True)
    nickname = db.Column(VARCHAR(100))
    sex = db.Column(VARCHAR(100))
    province = db.Column(VARCHAR(100))
    city = db.Column(VARCHAR(100))
    county = db.Column(VARCHAR(100))
    headimgurl = db.Column(VARCHAR(200))
    unionid = db.Column(VARCHAR(100))

    def __init__(self, **kwargs):
        pass


'''用来保存新的用户表'''


class CheckingUserInfoModel(db.Model):
    __tablename__ = "CheckingUserInfo"
    id = db.Column(Integer, db.ForeignKey('User.id'), primary_key=True)
    phone = db.Column(VARCHAR(100))
    email = db.Column(VARCHAR(100))
    name = db.Column(VARCHAR(100))
    realName = db.Column(VARCHAR(100))
    gender = db.Column(VARCHAR(100))
    bornDate = db.Column(DATE)  # 出生日期
    marriage = db.Column(VARCHAR(100))  # 婚姻状况
    friend = db.Column(VARCHAR(100))  # 交友要求
    hometown = db.Column(VARCHAR(100))
    company = db.Column(VARCHAR(100))
    livingPlace = db.Column(VARCHAR(100))
    job = db.Column(VARCHAR(100))
    housingCondition = db.Column(VARCHAR(100))
    economyCondition = db.Column(VARCHAR(100))
    city = db.Column(VARCHAR(100))
    p_height = db.Column(Integer)
    studyState = db.Column(VARCHAR(100))
    collageSchool = db.Column(VARCHAR(100))
    masterSchool = db.Column(VARCHAR(100))
    doctorSchool = db.Column(VARCHAR(100))
    education = db.Column(VARCHAR(100))
    major = db.Column(VARCHAR(100))
    about_you = db.Column(VARCHAR(100))
    about_me = db.Column(VARCHAR(100))
    avatar = db.Column(VARCHAR(100))
    personUrl = db.Column(VARCHAR(100))
    studentUrl = db.Column(VARCHAR(100))
    graduateUrl = db.Column(VARCHAR(100))
    otherUrl = db.Column(VARCHAR(100))
    qq = db.Column(VARCHAR(100))
    wechat = db.Column(VARCHAR(100))
    income = db.Column(VARCHAR(100))
    corporation_type = db.Column(VARCHAR(100))
    work_state = db.Column(VARCHAR(100))

    isReject = db.Column(Boolean)

    def __init__(self, **kwargs):
        pass


class ActivityModel(db.Model):
    __tablename__ = "Activity"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(VARCHAR(30))
    url = db.Column(VARCHAR(100))
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
    # realName = db.Column(Boolean)  # 是否需要真实信息
    activityBeginTime = db.Column(VARCHAR(100))
    activityEndTime = db.Column(VARCHAR(100))
    detail = db.Column(LONGBLOB)

    def __init__(self, **kwargs):
        pass


class PoolModel(db.Model):
    __tablename__ = "Pool"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(VARCHAR(100))
    url = db.Column(VARCHAR(100))
    createTime = db.Column(DATE)
    city = db.Column(VARCHAR(100))
    # realRequired = db.Column(Boolean)
    # initChance = db.Column(Integer)
    # removeTime = db.Column(DATE)
    # baseCharge = db.Column(Float)
    # boyBegin = db.Column(Integer)
    # girlBegin = db.Column(Integer)
    # ageIncrement = db.Column(Float)
    # sexIncrement = db.Column(Float)
    requirement = db.Column(VARCHAR(200))
    detail = db.Column(LONGBLOB)

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


class PostsModel(db.Model):
    __tablename__ = "Posts"
    id = db.Column(Integer, primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.id'))
    beginTime = db.Column(DATE)
    endTime = db.Column(DATE)  # 要传入的参数

    def __init__(self, userID, endTime):
        self.endTime = endTime
        self.userID = userID
        self.beginTime = datetime.now()


class RecruitModel(db.Model):
    __tablename__ = "Recruit"
    id = db.Column(Integer, primary_key=True)
    userID = db.Column(Integer, db.ForeignKey('User.id'))
    postsID = db.Column(Integer, db.ForeignKey('Posts.id'))
    time = db.Column(DATE)
    isSuccess = db.Column(Boolean)  # 是否要

    def __init__(self, userID, postsID, isSuccess):
        self.userID = userID
        self.postsID = postsID
        self.isSuccess = isSuccess
        self.time = datetime.now()


db.create_all()
