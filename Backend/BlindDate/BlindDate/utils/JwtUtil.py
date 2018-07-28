import jwt
import time

import config


class JwtUtil(object):
    @staticmethod
    def create_token(username):
        payload = {
            "iat": int(time.time()),
            "exp": int(time.time()) + 86400 * 7,
            "username": username,
            "scopes": ['open']
        }
        token = jwt.encode(payload, config.secret, algorithm='HS256')
        return token

    @staticmethod
    def verify_bearer_token(token):
        payload = jwt.decode(token, config.secret, algorithms=['HS256'])
        if payload:
            return True
        return False
