<template>
  <div>
    <img :src="img" auto style="width:100%;margin:0 auto;" height="180px"/>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%;font-weight: bold">{{name}}</div>
      </group-title>
      <cell title="创建时间">{{createTime}}</cell>
      <cell title="所属城市">{{city}}</cell>
    </group>
    <x-button type="primary" class="btn btn-bottom" @click.native="register_pool">确认报名
    </x-button>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%">简述</div>
      </group-title>
      <div v-html='detail'></div>
    </group>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, GroupTitle, Swiper} from "vux";
  import Cell from "vux/src/components/cell/index";
  import PoolApi from '../../api/pool' 

  export default {
    components: {
      Cell, XInput, Datetime, XButton, GroupTitle, Swiper
    },
    data() {
      return {
        img: 'http://placeholder.qiniudn.com/800x300/FF3B3B/ffffff',
        name: "苏州互选池",
        createTime: "2018年02月20日",
        city: "苏州市",
        detail: "<div style=\"text-align: center;\">【<font color=\"#990000\">活动时间</font>】</div><div style=\"text-align: center;\">dsa</div>"
      }
    },
    methods: {
      updateData(e = '') {
        this.detail = e;
        console.info(e);
      },
      success: function(status, text){
        if(status == 200){
          let result = JSON.parse(text)
          this.img = result.url
          this.city = result.city
          this.name = result.name
          this.detail = result.detail
          this.createTime = result.createTime
        }else if(status == 404){
          console.log("没有找到该候选池")
        }
      },
      register_success: function(){
        if(status == 200){
           console.log("报名成功")
        }else if(status == 404){
          console.log("没有找到这个候选池")
        }else if(status == 403){
          console.log("已经报名了这个候选池")
        }
      },
      register_pool: function(){
         PoolApi.registerPool(1, this.register_success, this.fail)
      },
      fail: function(err){
        console.log("错误发生了！！！")
        console.log(err)
      },
      checkSuccess(status,text){
        console.log("这里爱仕达所")
        if(status == 200){
           console.log("已经报名")
        }else if(status == 404){
          console.log("没有报名")
        }
      }
    },
    mounted(){
      console.log("here")
      PoolApi.checkRegister(this.$route.params.id, this.checkSuccess, this.fail)
      // PoolApi.getPool(this.$route.params.id, this.success, this.fail)
    }
  }
</script>

<style lang="less" type="text/less">
</style>
