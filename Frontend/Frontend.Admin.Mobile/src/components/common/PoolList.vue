<template>
  <div>
    <card v-for="item in poolList" v-bind:key="item.id">
      <div slot="content" class="card-padding">
        <img :src="item.url"
             style="width:80px;height:80px;display:inline;padding-right: 2%">
        <div class="content">
          <div class="content-title">
            {{item.title}}
          </div>
          <div class="content-time">
            创建时间：{{item.time}}
          </div>
          <div class="content-address">
            地点：{{item.address}}
          </div>
          <div class="content-address">
            加入要求：{{item.requirement}}
          </div>
        </div>
      </div>
      <div slot="footer" class="vux-1px-r">
        <flexbox>
          <flexbox-item>
            <div class="info">
              男（{{item.numOfBoy}}）
            </div>
          </flexbox-item>
          <flexbox-item>
            <div class="info">
              女（{{item.numOfGirl}}）
            </div>
          </flexbox-item>
        </flexbox>
      </div>
    </card>
  </div>
</template>

<script>
  import {Card, XButton, Flexbox, FlexboxItem} from "vux";
  import PoolApi from '../../api/pool'
  export default {
    components: {
      Card, XButton, Flexbox, FlexboxItem
    },
    data() {
      return {
        poolList: [
          {
            id: 1,
            url: "http://placeholder.qiniudn.com/640x300",
            title: "南京互选池",
            time: "2018年02月21日",
            address: "南京",
            requirement: "南京工作或在读",
            numOfBoy: 301,
            numOfGirl: 301
          },
          {
            id: 1,
            url: "http://placeholder.qiniudn.com/640x300",
            title: "南京互选池",
            time: "2018年02月21日",
            address: "南京",
            requirement: "南京工作或在读",
            numOfBoy: 301,
            numOfGirl: 301
          }
        ]
      }
    },
    methods: {
      success:function(status,text){
        if(status == 200){
        let result = JSON.parse(text)
        console.log(result)
        this.poolList = result
        }
        else
        console.log("有错误发生了")
      },
      fail:function(err){
        console.log(err)
      }
    },
    mounted(){
      PoolApi.getAllPool(1,this.success,this.fail)
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

  .content-time {
  }

  .content-address {
  }

  .info {
    text-align: center;
  }
</style>
