<template>
  <div>
    <activity-card-list/>
    <router-link :to="{path:'/admin/activity/add'}">
      <x-button type="primary" class="btn btn-bottom">发布活动
      </x-button>
    </router-link>
  </div>
</template>

<script>
  const ActivityCardList = () => import('../../common/ActivityCardList.vue');
  import {XButton} from 'vux';

  export default {
    components: {
      ActivityCardList, XButton
    },
  }
</script>

<style scoped>
  .btn {
  }

  .btn-bottom {
    position: absolute;
    /*z-index: 999;*/
    bottom: 48px;
    left: 0;
    width: 100%;
  }
</style>
