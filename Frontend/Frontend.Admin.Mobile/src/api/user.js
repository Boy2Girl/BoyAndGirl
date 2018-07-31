import base from './basequery'
import METHOD from './HttpMethod'
export default{
    ROLE : {
        USER: 'USER',
        ADMIN: 'ADMIN',
        PUBLISHER: 'PUBLISHER'
    },
  /**
     *
     * @param {String} userName
     * @param {String} passWord
     * @param {???} role
     * @param {function} resolve
     * @param {function} reject
     */
  signIn: async function (username, password, role, resolve, reject) {
    console.log('in log in:')
    console.log(username + ':' + password + ':' + role)
    var data = new FormData()
    data.append('username', username)
    data.append('password', password)
    data.append('role', role)
    base.query(data, resolve, reject, '/user', METHOD.POST)
  },

  /**
     *
     * @param {String} userName
     * @param {String} passWord
     * @param {String} role
     * @param {function} resolve
     * @param {function} reject
     */
  signUp: async function (userName, password, role, resolve, reject) {
    console.log('in sign in:')
    console.log(userName + ':' + password + ':' + role)
    var data = new FormData()
    data.append('username', userName)
    data.append('password', password)
    data.append('role', role)
    base.query(data, resolve, reject, '/user', METHOD.PUT)
  },
   /**
     * @param {Integer} id
     * @param {String} passWord
     * @param {function} reject
     */
  getUserInfo: async function (id, resolve, reject) {
    console.log('in get user info:')
    var data = new FormData()
    base.query(data, resolve, reject, '/user/info'+'/'+id, METHOD.GET)
  }

}
