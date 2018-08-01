// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from "./router";
import 'iview/dist/styles/iview.css';
import iView from 'iview';
import store from './store'
import "font-awesome.css";
import initRichText from './util/initHTMLEditor';
import {WechatPlugin, AjaxPlugin} from 'vux'

Vue.use(WechatPlugin);
Vue.use(AjaxPlugin);

Vue.http.get('/api', ({data}) => {
  Vue.wechat.config(data.data)
});
initRichText();
Vue.use(iView);
console.log(router);
Vue.config.productionTip = false;
const myVue = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app-box');
