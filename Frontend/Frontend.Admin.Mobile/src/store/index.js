import Vue from 'vue'
import Vuex from 'vuex'

import common from './modules/common'

Vue.use(Vuex)

var store = new Vuex.Store({
    modules: {
        common
    }
})

export default store;