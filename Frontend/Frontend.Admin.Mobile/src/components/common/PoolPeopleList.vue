<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <card v-for="item in poolPeopleList" v-bind:key="item.id" class="card-padding"
          :style="'box-shadow: -4px 4px 2px #dddddd; margin-left: 10px; margin-right: 10px; border-left: 15px '+
          generateColor(item.id) +' solid;border-radius: 15px'">
      <div slot="content">
        <div style="display: inline; width: 70%">
          <div style="display: inline-grid; margin-left: 10px;">
            <div style="display: inline; margin-top: 10px;">
              <div style="display: inline; margin-top: 10px; margin-bottom: 10px;">
                <font class="content-tag">{{item.education}}</font>
                <font class="content-title">{{item.username}}</font>
              </div>
            </div>
            <div class="cell-text" style="margin-top: 7px;">
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
            <div style="margin-left: 100px; margin-top: 2px; font-size: 14px; margin-bottom: 8px;"
                 v-on:click="love_it(item.id)"
                 @click.native="love_it(item.id)">
              <Icon type="ios-heart" style="color: #b1000d"></Icon>
              <font style="margin-left: 10px; margin-bottom: 10px;">{{concern}}</font>
            </div>
          </div>
        </div>
        <!--<x-button type="primary" class="btn btn-bottom" @click.native="love_it(item.id)">关注这个人</x-button>-->
        <div style="display: inline; float: right; margin-right: 30px; margin-top: 20px;">
          <img :src="item.source"
               style="width:120px; height:120px; display:inline; margin-left: 20px; padding-right: 2%;float: right; margin-bottom: 8px;">
        </div>
      </div>
    </card>
  </div>
</template>

<script>
  import {Card, Alert, XButton} from 'vux';
  import UserApi from '../../api/user'
  import PoolApi from '../../api/pool'
  import {mapGetters, mapMutations} from 'vuex'

  export default {

    components: {
      Card, Alert, XButton
    },
    data() {
      return {
        poolPeopleList: [
          // {
          //   id: 1,
          //   education: '本',
          //   username: '娜扎阿拉提',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // }
        ],
        show: false,
        content: '',
        title: '',
        windowSize: document.body.clientWidth,
        concern: ' 动心'
      }
    },
    methods: {
      ...mapMutations(['setToken', 'setUserID', 'setPoolID']),
      ...mapGetters(['getToken', 'getUserID', 'getPoolID']),
      success: function (status, text) {
        console.log("success")
        if (status === 200) {
          let result = JSON.parse(text);
          console.log(result);
          this.poolPeopleList = result
        }
        else {
          this.setState("错误", "目前无法获得互选池信息╮(╯_╰)╭");
        }
      },

      fail: function (err) {
        console.log(err);
        this.setState("错误", "网络错误");
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
      loveSuccess: function (status, text) {
        console.log("success")
        if (status === 200) {
          // todo
          // 设置状态，改变button为取消关注？
        }
        else {
          this.setState("错误", "目前无法获得互选池信息╮(╯_╰)╭");
        }
      },
      love_it: function (id) {
        console.log(id)
        PoolApi.loveSomeone(id, this.getPoolID(), this.loveSuccess, this.fail);
      }
    },
    mounted() {
      let name = this.$route.name;
      console.log(name)
      console.log(this.getPoolID())
      if (name === "poolPeople") {
        PoolApi.getUserInPool(this.getPoolID(), this.success, this.fail)
      } else if (name === 'poolMyPeople') {
        PoolApi.getLove(this.getPoolID(), 'from', this.success, this.fail);
      } else if (name === 'poolTwoPeople') {
        PoolApi.getLove(this.getPoolID(), 'to', this.success, this.fail);
      } else{
        PoolApi.getLove(this.getPoolID(), 'both', this.success, this.fail)
      }
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

  .pic-icon {
    width: 18px;
    height: 18px;
    margin-right: 4px;
    margin-bottom: -4px;
  }

</style>
