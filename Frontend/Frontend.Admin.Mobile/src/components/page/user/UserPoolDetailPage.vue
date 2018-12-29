<template>
  <div>
    <user-pool-detail/>
  </div>
</template>

<script>
  // import UserPoolDetail from '../../common/UserPoolDetail.vue'
  const UserPoolDetail = () => import('../../common/UserPoolDetail.vue')
  export default {
    components: {
      UserPoolDetail
    },
  }
</script>

<style scoped>

</style>
