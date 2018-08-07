<template>
  <div>
    <pool-tab/>
    <pool-list/>
  </div>
</template>

<script>
  import PoolPeopleList from '../../common/PoolPeopleList.vue';
  import PoolTab from '../../common/PoolTab.vue';
  import PoolList from '../../common/PoolList.vue';

  export default {
    components: {
      PoolTab, PoolPeopleList,PoolList
    }
  }
</script>

<style scoped>

</style>
