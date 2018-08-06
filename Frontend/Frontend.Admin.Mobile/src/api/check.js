import base from './basequery'
import METHOD from './HttpMethod'

export default {
  check
}

async function check(resolve, reject) {
  console.log('in add posts:');
  let data = new FormData();
  base.query(data, resolve, reject, '/check', METHOD.POST)
}
