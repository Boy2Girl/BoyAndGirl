<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <cell title="联系编号" :value="id"/>
      <cell title="个人资料（编辑）" link="/user/"/>
    </group>
    <group>
      <cell title="我的资料（分享）" link="/user"/>
    </group>
    <group>
      <cell title="我的活动" link="/user/list"/>
      <cell title="我的应征者" link="/user/post"/>
      <cell title="互选池互选成功记录" link=""/>
    </group>
    <group>
      <cell title="网站使用指南" link="/user/about"/>
    </group>
  </div>
</template>

<script>
  import {Group, Cell} from "vux";

  export default {
    components: {Group, Cell},
    data() {
      return {
        id: 10486
      }
    }
  }
</script>

<style scoped>

</style>
