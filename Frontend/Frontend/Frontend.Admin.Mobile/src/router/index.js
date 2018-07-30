import Vue from 'vue';
import BaseLayout from '../components/page/BaseLayout';
import HomePage from '../components/page/HomePage.vue';
import ActivityPage from '../components/page/ActivityPage.vue';
import PoolPage from '../components/page/PoolPage.vue';
import UserManagementPage from '../components/page/UserManagementPage.vue';
import {UserType} from "../models/user/UserType";
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: "base",
    component: BaseLayout,
    children: [
      {
        path: '',
        component: HomePage
      },
      {
        path: '/activity',
        component: ActivityPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: '/pool',
        component: PoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: '/user',
        component: UserManagementPage,
        meta: {
          requireAuth: [UserType.ADMIN],
        },
      }
    ]
  }
];

const router = new VueRouter({
  routes
});

export default router;

// router.beforeEach((to, from, next) => {
//   console.log("进入拦截");
//   next();
// if (to.meta.requireAuth) {
//   fetch(address+"user/checkState", {
//     method: 'get',
//     credentials: 'include',
//   }).then(res => {
//     return res.text()
//   }).then(text => {
//     console.log(text)
//     if (text!="false") {
//       let data1 = new FormData();
//       data1.append('userID',text);
//       fetch(address+"user/info", {
//         method: 'post',
//         body:data1,
//         credentials: 'include',
//       }).then(res => {
//         return res.text()
//       })
//         .then(text => {
//           //   var name = this.$route.query.redirect;
//           //  console.log(name)
//           var user = JSON.parse(text);
//           myVue.$store.state.name=user.name;
//           myVue.$store.state.userName = user.username;
//           myVue.$store.state.picture = user.picture;
//           console.log(myVue.$store.state)
//           // console.log(text)
//           //  this.$router.push({name:name,query:{redirect:this.name}})
//         })
//
//       // myVue.$store.state.name=text;
//       next();
//     }
//     else {
//       next({
//         path: '/login',
//         query: {redirect: to.name}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
//       })
//     }
//   })
//
// }
// else {
//   next();
// }
// });
