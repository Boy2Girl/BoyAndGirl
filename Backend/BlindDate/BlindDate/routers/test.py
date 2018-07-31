import os

from flask import request
from flask_restplus import Resource, fields, Namespace
from werkzeug.utils import secure_filename

ns = Namespace('test', description='关于用户')

login_parameters = ns.model('LoginParameters', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Test(Resource):

    # @login_require(Role.ADMIN, Role.PUBLISHER, Role.USER)
    @ns.doc('查看产生好感的全部异性')
    @ns.expect(login_parameters)
    def post(self):
        UPLOAD_FOLDER = 'static'
        print(request.form)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename, 200
