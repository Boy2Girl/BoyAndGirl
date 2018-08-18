<template>
  <user-activity/>
</template>

<script>
  // import UserActivity from '../../common/UserActivity.vue';
  const UserActivity = () => import('../../common/UserActivity.vue')
  export default {
    components: {
      UserActivity
    },
  }
</script>

<style scoped>

</style>
