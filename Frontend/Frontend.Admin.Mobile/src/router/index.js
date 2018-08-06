import Vue from 'vue';
import AdminBaseLayout from '../components/page/admin/BaseLayout';
import UserBaseLayout from '../components/page/user/BaseLayout';

import HomePage from '../components/page/common/HomePage';
import AdminActivityPage from '../components/page/admin/ActivityPage';
import AdminPoolPage from '../components/page/admin/PoolPage';
import UserManagementPage from '../components/page/admin/UserManagementPage';
import ActivityListPage from '../components/page/user/ActivityListPage';
import UserActivityPage from '../components/page/user/ActivityPage';
import UserPoolListPage from '../components/page/user/PoolListPage';
import UserPage from '../components/page/user/UserPage';
import VerifyUserPage from '../components/page/admin/VerifyUserPage'
import PostsPage from '../components/page/user/PostsPage';
import AdminPoolAddPage from '../components/page/admin/AdminPoolAddPage';
import UserPoolDetailPage from '../components/page/user/UserPoolDetailPage';
import PersonalInfoEditPage from '../components/page/user/PersonalInfoEditPage';
import PersonalInfoPage from '../components/page/user/PersonalInfoPage';
import MyPostOnePage from '../components/page/user/MyPostOnePage';
import OnePostMePage from '../components/page/user/OnePostMePage'
import PersonalActivityPage from '../components/page/user/PersonalActivityPage';
import PersonalPoolPage from '../components/page/user/PersonalPoolPage';
import HistoryActivityPage from '../components/page/user/HistoryActivityPage';
import FileUpLoader from '../components/common/FileUploader';
import SuccessPoolPage from '../components/page/user/SuccessPoolPage';
import PoolPeopleListPage from '../components/page/user/PoolPeopleListPage.vue';
import {UserType} from "../models/user/UserType";
import VueRouter from 'vue-router';
import CheckApi from '../api/check'

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
        component: ActivityListPage
      },
      {
        path: 'login',
        component: HomePage,
      },
      {
        path: 'activity',
        component: ActivityListPage,
        name: "activity"
      },
      {
        path: 'activity/:id',
        component: UserActivityPage
      },
      {
        path: 'pool',
        component: UserPoolListPage,
        name: 'pool',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'pool/:id',
        component: UserPoolDetailPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'poolPeople/:id',
        name: 'poolPeople',
        component: PoolPeopleListPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'posts',
        component: PostsPage,
        name: 'posts',
        meta: {
          requireAuth: [UserType.USER, UserType.ADMIN, UserType.PUBLISHER],
        }
      },
      {
        path: 'user',
        component: UserPage
      },
      {
        path: 'edit',
        component: PersonalInfoEditPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myPostOne',
        component: MyPostOnePage,
        name: "myPostOne",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'OnePostMe',
        component: OnePostMePage,
        name: 'OnePostMe',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'info',
        component: PersonalInfoPage,
        name: 'info',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myActivity',
        component: PersonalActivityPage,
        name: "myActivity",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'historyActivity',
        component: HistoryActivityPage,
        name: "historyActivity",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myPool',
        name: 'myPool',
        component: PersonalPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'successPool',
        name: 'successPool',
        component: SuccessPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
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
        path: 'login',
        component: HomePage,
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
        path: 'poolAdd',
        component: AdminPoolAddPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: '/admin/user',
        component: UserManagementPage,
        meta: {
          requireAuth: [UserType.ADMIN],
        },
      },
      {
        path: 'verify',
        component: VerifyUserPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      }
    ]
  }
];

const router = new VueRouter({
  routes
});

export default router;

function success(status, text) {
  console.log(text);
  if (status === 401) {
    console.log('请先登录');
    router.push('/user/login');
  }
  if (status === 200) {
    if (text === 'false') {
      console.log('没有登陆');
    }
    console.log("成功");
  } else {
    console.log("失败");
    // this.$router.push({
    //   path: '/login',
    //   query: {
    //     redirect: location.hostname
    //   }
    // });
    //window.location='http://localhost:8081/#/login';
  }
}

function fail(err) {
  console.log("错误发生了")
  console.log(err)
}

router.beforeEach((to, from, next) => {
  console.log("进入拦截");
  if (to.meta.requireAuth) {//查看是否需要权限登陆
    CheckApi.check(success, fail)
    next()
  } else {
    next()
  }
});
//   fetch('http://127.0.0.1:5000/api/'+"user/checkState", {
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
