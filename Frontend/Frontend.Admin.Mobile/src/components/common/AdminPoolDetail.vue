<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%">{{name}}</div>
      </group-title>
      <cell title="创建时间">{{createTime}}</cell>
      <cell title="所属城市">{{city}}</cell>
    </group>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <group-title slot="title">
        <div style="padding: 5%">简述</div>
      </group-title>
      <cell title="创建时间">{{createTime}}</cell>
      <cell title="所属城市">{{city}}</cell>
      <div v-html='detail'></div>
    </group>
  </div>
</template>

<script>
  import {XInput, Datetime, XButton, Group, GroupTitle} from "vux";
  import Cell from "vux/src/components/cell/index";

  export default {
    components: {
      Cell,
      XInput, Datetime, XButton, Group, GroupTitle
    },
    data() {
      return {
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
