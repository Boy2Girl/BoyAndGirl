<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/user/pool'" @on-item-click="onAllClick">所有互选池</tab-item>
    <tab-item v-else @on-item-click="onAllClick">所有互选池</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/myPool'" @on-item-click="onMineClick">我的互选池</tab-item>
    <tab-item v-else @on-item-click="onMineClick">我的互选池</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/successPool'" @on-item-click="onSuccessClick">互选成功记录</tab-item>
    <tab-item v-else @on-item-click="onSuccessClick">互选成功记录</tab-item>
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
        router.push('/user/pool');
      },
      onMineClick() {
        router.push('/user/myPool');
      },
      onSuccessClick() {
        router.push('/user/successPool');
      }
    }
  }
</script>

<style scoped>

</style>
