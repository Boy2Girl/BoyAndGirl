<template>
  <div>
    <FileUPloader :url="actionUrl" v-on:child-say="listenToMyBoy"/>
    <!-- <group label-width="4.5em" label-margin-right="2em" label-align="right"> -->
    <x-input title="活动名称" v-model="name"/>
    <datetime title="活动开始时间" v-model="activityBeginTime" value-text-align="left"/>
    <datetime title="活动结束时间" v-model="activityEndTime" value-text-align="left"/>
    <x-input title="活动地点" v-model="address"/>
    <datetime title="报名开始时间" v-model="registerBeginTime" value-text-align="left"/>
    <datetime title="报名结束时间" v-model="registerEndTime" value-text-align="left"/>
    <datetime title="互选开始时间" v-model="selectBeginTime" value-text-align="left"/>
    <datetime title="互选结束时间" v-model="selectEndTime" value-text-align="left"/>
    <x-input title="收费标准" v-model="chargeRule"/>
    <datetime format="YYYY" title="男士年龄递增费用免收起始" v-model="boyBeginAge"/>
    <datetime format="YYYY" title="女士年龄递增费用免收起始" v-model="girlBeginAge"/>
    <x-input type="number" title="每大一岁递增加收" v-model="increment"/>
    <x-input title="活动负责人微信" v-model="wechat"/>
    <group>
      <group-title slot="title">
        <div style="padding: 5%">详细信息：</div>
      </group-title>
      <vue-html5-editor :content="detail" :height="400"
                        @change="updateData"></vue-html5-editor>
    </group>
    <x-button type="primary" class="btn btn-bottom" @click.native="add_activity">确认增加
    </x-button>
  </div>
</template>

<script>
  import {XInput, Datetime, Group, GroupTitle, XButton} from "vux";
  import ActivityApi from '../../api/activity'
  import FileUPloader from './FileUploader'

  export default {
    components: {
      XInput, Datetime, Group, GroupTitle, XButton, FileUPloader
    },
    data() {
      return {
        actionUrl: "http://127.0.0.1:5000/api/test",
        url: "",
        name: "",
        activityBeginTime: "",
        activityEndTime: "",
        address: "",
        registerBeginTime: "",
        registerEndTime: "",
        selectBeginTime: "",
        selectEndTime: "",
        chargeRule: "",
        boyBeginAge: "",
        girlBeginAge: "",
        increment: "",
        wechat: "",
        detail: ""
      }
    },
    methods: {
      updateData(e = '') {
        this.detail = e;
        console.info(e);
      },
      add_activity() {
        if (this.url === "")
          console.log("请上传图片");
        else
          ActivityApi.addActivity(this.name, this.url, this.activityBeginTime, this.activityEndTime, this.address, this.registerBeginTime,
            this.registerEndTime, this.selectBeginTime, this.selectEndTime, this.chargeRule, this.boyBeginAge, this.girlBeginAge,
            this.increment, this.wechat, this.detail, this.success, this.fail);
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
        } else if (status === 500) {
          console.log("上传活动失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
      },
      listenToMyBoy: function (somedata) {
        this.url = somedata
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .btn {
  }

  .btn-bottom {
    position: absolute;
    z-index: 999;
    bottom: 47px;
    left: 0;
    width: 100%;
  }
</style>
