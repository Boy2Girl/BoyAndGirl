from functools import wraps

from flask import json, make_response, request
import config
from factory import DaoFactory
from publicdata import Role
from routers import api
from utils.JwtUtil import JwtUtil


def respond_err(error: str, status_code: int):
    response = make_response(json.dumps({"error": error}))
    response.status_code = status_code
    return response


def login_require(*roles: Role):
    '''
    标记在一个REST的方法上（比如User::get），表示这个方法需要验证是否登录（即是headers里是否有有效的Authorization: Bearer {token}）。
    这也会自动给方法加上api.doc注解，以能在访问API文档的时候提供加入token的选项

    如果没有登录，返回401
    如果已经登录，但是登录的用户角色不包含在参数里，返回403
    否则，在Request Context里增加一项{'current_role': 当前用户User对象}。
    可在接下来的处理中直接通过request.args.get('current_role')取用

    :param roles: 允许的用户的角色
    :return: decorator而已
    '''

    def decorator(func):
        @wraps(func)
        @api.doc(security='apikey')
        def wrapper(*args, **kws):
            print(request.headers)
            token = request.headers.get(config.token_header_key)
            print(token)
            if not token:
                return respond_err("No token", 401)

            token = token.split(config.token_header)[1]
            if not JwtUtil.verify_bearer_token(token):
                return respond_err("Invalid token", 401)
            else:
                username = JwtUtil.get_token_username(token)
                user = DaoFactory.userDao.get_user_by_username(username)

                if not user.role in roles:
                    return respond_err("Bad role", 403)

                request.args.add("current_role", user)
                return func(*args, **kws)

        return wrapper

    return decorator
