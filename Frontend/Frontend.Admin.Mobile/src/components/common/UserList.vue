<template>
  <div>
    <div style="margin:5%">
      <Input style="margin-bottom:5%" size="large" search enter-button placeholder="输入用户名以搜索用户"/>
      <Table border stripe :columns="userList" :data="userData"></Table>
    </div>
    <x-button type="primary" style="position:fixed; bottom: 47px;" link="/admin/verify">审核用户</x-button>
  </div>
</template>

<script>
  import {UserType} from "../../models/user/UserType";
  import {XButton} from "vux";
  import UserApi from '../../api/user';

  export default {
    components: {
      XButton
    },
    data() {
      return {
        userList: [
          {
            title: 'ID',
            key: 'uID',
            fixed: 'left'
          },
          {
            title: '用户名',
            key: 'username',
          },
          {
            title: '操作',
            key: 'action',
            render: (h, params) => {
              if (this.userData[params.index].role === UserType.USER) {
                return h('div', [
                  h('Button', {
                    props: {
                      type: 'primary'
                    },
                    on: {
                      click: () => {

                      }
                    }
                  }, '给予权限')
                ]);
              }
              else {
                return h('div', [
                  h('Button', {
                    props: {
                      type: 'error'
                    },
                    on: {
                      click: () => {

                      }
                    }
                  }, '剥夺权限')
                ]);
              }
            }
          }
        ],
        userData: [
          {
            uID: '1312312312',
            username: '123',
            password: '123',
            role: UserType.USER
          },
          {
            uID: '2',
            username: '1234',
            password: '1235',
            role: UserType.PUBLISHER
          },
          {
            uID: '3',
            username: '1238',
            password: '1239',
            role: UserType.ADMIN
          },
          {
            uID: '4',
            username: '54',
            password: '46',
            role: UserType.USER
          }
        ]
      }
    },
    methods: {
      success: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text);
          console.log(result);
          this.poolPeopleList = result
        } else if (status === 500) {
          console.log("上传互选池失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err)
      },
    },
    mounted() {
      UserApi.getUserList(this.success, this.fail);
    }
  }
</script>

<style scoped>
</style>
