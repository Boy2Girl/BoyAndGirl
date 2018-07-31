<template>
<div>
  <Post/>
  <Post/>
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
