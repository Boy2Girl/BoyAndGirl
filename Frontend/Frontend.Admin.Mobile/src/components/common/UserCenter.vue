<template>
  <div>
    <div class="avatar-container">
      <img class="avatar" :src="avatarUrl"/>
    </div>
    <group style="margin-top: -5%">
      <cell class="cell-text" title="联系编号" :value="id">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/index.png">
      </cell>
      <cell class="cell-text" title="我的状态" :value="state">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/find.png">
      </cell>
      <cell class="cell-text" title="个人资料（编辑）" link="/user/edit">
        <img slot="icon" width="20" style="display:block;margin-right:5px;" src="../../assets/edit_color.png">
      </cell>
    </group>
    <group>
      <cell class="cell-text" title="我的资料（分享）" :link="'/user/info/'+this.id">
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
    <x-button :gradients="['#43aaa7','#55bdd9']" @click.native="signOut"
              style="margin-top: 10px;">
      登出
    </x-button>
    <div style="height: 50px"></div>
  </div>
</template>

<script>
  import {Group, Cell, XButton} from "vux";
  import Icon from "vux/src/components/icon/index";
  import {mapGetters, mapMutations} from 'vuex';
  import check from '../../api/check';
  import UserApi from '../../api/user';

  export default {
    components: {
      Icon,
      Group, Cell, XButton},
    data() {
      return {
        id: 0,
        avatarUrl: 'http://placeholder.qiniudn.com/640x300',
        state: '待审核'
      }
    },
    methods: {
      ...mapGetters(['getToken', 'getUserID']),
      ...mapMutations(['setToken', 'setUserID']),
      success: function (state, text) {
        if(state === 200){
          let result = (JSON.parse(text));
          if(!result['isReal']) {
            this.state = '待审核';
            UserApi.getUserInfo(this.id, 'False', this.loadSuccess, this.fail);
          }
          else {
            this.state = '已审核';
            UserApi.getUserInfo(this.id, 'True', this.loadSuccess, this.fail);
          }
        }
      },
      fail: function () {
        console.log('error')
      },
      loadSuccess: function (status, text) {
        var result = (JSON.parse(text));
        console.log(result);
        if (status === 200) {
          this.avatarUrl = result['avatar'];
        }
      },
      signOut: function () {
        console.log('logout');
        this.$router.push('login');
        this.setToken('');
        this.setUserID('0');
      }
    },
    mounted(){
      this.id = this.getUserID();

      check.check(this.success, this.fail)
      // 得到用户目前状态

    }
  }
</script>

<style scoped>
  .avatar-container {
    text-align: center;
    padding: 10%;
    width: 100%;
    height: 20%;
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
