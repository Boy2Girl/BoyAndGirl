from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException, AlreadyExists
from run import session,db
from model import UserModel, PoolModel, PoolJoinModel, RecruitModel


class RecruitDao(DaoUtil):

    def get_recruit(self, user_id, posts_id):
        try:
            recruit = session.query(RecruitModel).filter(RecruitModel.userID == user_id).\
                filter(RecruitModel.postsID == posts_id).first()
            if recruit:
                raise AlreadyExists
        except AlreadyExists:
            raise AlreadyExists
        except:
            raise SystemError

