<template>
  <div>
    <img src="../../assets/poolname.png" style="height: 35px; width: 35px; position: absolute; top: 20px; left: 10px"/>
    <x-input title="互选池名称" placeholder="请输入名称"
             style="padding: 5%; font-weight: bold; font-size: 24px; color: #464448; width: 90%; margin-left: 10%"
             v-model="name"/>
    <div label-width="4.5em" label-margin-right="2em" label-align="right">
      <datetime title="创建时间" v-model="createTime"/>
      <selector style="height: 40px" title="城市" placeholder="请选择城市" direction="rtl" v-model="city"
                :options="cityList"></selector>
      <x-input title="加入条件" text-align="right" v-model="rule"/>
      <x-textarea title="简述"/>
      <x-input :disabled="isDisable" title="互选池照片" style="color: #5d5e5c"/>
    </div>

    <FileUPloader :url="actionUrl" v-on:child-say="listenToMyBoy"/>
    <div label-width="4.5em" label-margin-right="2em" label-align="right">
      <vue-html5-editor :content="detail" :height="400"
                        @change="updateData"></vue-html5-editor>
    </div>

    <x-button type="primary" class="btn btn-bottom" @click.native="add_pool">确认增加
    </x-button>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, GroupTitle, Selector, XTextarea} from "vux"
  import Cell from "vux/src/components/cell/index"
  import PoolApi from '../../api/pool'
  import FileUPloader from './FileUploader'
  import baseUrl from '../../api/basequery'

  export default {
    components: {
      XTextarea,
      Cell, XInput, Datetime, XButton, GroupTitle, Selector, FileUPloader
    },
    data() {
      return {
        actionUrl: baseUrl.baseUrl + '/test',
        url: "",
        cityList: ["上海", '合肥', '北京', '深圳'],
        name: "",
        createTime: "",
        city: "",
        rule: "",
        detail: "",
        isDisable: true,
      }
    },
    methods: {
      mounted() {
        console.log("hhh" + this.actionUrl)
      },
      updateData(e = '') {
        this.detail = e
        console.info(e)
      },
      listenToMyBoy: function (somedata) {
        this.url = somedata
      },
      add_pool: function () {
        if (this.url === "")
          this.setState("失败", "请上传图片")
        else
          PoolApi.addPool(this.url, this.name, this.createTime, this.city, this.detail, this.success, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
          this.$router.go(-1)
        } else if (status === 500) {
          this.setState("错误", "上传互选池失败")
        }
      },
      fail: function (err) {
        console.log(err)
        this.setState("错误", "网络错误")
      },
      setState: function (title, content) {
        this.title = title
        this.content = content
        this.show = true
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .btn {
  }

  .btn-bottom {
    position: fixed;
    /*z-index: 999;*/
    bottom: 48px;
    left: 0;
    width: 100%;
  }
</style>
