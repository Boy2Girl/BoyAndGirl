from model import UserModel, UserInfoModel, PoolModel, ActivityModel, PostsModel, RecruitModel, CheckingUserInfoModel
from vo import UserVO, UserInfoVO, PoolVO, ActivityVO, ActivityListVO, PoolListVO, PostListVo, RecruitVo, UserListVO


class UserConverter:

    def toModel(self, userVO: UserVO):
        user = UserModel()
        user.username = userVO.username
        user.password = userVO.password
        user.role = userVO.role
        return user

    def toVO(self, userModel: UserModel):
        vo = UserVO(1)
        vo.id = userModel.id
        vo.username = userModel.username
        vo.password = userModel.password
        vo.role = str(userModel.role).split(".")[1]
        return vo


class UserInfoConverter:

    def toModel(self, userInfoVO: UserInfoVO):
        ### 只能直接转化成待审核的状态
        user = CheckingUserInfoModel()
        user.id = userInfoVO.id
        user.phone = userInfoVO.phone
        user.email = userInfoVO.email
        user.name = userInfoVO.name
        user.realName = userInfoVO.realName
        user.gender = userInfoVO.gender
        user.bornDate = userInfoVO.bornDate  # 出生日期
        user.marriage = userInfoVO.marriage  # 婚姻状况
        user.friend = userInfoVO.friend  # 交友要求
        user.hometown = userInfoVO.hometown
        user.company = userInfoVO.company
        user.livingPlace = userInfoVO.livingPlace
        user.job = userInfoVO.job
        user.housingCondition = userInfoVO.housingCondition
        user.economyCondition = userInfoVO.economyCondition
        user.city = userInfoVO.city
        user.p_height = userInfoVO.p_height
        user.studyState = userInfoVO.studyState
        user.collageSchool = userInfoVO.collageSchool
        user.masterSchool = userInfoVO.masterSchool
        user.doctorSchool = userInfoVO.doctorSchool
        user.education = userInfoVO.education
        user.major = userInfoVO.major
        user.about_you = userInfoVO.about_you
        user.about_me = userInfoVO.about_me
        user.avatar = userInfoVO.avatar
        user.personUrl = userInfoVO.personUrl
        user.studentUrl = userInfoVO.studentUrl
        user.graduateUrl = userInfoVO.graduateUrl
        user.otherUrl = userInfoVO.otherUrl
        user.qq = userInfoVO.qq
        user.wechat = userInfoVO.wechat
        user.income = userInfoVO.income
        user.corporation_type = userInfoVO.corporation_type
        user.work_state = userInfoVO.work_state
        user.isReject = False
        return user

    def toVO(self, userInfoVO:  UserInfoModel):
        user = UserInfoVO(1)
        user.id = userInfoVO.id
        user.phone = userInfoVO.phone
        user.email = userInfoVO.email
        user.name = userInfoVO.name
        user.realName = userInfoVO.realName
        user.gender = userInfoVO.gender
        user.bornDate = userInfoVO.bornDate  # 出生日期
        user.marriage = userInfoVO.marriage  # 婚姻状况
        user.friend = userInfoVO.friend  # 交友要求
        user.hometown = userInfoVO.hometown
        user.company = userInfoVO.company
        user.livingPlace = userInfoVO.livingPlace
        user.job = userInfoVO.job
        user.housingCondition = userInfoVO.housingCondition
        user.economyCondition = userInfoVO.economyCondition
        user.city = userInfoVO.city
        user.p_height = userInfoVO.p_height
        user.studyState = userInfoVO.studyState
        user.collageSchool = userInfoVO.collageSchool
        user.masterSchool = userInfoVO.masterSchool
        user.doctorSchool = userInfoVO.doctorSchool
        user.education = userInfoVO.education
        user.major = userInfoVO.major
        user.about_you = userInfoVO.about_you
        user.about_me = userInfoVO.about_me
        user.avatar = userInfoVO.avatar
        user.personUrl = userInfoVO.personUrl
        user.studentUrl = userInfoVO.studentUrl
        user.graduateUrl = userInfoVO.graduateUrl
        user.otherUrl = userInfoVO.otherUrl
        user.qq = userInfoVO.qq
        user.wechat = userInfoVO.wechat
        user.income = userInfoVO.income
        user.corporation_type = userInfoVO.corporation_type
        user.work_state = userInfoVO.work_state
        return user

    def mockToReal(self, userInfoVO: CheckingUserInfoModel):
        user = UserInfoModel()
        user.id = userInfoVO.id
        user.phone = userInfoVO.phone
        user.email = userInfoVO.email
        user.name = userInfoVO.name
        user.realName = userInfoVO.realName
        user.gender = userInfoVO.gender
        user.bornDate = userInfoVO.bornDate  # 出生日期
        user.marriage = userInfoVO.marriage  # 婚姻状况
        user.friend = userInfoVO.friend  # 交友要求
        user.hometown = userInfoVO.hometown
        user.company = userInfoVO.company
        user.livingPlace = userInfoVO.livingPlace
        user.job = userInfoVO.job
        user.housingCondition = userInfoVO.housingCondition
        user.economyCondition = userInfoVO.economyCondition
        user.city = userInfoVO.city
        user.p_height = userInfoVO.p_height
        user.studyState = userInfoVO.studyState
        user.collageSchool = userInfoVO.collageSchool
        user.masterSchool = userInfoVO.masterSchool
        user.doctorSchool = userInfoVO.doctorSchool
        user.education = userInfoVO.education
        user.major = userInfoVO.major
        user.about_you = userInfoVO.about_you
        user.about_me = userInfoVO.about_me
        user.avatar = userInfoVO.avatar
        user.personUrl = userInfoVO.personUrl
        user.studentUrl = userInfoVO.studentUrl
        user.graduateUrl = userInfoVO.graduateUrl
        user.otherUrl = userInfoVO.otherUrl
        user.qq = userInfoVO.qq
        user.wechat = userInfoVO.wechat
        user.income = userInfoVO.income
        user.corporation_type = userInfoVO.corporation_type
        user.work_state = userInfoVO.work_state
        user.isReject = False
        return user


class PoolConverter:

    def toModel(self, poolVO: PoolVO):
        pool = PoolModel()
        # pool.poolID = poolVO.poolID
        pool.createTime = poolVO.createTime
        pool.city = poolVO.city
        pool.url = poolVO.url
        pool.name = poolVO.name
        # pool.realRequired = poolVO.realRequired
        # pool.initChance = poolVO.initChance
        # pool.removeTime = poolVO.removeTime
        # pool.baseCharge = poolVO.baseCharge
        # pool.boyBegin = poolVO.boyBegin
        # pool.girlBegin = poolVO.girlBegin
        # pool.ageIncrement = poolVO.ageIncrement
        # pool.sexIncrement = poolVO.sexIncrement
        pool.requirement = poolVO.requirement
        pool.detail = poolVO.detail.encode()
        return pool

    def toVO(self, poolModel: PoolModel):
        pool = PoolVO()
        pool.id = poolModel.id
        pool.url = poolModel.url
        pool.createTime = poolModel.createTime
        pool.city = poolModel.city
        pool.name = poolModel.name
        # pool.realRequired = poolModel.realRequired
        # pool.initChance = poolModel.initChance
        # pool.removeTime = poolModel.removeTime
        # pool.baseCharge = poolModel.baseCharge
        # pool.boyBegin = poolModel.boyBegin
        # pool.girlBegin = poolModel.girlBegin
        # pool.ageIncrement = poolModel.ageIncrement
        # pool.sexIncrement = poolModel.sexIncrement
        pool.requirement = poolModel.requirement
        pool.detail = poolModel.detail.decode()
        return pool


class ActivityConverter:

    def toModel(self, activityVO: ActivityVO):
        activity = ActivityModel()
        # id 暂且不管
        activity.url = activityVO.url
        activity.name = activityVO.name
        activity.location = activityVO.location
        activity.registerBeginTime = activityVO.registerBeginTime
        activity.registerEndTime = activityVO.registerEndTime
        activity.selectBeginTime = activityVO.selectBeginTime
        activity.selectEndTime = activityVO.selectEndTime
        activity.chargeRule = activityVO.chargeRule
        activity.boyBeginAge = activityVO.boyBeginAge
        activity.girlBeginAge = activityVO.girlBeginAge
        activity.increment = activityVO.increment
        activity.wechat = activityVO.wechat

        # activity.realName = activityVO.realName  # 是否需要真实信息
        activity.activityBeginTime = activityVO.activityBeginTime
        activity.activityEndTime = activityVO.activityEndTime
        activity.detail = activityVO.detail.encode()
        return activity

    def toVO(self, activityModel: ActivityModel):
        activity = ActivityVO()
        activity.url = activityModel.url
        activity.name = activityModel.name
        activity.id = activityModel.id
        activity.location = activityModel.location
        activity.registerBeginTime = activityModel.registerBeginTime
        activity.registerEndTime = activityModel.registerEndTime
        activity.selectBeginTime = activityModel.selectBeginTime
        activity.selectEndTime = activityModel.selectEndTime
        activity.chargeRule = activityModel.chargeRule
        activity.boyBeginAge = activityModel.boyBeginAge
        activity.girlBeginAge = activityModel.girlBeginAge
        activity.increment = activityModel.increment
        activity.wechat = activityModel.wechat
        # activity.realName = activityModel.realName  # 是否需要真实信息
        activity.activityBeginTime = activityModel.activityBeginTime
        activity.activityEndTime = activityModel.activityEndTime
        activity.detail = activityModel.detail.decode()
        return activity


class ActivityListConverter:

    def toVO(self, activityModel: ActivityModel):
        activity = ActivityListVO()
        activity.id = activityModel.id
        activity.url = activityModel.url
        activity.title = activityModel.name
        activity.time = str(activityModel.activityBeginTime) + " - " + str(activityModel.activityEndTime)
        activity.address = activityModel.location
        """这边先写一个mock"""
        activity.numOfRead = 10
        activity.numOfSign = 10
        return activity


class PoolListConverter:

    def toVO(self, poolModel: PoolModel):
        pool = PoolListVO()
        pool.id = poolModel.id
        pool.url = poolModel.url
        pool.title = poolModel.name
        pool.time = poolModel.createTime
        pool.address = poolModel.city
        pool.requirement = "南京工作或在读"
        pool.numOfBoy = 301
        pool.numOfGirl = 301
        return pool


class RecruitListConverter:

    def toVO(self, recruitModel: RecruitModel):
        recruit = RecruitVo()
        recruit.id = recruitModel.id
        recruit.userId = recruitModel.userID
        recruit.time = recruitModel.time


class PostsListConverter:

    def toVO(self, posts: PostsModel, userInfo: UserInfoModel):
        post = PostListVo()
        post.id = posts.id
        post.education = userInfo.education
        post.username = userInfo.name
        post.birthDate = str(userInfo.bornDate)
        post.city = userInfo.city
        post.school = userInfo.collageSchool
        post.career = userInfo.job
        post.source = userInfo.avatar
        print(post)
        return post


class UserListConverter:

    def toVO(self, userInfo: UserInfoModel):
        post = UserListVO()
        post.id = userInfo.id
        post.education = userInfo.education
        post.username = userInfo.name
        post.birthDate = str(userInfo.bornDate)
        post.city = userInfo.city
        post.school = userInfo.collageSchool
        post.career = userInfo.job
        post.source = userInfo.avatar
        return post
