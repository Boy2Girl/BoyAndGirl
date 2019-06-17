import base from './basequery'
import METHOD from './HttpMethod'
import dateUtil from '../util/dateUtil'

export default {
  addPosts, recruit_someone, getByUser, get, getMy, isAddedPosts, deletePosts
}

// 判断用户是否发过帖子
async function isAddedPosts(resolve, reject) {
  console.log('in judge:')
  var data = new FormData()
  base.query(data, resolve, reject, '/posts/check', METHOD.POST)
}

async function addPosts(resolve, reject) {
  console.log('in add posts:')
  var data = new FormData()
  data.append('endTime', dateUtil.getNowFormatDate())
  base.query(data, resolve, reject, '/posts', METHOD.PUT)
}

// 删除帖子
async function deletePosts(resolve, reject) {
  console.log('in delete posts:')
  var data = new FormData()
  data.append('endTime', dateUtil.getNowFormatDate())
  base.query(data, resolve, reject, '/posts', METHOD.DELETE)
}

async function recruit_someone(postsID, resolve, reject) {
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

async function get(type, id, search, resolve, reject) {
  console.log('in get all posts')
  var data = new FormData()
  data.append('id', id)
  data.append('type', type)
  base.query(data, resolve, reject, '/posts?id=' + id + '&type=' + type + '&search='+search, METHOD.GET)
}

async function getMy(resolve, reject) {
  console.log('in get my posts:')
  var data = new FormData()
  base.query(data, resolve, reject, '/posts', METHOD.DELETE)
}
