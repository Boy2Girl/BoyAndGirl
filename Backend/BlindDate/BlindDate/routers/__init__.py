from flask import Blueprint
from flask_restplus import Api

api_blueprint = Blueprint("open_api", __name__, url_prefix="/api")
api = Api(api_blueprint, version='1.0', title='交友类小程序后端',
          description='交友类小程序后端api')

# schema_activity = api.model('SchemaActivity', {
#     'url': fields.String(required=True, description='活动网址'),
#     'title': fields.String(required=True, description='活动标题')
# })
