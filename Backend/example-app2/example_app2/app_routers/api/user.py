# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class User(Resource):

    def post(self):
        params = request.args
        print(params)
        return None, 200, {}

    def put(self):
        username = request.form
        print(username['username'])
        return None, 200, {}