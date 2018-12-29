<template>
  <activity-list/>
</template>

<script>
  // import ActivityList from '../../common/ActivityList.vue';

  const ActivityList = () => import('../../common/ActivityList.vue')

  export default {
    components: {
      ActivityList
    },
  }
</script>

<style scoped>

</style>
