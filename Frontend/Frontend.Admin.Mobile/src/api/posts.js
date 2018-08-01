import base from './basequery'
import METHOD from './HttpMethod'
export default{
  addPosts,recruit_someone
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