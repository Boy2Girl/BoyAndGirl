<template>
  <div style="margin:5%">
    <Input style="margin-bottom:5%" size="large" search enter-button placeholder="输入用户名以搜索用户"/>
    <Table border stripe :columns="userList" :data="userData"></Table>
  </div>
</template>

<script>
  import {UserType} from "../../models/user/UserType";

  export default {
    data() {
      return {
        userList: [
          {
            title: 'ID',
            key: 'uID',
            width: 100,
            fixed: 'left'
          },
          {
            title: '用户名',
            key: 'username',
            width: 100
          },
          {
            title: '密码',
            key: 'password',
            width: 100
          },
          {
            title: '性别',
            key: 'sex',
            width: 100
          },
          {
            title: '操作',
            key: 'action',
            width: 100,
            render: (h, params) => {
              console.log(params.index);
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
            sex: '男',
            role: UserType.USER
          },
          {
            uID: '2',
            username: '1234',
            password: '1235',
            sex: '男',
            role: UserType.PUBLISHER
          },
          {
            uID: '3',
            username: '1238',
            password: '1239',
            sex: '男',
            role: UserType.ADMIN
          },
          {
            uID: '4',
            username: '54',
            password: '46',
            sex: '男',
            role: UserType.USER
          }]
      }
    }
  }
</script>

<style scoped>
</style>
