<template>
  <div>
    <card v-for="item in poolPeopleList" v-bind:key="item.id" class="card-padding">
      <div slot="content">
        <div class="content">
          <div style="display: inline-block;">
            <div style="display: inline;margin:2%">
              <div style="display: inline;">
                <div class="content-tag">{{item.education}}</div>
              </div>
              <div class="content-title">
                {{item.username}}
              </div>
            </div>
            <div class="content-time">
              出生年份：{{item.birthDate}}
            </div>
            <div class="content-address">
              所在城市：{{item.city}}
            </div>
            <div class="content-address">
              本科学校：{{item.school}}
            </div>
            <div class="content-address">
              职业：{{item.career}}
            </div>
          </div>
          <div style="display: inline;float: right;padding: 10px;padding-left: 150px">
            <img :src="item.source"
                 style="width:80px;height:80px;display:inline;padding-right: 2%;float: right">
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
          {
            id: 1,
            education: '本',
            username: '娜扎阿拉提',
            birthDate: '1980',
            city: '南京',
            school: '南京大学',
            career: '金融',
            source: require("../../assets/logo.jpg")
          }
        ]
      }
    },
    methods:{
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
      }
    },
    mounted(){
      UserApi.getUserList(this.success,this.fail)
    }
  }
</script>

<style scoped>
  .card-padding {
    display: flex;
    margin: 3%;
    padding: 3%;
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
    display: inline;
    font-size: 10px;
    font-weight: bold;
    margin-right: 5px;
    text-align: center;
    padding: 1px;
    border-radius: 5px;
    opacity: 0.85;
    background-color: #00CC66;
  }

  .content-time {
  }

  .content-address {
  }

</style>
