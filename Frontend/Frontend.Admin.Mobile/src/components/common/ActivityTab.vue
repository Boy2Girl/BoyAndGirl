<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/user/historyActivity'" @on-item-click="onToHistoryClick">往期活动
    </tab-item>
    <tab-item v-else @on-item-click="onToHistoryClick">往期活动</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/myActivity'" @on-item-click="onToMineClick">我的活动</tab-item>
    <tab-item v-else @on-item-click="onToMineClick">我的活动</tab-item>
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
      onToHistoryClick() {
        router.push('/user/historyActivity');
      },
      onToMineClick() {
        router.push('/user/myActivity');
      }
    },
  }
</script>

<style scoped>

</style>
