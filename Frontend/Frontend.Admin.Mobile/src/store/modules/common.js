export default {
    state: {
      debug: false,
      token: "",
      user_id: "",
      pool_id: "",
      isLogIn: false
    },
    mutations: {
      setToken (state, payload) {
        if (state.debug) {
          console.log('token user changed in vuex')
          console.log(payload)
        }
        state.token = payload
        localStorage.setItem('token', payload)
      },
      setUserID (state, payload) {
        if (state.debug) {
          console.log('token user changed in vuex')
          console.log(payload)
        }
        state.user_id = payload
        localStorage.setItem('userID', payload)
      },
      setPoolID (state, payload) {
        if (state.debug) {
          console.log('token user changed in vuex')
          console.log(payload)
        }
        state.pool_id = payload
        localStorage.setItem('poolID', payload)
      },
      setIsLogin (state, payload) {
        if (state.debug) {
          console.log('islogin changed in vuex')
          console.log(payload)
        }
        state.isLogIn = state
        localStorage.setItem('isLogIn', payload)
      },
    },
    getters: {
      getToken: state  => {
        return localStorage.getItem('token')
      },
      getUserID: state  => {
        return localStorage.getItem('userID')
      },
      getPoolID: state  => {
        return localStorage.getItem('poolID')
      },
      getIsLogIn: state => {
        return localStorage.getItem('isLogIn')
      }
    }
}
