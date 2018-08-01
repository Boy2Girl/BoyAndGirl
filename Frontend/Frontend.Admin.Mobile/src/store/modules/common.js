export default {
    state: {
      debug: true,
      token: "111",
      user_id: ""
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
    },
    getters: {
      getToken: state  => {
        return localStorage.getItem('token')
      },
      getUserID: state  => {
        return localStorage.getItem('userID')
      },
    }
}