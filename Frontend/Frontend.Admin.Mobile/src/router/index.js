import Vue from 'vue';
// import AdminBaseLayout from '../components/page/admin/BaseLayout';
// import UserBaseLayout from '../components/page/user/BaseLayout';

// import HomePage from '../components/page/common/HomePage';
// import AdminActivityPage from '../components/page/admin/ActivityPage';
// import AdminPoolPage from '../components/page/admin/PoolPage';
// import UserManagementPage from '../components/page/admin/UserManagementPage';
// import ActivityListPage from '../components/page/user/ActivityListPage';
// import UserActivityPage from '../components/page/user/ActivityPage';
// import UserPoolListPage from '../components/page/user/PoolListPage';
// import UserPage from '../components/page/user/UserPage';
// import VerifyUserPage from '../components/page/admin/VerifyUserPage';
// import VertfyUserListPage from '../components/page/admin/VertfyUserListPage';
// import PostsPage from '../components/page/user/PostsPage';
// import AdminPoolAddPage from '../components/page/admin/AdminPoolAddPage';
// import UserPoolDetailPage from '../components/page/user/UserPoolDetailPage';
// import PersonalInfoEditPage from '../components/page/user/PersonalInfoEditPage';
// import PersonalInfoPage from '../components/page/user/PersonalInfoPage';
// import MyPostOnePage from '../components/page/user/MyPostOnePage';
// import OnePostMePage from '../components/page/user/OnePostMePage'
// import PersonalActivityPage from '../components/page/user/PersonalActivityPage';
// import PersonalPoolPage from '../components/page/user/PersonalPoolPage';
// import HistoryActivityPage from '../components/page/user/HistoryActivityPage';
// import FileUpLoader from '../components/common/FileUploader';
// import SuccessPoolPage from '../components/page/user/SuccessPoolPage';
// import PoolPeopleListPage from '../components/page/user/PoolPeopleListPage.vue';
// import PoolMyPeopleListPage from '../components/page/user/PoolMyPeopleListPage.vue';
// import PoolTwoPeopleListPage from '../components/page/user/PoolTwoPeopleListPage.vue';
import {UserType} from "../models/user/UserType";
import VueRouter from 'vue-router';
import CheckApi from '../api/check'

Vue.use(VueRouter);

const routes = [
  {
    path: '/test',
    name: "test",
    component: (resolve) => {require(['../components/common/FileUploader'], resolve)},
    // component: FileUpLoader,
  },
  {
    path: '/user',
    name: "user_base",
    component: (resolve) => {require(['../components/page/user/BaseLayout'], resolve)},
    // component: UserBaseLayout,
    children: [
      {
        path: '',
        component: (resolve) => {require(['../components/page/user/ActivityListPage'], resolve)}
        // component: (()=>import('../components/page/user/ActivityListPage'))
        // component: ActivityListPage
      },
      {
        path: 'login',
        component: (resolve) => {require(['../components/page/common/HomePage'], resolve)}
        // component: (()=>import('../components/page/common/HomePage'))
        // component: HomePage,
      },
      {
        path: 'activity',
        component: (resolve) => {require(['../components/page/user/ActivityListPage'], resolve)},
        // component: (()=>import('../components/page/user/ActivityListPage')),
        // component: ActivityListPage,
        name: "activity"
      },
      {
        path: 'activity/:id',
        component: (resolve) => {require(['../components/page/user/ActivityPage'], resolve)},
        // component: resolve => require(['../components/page/user/ActivityPage'], resolve),
        // component: (()=>import('../components/page/user/ActivityPage'))
        // component: UserActivityPage
      },
      {
        path: 'pool',
        component: (resolve) => {require(['../components/page/user/PoolListPage'], resolve)},
        // component: (()=>import('../components/page/user/PoolListPage')),
        // component: UserPoolListPage,
        name: 'pool',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'pool/:id',
        component: (resolve) => {require(['../components/page/user/UserPoolDetailPage'], resolve)},
        // component: (()=>import('../components/page/user/UserPoolDetailPage')),
        // component: UserPoolDetailPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'poolPeople',
        name: 'poolPeople',
        component: (resolve) => {require(['../components/page/user/PoolPeopleListPage.vue'], resolve)},
        // component: (()=>import('../components/page/user/PoolPeopleListPage.vue')),
        // component: PoolPeopleListPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'poolMyPeople',
        name: 'poolMyPeople',
        component: (resolve) => {require(['../components/page/user/PoolMyPeopleListPage.vue'], resolve)},
        // component: (()=>import('../components/page/user/PoolMyPeopleListPage.vue')),
        // component: PoolMyPeopleListPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'poolTwoPeople',
        name: 'poolTwoPeople',
        component: (resolve) => {require(['../components/page/user/PoolTwoPeopleListPage.vue'], resolve)},
        // component: (()=>import('../components/page/user/PoolTwoPeopleListPage.vue')),
        // component: PoolTwoPeopleListPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        },
      },
      {
        path: 'posts',
        component: (resolve) => {require(['../components/page/user/PostsPage'], resolve)},
        // component: (()=>import('../components/page/user/PostsPage')),
        // component: PostsPage,
        name: 'posts',
        meta: {
          requireAuth: [UserType.USER, UserType.ADMIN, UserType.PUBLISHER],
        }
      },
      {
        path: 'user',
        component: (resolve) => {require(['../components/page/user/UserPage'], resolve)},
        // component: (()=>import('../components/page/user/UserPage')),
        // component: UserPage
      },
      {
        path: 'edit',
        component: (resolve) => {require(['../components/page/user/PersonalInfoEditPage'], resolve)},
        // component: (()=>import('../components/page/user/PersonalInfoEditPage')),
        // component: PersonalInfoEditPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myPostOne',
        component: (resolve) => {require(['../components/page/user/MyPostOnePage'], resolve)},
        // component: (()=>import('../components/page/user/MyPostOnePage')),
        // component: MyPostOnePage,
        name: "myPostOne",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'OnePostMe',
        component: (resolve) => {require(['../components/page/user/OnePostMePage'], resolve)},
        // component: (()=>import('../components/page/user/OnePostMePage')),
        // component: OnePostMePage,
        name: 'OnePostMe',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'info',
        component: (resolve) => {require(['../components/page/user/PersonalInfoPage'], resolve)},
        // component: (()=>import('../components/page/user/PersonalInfoPage')),
        // component: PersonalInfoPage,
        name: 'info',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'info/:id',
        component: (resolve) => {require(['../components/page/user/PersonalInfoPage'], resolve)},
        // component: (()=>import('../components/page/user/PersonalInfoPage')),
        // component: PersonalInfoPage,
        name: 'info',
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myActivity',
        component: (resolve) => {require(['../components/page/user/PersonalActivityPage'], resolve)},
        // component: (()=>import('../components/page/user/PersonalActivityPage')),
        // component: PersonalActivityPage,
        name: "myActivity",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'historyActivity',
        component: (resolve) => {require(['../components/page/user/HistoryActivityPage'], resolve)},
        // component: (()=>import('../components/page/user/HistoryActivityPage')),
        // component: HistoryActivityPage,
        name: "historyActivity",
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'myPool',
        name: 'myPool',
        component: (resolve) => {require(['../components/page/user/PersonalPoolPage'], resolve)},
        // component: (()=>import('../components/page/user/PersonalPoolPage')),
        // component: PersonalPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      },
      {
        path: 'successPool',
        name: 'successPool',
        component: (resolve) => {require(['../components/page/user/SuccessPoolPage'], resolve)},
        // component: (()=>import('../components/page/user/SuccessPoolPage')),
        // component: SuccessPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER, UserType.USER],
        }
      }
    ]
  },
  {
    path: '/admin',
    name: "admin_base",
    component: (resolve) => {require(['../components/page/admin/BaseLayout'], resolve)},
    // component: AdminBaseLayout,
    children: [
      {
        path: '',
        component: (resolve) => {require(['../components/page/common/HomePage'], resolve)},
        // component: (()=>import('../components/page/common/HomePage')),
        // component: HomePage
      },
      {
        path: 'login',
        component: (resolve) => {require(['../components/page/common/HomePage'], resolve)},
        // component: (()=>import('../components/page/common/HomePage')),
        // component: HomePage,
      },
      {
        path: 'activity',
        component: (resolve) => {require(['../components/page/admin/ActivityPage'], resolve)},
        // component: (()=>import('../components/page/admin/ActivityPage')),
        // component: AdminActivityPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'pool',
        component: (resolve) => {require(['../components/page/admin/PoolPage'], resolve)},
        // component: (()=>import('../components/page/admin/PoolPage')),
        // component: AdminPoolPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'poolAdd',
        component: (resolve) => {require(['../components/page/admin/AdminPoolAddPage'], resolve)},
        // component: (()=>import('../components/page/admin/AdminPoolAddPage')),
        // component: AdminPoolAddPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: '/admin/user',
        component: (resolve) => {require(['../components/page/admin/UserManagementPage'], resolve)},
        // component: (()=>import('../components/page/admin/UserManagementPage')),
        // component: UserManagementPage,
        meta: {
          requireAuth: [UserType.ADMIN],
        },
      },
      {
        path: 'verify/:id',
        component: (resolve) => {require(['../components/page/admin/VerifyUserPage'], resolve)},
        // component: (()=>import('../components/page/admin/VerifyUserPage')),
        // component: VerifyUserPage,
        meta: {
          requireAuth: [UserType.ADMIN, UserType.PUBLISHER],
        },
      },
      {
        path: 'verify',
        component: (resolve) => {require(['../components/page/admin/VerifyUserPage'], resolve)},
        // component: (()=>import('../components/page/admin/VerifyUserPage')),
        // component: VertfyUserListPage,
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
  // console.log(text);
  if (status === 401) {
    // console.log('请先登录');
    if(router.app.$route.path.split('/')[1] == 'admin'){
      router.push('/admin');
    }else{
      router.push('/user/login')
    }
  }
  if (status === 200) {
    if (text === 'false') {
      // console.log('没有登陆');
    }
    // console.log("成功");
  } else {
    // console.log("失败");
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
