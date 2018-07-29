from model import UserModel, UserInfoModel, PoolModel
from vo import UserVO, UserInfoVO, PoolVO


class UserConverter:

    def toModel(self, userVO: UserVO):
        user = UserModel()
        user.userID = userVO.userID
        user.username = userVO.username
        user.password = userVO.password
        user.role = userVO.role
        return user

    def toVO(self, userModel:UserModel):
        vo = UserVO(1)
        vo.userID = userModel.userID
        vo.username = userModel.username
        vo.password = userModel.password
        vo.role = userModel.role
        return vo


class UserInfoConverter:

    def toModel(self, userInfoVO: UserInfoVO):
        user = UserInfoModel()
        user.userID = userInfoVO.userID
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
        vo.userID = model.userID
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
        pool.poolID = poolVO.poolID
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
        pool.poolID = poolModel.poolID
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
