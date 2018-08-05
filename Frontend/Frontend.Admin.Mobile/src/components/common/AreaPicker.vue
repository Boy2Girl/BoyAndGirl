<template>
  <div>
    <img src="../../assets/location.png" style="height: 20px; height: 20px; position: absolute; top: 47px; left: 11px"/>
    <x-button style="border-width: 0px; font-size: 10px; text-align: left; padding-left: 38px" :plain="isPlain" @click.native="showPopupPicker=true" >地区:
      {{myArea[0]}}</x-button>
    <popup-picker :show.sync="showPopupPicker" :show-cell="false" :data="areas" v-model="myArea"/>

  </div>
 </template>

<script>
  import { PopupPicker, XButton} from 'vux';


  export default {
    components: {
      PopupPicker, XButton
    },
    data(){
      return{
        areas: [['南京', '苏州']],
        myArea: ['南京'],
        showPopupPicker: false,
        isPlain: true
      }
    },
    methods: {

    }
  }
</script>

<style scoped>

</style>
