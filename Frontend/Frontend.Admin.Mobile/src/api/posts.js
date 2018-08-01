import base from './basequery'
import METHOD from './HttpMethod'
export default{
  addPosts,recruit_someone,getByUser,getAll,getMy
}
/**
   * @param {function} name
   * @param {function} createTime
   * @param {function} city
   * @param {function} detail
   * @param {function} resolve
   * @param {function} reject
*/
async function addPosts(resolve, reject) {
    console.log('in add posts:')
    var data = new FormData()
    data.append('endTime', "2018-7-12")
    base.query(data, resolve, reject, '/posts', METHOD.PUT)
}


async function recruit_someone(postsID,resolve, reject) {
    console.log('in add posts:')
    var data = new FormData()
    data.append('postsID', postsID)
    base.query(data, resolve, reject, '/posts', METHOD.POST)
}

async function getByUser(resolve, reject) {
    console.log('in add posts:')
    var data = new FormData()
    base.query(data, resolve, reject, '/posts', METHOD.PATCH)
}

async function getAll(resolve, reject) {
    console.log('in add posts:')
    var data = new FormData()
    base.query(data, resolve, reject, '/posts', METHOD.GET)
}

async function getMy(resolve, reject) {
    console.log('in add posts:')
    var data = new FormData()
    base.query(data, resolve, reject, '/posts', METHOD.DELETE)
}