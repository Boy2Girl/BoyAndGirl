# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g ,make_response,Response
import flask
from . import Resource
from ..validators import request_validate, response_filter

from factory.BlFactory import userBl
from model import UserModel


class User(Resource):

    """ 登录 """
    def post(self):
        username = request.form['username']
        password = request.form['password']
        result = userBl.check_user(UserModel(username, password))
        print(result)
        return {"aa"}, 400, "123456"


    """ 注册 """
    @response_filter
    def put(self):
        # TestModel("law")
        username = request.form['username']
        password = request.form['password']
        userBl.save_user(UserModel(username, password))
        rsp = make_response('pong')
        rsp.mimetype = 'text/plain'
        rsp.headers['x-tag'] = 'sth. magic'
        return {"aa":11}, 200, rsp