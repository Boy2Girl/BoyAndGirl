<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/admin/verify'" @on-item-click="onAllClick">待审核用户</tab-item>
    <tab-item v-else @on-item-click="onAllClick">待审核用户</tab-item>
    <tab-item selected v-if="this.$route.path==='/admin/verified'" @on-item-click="onMineClick">已审核用户</tab-item>
    <tab-item v-else @on-item-click="onMineClick">已审核用户</tab-item>
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
        router.push('/admin/verify');
      },
      onMineClick() {
        router.push('/admin/verified');
      },
    }
  }
</script>

<style scoped>

</style>
