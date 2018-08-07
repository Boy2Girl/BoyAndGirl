<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content" @on-hide="onHide"/>
    </div>
    <img :src="img" auto style="width:100%;margin:0 auto;" height="180px"/>
    <div style="display: inline; margin-bottom: 20px;">
      <div class="title">互选池名称</div>
      <div style="float: right; font-size: 20px; margin-right: 15px; color: #6b6a66">{{name}}</div>
    </div>

    <cell title="创建时间" style="margin-top: 10px;" class="cell-font">{{createTime}}</cell>
    <cell title="所属城市" class="cell-font">{{city}}</cell>

    <div class="title">互选池简介</div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right" style="margin-top: -10px;">
      <div v-html='detail'></div>
    </group>

    <x-button :gradients="['#43aaa7','#55bdd9']" class="btn btn-bottom" style="position: fixed; bottom: 47px;"
              @click.native="register_pool">确认报名
    </x-button>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, GroupTitle, Swiper, Group, Alert} from "vux";
  import Cell from "vux/src/components/cell/index";
  import PoolApi from '../../api/pool';
  import CheckApi from '../../api/check';

  export default {
    components: {
      Cell, XInput, Datetime, XButton, GroupTitle, Swiper, Group, Alert
    },
    data() {
      return {
        show: false,
        isRegistered: false,
        title: '',
        content: '',
        img: '',
        name: "",
        createTime: "",
        city: "",
        detail: ""
      }
    },
    methods: {
      updateData(e = '') {
        this.detail = e;
        console.info(e);
      },
      success: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text);
          this.img = result.url;
          this.city = result.city;
          this.name = result.name;
          this.detail = result.detail;
          this.createTime = result.createTime;
        } else if (status === 404) {
          console.log("没有找到该候选池");
          this.setState('错误', '网络故障');
        }
      },
      register_success: function (status) {
        if (status === 200) {
          console.log("报名成功");

          this.isRegistered = true;
          this.setState('成功', '您已成功进入该互选池');
        } else if (status === 404) {
          this.setState('失败', '数据库出问题啦');
        } else if (status === 403) {
          this.setState('失败', '您已经报名参加本互选池了');
        }
      },
      register_pool: function () {
        CheckApi.check(this.check_success, this.fail);
      },
      check_success: function(status, text){
        if (status === 200) {
          let result = JSON.parse(text)
          if(!result.isReal){
            this.setState("失败", "您还没有实名认证，不能进入互选池");
          }else{
            PoolApi.registerPool(this.$route.params.id, this.register_success, this.fail)
          }
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err);
        this.setState('错误', '网络故障');
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      },
      onHide: function () {
        if(this.isRegistered) {
          this.isRegistered = false;
          this.$router.go(-1);
        }
      }
    },
    mounted() {
      PoolApi.getPool(this.$route.params.id, this.success, this.fail);
    }
  }
</script>

<style lang="less" type="text/less">
  .cell-font {
    font-size: small;
  }

  .title {
    font-size: 20px;
    font-weight: bold;
    margin-left: 20px;
    display: inline;
  }

</style>
