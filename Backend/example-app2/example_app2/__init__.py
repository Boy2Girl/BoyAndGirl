# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import app_routers


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        app_routers.bp,
        url_prefix='/app/routers')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)