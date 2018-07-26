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
from app.factory.DataFactory import userData
from app.model.User import User


@app.route('/')
def show_posts():
    return redirect('http://0.0.0.0:8000/static/swagger-ui/index.html')


@app.route('/user', methods=['POST'])
def sign_up():
    data = json.loads(request.form.data, encoding="utf-8")
    user = User()
    user.userName = "123"
    user.passWord = "123"
    user.email = data["email"]
    return userData.save_user(user=user)
