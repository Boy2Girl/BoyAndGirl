<template>
<div>
  <h1>user posts page</h1>
  <Post></Post>
  <Info></Info>
</div>
</template>

<script>
    import Post from '../../common/Post.vue';
    import Info from '../../common/PersonalInfo.vue';

    export default {
      components:{
        Post, Info
      }
    }
</script>

<style scoped>

</style>
