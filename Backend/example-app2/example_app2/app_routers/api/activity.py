# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Activity(Resource):

    def get(self):
        print(g.args)

        return None, 200, {}

    def post(self):
        print(g.args)

        return None, 200, {}

    def put(self):
        print(g.args)

        return None, 200, {}