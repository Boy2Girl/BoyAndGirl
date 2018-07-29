import flask
from flask import json

from config import token_header
from factory import DaoFactory
from publicdata import Role
from utils.JwtUtil import JwtUtil


def login_require(*roles):
    def decorator(func):
        def wrapper(*args, **kws):
            token = ""
            try:
                token = flask.request.headers.get("token").split(token_header)[1]
            except:
                response = flask.make_response(json.dumps(
                    {"error": "access denied"}))
                response.status_code = 403
                return response
            if not JwtUtil.verify_bearer_token(token):
                response = flask.make_response(json.dumps(
                    {"error": "wrong token"}))
                response.status_code = 403
                return response
            else:
                username = JwtUtil.get_token_username(token)
                role = DaoFactory.userDao.get_user_by_username(username).role
                for i in range(roles.__len__()):
                    if role == roles[i]:
                        return func(*args, **kws)
                response = flask.make_response(json.dumps(
                    {"error": "access denied"}))
                response.status_code = 403
                return response

        return wrapper

    return decorator
