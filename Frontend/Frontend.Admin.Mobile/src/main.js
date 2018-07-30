// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from "./router";
import 'iview/dist/styles/iview.css';
import iView from 'iview';
import "font-awesome.css";
import initRichText from './util/initHTMLEditor';

initRichText();
Vue.use(iView);
console.log(router);
Vue.config.productionTip = false;
const myVue = new Vue({
  router,
  render: h => h(App)
}).$mount('#app-box');
