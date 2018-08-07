import base from './basequery'
import METHOD from './HttpMethod'
export default{
  addPosts,recruit_someone,getByUser,get,getMy
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

async function get(type, id, resolve, reject) {
    console.log('in get all posts');
    var data = new FormData();
    data.append('id', id);
    data.append('type', type);
    base.query(data, resolve, reject, '/posts?id='+id+'&type='+type, METHOD.GET)
}

async function getMy(resolve, reject) {
    console.log('in get my posts:')
    var data = new FormData()
    base.query(data, resolve, reject, '/posts', METHOD.DELETE)
}
