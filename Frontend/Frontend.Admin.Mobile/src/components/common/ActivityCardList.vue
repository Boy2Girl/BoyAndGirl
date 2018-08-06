<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <card v-for="item in activityList" v-bind:key="item.id">
      <div slot="content" class="card-padding" @click="route(item.id)">
        <img :src="item.url"
             style="width:80px;height:80px;display:inline;padding-right: 2%">
        <div class="content">
          <div class="content-title">
            {{item.title}}
          </div>
          <div>
            <div class="content-tag">
              <div class="content-tag" style="background-color: blue;color:white;">品牌活动
              </div>
              <div class="content-tag" style="background-color: yellow;color:black;">互动交友
              </div>
              <div class="content-tag" style="background-color: red;color:white;">轻松快乐
              </div>
            </div>
            <div class="content-time">
              时间：{{item.time}}
            </div>
            <div class="content-address">
              地点：{{item.address}}
            </div>
          </div>
        </div>
      </div>
      <div slot="footer">
        <flexbox>
          <flexbox-item>
            <div class="info">
              <Icon type="ios-heart-outline"></Icon>
              {{item.numOfRead}} 阅读
            </div>
          </flexbox-item>
          <flexbox-item>
            <div class="info">
              <Icon type="ios-people" style="color: deepskyblue"/>
              {{item.numOfSign}} 报名
            </div>
          </flexbox-item>
        </flexbox>
      </div>
    </card>
  </div>
</template>

<script>
  import {Card, XButton, Flexbox, FlexboxItem, Alert} from "vux";
  import ActivityApi from '../../api/activity'
  import router from "../../router";

  export default {
    components: {
      Card, XButton, Flexbox, FlexboxItem, Alert
    },
    data() {
      return {
        activityList: [
          // {
          //   id: 1,
          //   url: "http://placeholder.qiniudn.com/640x300",
          //   title: "周三-单身大作战",
          //   time: "2018-08-01 19:00 ~ 2018-08-01 22:00",
          //   address: "专属微信群",
          //   numOfRead: 168,
          //   numOfSign: 15
          // },
          // {
          //   id: 2,
          //   url: "http://placeholder.qiniudn.com/640x300",
          //   title: "周三-单身大作战",
          //   time: "2018-08-01 19:00 ~ 2018-08-01 22:00",
          //   address: "专属微信群",
          //   numOfRead: 168,
          //   numOfSign: 15
          // }
        ],
        show: false,
        content: '',
        title: ''
      }
    },
    mounted() {
      let name = this.$route.name;
      if (name === "activity") {
        ActivityApi.getAllActivity(0, false, this.success, this.fail)
      } else if (name === "myActivity") {
        ActivityApi.getByUser(this.success, this.fail);
      } else if (name === "historyActivity") {
        ActivityApi.getAllActivity(0, false, this.success, this.fail)
      }
    },
    methods: {
      route: (id) => {
        router.push('/user/activity/' + id);
      },
      success: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text)
          console.log(result);
          this.activityList = result
        } else {
          console.log("有错误发生了");
          this.setState('错误', "您没有参加过活动");
        }
      },
      fail: function (err) {
        this.setState('错误', err);
        console.log(err)
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      }
    }
  }
</script>

<style scoped lang="less">
  .card-padding {
    display: flex;
    margin: 3%;
  }

  .card-footer {
    display: inline;
  }

  .content {
    display: inline;
  }

  .content-title {
    font-size: 16px;
    font-weight: bold;
  }

  .content-tag {
    display: inline;
    font-size: 10px;
    font-weight: bold;
    margin-right: 5px;
    text-align: center;
    padding: 1px;
    border-radius: 3px;
    opacity: 0.85;
  }

  .content-time {
  }

  .content-address {
    float: left;
  }

  .info {
    text-align: center;
  }
</style>
