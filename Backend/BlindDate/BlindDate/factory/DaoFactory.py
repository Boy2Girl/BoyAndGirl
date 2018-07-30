# -*- coding: utf-8 -*-
from dao.UserDao import UserDao
from dao.ActivityDao import ActivityDao
from dao.LoveRelationDao import LoveRelationDao
from dao.PoolDao import PoolDao
from dao.PoolJoinDao import PoolJoinDao
from dao.UserInfoDao import UserInfoDao
from dao.ActivityJoinDao import ActivityJoinDao
from dao.PostsDao import PostsDao
from dao.RecruitDao import RecruitDao

userDao = UserDao()
activityJoinDao = ActivityJoinDao()
activityDao = ActivityDao()
loveRelationDao = LoveRelationDao()
poolDao = PoolDao()
poolJoinDao = PoolJoinDao()
userInfoDao = UserInfoDao()
postsDao = PostsDao()
recruitDao = RecruitDao()
