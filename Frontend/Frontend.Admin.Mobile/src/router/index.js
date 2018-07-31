import Vue from 'vue';
import AdminBaseLayout from '../components/page/admin/BaseLayout';
import UserBaseLayout from '../components/page/user/BaseLayout';

import HomePage from '../components/page/common/HomePage';
import AdminActivityPage from '../components/page/admin/ActivityPage';
import AdminPoolPage from '../components/page/admin/PoolPage';
import UserManagementPage from '../components/page/admin/UserManagementPage';
import ActivityListPage from '../components/page/user/ActivityListPage';
import UserActivityPage from '../components/page/user/ActivityPage';
import UserPoolPage from '../components/page/user/PoolPage';
import UserPage from '../components/page/user/UserPage';
import PostsPage from '../components/page/user/PostsPage';

import FileUpLoader from '../components/common/FileUploader';

import {UserType} from "../models/user/UserType";
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/test',
    name: "test",
    component: FileUpLoader,
  },
  {
    path: '/user',
    name: "user_base",
    component: UserBaseLayout,
    children: [
      {
        path: '',
        component: HomePage
      },
      {
        path: 'list',
        component: ActivityListPage
      },
      {
        path: 'activity',
        component: UserActivityPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'pool',
        component: UserPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'posts',
        component: PostsPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'user',
        component: UserPage,
        meta: {
          requireAuth: [UserType.ADMIN],
        },
      }
    ]
  },
  {
    path: '/admin',
    name: "admin_base",
    component: AdminBaseLayout,
    children: [
      {
        path: '',
        component: HomePage
      },
      {
        path: 'activity',
        component: AdminActivityPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'pool',
        component: AdminPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'user',
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
