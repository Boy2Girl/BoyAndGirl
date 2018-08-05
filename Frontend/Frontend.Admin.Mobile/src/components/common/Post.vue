<template>
  <div>
    <card v-for="item in postList" v-bind:key="item.id" class="mycard"
          :style="'box-shadow: -4px 4px 2px #dddddd; margin-left: 10px; margin-right: 10px; border-left: 15px '+
          generateColor(item.id) +' solid;border-radius: 15px'">
      <div slot="content" class="card-padding" @click="route(item.id, toPost)">
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
      <x-button class='button1' style="margin-bottom: 12px" v-if="toPost" type="primary"
                @click.native="addPosts">增加
      </x-button>
    </group>
    <group>
      <x-button class='button1' style="position:fixed; bottom:47px;" v-if="toPost" type="primary"
                @click.native="addPosts">增加
      </x-button>
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
          // {
          //   id: 1,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // },
          // {
          //   id: 2,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // },
          // {
          //   id: 3,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // },
          // {
          //   id: 4,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // },
          // {
          //   id: 5,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // },
          // {
          //   id: 6,
          //   education: '本',
          //   username: 'dhh',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // }
        ],
        windowSize: document.body.clientWidth,
        toPost: false
      }
    },
    methods: {
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
        PostsApi.addPosts(this.success, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
        } else if (status === 500) {
          console.log("上传互选池失败")
        }
      },
      getSuccess: function (status, text) {
        if (status === 200) {
          let result = (JSON.parse(text));
          console.log(result);
          this.postList = result
        } else if (status === 500) {
          console.log("上传互选池失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err)
      },
      recruit() {
        PostsApi.recruit_someone(3, this.success, this.fail)
      },
      generateColor: function (id) {
        let array = ['#2f8bc3', '#a53cc3', '#29a83b', '#c3271e'];
        return array[id % 4];

      }
    },
    mounted() {
      let name = this.$route.name;
      let toPost = this.toPost;
      if (name === 'posts') {
        PostsApi.getAll(this.getSuccess, this.fail);
        toPost = true;
      }
      else if (name === 'myPostOne') {
        PostsApi.getByUser(this.getSuccess, this.fail);
        toPost = false;
      }
      else if (name === 'OnePostMe') {
        PostsApi.getMy(this.getSuccess, this.fail);
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
