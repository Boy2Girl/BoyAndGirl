// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from "./router";
import 'iview/dist/styles/iview.css';
import store from './store'
// import "font-awesome.css";
import initRichText from './util/initHTMLEditor';
import {ConfirmPlugin, WechatPlugin, LoadingPlugin, ToastPlugin, AlertPlugin} from 'vux'

Vue.use(AlertPlugin);
Vue.use(ToastPlugin);
Vue.use(LoadingPlugin);
Vue.use(ConfirmPlugin);
Vue.use(WechatPlugin);
// Vue.use(AjaxPlugin);

// Vue.http.get('/api', ({data}) => {
//   Vue.wechat.config(data.data)
// });
initRichText();
console.log(router);
Vue.config.productionTip = false;
const myVue = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app-box');
