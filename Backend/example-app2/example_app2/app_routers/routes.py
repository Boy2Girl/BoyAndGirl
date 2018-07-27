# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user import User
from .api.user_info import UserInfo
from .api.user_info_uID import UserInfoUid
from .api.activity_aID import ActivityAid
from .api.activity import Activity
from .api.pool_pID import PoolPid
from .api.pool import Pool
from .api.pool_love import PoolLove
from .api.pool_love_uID import PoolLoveUid


routes = [
    dict(resource=User, urls=['/user'], endpoint='user'),
    dict(resource=UserInfo, urls=['/user/info'], endpoint='user_info'),
    dict(resource=UserInfoUid, urls=['/user/info/<uID>'], endpoint='user_info_uID'),
    dict(resource=ActivityAid, urls=['/activity/<aID>'], endpoint='activity_aID'),
    dict(resource=Activity, urls=['/activity'], endpoint='activity'),
    dict(resource=PoolPid, urls=['/pool/<pID>'], endpoint='pool_pID'),
    dict(resource=Pool, urls=['/pool'], endpoint='pool'),
    dict(resource=PoolLove, urls=['/pool/love'], endpoint='pool_love'),
    dict(resource=PoolLoveUid, urls=['/pool/love/<uID>'], endpoint='pool_love_uID'),
]