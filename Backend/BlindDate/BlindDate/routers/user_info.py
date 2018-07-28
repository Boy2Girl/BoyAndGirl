from flask import request
from flask_restplus import Resource, Namespace

ns = Namespace('user/info', description='关于用户信息')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class User(Resource):

    @ns.doc('修改')
    @ns.expect()
    def post(self):
        username = request.form['username']
        password = request.form['password']
        # return userBl.check_user(UserModel(username, password)), 200, {}
        return 123

    @ns.doc('填写')
    def put(self):
        # TestModel("law")
        username = request.form['username']
        password = request.form['password']
        # userBl.save_user(UserModel(username, password))
        return None, 200, {}
