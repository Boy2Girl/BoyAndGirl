<template>
  <div>
    <img src="../../assets/poolname.png" style="height: 35px; width: 35px; position: absolute; top: 20px; left: 10px"/>
    <x-input title="互选池名称"  placeholder="请输入名称"
             style="padding: 5%; font-weight: bold; font-size: 24px; color: #464448; width: 90%; margin-left: 10%" v-model="name"/>
    <div label-width="4.5em" label-margin-right="2em" label-align="right">
      <datetime title="创建时间" v-model="createTime"/>
      <selector style="height: 40px" title="城市" placeholder="请选择城市" direction="rtl" v-model="city" :options="cityList"></selector>
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
  import {XInput, Datetime, XButton, GroupTitle, Selector, XTextarea} from "vux";
  import Cell from "vux/src/components/cell/index";
  import PoolApi from '../../api/pool'
  import FileUPloader from './FileUploader'

  export default {
    components: {
      XTextarea,
      Cell, XInput, Datetime, XButton, GroupTitle, Selector, FileUPloader
    },
    data() {
      return {
        actionUrl: "http://127.0.0.1:5000/api/test",
        url: "",
        cityList: ["苏州", "南京"],
        name: "苏州互选池",
        createTime: "2018年02月20日",
        city: "苏州市",
        rule: "年满30周岁",
        detail: "<div style=\"text-align: center;\">【<font color=\"#990000\">活动时间</font>】</div><div style=\"text-align: center;\">dsa</div>",
        isDisable: true,
      }
    },
    methods: {
      updateData(e = '') {
        this.detail = e;
        console.info(e);
      },
      listenToMyBoy: function (somedata) {
        this.url = somedata
      },
      add_pool: function () {
        if (this.url === "")
          console.log("请上传图片");
        else
          PoolApi.addPool(this.url, this.name, this.createTime, this.city, this.detail, this.success, this.fail);
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
        } else if (status === 500) {
          console.log("上传互选池失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
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
    bottom: 47px;
    left: 0;
    width: 100%;
  }
</style>
