import base from './basequery'
import METHOD from './HttpMethod'
export default{
  createOrder
}

// 创建订单
async function createOrder(resolve, reject){
  console.log('in create order:')
  let data = new FormData()
  base.query(data, resolve, reject, '/', METHOD.GET)
}
