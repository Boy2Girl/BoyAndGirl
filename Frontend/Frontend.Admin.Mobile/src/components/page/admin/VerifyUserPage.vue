<template>
  <div>
    <personal-info/>
    <br>
    <br>
    <br>
    <x-button type="primary" style="position: fixed; bottom: 47px; width: 50%; margin-left: 50%"  @click.native="pass">审核通过
    </x-button>
    <x-button type="warn" style="position: fixed; bottom: 47px; width: 50%"  @click.native="reject">审核不通过</x-button>
  </div>
</template>

<script>
  import PersonalInfo from '../../common/PersonalInfo.vue';
  import {XButton} from 'vux';
  import UserApi from '../../../api/user';
  import router from "../../../router";

  export default {
    components: {
      PersonalInfo, XButton
    },
    methods: {
      success(status, text) {
        if (status === 200) {
          router.push('admin/verify');
        } else if (status === 404) {
          console.log("找不到该用户");
        } else if (status === 403) {
          console.log("无权限");
        } else {
          console.log("系统错误");
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err);
      },
      pass() {
        const segments = this.$route.path.split('/');
        const userID = segments[segments.length - 1];
        UserApi.verifyOneUser(userID, true, this.success, this.fail);
      },
      reject() {
        const segments = this.$route.path.split('/');
        const userID = segments[segments.length - 1];
        UserApi.verifyOneUser(userID, false, success, fail);
      }
    }
  }
</script>

<style scoped>

</style>
