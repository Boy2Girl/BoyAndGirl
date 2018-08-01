<template>
  <div>
    <pool-tab/>
    <post/>
  </div>
</template>

<script>
  import Post from '../../common/Post.vue';
  import Info from '../../common/PersonalInfo.vue';
  import PoolTab from '../../common/PoolTab.vue';

  export default {
    components: {
      Post, Info, PoolTab
    }
  }
</script>

<style scoped>

</style>
