from dao.DaoUtil import DaoUtil
from exceptions import NotFoundException, AlreadyExists
from run import session, db
from model import UserModel, PoolModel, PoolJoinModel, PostsModel, RecruitModel


class PostsDao(DaoUtil):

    def get_posts_by_user(self, user_id):
        try:
            posts = session.query(PostsModel).filter(PostsModel.userID == user_id).all()
            return posts
        except:
            raise SystemError

    ### 我应征的人
    def get_posts_by_user_id(self, user_id):
        try:
            posts = session.query(PostsModel).join(RecruitModel). \
                filter(RecruitModel.userID == user_id).filter(PostsModel.id == RecruitModel.postsID).all()
            return posts
        except:
            raise SystemError

    def get_all(self):
        try:
            posts = session.query(PostsModel).all()
            return posts
        except:
            raise SystemError

    def get_my(self, user_id):
        try:
            posts = session.query(RecruitModel).join(PostsModel). \
                filter(PostsModel.userID == user_id).filter(PostsModel.id == RecruitModel.postsID).all()
            return posts
        except:
            raise SystemError


