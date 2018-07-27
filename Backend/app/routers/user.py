# -*- coding: utf-8 -*-
from flask import (
    redirect,
    json,
    request,
    Blueprint)
from app.factory.DataFactory import userData
from app.model.User import User
user = Blueprint('user', __name__)


@user.route('/')
def show_posts():
    return redirect('http://0.0.0.0:8000/static/swagger-ui/index.html')


@user.route('/user', methods=['POST'])
def sign_up():
    print("aaa")
    data = json.loads(request.form.data, encoding="utf-8")
    user = User()
    user.userName = "123"
    user.passWord = "123"
    user.email = data["email"]
    return userData.save_user(user=user)
    return "receive"
