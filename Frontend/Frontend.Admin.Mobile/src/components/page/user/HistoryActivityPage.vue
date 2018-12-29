<template>
  <div>
    <activity-tab/>
    <activity-card-list/>
  </div>
</template>

<script>
  // import ActivityCardList from '../../common/ActivityCardList.vue';
  // import ActivityTab from '../../common/ActivityTab';

  const ActivityCardList = () => import('../../common/ActivityCardList.vue')
  const ActivityTab = () => import('../../common/ActivityTab')

  export default {
    components: {
      ActivityCardList, ActivityTab
    },
  }
</script>

<style scoped>

</style>
