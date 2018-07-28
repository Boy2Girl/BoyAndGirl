# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from model import TestModel
from . import Resource

from factory.BlFactory import userBl
from model import UserModel

class User(Resource):


    """ 登录 """
    def post(self):

        return None, 200, {}

    """ 注册 """
    def put(self):
        # TestModel("law")
        username = request.form['username']
        password = request.form['password']
        userBl.save_user(UserModel(username, password))
        return None, 200, {}