<template>
  <div>
    <user-tab/>
    <verify-user-list/>
  </div>
</template>

<script>
  // import VerifyUserList from '../../common/VerifyUserList.vue';
  import UserTab from "../../common/UserTab"

  const VerifyUserList = () => import('../../common/VerifyUserList.vue')
  export default {
    components: {
      UserTab,
      VerifyUserList
    }
  }
</script>

<style scoped>

</style>
