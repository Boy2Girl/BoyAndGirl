<template>
  <div>
    <group label-width="4.5em" label-margin-right="2em" label-align="right">
      <datetime title="活动开始时间" v-model="activityBeginTime" value-text-align="left"></datetime>
      <datetime title="活动结束时间" v-model="activityEndTime" value-text-align="left"></datetime>
      <x-input title="活动地点" v-model="address"></x-input>
      <datetime title="报名开始时间" v-model="registerBeginTime" value-text-align="left"></datetime>
      <datetime title="报名结束时间" v-model="registerEndTime" value-text-align="left"></datetime>
      <x-input title="上<i class='vux-blank-half'></i>报<i class='vux-blank-half'></i>人" v-model="value1"></x-input>
      <x-number title="Quantity" align="left" v-model="numberValue" button-style="round" :min="0" :max="5"></x-number>
      <datetime title="时&emsp;&emsp;&nbsp;间" v-model="time1" value-text-align="left"></datetime>
      <selector title="隐患类别" :options="['工艺技术', '其他']" v-model="value2"></selector>
      <selector title="隐患类别" placeholder="Placeholder" :options="['工艺技术', '其他']" v-model="value7"></selector>
      <selector title="隐患类别" :options="['工艺技术', '其他']" v-model="value8"></selector>
      <x-input title="隐患部位" placeholder="必填" v-model="value3"></x-input>
      <x-input title="密码" type="password" placeholder="必填" v-model="value4"></x-input>
      <popup-picker title="请选择" :data="list" v-model="value5" value-text-align="left"></popup-picker>
      <popup-picker title="请选择" placeholder="Required" :data="list" v-model="value6"
                    value-text-align="left"></popup-picker>
      <x-address title="地址选择" v-model="addressValue" raw-value :list="addressData" value-text-align="left"></x-address>
      <x-textarea title="详细信息" placeholder="请填写详细信息" :show-counter="false" :rows="3"></x-textarea>
      <x-textarea placeholder="请填写详细信息" :show-counter="false" :rows="3">
        <img slot="restricted-label" style="display:inline-block;vertical-align:middle;"
             src="http://dn-placeholder.qbox.me/110x110/FF2D55/000" width="24" height="24">
      </x-textarea>
    </group>
  </div>
</template>

<script>
  import {XInput,Datetime} from "vux";

  export default {
    components: {
      XInput,Datetime
    },
    data(){
      return {
        activityBeginTime:"",
        activityEndTime:"",
        address:"",
        registerBeginTime:"",
        registerEndTime:"",

      }
    }
  }
</script>

<style scoped>

</style>
