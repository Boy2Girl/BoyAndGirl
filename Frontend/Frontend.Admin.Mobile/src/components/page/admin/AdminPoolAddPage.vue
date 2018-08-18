<template>
  <div>
    <admin-pool-detail/>
  </div>
</template>

<script>
  // import AdminPoolDetail from '../../common/AdminPoolDetail.vue'
  const AdminPoolDetail = () => import('../../common/AdminPoolDetail.vue')
  export default {
    components: {
      AdminPoolDetail
    },
  }
</script>

<style scoped>

</style>
