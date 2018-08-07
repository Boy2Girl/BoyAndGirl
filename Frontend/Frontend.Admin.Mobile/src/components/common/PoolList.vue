<template>
  <div>
    <card v-for="item in poolList" v-bind:key="item.id"
          style="box-shadow: -4px 4px 2px #d5d5d5; margin-left: 8px; margin-right: 8px; margin-top: 5px">
      <div slot="content" class="card-padding" @click="route(item.id)">
        <img :src="item.url"
             style="width:80px;height:80px;display:inline;padding-right: 2%">
        <div class="content">
          <div class="content-title">
            {{item.title}}
          </div>
          <div class="content-text">
            创建时间：{{item.time}}
          </div>
          <div class="content-text">
            地点：{{item.address}}
          </div>
          <div class="content-text">
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
  import router from "../../router";
  import {mapGetters, mapMutations} from 'vuex'

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
            numOfGirl: 301,
          }
        ],
        id: ''
      }
    },
    methods: {
      ...mapMutations(['setToken', 'setUserID', 'setPoolID']),
      ...mapGetters(['getToken', 'getUserID', 'getPoolID']),
      success: function (status, text) {
        if (status == 200) {
          let result = JSON.parse(text)
          console.log(result)
          this.poolList = result
        }
        else
          console.log("有错误发生了")
      },
      fail: function (err) {
        console.log(err)
      },
      checkSuccess: function (status, text) {
        this.setPoolID(this.id)
        if (status == 200) {
          this.$router.push('/user/poolPeople')
        } else if (status == 404) {
          this.$router.push('/user/pool/' + this.id)
        }
      },
      route: function (id) {
        if(this.$route.path.split('/')[1]!='admin'){
            this.id = id;
            // 在这里还要判断是不是报名了，还要判断是不是进入...list
            PoolApi.checkRegister(id, this.checkSuccess, this.fail)
        }
      }
    },
    mounted() {
      // 这边还要分情况进行讨论
      let name = this.$route.name;
      console.log(name)
      if (name === "pool") {
        PoolApi.getAllPool(1, this.success, this.fail)
      } else if (name == 'myPool' || name == 'successPool') {
        PoolApi.getPoolByUser(this.success, this.fail)
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
    margin-left: 10px;
  }

  .content-title {
    font-size: 18px;
    font-weight: bold;
  }

  .content-text {
    font-size: 12px;
  }

  .info {
    text-align: center;
  }
</style>
