<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/user/posts'" @on-item-click="onAllClick">所有应征</tab-item>
    <tab-item v-else @on-item-click="onAllClick">所有应征</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/myPostOne'" @on-item-click="onMineClick">我的应征者</tab-item>
    <tab-item v-else @on-item-click="onMineClick">我应征的人</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/OnePostMe'" @on-item-click="onOneClick">应征我的人</tab-item>
    <tab-item v-else @on-item-click="onMineClick">应征我的人</tab-item>
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
        router.push('/user/myPostOne');
      },
      onOneClick() {
        router.push('/user/OnePostMe');
      }
    }
  }
</script>

<style scoped>

</style>
