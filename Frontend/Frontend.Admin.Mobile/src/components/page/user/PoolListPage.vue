<template>
  <div>
    <pool-tab/>
    <area-picker/>
    <pool-list/>
  </div>
</template>

<script>
  import PoolList from '../../common/PoolList.vue';
  import PoolTab from '../../common/PoolTab.vue';
  import AreaPicker from '../../common/AreaPicker.vue';

  export default {
    components: {
      PoolList, PoolTab, AreaPicker
    },
  }
</script>

<style scoped>

</style>
