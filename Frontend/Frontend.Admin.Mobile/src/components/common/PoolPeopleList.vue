<template>
  <div>
    <card v-for="item in poolPeopleList" v-bind:key="item.id" class="card-padding"
          :style="'box-shadow: -4px 4px 2px #dddddd; margin-left: 10px; margin-right: 10px; border-left: 15px '+
          generateColor(item.id) +' solid;border-radius: 15px'">
      <div slot="content">
        <div class="content">
          <div style="display: inline-block; margin-left: 10px;">
            <div style="display: inline; margin-top: 10px">
              <div style="display: inline; margin-top: 10px; margin-bottom: 10px">
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
          <div style="display: inline;float: right;padding: 10px 10px 10px 150px;">
            <img :src="item.source"
                 :style="'width:'+windowSize*0.3+'px; height:'+windowSize*0.3+'px; display:inline; padding-right: 2%;float: right; margin-top: -120px'">
          </div>
        </div>
      </div>
    </card>
  </div>
</template>

<script>
  import {Card} from 'vux';
  import UserApi from '../../api/user'

  export default {

    components: {
      Card
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
          // },
          // {
          //   id: 2,
          //   education: '本',
          //   username: '娜扎阿拉提',
          //   birthDate: '1980',
          //   city: '南京',
          //   school: '南京大学',
          //   career: '金融',
          //   source: require("../../assets/logo.jpg")
          // }
        ],
        windowSize: document.body.clientWidth,
      }
    },
    methods: {
      success: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text);
          console.log(result);
          this.poolPeopleList = result
        }
        else
          console.log("有错误发生了")
      },

      fail: function (err) {
        console.log(err)
      },
      generateColor: function (id) {
        let array = ['#2f8bc3', '#a53cc3', '#29a83b', '#c3271e'];
        return array[id % 4];

      }
    },
    mounted() {
      UserApi.getUserList(this.success, this.fail)
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

  .pic-icon {
    width: 18px;
    height: 18px;
    margin-right: 4px;
    margin-bottom: -4px;
  }

</style>
