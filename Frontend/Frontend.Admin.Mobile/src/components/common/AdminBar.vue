<template>
  <div class="tabs">
    <!--命名路由-->

    <ul>
      <!--this inspection reports XML/HTML tags with missing mandatory attrbutes ,you can specify attrbute name that should not  be reported-->
      <!--home被点击后，一直处于激活状态，因此需要使用精确匹配模式，在router-link中添加exact属性-->

      <router-link :to="{path: '/admin/activity'}" tag="li">
        <Icon type="social-buffer" size="20"></Icon>
        <div class="font">{{tabBar1}}</div>
      </router-link>
      <router-link :to="{path:'/admin/pool'}" tag="li">
        <Icon type="plus-circled" size="20"></Icon>
        <div class="font">{{tabBar2}}</div>
      </router-link>
      <router-link :to="{path:'/admin/verify'}" tag="li">
        <Icon type="ios-alarm" size="20"></Icon>
        <div class="font">{{tabBar3}}</div>
      </router-link>
      <router-link :to="{path:'/admin/user'}" tag="li">
        <Icon type="person" size="20"></Icon>
        <div class="font">{{tabBar4}}</div>
      </router-link>
    </ul>
  </div>
</template>

<script>
  import SENTENCES from "../../assets/sentences";
  import {Icon} from 'iview';
  export default {
    components: {Icon},
    data() {
      return {
        tabBar1: SENTENCES.MENU.ACTIVITY,
        tabBar2: SENTENCES.MENU.POOL,
        tabBar3: SENTENCES.MENU.USER_VERIFY,
        tabBar4: SENTENCES.MENU.USER_MANAGEMENT
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .tabs {
    z-index: 2000;
    position: fixed;
    bottom: 0;
    left: 0;
    background-color: #ffffff;
    box-shadow: 0 2px 4px #000;
    width: 100%;
    & > ul, & > ul > li {
      margin: 0;
      padding: 0;
    }
    ul {
      display: table;
      width: 100%;
      & > li {
        text-align: center;
        font-size: 25;
        display: table-cell;
        cursor: pointer;
        &.router-link-active {
          color: #6A005F;
        }
        & > div {
          font-size: 15px;
          & > i {
            font-size: 30px;
          }
        }
      }
    }
  }
</style>
