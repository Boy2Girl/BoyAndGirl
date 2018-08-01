<template>
  <div>
    <post-tab/>
    <Post/>
  </div>
</template>

<script>
  import Post from '../../common/Post.vue';
  import Info from '../../common/PersonalInfo.vue';
  import PostTab from '../../common/PostTab.vue';

  export default {
    components: {
      Post, Info, PostTab
    }
  }
</script>

<style scoped>

</style>
