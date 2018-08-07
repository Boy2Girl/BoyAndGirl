from exceptions import AlreadyExists
from run import session,db
from model import UserModel, LoveRelationModel, UserInfoModel
import traceback
from dao.DaoUtil import DaoUtil
from sqlalchemy.orm import aliased


class LoveRelationDao(DaoUtil):

    def get_your_love(self, user_id, pool_id):
        try:
            lovers = session.query(UserInfoModel).join(LoveRelationModel,LoveRelationModel.toID == UserInfoModel.id)\
                .filter(LoveRelationModel.fromID == user_id)\
                .filter(LoveRelationModel.poolID == pool_id).all()
            return lovers
        except:
            raise SystemError

    def get_true_love(self, user_id, pool_id):
        try:
            alaised1 = aliased(LoveRelationModel)
            alaised2 = aliased(LoveRelationModel)
            lovers = (session.query(alaised1.toID).join(alaised2).filter(alaised1.fromID == alaised2.toID).filter(
                alaised2.toID == alaised1.fromID).filter(alaised1.fromID == user_id)
                       .filter(alaised1.poolID == pool_id).all())
            return [i[0] for i in lovers]
        except:
            raise SystemError

    def get_relation(self, from_id, to_id, pool_id):
        try:
            relation = session.query(LoveRelationModel).filter(LoveRelationModel.fromID == from_id).\
                filter(LoveRelationModel.toID == to_id).filter(LoveRelationModel.poolID == pool_id).first()
            if relation:
                raise AlreadyExists
        except AlreadyExists:
            raise AlreadyExists
        except:
            raise SystemError

