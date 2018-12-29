from flask_restplus import Resource, fields, Namespace
from wechatpy import WeChatPay

import config
from exceptions import PasswordWrongException, NotFoundException

ns = Namespace('user', description='关于用户（登录注册）')

pay_parameters = ns.model('PayParameters', {
    'username': fields.String(required=True, description='用户名'),
    'money': fields.Float(required=True, description='金额')
})

pay_parser = ns.parser()
pay_parser.add_argument('username', type=str, help='用户名', location='form')
pay_parser.add_argument('money', type=float, help='金额', location='form')


@ns.route('')
@ns.response(200, 'OK')
@ns.response(404, '没有找到用户名或者密码')
@ns.response(403, '用户名或者密码不正确')
@ns.response(500, '内部错误')
class Pay(Resource):
    wechat_pay = WeChatPay(appid=config.app_id, api_key=config.app_key, mch_id=config.mch_id,
                           mch_cert=config.mch_cert, mch_key=config.mch_key)
    wechat_order = wechat_pay.order
    wechat_jsapi = wechat_pay.jsapi

    @ns.doc(decription="支付")
    @ns.expect(pay_parser)
    def post(self):
        try:
            total_fee = 1
            open_id = "o0brw0vGiaeGMmezMumz2MJ3T4s4"
            order_params = self.wechat_order.create(trade_type="JSAPI", body=config.body, total_fee=total_fee,
                                                    notify_url=config.notify_url, user_id=open_id)
            print(order_params)
            prepay_id = order_params.prepay_id
            pay_params = self.wechat_order.get_jsapi_params(prepay_id, jssdk=True)
            print(pay_params)
            return pay_params, 200
        except PasswordWrongException:
            return {'error': 'wrong password'}, 403
        except NotFoundException:
            return {'error': 'user not found'}, 404
