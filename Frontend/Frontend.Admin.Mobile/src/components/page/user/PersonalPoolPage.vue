<template>
  <div>
    <pool-tab/>
    <post-list/>
  </div>
</template>

<script>
  // import PostList from '../../common/PoolList.vue';
  // import PoolTab from '../../common/PoolTab.vue';

  const PostList = () => import('../../common/PoolList.vue')
  const PoolTab = () => import('../../common/PoolTab.vue')
  export default {
    components: {
      PostList, PoolTab
    }
  }
</script>

<style scoped>

</style>
