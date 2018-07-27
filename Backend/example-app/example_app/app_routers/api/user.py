# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class User(Resource):

    def post(self):

        return None, 200, None

    def get(self):

        return "???", 200, "???"

    def put(self):

        return None, 201, None