<template>
  <div>
    <user-center/>
  </div>
</template>

<script>
  // import UserCenter from '../../common/UserCenter.vue'

  const UserCenter = () => import('../../common/UserCenter.vue')
  export default {
    components: {
      UserCenter
    },
  }
</script>

<style scoped>

</style>
