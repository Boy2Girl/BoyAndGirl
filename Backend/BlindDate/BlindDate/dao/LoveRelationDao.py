from run import session,db
from model import UserModel, LoveRelationModel
import traceback
from dao.DaoUtil import DaoUtil
from sqlalchemy.orm import aliased


class LoveRelationDao(DaoUtil):

    def get_your_love(self, user_id):
        try:
            lovers = session.query(LoveRelationModel.toID).filter(LoveRelationModel.fromID == user_id)
            return lovers
        except:
            raise SystemError

    def get_true_love(self, user_id):
        try:
            alaised1 = aliased(LoveRelationModel)
            alaised2 = aliased(LoveRelationModel)
            lovers = (session.query(alaised1.toID).join(alaised2).filter(alaised1.fromID == alaised2.toID).filter(
                alaised2.toID == alaised1.fromID).filter(alaised1.fromID == user_id))
            return lovers
        except:
            raise SystemError


