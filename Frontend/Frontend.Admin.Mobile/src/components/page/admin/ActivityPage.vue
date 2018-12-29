<template>
  <div>
    <admin-activity/>
  </div>
</template>

<script>
  // import AdminActivity from '../../common/AdminActivity.vue';
  const AdminActivity = () => import('../../common/AdminActivity.vue')
  export default {
    components: {
      AdminActivity
    },
  }
</script>

<style scoped>

</style>
