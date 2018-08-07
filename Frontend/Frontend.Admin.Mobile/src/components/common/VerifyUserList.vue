<template>
  <div>
    <div style="margin:5%">
      <Input v-model="keyId" style="margin-bottom:5%" size="large" search enter-button placeholder="输入用户名以搜索用户"
             @input="search"/>
      <Table border stripe :columns="userList" :data="userData"></Table>
    </div>
  </div>
</template>

<script>
  import UserApi from '../../api/user';
  import router from "../../router";

  export default {
    data() {
      return {
        keyId: "",
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
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary'
                  },
                  on: {
                    click: () => {
                      router.push('/admin/verify/' + this.userData[params.index].uID);
                    }
                  }
                }, '审核')
              ]);

            }
          }
        ],
        rawUserData: [],
        userData: []
      }
    },
    methods: {
      search: function () {
        let result = [];
        for (let i = 0; i < this.rawUserData.length; i++) {
          if ((this.rawUserData[i].uID + "").indexOf(this.keyId) >= 0) {
            result.push(this.rawUserData[i]);
          }
        }
        this.userData = result;
      },
      loadUserList: function () {
        UserApi.getVerifyUserList(this.success, this.fail);
      },
      success: function (status, text) {
        let that = this;
        if (status === 200) {
          let result = JSON.parse(text);
          console.log(result)
          console.log(result.length);
          this.rawUserData = that.listConvert(result);
          this.userData = this.rawUserData;
          this.search();
        } else if (status === 500) {
          console.log("加载失败");
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err);
      },
      listConvert: function (userList) {
        let result = [];
        for (let i = 0; i < userList.length; i++) {
          let user = {
            "uID": userList[i].id,
            "username": userList[i].username,
            "password": userList[i].password,
            "role": userList[i].role,
          };
          result.push(user);
        }
        return result;
      }
    },
    mounted() {
      this.loadUserList();
    }
  }
</script>

<style scoped>
</style>
