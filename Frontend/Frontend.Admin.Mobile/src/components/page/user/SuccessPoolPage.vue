<template>
  <div>
    <pool-tab/>
    <pool-people-list/>
  </div>
</template>

<script>
  import PoolPeopleList from '../../common/PoolPeopleList.vue';
  import Info from '../../common/PersonalInfo.vue';
  import PoolTab from '../../common/PoolTab.vue';

  export default {
    components: {
      PoolTab, PoolPeopleList
    }
  }
</script>

<style scoped>

</style>
