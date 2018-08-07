import base from './basequery'
import METHOD from './HttpMethod'

export default {
  ROLE: {
    USER: 'USER',
    ADMIN: 'ADMIN',
    PUBLISHER: 'PUBLISHER'
  },
  /**
   *
   * @param username
   * @param password
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
    console.log('in sign up:')
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
    base.query(data, resolve, reject, '/user/info' + '/' + id+'?isChecked=True', METHOD.GET)
  },
  addUserInfo, getUserList, updateUserAuth, getVerifyUserList, verifyOneUser

}

async function getUserList(resolve, reject) {
  console.log('in add userInfo:')
  var data = new FormData()
  base.query(data, resolve, reject, '/user', METHOD.GET)
}

/**
 * @param {function} name
 * @param {function} createTime
 * @param {function} city
 * @param {function} detail
 * @param {function} resolve
 * @param {function} reject
 */
async function addUserInfo(form, resolve, reject) {
  console.log('in add userInfo:');
  var data = new FormData();
  console.log(form);
  data.append('id', form.index);
  data.append('avatarUrl', form.avatarUrl);
  data.append('personUrl', form.personUrl);
  data.append('studentUrl', form.studentUrl);
  data.append('otherUrl', form.otherUrl);
  data.append('graduateUrl', form.otherUrl);
  data.append('phone', form.phone);
  data.append('email', form.email);
  data.append('qq', form.qq);
  data.append('wechat', form.wechat);
  data.append('nickname', form.nickname);
  data.append('gender', form.gender[0]);
  data.append('p_height', form.p_height);
  data.append('birthDate', form.birthDate);
  data.append('marriage', form.marriage[0]);
  data.append('friend', form.friend[0]);
  data.append('hometown', form.hometown);
  data.append('city', form.city);
  data.append('live', form.live);
  data.append('studyState', form.studyState);
  data.append('collageSchool', form.collageSchool);
  data.append('masterSchool', form.masterSchool);
  data.append('doctorSchool', form.doctorSchool);
  data.append('education', form.education[0]);
  data.append('major', form.major);
  data.append('corporation', form.corporation);
  data.append('work_state', form.work_state);
  data.append('career', form.career);
  data.append('corporation_type', form.corporation_type);
  data.append('income', form.income);
  data.append('house_state', form.house_state);
  data.append('family_state', form.family_state);
  data.append('name', form.name);
  data.append('about_you', form.about_you);
  data.append('about_me', form.about_me);
  console.log(data);
  base.query(data, resolve, reject, '/user/info', METHOD.PUT)
}

/**
 *
 * @param userID
 * @param increase
 * @param resolve
 * @param reject
 * @returns {Promise<void>}
 */
async function updateUserAuth(userID, increase, resolve, reject) {
  console.log('in update userAuth:');
  let data = new FormData();
  data.append('userID', userID);
  data.append('increase', increase);
  base.query(data, resolve, reject, '/check', METHOD.PATCH);
}


async function getVerifyUserList(resolve, reject) {
  console.log('in update get verify user list:');
  let data = new FormData();
  base.query(data, resolve, reject, '/user/info', METHOD.GET);
}

async function verifyOneUser(userID, isPass, resolve, reject) {
  console.log('in update get verify user list:');
  let data = new FormData();
  data.append('userID', userID);
  data.append('isPass', isPass);
  base.query(data, resolve, reject, '/user/info', METHOD.PATCH);
}
