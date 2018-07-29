from model import UserModel, UserInfoModel, PoolModel, ActivityModel
from vo import UserVO, UserInfoVO, PoolVO, ActivityVO


class UserConverter:

    def toModel(self, userVO: UserVO):
        user = UserModel()
        user.username = userVO.username
        user.password = userVO.password
        user.role = userVO.role
        print(user.__dict__)
        return user

    def toVO(self, userModel:UserModel):
        vo = UserVO(1)
        vo.id = userModel.id
        vo.username = userModel.username
        vo.password = userModel.password
        vo.role = userModel.role
        return vo


class UserInfoConverter:

    def toModel(self, userInfoVO: UserInfoVO):
        user = UserInfoModel()
        user.id = userInfoVO.id
        user.phone = userInfoVO.phone
        user.email = userInfoVO.email
        user.name = userInfoVO.name
        user.realName = userInfoVO.realName
        user.gender = userInfoVO.gender
        user.bornDate = userInfoVO.bornDate
        user.detailLocation = userInfoVO.detailLocation
        user.marriage = userInfoVO.marriage
        user.friend = userInfoVO.friend  # 交友要求
        user.hometown = userInfoVO.hometown
        user.schoolLevel = userInfoVO.schoolLevel
        user.company = userInfoVO.company
        user.livingPlace = userInfoVO.livingPlace
        user.job = userInfoVO.livingPlace
        user.housingCondition = userInfoVO.housingCondition
        user.economyCondition = userInfoVO.economyCondition
        return user

    def toVO(self, model: UserInfoModel):
        vo = UserInfoVO(1)
        vo.id = model.id
        vo.phone = model.phone
        vo.email = model.email
        vo.name = model.name
        vo.realName = model.realName
        vo.gender = model.gender
        vo.bornDate = model.bornDate
        vo.detailLocation = model.detailLocation
        vo.marriage = model.marriage
        vo.friend = model.friend  # 交友要求
        vo.hometown = model.hometown
        vo.schoolLevel = model.schoolLevel
        vo.company = model.company
        vo.livingPlace = model.livingPlace
        vo.job = model.job
        vo.housingCondition = model.housingCondition
        vo.economyCondition = model.housingCondition
        return vo


class PoolConverter:

    def toModel(self, poolVO: PoolVO):
        pool = PoolModel()
        # pool.poolID = poolVO.poolID
        pool.createTime = poolVO.createTime
        pool.city = poolVO.city
        pool.realRequired = poolVO.realRequired
        pool.initChance = poolVO.initChance
        pool.removeTime = poolVO.removeTime
        pool.baseCharge = poolVO.baseCharge
        pool.boyBegin = poolVO.boyBegin
        pool.girlBegin = poolVO.girlBegin
        pool.ageIncrement = poolVO.ageIncrement
        pool.sexIncrement = poolVO.sexIncrement
        pool.requirement = poolVO.requirement
        return pool

    def toVO(self, poolModel: PoolModel):
        pool = PoolVO()
        pool.id = poolModel.id
        pool.createTime = poolModel.createTime
        pool.city = poolModel.city
        pool.realRequired = poolModel.realRequired
        pool.initChance = poolModel.initChance
        pool.removeTime = poolModel.removeTime
        pool.baseCharge = poolModel.baseCharge
        pool.boyBegin = poolModel.boyBegin
        pool.girlBegin = poolModel.girlBegin
        pool.ageIncrement = poolModel.ageIncrement
        pool.sexIncrement = poolModel.sexIncrement
        pool.requirement = poolModel.requirement
        return pool


class ActivityConverter:

    def toModel(self, activityVO: ActivityVO):
        activity = ActivityModel()
        # id 暂且不管
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
        activity.realName = activityVO.realName  # 是否需要真实信息
        return activity

    def toVO(self, activityModel: ActivityModel):
        activity = ActivityVO()
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
        activity.realName = activityModel.realName  # 是否需要真实信息
        return activity
