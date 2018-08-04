<template>
  <div>
    <card v-for="item in postList" v-bind:key="item.id">
      <div slot="content" class="card-padding" @click="route(item.id, toPost)">
          <div class="content">
            <div style="display: inline-block;">
              <div style="display: inline; margin-top: 10px">
                <div style="display: inline; margin-top: 10px; margin-bottom: 10px">
                  <font class="content-tag">{{item.education}}</font>
                  <font class="content-title">{{item.username}}</font>
                </div>
              </div>
              <div class="cell-text" style="margin-top: 7px">
                出生年份：{{item.birthDate}}
              </div>
              <div class="cell-text">
                所在城市：{{item.city}}
              </div>
              <div class="cell-text">
                本科学校：{{item.school}}
              </div>
              <div class="cell-text">
                职业：{{item.career}}
              </div>
            </div>
            <div style="display: inline;float: right;padding: 10px;padding-left: 150px">
              <img :src="item.source"
                   :style="'width:'+windowSize*0.3+'px; height:'+windowSize*0.3+'px; display:inline; padding-right: 2%;float: right; margin-top: -120px'">
            </div>
          </div>
        </div>
    </card>
    <group>
      <x-button class='button1' style="position:fixed; bottom:48px;" v-if="toPost" :gradients="['#c6634b','#e9672c']" @click.native="addPosts">增加</x-button>
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
          let result = (JSON.parse(text));
          console.log(result);
          this.postList = result
        }else if(status == 500){
          console.log("上传互选池失败")
        }
      },
      fail: function(err){
        console.log("错误发生了！！！");
        console.log(err)
      },
      recruit(){
        PostsApi.recruit_someone(3,this.success,this.fail)
      }
    },
    mounted(){
      let name = this.$route.name;
      let toPost = this.toPost;
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
  .card-padding {
    display: flex;
    margin-left: 3%;
    margin-right: 3%;
    padding-top: 1.5%;
  }

  .content {
    display: inline;
  }

  .content-title {
    font-size: 16px;
    font-weight: bold;
    display: inline;
  }

  .content-tag {
    font-size: 10px;
    font-weight: bold;
    margin-right: 5px;
    text-align: center;
    padding: 4px;
    border-radius: 4px;
    width: 110%;
    height: 110%;
    background-color: #17872b;
    color: white;
  }

  .cell-text{
    font-size: smaller;
    padding-bottom: 0px;
    padding-top: 2px;
  }
</style>
