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
        token = str(jwt.encode(payload, config.secret, algorithm='HS256'), encoding="utf-8")
        return token

    @staticmethod
    def verify_bearer_token(token):
        payload = jwt.decode(token, config.secret, algorithms=['HS256'])
        if payload:
            return True
        return False

    @staticmethod
    def get_token_username(token):
        if config.token_header in token:
            token = token.split(config.token_header)[1]
        payload = jwt.decode(token, config.secret, algorithms=['HS256'])
        return payload["username"]
