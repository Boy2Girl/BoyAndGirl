import os

from flask import request
from flask_restplus import Resource, fields, Namespace
from werkzeug.utils import secure_filename

ns = Namespace('test', description='关于上传文件使用')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, 'user not found')
@ns.response(403, 'access denied')
@ns.response(500, 'system error')
class Test(Resource):

    @ns.doc('上传文件使用')
    def post(self):
        UPLOAD_FOLDER = 'static'
        print(request.form)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename, 200
