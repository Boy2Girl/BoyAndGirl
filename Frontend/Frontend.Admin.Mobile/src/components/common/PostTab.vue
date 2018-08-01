<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/user/posts'" @on-item-click="onAllClick">所有应征</tab-item>
    <tab-item v-else @on-item-click="onAllClick">所有应征</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/myPost'" @on-item-click="onMineClick">我的应征者</tab-item>
    <tab-item v-else @on-item-click="onMineClick">我的应征者</tab-item>
  </tab>
</template>

<script>
  import {Tab, TabItem} from 'vux';
  import router from "../../router";

  export default {
    components: {
      Tab, TabItem
    },
    methods: {
      onAllClick() {
        router.push('/user/posts');
      },
      onMineClick() {
        router.push('/user/myPost');
      }
    }
  }
</script>

<style scoped>

</style>
