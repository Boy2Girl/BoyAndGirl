<template>
  <div>
    <pool-tab/>
    <pool-list/>
  </div>
</template>

<script>
  import PoolList from '../../common/PoolList.vue';
  import PoolTab from '../../common/PoolTab.vue';

  export default {
    components: {
      PoolList, PoolTab
    },
  }
</script>

<style scoped>

</style>
