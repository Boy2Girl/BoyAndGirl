<template>
  <tab>
    <tab-item selected v-if="this.$route.path==='/user/poolPeople'" @on-item-click="onAllClick">所有人</tab-item>
    <tab-item v-else @on-item-click="onAllClick">所有人</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/poolMyPeople'" @on-item-click="onMineClick">我选择的人</tab-item>
    <tab-item v-else @on-item-click="onMineClick">我选择的人</tab-item>
    <tab-item selected v-if="this.$route.path==='/user/poolTwoPeople'" @on-item-click="onSuccessClick">互选成功的人</tab-item>
    <tab-item v-else @on-item-click="onSuccessClick">互选成功的人</tab-item>
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
        router.push('/user/poolPeople');
      },
      onMineClick() {
        router.push('/user/poolMyPeople');
      },
      onSuccessClick() {
        router.push('/user/poolTwoPeople');
      }
    }
  }
</script>

<style scoped>

</style>
