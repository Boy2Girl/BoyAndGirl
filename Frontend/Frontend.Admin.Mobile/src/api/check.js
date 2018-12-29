import base from './basequery'
import METHOD from './HttpMethod'

export default {
  check
}

async function check(resolve, reject) {
  console.log('in check:');
  let data = new FormData();
  base.query(data, resolve, reject, '/check', METHOD.POST)
}
