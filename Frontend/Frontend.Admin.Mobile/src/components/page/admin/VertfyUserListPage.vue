<template>
  <verify-user-list/>
</template>

<script>
  // import VerifyUserList from '../../common/VerifyUserList.vue';
  const VerifyUserList = () => import('../../common/VerifyUserList.vue')
  export default {
    components: {
      VerifyUserList
    }
  }
</script>

<style scoped>

</style>
