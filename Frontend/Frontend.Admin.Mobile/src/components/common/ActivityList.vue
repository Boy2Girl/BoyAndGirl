<template>
  <div>
    <img src="../../assets/location.png" style="height: 20px; position: absolute; top: 4px; left: 11px"/>
    <x-button style="border-width: 0px; font-size: 10px; text-align: left; padding-left: 38px; width: 50%; margin-left: 0px;" :plain="isPlain" @click.native="showPopupPicker=true" >地区:
      {{myArea[0]}}</x-button>
    <popup-picker :show.sync="showPopupPicker" :show-cell="false" :data="areas" v-model="myArea"/>
    <router-link :to="{path:'/user/historyActivity'}">
      <Button style="width: 50%; margin-left: 50%; position: absolute; top: 0px;" type="text" icon="ios-search">往期活动</Button>
    </router-link>
    <swiper :list="activityList" auto style="width:100%;margin:0 auto;" height="180px" dots-class="custom-bottom"
            dots-position="center"/>
    <divider>活动报名</divider>
    <activity-card-list/>
  </div>
</template>

<script>
  import {Swiper, Divider, PopupPicker, XButton} from "vux";
  // const Foo = () => import('./Foo.vue').then(m => m.default)
  const ActivityCardList = () => import('./ActivityCardList.vue')
  // import ActivityCardList from './ActivityCardList.vue';
  import {Button} from 'iview'
  export default {
    components: {
      Swiper, Divider, ActivityCardList, PopupPicker, XButton,Button
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
        ],
        areas: [['南京', '苏州']],
        myArea: ['南京'],
        showPopupPicker: false,
        isPlain: true
      }
    },
    mounted(){
      console.log(this.$route.query.code)
    }

  }
</script>

<style scoped>
</style>
