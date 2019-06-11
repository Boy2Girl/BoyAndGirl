<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <img src="../../assets/activity.png" style="height: 35px; width: 35px; position: absolute; top: 20px; left: 10px"/>
    <x-input title="活动名称"
             style="padding: 5%; font-weight: bold; font-size: 24px; color: #464448; width: 90%; margin-left: 10%"
             placeholder="请输入活动名称" v-model="name"/>
    <!--<x-input title="活动名称" text-align="right" v-model="name"/>-->
    <datetime title="活动开始时间" v-model="activityBeginTime" value-text-align="right"/>
    <datetime title="活动结束时间" v-model="activityEndTime" value-text-align="right"/>
    <x-input title="活动地点" text-align="right" v-model="address"/>
    <datetime title="报名开始时间" v-model="registerBeginTime" value-text-align="right"/>
    <datetime title="报名结束时间" v-model="registerEndTime" value-text-align="right"/>
    <datetime title="互选开始时间" v-model="selectBeginTime" value-text-align="right"/>
    <datetime title="互选结束时间" v-model="selectEndTime" value-text-align="right"/>
    <x-input title="收费标准" text-align="right" v-model="chargeRule"/>
    <datetime format="YYYY" title="男士年龄递增费用免收起始" v-model="boyBeginAge"/>
    <datetime format="YYYY" title="女士年龄递增费用免收起始" v-model="girlBeginAge"/>
    <x-input type="number" text-align="right" title="每大一岁递增加收" v-model="increment"/>
    <x-input title="活动负责人微信" text-align="right" v-model="wechat"/>
    <FileUPloader :url="actionUrl" v-on:child-say="listenToMyBoy"/>
    <group>
      <group-title slot="title">
        <div style="padding: 0; color: black">详细信息：</div>
      </group-title>
      <vue-html5-editor :content="detail" :height="300" :z-index="index"
                        @change="updateData"></vue-html5-editor>
    </group>
    <x-button type="primary" class="btn btn-bottom" @click.native="add_activity">{{this.$route.name ===
      'modify'?'确认修改':'确认增加'}}
    </x-button>
  </div>
</template>

<script>
  import {XInput, Datetime, Group, GroupTitle, XButton, Alert} from "vux"
  import ActivityApi from '../../api/activity'
  import FileUPloader from './FileUploader'
  import baseUrl from '../../api/basequery'

  export default {
    components: {
      XInput, Datetime, Group, GroupTitle, XButton, FileUPloader, Alert
    },
    data() {
      return {
        actionUrl: baseUrl.baseUrl + '/test',
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
        detail: "",
        index: 1,
        show: false,
        title: '',
        content: ''
      }
    },
    methods: {
      updateData(e = '') {
        this.detail = e
        console.info(e)
      },
      add_activity() {
        if (this.url === "") {
          console.log("请上传图片")
          this.setState("失败", "请上传图片")
        }
        else if (this.$route.name === 'modify') {
          ActivityApi.modifyActivity(this.$route.params.id, this.name, this.url, this.activityBeginTime, this.activityEndTime, this.address, this.registerBeginTime,
            this.registerEndTime, this.selectBeginTime, this.selectEndTime, this.chargeRule, this.boyBeginAge, this.girlBeginAge,
            this.increment, this.wechat, this.detail, this.success, this.fail)
        }
        else
          ActivityApi.addActivity(this.name, this.url, this.activityBeginTime, this.activityEndTime, this.address, this.registerBeginTime,
            this.registerEndTime, this.selectBeginTime, this.selectEndTime, this.chargeRule, this.boyBeginAge, this.girlBeginAge,
            this.increment, this.wechat, this.detail, this.success, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
          // 应该弹出框，然后清除上面已经插入的数据
          // this.$root.reload();
        } else if (status === 500) {
          this.setState("错误", "上传活动失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
        this.setState("错误", "网络错误")
      },
      listenToMyBoy: function (somedata) {
        this.url = somedata
      },
      setState: function (title, content) {
        this.title = title
        this.content = content
        this.show = true
      },
      getSuccess: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text)
          console.log(result)
          this.activityBeginTime = result.activityBeginTime
          this.activityEndTime = result.activityEndTime
          this.address = result.location
          this.registerBeginTime = result.registerBeginTime
          this.registerEndTime = result.registerBeginTime
          this.selectBeginTime = result.selectBeginTime
          this.selectEndTime = result.selectEndTime
          this.chargeRule = result.chargeRule
          this.boyBeginAge = result.boyBeginAge
          this.girlBeginAge = result.girlBeginAge
          this.increment = result.increment
          this.wechat = result.wechat
          this.detail = result.detail
          this.url = result.url
        } else if (status === 500) {
          console.log("获取活动失败")
          this.setState("失败", "获取活动失败")
        } else if (status === 404) {
          console.log("没有该活动")
          this.setState("失败", "没有该活动")
        }
      },
      getFail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
        this.setState("错误", "网络错误")
      },
    },
    mounted() {
      if (this.$route.name === 'modify') {
        console.log('hhhhhhhhh')
        ActivityApi.getActivity(this.$route.params.id, this.getSuccess, this.getFail)
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .btn {
  }

  .btn-bottom {
    position: fixed;
    bottom: 48px;
    left: 0;
    width: 100%;
  }
</style>
