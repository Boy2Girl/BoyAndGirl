<template>
  <div>
    <post-tab/>
    <Post/>
  </div>
</template>

<script>
  // import Post from '../../common/Post.vue';
  // import PostTab from '../../common/PostTab.vue';

  const Post = () => import('../../common/Post.vue')
  const PostTab = () => import('../../common/PostTab.vue')

  export default {
    components: {
      Post, PostTab
    }
  }
</script>

<style scoped>

</style>
