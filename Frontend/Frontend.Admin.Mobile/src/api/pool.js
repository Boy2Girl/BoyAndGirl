import base from './basequery'
import METHOD from './HttpMethod'
export default{
  addPool,getPool,registerPool,getAllPool,getPoolByUser
}
/**
   * @param {function} name
   * @param {function} createTime
   * @param {function} city
   * @param {function} detail
   * @param {function} resolve
   * @param {function} reject
*/
async function addPool(url,name,createTime,city,
    detail,resolve, reject) {
    console.log('in add activity:')
    var data = new FormData()
    data.append('url', url)
    data.append('createTime', createTime)
    data.append('name', name)
    data.append('city', city)
    data.append('detail', detail)
    data.append('requirement', "")
    base.query(data, resolve, reject, '/pool', METHOD.PUT)
}


async function getPool(id,resolve, reject){
    console.log('in get pool:')
    var data = new FormData()
    base.query(data, resolve, reject, '/pool'+'/'+id, METHOD.GET)
}           

async function registerPool(id, resolve, reject){
    console.log('in register activity:')
    var data = new FormData()
    data.append('pID', id)
    base.query(data, resolve, reject, '/pool', METHOD.POST)
}                           

async function getAllPool(begin, resolve, reject){
    console.log('in get pool list:')
    var data = new FormData()
    base.query(data, resolve, reject, '/pool'+'?begin='+begin, METHOD.GET)
}

async function getPoolByUser(resolve, reject){
    console.log('in get pool list:')
    var data = new FormData()
    base.query(data, resolve, reject, '/pool', METHOD.PATCH)
}