<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <card v-for="item in postList" v-bind:key="item.id" class="mycard"
          :style="'box-shadow: -4px 4px 2px #dddddd; margin-left: 10px; margin-right: 10px; border-left: 15px '+
          generateColor(item.id) +' solid;border-radius: 15px'">
      <div slot="content" class="card-padding" @click="route(item.userID, toPost)">
        <div class="content">
          <div style="display: inline-block;">
            <div style="display: inline; margin-top: 10px">
              <div style="display: inline; margin-top: 10px; margin-bottom: 5px">
                <font class="content-tag">{{item.education}}</font>
                <font class="content-title">{{item.username}}</font>
              </div>
            </div>
            <div class="cell-text" style="margin-top: 7px">
              <img src="../../assets/date.png" class="pic-icon"/>
              出生年份：{{item.birthDate}}
            </div>
            <div class="cell-text">
              <img src="../../assets/city.png" class="pic-icon"/>
              所在城市：{{item.city}}
            </div>
            <div class="cell-text">
              <img src="../../assets/school.png" class="pic-icon"/>
              本科学校：{{item.school}}
            </div>
            <div class="cell-text">
              <img src="../../assets/work.png" class="pic-icon"/>
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
      <x-button class='button1' style="position:fixed; bottom:47px;" :gradients="['#43aaa7','#55bdd9']" v-if="toPost"
                @click.native="addPosts">增加
      </x-button>
    </group>
  </div>
</template>

<script>
  import {Card, CellFormPreview, Group, Cell, XButton, Alert} from 'vux'
  import PostsApi from '../../api/posts';
  import CheckApi from '../../api/check';
  import router from '../../router/index.js';
  import {mapGetters, mapMutations} from 'vuex';
  import UserApi from "../../api/user"
  export default {

    components: {
      Card, CellFormPreview, Group, Cell, XButton, Alert
    },
    data() {
      return {
        postList: [],
        windowSize: document.body.clientWidth,
        toPost: false,
        show: false,
        title: '',
        content: ''
      }
    },
    methods: {
      ...mapGetters(['getToken', 'getUserID']),
      ...mapMutations(['setToken', 'setUserID']),

      route: (id, toPost) => {
        router.push({
          name: 'info',
          params: {
            id: id,
            toPost: toPost
          }
        });
        // router.push('/user/info/'+id);
      },
      addPosts() {
        /**
         *  先检查有没有实名认证
         */
        CheckApi.check(this.checkSuccess, this.fail)
      },
      checkSuccess: function(status, text){
        if (status === 200) {
          let result = JSON.parse(text)
          if(result.isReal == false){
            this.setState("失败", "您还没有实名认证，不能进行发帖应征");
          }else{
            PostsApi.addPosts(this.success, this.fail)
          }
        }
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入");
          let name = this.$route.name;
          if (name === 'posts') {
            this.setState("成功", "您已成功参与互选");
          }
          else if (name === 'myPostOne') {
            this.setState("成功", "您已应征此人，静静等待他的回复吧");
          }
        } else if (status === 500) {
          console.log("上传互选池失败");
          this.setState("失败", "系统没有找到你qwq");
        }
      },
      getSuccess: function (status, text) {
        if (status === 200) {
          let result = (JSON.parse(text));
          console.log(result)
          this.postList = result
        } else if (status === 500) {
          console.log("获取帖子失败");
          this.setState("提醒", "目前没有记录，请耐心等待");
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err);
        this.setState("失败", "网络错误");
      },
      recruit() {
        PostsApi.recruit_someone(3, this.success, this.fail)
      },
      generateColor: function (id) {
        let array = ['#2f8bc3', '#a53cc3', '#29a83b', '#c3271e'];
        return array[id % 4];

      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      },

      getOpenIdSuccess: function (status, text) {
        console.log(JSON.parse(text));
        console.log(status);

        let response = JSON.parse(text)
        this.setToken(response.token);
        this.setUserID("A"+response.userID);

        PostsApi.get('all', 1, this.getSuccess, this.fail);

        console.log("拿到openid");
      },
      getOpenIdFail: function (e) {
        console.log("发现错误！！！");
        console.log(e);
        console.log("没有拿到openid");
      },
    },
    mounted() {
      let name = this.$route.name;
      let toPost = false;
      if (name === 'posts') {
        UserApi.getOpenid(window.location.href.split('=')[1].split('&')[0], this.getOpenIdSuccess, this.getOpenIdFail)
        toPost = true;
      }
      else if (name === 'myPostOne') {
        PostsApi.get('myPost', this.getUserID(), this.getSuccess, this.fail);
        toPost = false;
      }
      else if (name === 'OnePostMe') {
        PostsApi.get('postMy', this.getUserID(), this.getSuccess, this.fail);
        toPost = false;
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

  .cell-text {
    font-size: smaller;
    padding-bottom: 0px;
    padding-top: 2px;
  }

  .mycard:hover {
    box-shadow: -5px 5px 2px #bdbdbd;
  }

  .pic-icon {
    width: 18px;
    height: 18px;
    margin-right: 4px;
    margin-bottom: -4px;
  }
</style>
