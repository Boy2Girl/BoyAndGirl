# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['DEBU G'] = True
    app.config['SECRET_KEY'] = 'wfhg9hr-1jfpjf-p3j-=vgf0pvmo3k=2-3rj0-3j=gn[=3-g[mj'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test'
    return app


def create_db(app):
    print("create db")
    db = SQLAlchemy(app)
    return db


def register(app):
    import app_routers
    app.register_blueprint(
        app_routers.bp,
        url_prefix='/app/routers')


app = create_app()
db = create_db(app)
session = db.session

db.create_all()

if __name__ == '__main__':
    register(app)
    app.run(debug=True)
