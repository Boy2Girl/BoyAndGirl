<template>
  <div>
    <pool-list/>
    <router-link :to="{path:'/admin/poolAdd'}">
      <x-button type="primary" class="btn btn-bottom" @click.native="add_pool">新增候选池
      </x-button>
    </router-link>
  </div>
</template>

<script>
  import PoolList from '../../common/PoolList';
  import {XButton} from 'vux';

  export default {
    components: {
      PoolList, XButton
    }
  }
</script>

<style scoped>
  .btn {
  }

  .btn-bottom {
    position: absolute;
    /*z-index: 999;*/
    bottom: 6.5%;
    left: 0;
    width: 100%;
  }
</style>
