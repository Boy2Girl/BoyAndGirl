<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <x-input style="padding: 5%" v-model="name"/>
      </group-title>
      <datetime title="创建时间" v-model="createTime"/>
      <selector placeholder="请选择城市" v-model="city" :options="cityList"></selector>
    </group>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%">简述</div>
      </group-title>
      <vue-html5-editor :content="detail" :height="400"
                        @change="updateData"></vue-html5-editor>
    </group>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, GroupTitle, Selector} from "vux";
  import Cell from "vux/src/components/cell/index";

  export default {
    components: {
      Cell, XInput, Datetime, XButton, GroupTitle, Selector
    },
    data() {
      return {
        cityList: ["苏州", "南京"],

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
      }
    }
  }
</script>

<style lang="less" type="text/less">
</style>
