<template>
  <div>
    <router-link :to="{path:'/user/historyActivity'}">
      <Button style="width: 100%" type="text" icon="ios-search">往期活动</Button>
    </router-link>
    <swiper :list="activityList" auto style="width:100%;margin:0 auto;" height="180px" dots-class="custom-bottom"
            dots-position="center"/>
    <divider>活动报名</divider>
    <activity-card-list/>
  </div>
</template>

<script>
  import {Swiper, Divider} from "vux";
  import ActivityCardList from './ActivityCardList.vue';

  export default {
    components: {
      Swiper, Divider, ActivityCardList
    },
    data() {
      return {
        activityList: [
          {
            url: 'javascript:',
            img: 'http://placeholder.qiniudn.com/800x300/FF3B3B/ffffff'
          },
          {
            url: 'javascript:',
            img: 'http://placeholder.qiniudn.com/800x300/FFEF7D/ffffff'
          },
          {
            url: 'javascript:',
            img: 'http://placeholder.qiniudn.com/800x300/8AEEB1/ffffff'
          }
        ]
      }
    }
  }
</script>

<style scoped>
</style>
