# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['DEBUG'] = True
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['SECRET_KEY'] = 'wfhg9hr-1jfpjf-p3j-=vgf0pvmo3k=2-3rj0-3j=gn[=3-g[mj'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@112.74.49.28/BoyAndGirl'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 50
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 50

    return app


def create_db(app):
    db = SQLAlchemy(app)
    return db


def register_api():
    from routers.user import ns as user_ns
    from routers.user_info import ns as user_info_ns
    from routers.Pool import ns as pool_ns
    from routers.love import ns as love_ns
    from routers.activity import ns as activity_ns
    from routers.Posts import ns as posts_ns
    from routers.test import ns as test_ns
    from routers.check import ns as check_ns
    from routers.pay import ns as pay_ns
    from routers import api
    api.add_namespace(user_ns)
    api.add_namespace(user_info_ns)
    api.add_namespace(pool_ns)
    api.add_namespace(love_ns)
    api.add_namespace(activity_ns)
    api.add_namespace(posts_ns)
    api.add_namespace(test_ns)
    api.add_namespace(check_ns)
    api.add_namespace(pay_ns)


def register(app):
    from routers import api_blueprint
    app.register_blueprint(api_blueprint)


app = create_app()
db = create_db(app)
session = db.session

if __name__ == '__main__':
    register_api()
    register(app)
    app.run(debug=False)
