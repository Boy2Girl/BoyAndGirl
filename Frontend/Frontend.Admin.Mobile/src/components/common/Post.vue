<template>
  <div>
    <card v-for="item in postList" v-bind:key="item.id">
      <div slot="content" class="card-padding" @click="route(item.id, toPost)">
        <div class="content">
          <div>
            <font
             style="background-color: #17872b; color: white; padding: 4px; width: 110%; height: 110%; margin-left: 1%; margin-right: 1%">{{item.education}}</font>
            <font style="font-weight: bolder">{{item.username}}</font>
          </div>
          <group>
            <cell class="cell-font" title="出生年份:" :style="'width:'+windowSize*0.65+'px'"> {{item.birthDate}}</cell>
            <cell class="cell-font" title="所在城市:"> {{item.city}}</cell>
            <cell class="cell-font" title="本科学校:">{{item.school}}</cell>
            <cell class="cell-font" title="职业:">{{item.career}}</cell>
          </group>
        </div>
        <img :src="item.source" :style="'width:'+windowSize*0.3+'px; height:'+windowSize*0.3+'px; margin-top: 20px'"/>
      </div>
    </card>

    <group>
      <x-button class='button1' style="position:fixed; bottom:48px;" v-if="toPost" :gradients="['#a66dcb','#e015fa']" @click.native="addPosts">增加</x-button>
    </group>
  </div>
</template>

<script>
  import {Card, CellFormPreview, Group, Cell, XButton} from 'vux'
  import PostsApi from '../../api/posts'
  import posts from '../../api/posts';
  import router from '../../router/index.js'

  export default {

    components: {
      Card, CellFormPreview, Group, Cell, XButton
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
          },
          {
            id: 2,
            education: '本',
            username: 'dhh',
            birthDate: '1980',
            city: '南京',
            school: '南京大学',
            career: '金融',
            source: require("../../assets/logo.jpg")
          }
        ],
        windowSize: document.body.clientWidth,
        toPost: false
      }
    },
    methods:{
      route: (id, toPost)=> {
        router.push({
          name:'info',
          params: {
            id:id,
            toPost: toPost
          }
        });
        // router.push('/user/info/'+id);
      } ,
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
      getSuccess: function(status, text){
        if(status == 200){
          let result = (JSON.parse(text))
          console.log(result)
          this.postList = result
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
    },
    mounted(){
      let name = this.$route.name;
      let toPost = this.toPost
      if(name == 'posts'){
        PostsApi.getAll(this.getSuccess, this.fail);
        toPost=true;
      }
      else if(name == 'myPostOne'){
        PostsApi.getByUser(this.getSuccess,this.fail);
        toPost=false;
      }
      else if(name == 'OnePostMe'){
        PostsApi.getMy(this.getSuccess,this.fail);
        toPost=false;
      }
      this.toPost = toPost
    }
  }
</script>

<style scoped>
  .cell-font {
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
  }
  .card-padding {
    display: flex;
    margin: 3%;
  }
  .content {
    display: inline;
  }
</style>
