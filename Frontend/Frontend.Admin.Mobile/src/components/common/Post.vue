<template>
  <div>
  <div style="border-color: #a8a7a9; width: 98%; height: 170px; border-style: solid; margin-left: 1%; margin-bottom: 2%">
    <div style="width: 65%; float: left; margin-top: 1%">
      <div style="margin-bottom: 2px">
        <font style="background-color: #17872b; color: white; padding: 4px; width: 110%; height: 110%; margin-left: 1%; margin-right: 1%">{{education}}</font>
        <font style="font-weight: bolder">{{username}}</font>
      </div>
      <group>
        <cell class="cell-font" title="出生年份:"> {{birthDate}}</cell>
        <cell class="cell-font" title="所在城市:"> {{city}}</cell>
        <cell class="cell-font" title="应征是否需要审核：">{{isCheck}}</cell>
        <cell class="cell-font" title="本科学校:">{{school}}</cell>
        <cell class="cell-font" title="职业:">{{career}}</cell>
      </group>
    </div>
    <div style="width: 30%; float: right; margin-right: 2%; margin-top: 1%">
      <img :src="source" style="width: 100%"/>
    </div>
  </div>
  </div>
</template>

<script>
    import { CellFormPreview, Group, Cell } from 'vux'

    export default {

        components:{
          CellFormPreview, Group, Cell
        },
        data(){

          return {
            education: '本',
            username: 'dhh',
            birthDate: '1980',
            city: '南京',
            isCheck: '是',
            school: '南京大学',
            career: '金融',
            source: require("../../assets/logo.jpg")
          }
        }
    }
</script>

<style scoped>
  .cell-font{
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
  }
</style>
