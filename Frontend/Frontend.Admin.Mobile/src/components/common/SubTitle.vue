<template>
  <div class="sub-title">
    {{value}}
  </div>
</template>

<script>
  export default {
    props: {
      value: String
    }
  }
</script>

<style scoped>
  .sub-title {
    position: absolute;
    width: 100%;
  }

  .sub-title div {
    line-height: 20px;
  }

  /*CSS伪类用法*/
  .sub-title div:after, .wrap div:before {
    position: absolute;
    top: 50%;
    background: #FF66FF;
    content: "-";
    height: 1px;
    width: 45%;
  }

  /*调整背景横线的左右距离*/
  .sub-title div:before {
    left: 0;
  }

  .sub-title div:after {
    right: 0;
  }

  /*.sub-title {*/
  /*line-height: 60px;*/
  /*text-align: center;*/
  /*}*/

  /*.sub-title .border-left {*/
  /*display: inline-block;*/
  /*width: 15px;*/
  /*border-top: 1px solid #FF66FF;*/
  /*}*/

  /*.sub-title .border-right {*/
  /*display: inline-block;*/
  /*width: 67%;*/
  /*border-top: 1px solid #FF66FF;*/
  /*}*/

  /*.sub-title .border-txt {*/
  /*color: #686868;*/
  /*vertical-align: -4px;*/
  /*font-weight: bold;*/
  /*font-size: medium;*/
  /*}*/
</style>
