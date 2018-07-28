# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'wfhg9hr-1jfpjf-p3j-=vgf0pvmo3k=2-3rj0-3j=gn[=3-g[mj'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/BoyAndGirl'

    return app


def create_db(app):
    print("create db")
    db = SQLAlchemy(app)
    return db


def register_api():
    from routers.user import ns as user_ns
    from routers.user_info import ns as user_info_ns
    from routers import api
    api.add_namespace(user_ns)
    api.add_namespace(user_info_ns)


def register(app):
    from routers import api_blueprint
    app.register_blueprint(api_blueprint)


app = create_app()
db = create_db(app)
session = db.session


if __name__ == '__main__':
    register_api()
    register(app)
    app.run(debug=True)
