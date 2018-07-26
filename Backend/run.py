# -*- coding: utf-8 -*-
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    json,
    render_template,
    request,
    url_for,
)
from app.factory.DaoFactory import userDao
from app.model.User import User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'wfhg9hr-1jfpjf-p3j-=vgf0pvmo3k=2-3rj0-3j=gn[=3-g[mj'

if __name__ == '__main__':
    app.run(port=8080)
