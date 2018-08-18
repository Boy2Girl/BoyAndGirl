<template>
  <div>
    <pool-tab/>
    <pool-list/>
  </div>
</template>

<script>
  // import PoolList from '../../common/PoolList.vue';
  // import PoolTab from '../../common/PoolTab.vue';

  
  const PoolTab = () => import('../../common/PoolTab.vue')
  const PoolList = () => import('../../common/PoolList.vue')
  export default {
    components: {
      PoolList, PoolTab
    },
    mounted(){
      console.log("pool page init")
    }
  }
</script>

<style scoped>

</style>
