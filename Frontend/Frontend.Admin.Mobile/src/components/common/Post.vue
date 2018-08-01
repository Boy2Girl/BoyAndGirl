<template>
  <div>
    <div v-for="item in postList" v-bind:key="item.id"
         style="border-color: #a8a7a9; width: 98%; height: 170px; border-style: solid; margin-left: 1%; margin-bottom: 2%">
      <div style="width: 65%; float: left; margin-top: 1%">
        <div style="margin-bottom: 2px">
          <font
            style="background-color: #17872b; color: white; padding: 4px; width: 110%; height: 110%; margin-left: 1%; margin-right: 1%">{{education}}</font>
          <font style="font-weight: bolder">{{item.username}}</font>
        </div>
        <group>
          <cell class="cell-font" title="出生年份:"> {{item.birthDate}}</cell>
          <cell class="cell-font" title="所在城市:"> {{item.city}}</cell>
          <cell class="cell-font" title="本科学校:">{{item.school}}</cell>
          <cell class="cell-font" title="职业:">{{item.career}}</cell>
        </group>
      </div>
      <div style="width: 30%; float: right; margin-right: 2%; margin-top: 30px">
        <img :src="source" style="width: 130px"/>
      </div>
    </div>
  </div>
</template>

<script>
  import {CellFormPreview, Group, Cell} from 'vux'

  export default {

    components: {
      CellFormPreview, Group, Cell
    },
    data() {

      return {
        postList: [
          {
            id: 1,
            education: '本',
            username: 'dhh',
            birthDate: '1980',
            city: '南京',
            school: '南京大学',
            career: '金融',
            source: require("../../assets/logo.jpg")
          }
        ]
      }
    }
  }
</script>

<style scoped>
  .cell-font {
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
  }
</style>
