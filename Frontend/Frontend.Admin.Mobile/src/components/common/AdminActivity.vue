<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
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
    </group>
    <group>
      <group-title slot="title">
        <div style="padding: 5%">详细信息：</div>
      </group-title>
      <vue-html5-editor :content="content" :height="400"
                        @change="updateData"></vue-html5-editor>
    </group>
  </div>
</template>

<script>
  import {XInput, Datetime} from "vux";

  export default {
    components: {
      XInput, Datetime
    },
    data() {
      return {
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
      }
    }
  }
</script>

<style scoped>

</style>
