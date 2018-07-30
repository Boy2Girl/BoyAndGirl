<template>
    <div>
      <div class="sub-title">
        个人相册
      </div>
      <group>
        <img :src="source" class="photo"/>
      </group>

      <div class="sub-title">
        基本信息
      </div>
      <group>
        <cell class="cell-font" title="昵称:"> {{birthDate}}</cell>
        <cell class="cell-font" title="编号:"> {{city}}</cell>
        <cell class="cell-font" title="性别：">{{isCheck}}</cell>
        <cell class="cell-font" title="身高:">{{school}}</cell>
        <cell class="cell-font" title="出生日期:">{{career}}</cell>
        <cell class="cell-font" title="婚姻状况:">{{career}}</cell>
        <cell class="cell-font" title="交友类型:">{{career}}</cell>
      </group>

      <div class="sub-title">
        坐标
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>

      <div class="sub-title">
        学校
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>

      <div class="sub-title">
        工作
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>

      <div class="sub-title">
        住房/家庭情况
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>

      <div class="sub-title">
        想说的话
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>
    </div>
</template>

<script>
    import { CellFormPreview, Group, Cell } from 'vux'
    export default {
      components:{
        CellFormPreview, Group, Cell
      },
      data() {
        return {
          source: require(),
          birthDate: '',
          city: '',
          school: "",
          career: "",
          isCheck: "",
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
  }

  .photo{
    width: 30%;
    margin: 5%;
  }
</style>
