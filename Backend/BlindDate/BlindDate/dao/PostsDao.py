from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException, AlreadyExists
from run import session,db
from model import UserModel, PoolModel, PoolJoinModel, PostsModel


class PostsDao(DaoUtil):

    def get_posts_by_user(self, user_id):
        try:
            posts = session.query(PostsModel).filter(PostsModel.userID == user_id).first()
            if posts:
                raise AlreadyExists
        except AlreadyExists:
            raise AlreadyExists
        except:
            raise SystemError

