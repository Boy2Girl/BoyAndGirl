<template>
  <div>
    <card v-for="item in activityList" v-bind:key="item.id">
      <div slot="content" class="card-padding">
        <img src="http://placeholder.qiniudn.com/640x300"
             style="width:80px;height:80px;display:inline;padding-right: 2%">
        <div class="content">
          <div class="content-title">
            {{item.title}}
          </div>
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
      <div slot="footer" class="vux-1px-r">
        <flexbox>
          <flexbox-item>
            <div class="info">
              <Icon type="ios-heart-outline"/>
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
  import {Card, XButton, Flexbox, FlexboxItem} from "vux";

  export default {
    components: {
      Card, XButton, Flexbox, FlexboxItem
    },
    data() {
      return {
        activityList: [
          {
            id: 1,
            title: "周三-单身大作战",
            time: "2018-08-01 19:00 ~ 2018-08-01 22:00",
            address: "专属微信群",
            numOfRead: 168,
            numOfSign: 15
          },
          {
            id: 2,
            title: "周三-单身大作战",
            time: "2018-08-01 19:00 ~ 2018-08-01 22:00",
            address: "专属微信群",
            numOfRead: 168,
            numOfSign: 15
          }
        ]
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
    border-radius: 5px;
  }

  .content-time {
  }

  .content-address {
  }

  .info {
    text-align: center;
  }
</style>
