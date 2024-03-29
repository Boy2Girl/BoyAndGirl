import base from './basequery'
import METHOD from './HttpMethod'

export default {
  addActivity, getActivity, registerActivity, getAllActivity, leaveActivity, getByUser, checkRegister, modifyActivity
}

/**
 *
 * @param {function} activityBeginTime
 * @param {function} activityEndTime
 * @param {function}  address
 * @param {function}  registerBeginTime
 * @param {function}  registerEndTime
 * @param {function} selectBeginTime
 * @param {function} selectEndTime
 * @param {function} chargeRule
 * @param {function} boyBeginAge
 * @param {function} girlBeginAge
 * @param {function} increment
 * @param {function} wechat
 * @param {function} detail
 * @param {function} resolve
 * @param {function} reject
 */
async function addActivity(name, url, activityBeginTime,
                           activityEndTime, address, registerBeginTime, registerEndTime, selectBeginTime,
                           selectEndTime, chargeRule, boyBeginAge, girlBeginAge, increment, wechat, detail,
                           resolve, reject) {
  console.log('in add activity:')
  var data = new FormData()
  data.append('name', name)
  data.append('url', url)
  data.append('location', address)
  data.append('registerBeginTime', registerBeginTime)
  data.append('registerEndTime', registerEndTime)
  data.append('selectBeginTime', selectBeginTime)
  data.append('selectEndTime', selectEndTime)
  data.append('chargeRule', chargeRule)
  data.append('boyBeginAge', boyBeginAge)
  data.append('girlBeginAge', girlBeginAge)
  data.append('increment', increment)
  data.append('wechat', wechat)
  // 相对于后端新增的在下面
  data.append('activityBeginTime', activityBeginTime)
  data.append('activityEndTime', activityEndTime)
  data.append('detail', detail)

  base.query(data, resolve, reject, '/activity', METHOD.PUT)
}

async function modifyActivity(id, name, url, activityBeginTime,
                              activityEndTime, address, registerBeginTime, registerEndTime, selectBeginTime,
                              selectEndTime, chargeRule, boyBeginAge, girlBeginAge, increment, wechat, detail,
                              resolve, reject) {
  console.log('in modify activity:')
  var data = new FormData()
  data.append('id', id)
  data.append('name', name)
  data.append('url', url)
  data.append('location', address)
  data.append('registerBeginTime', registerBeginTime)
  data.append('registerEndTime', registerEndTime)
  data.append('selectBeginTime', selectBeginTime)
  data.append('selectEndTime', selectEndTime)
  data.append('chargeRule', chargeRule)
  data.append('boyBeginAge', boyBeginAge)
  data.append('girlBeginAge', girlBeginAge)
  data.append('increment', increment)
  data.append('wechat', wechat)
  // 相对于后端新增的在下面
  data.append('activityBeginTime', activityBeginTime)
  data.append('activityEndTime', activityEndTime)
  data.append('detail', detail)

  base.query(data, resolve, reject, '/activity/'+id, METHOD.PUT)
}

async function getActivity(id, resolve, reject) {
  console.log('in get activity:')
  var data = new FormData()
  base.query(data, resolve, reject, '/activity' + '/' + id, METHOD.GET)
}

async function registerActivity(id, resolve, reject) {
  console.log('in register activity:')
  var data = new FormData()
  data.append('aID', id)
  base.query(data, resolve, reject, '/activity', METHOD.POST)
}

async function leaveActivity(id, resolve, reject) {
  console.log('in leave activity:')
  var data = new FormData()
  data.append('aID', id)
  base.query(data, resolve, reject, '/activity', METHOD.DELETE)
}

async function getAllActivity(begin, isCurrent, resolve, reject) {
  console.log('in register activity:')
  var data = new FormData()
  base.query(data, resolve, reject, '/activity' + '?begin=' + begin + '&isCurrent=' + isCurrent, METHOD.GET)
}


async function getByUser(resolve, reject) {
  console.log('in get by user:')
  var data = new FormData()
  base.query(data, resolve, reject, '/activity', METHOD.PATCH)
}

async function checkRegister(aID, resolve, reject) {
  console.log('in get by user:')
  var data = new FormData()
  // data.append("aID", aID)
  base.query(data, resolve, reject, '/activity/' + aID, METHOD.POST)
}
