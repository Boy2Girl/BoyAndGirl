<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <cell title="活动时间" :value="activityTime" value-text-align="left"/>
      <cell title="活动地点" :value="address"/>
      <cell title="报名时间" :value="registerTime" value-text-align="left"/>
      <cell title="互选时间" :value="selectBeginTime" value-text-align="left"/>
      <cell title="收费规则" :value="chargeRule"/>
      <cell title="男/女年龄递增费用免收起始" :value="chargeBeginAge"/>
      <cell title="每大一岁递增加收" :value="increment"/>
      <cell title="活动负责人微信" v-model="wechat"/>
    </group>
    <group>
      <group-title slot="title">
        <div style="padding: 5%">详细信息：</div>
      </group-title>
      <div v-html='detail'></div>
    </group>
  </div>
</template>

<script>
  import {Cell} from "vux";

  export default {
    components: {
      Cell
    },
    data() {
      return {
        activityTime: "07月29日14:30~07月29日17:30",
        address: "金陵大饭店",
        registerTime: "07月18日13:59~07月29日14:00",
        selectTime: "07月29日14:00~08月03日23:55",
        chargeRule: "顺序+年龄递增收费",
        chargeBeginAge: "1991/1995",
        increment: "￥5.00",
        wechat: "1805318057",
        detail: "<div style=\"text-align: center;\">【<font color=\"#990000\">活动时间</font>】</div><div style=\"text-align: center;\">dsa</div>"
      }
    },
  }
</script>

<style scoped>

</style>
