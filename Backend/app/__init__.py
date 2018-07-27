# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routers.user import user


app = Flask(__name__, static_folder="static")
app.config['DEBU G'] = True
app.config['SECRET_KEY'] = 'wfhg9hr-1jfpjf-p3j-=vgf0pvmo3k=2-3rj0-3j=gn[=3-g[mj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test'
db = SQLAlchemy(app)
session = db.session
app.register_blueprint(user)


if __name__ == '__main__':
    app.run(port=8080)

