<template>
  <div>
    <div class="avatar-container">
      <img class="avatar" :src="avatarUrl"/>
    </div>
    <group style="margin-top: -5%">
      <cell class="cell-text" title="联系编号" :value="id">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/index.png">
      </cell>
      <cell class="cell-text" title="个人资料（编辑）" link="/user/edit">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/edit_color.png">
      </cell>
    </group>
    <group>
      <cell class="cell-text" title="我的资料（分享）" link="/user/info">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/share.png">
      </cell>
    </group>
    <group>
      <cell class="cell-text" title="我的活动" link="/user/myActivity">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/activity.png">
      </cell>
      <cell class="cell-text" title="我应征的人" link="/user/myPostOne">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/post_me.png">
      </cell>
      <cell class="cell-text" title="应征我的人" link="/user/onePostMe">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/find.png">
      </cell>
      <cell class="cell-text" title="互选池互选成功记录" link="/user/successPool">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/choose.png">
      </cell>
    </group>
    <group>
      <cell class="cell-text" title="网站使用指南" link="/user/about">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/about.png">
      </cell>
    </group>
  </div>
</template>

<script>
  import {Group, Cell} from "vux";
  import Icon from "vux/src/components/icon/index";
  import {mapGetters} from 'vuex';

  export default {
    components: {
      Icon,
      Group, Cell},
    data() {
      return {
        id: 0,
        avatarUrl: 'http://placeholder.qiniudn.com/640x300'
      }
    },
    methods: {
      ...mapGetters(['getToken', 'getUserID']),
    },
    mounted(){
      this.id = this.getUserID();
    }
  }
</script>

<style scoped>
  .avatar-container {
    text-align: center;
    padding: 10%;
    width: 100%;
    height: 30%;
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
