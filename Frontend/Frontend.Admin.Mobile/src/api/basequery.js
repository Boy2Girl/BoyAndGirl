export default {
  // baseUrl: 'http://www.injusalon.com:5000/api',
  baseUrl: 'http://www.queqiaolianyi.online:5000/api',
  // baseUrl: 'http://127.0.0.1:5000/api',

  query
}

/**
 *
 * @param {*} params
 * @param {*} resolve
 * @param {*} reject
 * @param {*} root
 * @param method
 */
async function query(params, resolve, reject, root, method) {
  // console.log('in base query:' + root);
  // console.log(params);
  try {
    let request = {};
    var headers = new Headers();
    headers.append('token', 'Bearer '+localStorage.getItem('token'));
    request.headers = headers;
    request.method = method;
    if (method !== 'GET' && method !== 'HEAD') request.body = params;
    let res = await fetch(this.baseUrl + root, request)
    let result = await res.text();
    resolve(res.status, result)
  } catch (e) {
    reject(e)
  }
}
