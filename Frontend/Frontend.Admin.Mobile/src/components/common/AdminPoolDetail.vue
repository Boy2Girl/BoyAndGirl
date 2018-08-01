<template>
  <div>
    <FileUPloader :url="actionUrl" v-on:child-say="listenToMyBoy">
    </FileUPloader>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <x-input style="padding: 5%" v-model="name"/>
      </group-title>
      <datetime title="创建时间" v-model="createTime"/>
      <selector placeholder="请选择城市" v-model="city" :options="cityList"></selector>
      <x-input placeholder="加入条件" v-model="rule"/>
    </group>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%">简述</div>
      </group-title>
      <vue-html5-editor :content="detail" :height="400"
                        @change="updateData"></vue-html5-editor>
    </group>
    <x-button type="primary" class="btn btn-bottom" @click.native="add_pool">确认增加
    </x-button>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, GroupTitle, Selector} from "vux";
  import Cell from "vux/src/components/cell/index";
  import PoolApi from '../../api/pool'
  import FileUPloader from './FileUploader'

  export default {
    components: {
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
        detail: "<div style=\"text-align: center;\">【<font color=\"#990000\">活动时间</font>】</div><div style=\"text-align: center;\">dsa</div>"
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
    position: absolute;
    /*z-index: 999;*/
    bottom: 47px;
    left: 0;
    width: 100%;
  }
</style>
