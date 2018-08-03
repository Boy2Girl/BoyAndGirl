<template>
  <div class="tabs">
    <!--命名路由-->

    <ul>
      <!--this inspection reports XML/HTML tags with missing mandatory attrbutes ,you can specify attrbute name that should not  be reported-->
      <!--home被点击后，一直处于激活状态，因此需要使用精确匹配模式，在router-link中添加exact属性-->
      <router-link :to="{path:'/user/activity'}" tag="li">
        <Icon type="social-buffer" size="20"/>
        <div class="font">{{tabBar1}}</div>
      </router-link>
      <router-link :to="{path:'/user/pool'}" tag="li">
        <Icon type="plus-circled" size="20"/>
        <div class="font">{{tabBar2}}</div>
      </router-link>
      <router-link :to="{path:'/user/posts'}" tag="li">
        <Icon type="person" size="20"/>
        <div class="font">{{tabBar3}}</div>
      </router-link>
      <router-link :to="{path:'/user/user'}" tag="li">
        <Icon type="person" size="20"/>
        <div class="font">{{tabBar4}}</div>
      </router-link>
    </ul>
  </div>
</template>

<script>
  import SENTENCES from "../../assets/sentences";

  export default {
    components: {

    },
    data() {
      return {
        tabBar1: SENTENCES.User_MENU.ACTIVITY,
        tabBar2: SENTENCES.User_MENU.POOL,
        tabBar3: SENTENCES.User_MENU.POSTS,
        tabBar4: SENTENCES.User_MENU.USER
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .tabs {
    position: fixed;
    bottom: 0;
    left: 0;
    background-color: #fff;
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
