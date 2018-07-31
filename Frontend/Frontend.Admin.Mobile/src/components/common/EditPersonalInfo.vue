<template>
  <div>
    <div class="sub-title">
      个人相册
    </div>
    <group>
      <img :src="source" class="photo"/>
      <img src="../../assets/add.png" class="photo"/>
    </group>

    <div class="sub-title">
      基本信息
    </div>
    <group>
      <cell class="cell-font" title="昵称:" :value="birthDate"/>
      <cell class="cell-font" title="编号:" :value="index"/>
      <popup-picker title="性别" class="cell-font" :data="list_gender" value-text-align="right" v-model="gender"/>
      <x-input class="cell-font" title="身高:" :value="p_height"/>
      <x-input class="cell-font" title="出生日期:" :value="birthDate"/>
      <popup-picker class="cell-font" title="婚姻状况:" :data="list_state" value-text-align="right" v-model="state"/>
      <popup-picker class="cell-font" title="交友类型:" :data="list_type" value-text-align="right" v-model="type"/>
    </group>

    <div class="sub-title">
      坐标
    </div>
    <group>
      <x-input class="cell-font" title="家乡:" v-model="hometown"/>
      <x-input class="cell-font" title="所在城市:" v-model="city"/>
      <x-input class="cell-font" title="居住地点：" v-model="live"/>
    </group>

    <div class="sub-title">
      学校
    </div>
    <group>
      <x-input class="cell-font" title="目前状态:" v-model="studyState"/>
      <x-input class="cell-font" title="本科学校:" v-model="collageSchool"/>
      <x-input class="cell-font" title="硕士学校:" v-model="masterSchool"/>
      <x-input class="cell-font" title="博士学校:" v-model="doctorSchool"/>
      <x-input class="cell-font" title="学历:" v-model="education"/>
      <x-input class="cell-font" title="专业:" v-model="major"/>
    </group>

    <div class="sub-title">
      工作
    </div>
    <group>
      <x-input class="cell-font" title="工作单位:" v-model="corporation"/>
      <x-input class="cell-font" title="工作状况:" v-model="work_state"/>
      <x-input class="cell-font" title="职业：" v-model="career"/>
      <x-input class="cell-font" title="单位类型:" v-model="corporation_type"/>
      <x-input class="cell-font" title="年收入（实际/预期）:" v-model="income"/>
    </group>

    <div class="sub-title">
      住房/家庭情况
    </div>
    <group>
      <x-input class="cell-font" title="住房情况:" v-model="house_state"/>
      <x-input class="cell-font" title="家庭情况:" v-model="family_state"/>
    </group>

    <div class="sub-title">
      想说的话
    </div>
    <group>
      <x-textarea class="cell-font" title="关于我:" v-model="about_me"/>
      <x-textarea class="cell-font" title="关于你:" v-model="about_you"/>
    </group>

    <x-button style="margin-top: 10px" type="primary">保存</x-button>
  </div>
</template>

<script>
  import { XButton, GroupTitle, Group, Cell, XInput, Selector, PopupPicker, Datetime, XNumber, ChinaAddressData, XAddress, XTextarea, XSwitch } from 'vux'

  export default {
    components: {
      XButton,
      Group,
      GroupTitle,
      Cell,
      XInput,
      Selector,
      PopupPicker,
      XAddress,
      Datetime,
      XNumber,
      XTextarea,
      XSwitch
    },
    data () {
      return {
        source: require('../../assets/background.jpg'),
        nickname: ' ',
        index: '',
        gender: [],
        p_height: '',
        birthDate: '2828',
        state: [],
        type: [],
        hometown: '',
        city: '',
        live: '',
        studyState: '',
        collageSchool: '',
        masterSchool: '',
        doctorSchool: '',
        education: '',
        major: '',
        corporation: '',
        work_state: '',
        career: '',
        corporation_type: '',
        income: '',
        house_state: '',
        family_state: '',
        about_you: '',
        about_me: '',
        list_gender: [['男','女']],
        list_state: [['未婚', '离婚未育', '离异子女判给对方', '离异子女跟自己', '丧偶未育', '丧偶子女跟自己', '丧偶子女不跟自己', '其他']],
        list_type: [['恋爱', '结婚']]
      }
    }
  }
</script>

<style scoped>
  .sub-title{
    background-color: #875927;
    color: white;
    padding: 4px;
    width: 110%;
    height: 110%;
    margin-left: 1%;
    margin-right: 1%;
    margin-top: 20px;
  }

  .cell-font{
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
    value-text-align: right;
  }

  .photo{
    width: 30%;
    height: 30%;
    margin: 5%;
  }
</style>
