<template>
  <div>
    <div class="avatar-container">
      <img class="avatar" :src="avatarUrl"/>
    </div>
    <group style="margin-top: -5%">
      <cell class="cell-text" title="联系编号" :value="id"/>
      <cell class="cell-text" title="个人资料（编辑）" link="/user/edit"/>
    </group>
    <group>
      <cell class="cell-text" title="我的资料（分享）" link="/user/info"/>
    </group>
    <group>
      <cell class="cell-text" title="我的活动" link="/user/myActivity"/>
      <cell class="cell-text" title="我应征的人" link="/user/myPostOne"/>
      <cell class="cell-text" title="应征我的人" link="/user/onePostMe"/>
      <cell class="cell-text" title="互选池互选成功记录" link="/user/successPool"/>
    </group>
    <group>
      <cell class="cell-text" title="网站使用指南" link="/user/about"/>
    </group>
  </div>
</template>

<script>
  import {Group, Cell} from "vux";

  export default {
    components: {Group, Cell},
    data() {
      return {
        id: 10486,
        avatarUrl: 'http://placeholder.qiniudn.com/640x300'
      }
    }
  }
</script>

<style scoped>
  .avatar-container {
    text-align: center;
    padding: 10%;
    background: url("../../assets/background.jpg");
  }

  .avatar {
    width: 70px;
    height: 70px;
    border-radius: 70px;
  }

  .cell-text{
    font-size: smaller;
  }
</style>
