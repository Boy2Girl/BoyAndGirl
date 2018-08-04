<template>
  <div>
    <post-tab/>
    <area-picker/>
    <Post/>
  </div>
</template>

<script>
  import Post from '../../common/Post.vue';
  import PostTab from '../../common/PostTab.vue';
  import AreaPicker from '../../common/AreaPicker.vue'

  export default {
    components: {
      Post, PostTab, AreaPicker
    }
  }
</script>

<style scoped>

</style>
