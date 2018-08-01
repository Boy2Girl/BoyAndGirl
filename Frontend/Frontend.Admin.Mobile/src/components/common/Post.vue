<template>
  <div>
    <div v-for="item in postList" v-bind:key="item.id"
         style="border-color: #a8a7a9; width: 98%; height: 170px; border-style: solid; margin-left: 1%; margin-bottom: 2%">
      <div style="width: 65%; float: left; margin-top: 1%">
        <div style="margin-bottom: 2px">
          <font
            style="background-color: #17872b; color: white; padding: 4px; width: 110%; height: 110%; margin-left: 1%; margin-right: 1%">{{item.education}}</font>
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
        <img :src="item.source" style="width: 130px"/>
      </div>
    </div>
    <group>
      <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="addPosts">增加</x-button>
     <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="recruit">应征某人</x-button>
    </group>
  </div>
</template>

<script>
  import {CellFormPreview, Group, Cell, XButton} from 'vux'
  import PostsApi from '../../api/posts'
  export default {

    components: {
      CellFormPreview, Group, Cell, XButton
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
    },
    methods:{
      addPosts(){
        PostsApi.addPosts(this.success,this.fail)
      },
      success: function(status, text){
        if(status == 200){
          console.log("成功插入")
        }else if(status == 500){
          console.log("上传互选池失败")
        }
      },
      fail: function(err){
        console.log("错误发生了！！！")
        console.log(err)
      },
      recruit(){
        PostsApi.recruit_someone(3,this.success,this.fail)
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
