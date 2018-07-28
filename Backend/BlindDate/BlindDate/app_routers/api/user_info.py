# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from ..validators import request_validate, response_filter
from flask import request, g

from . import Resource
from .. import schemas


class UserInfo(Resource):
    @response_filter
    def get(self):

        return "hhh", 200, "hhhh"

    def put(self):

        return None, 200, None