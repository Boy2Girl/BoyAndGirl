<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <img :src="url" auto style="width:100%;margin:0 auto;" height="180px"/>
    <!-- <group label-width="4.5em" label-margin-right="2em" label-align="right"> -->
    <cell title="活动时间" :value="activityTime" value-text-align="left"/>
    <cell title="活动地点" :value="address"/>
    <cell title="报名时间" :value="registerTime" value-text-align="left"/>
    <cell title="互选时间" :value="selectTime" value-text-align="left"/>
    <cell title="收费规则" :value="chargeRule"/>
    <cell title="男/女年龄递增费用免收起始" :value="chargeBeginAge"/>
    <cell title="每大一岁递增加收" :value="increment"/>
    <cell title="活动负责人微信" v-model="wechat"/>
    <!-- </group> -->
    <!-- <group>
      <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="register_activity">报名活动</x-button>
    </group> -->
    <group>
      <group-title slot="title">
        <div style="padding: 5%;">详细信息：</div>
      </group-title>
      <div v-html='detail'></div>
    </group>
    <x-button v-if="!isRegistered" type="primary" class="btn btn-bottom" @click.native="register_activity">确认报名
    </x-button>
    <x-button v-else type="warn" class="btn btn-bottom" @click.native="cancel">取消报名</x-button>
    <div class="bottom">
    </div>
  </div>
</template>

<script>
  import {Cell, Group, GroupTitle, XButton, Alert} from "vux";
  import {mapGetters, mapMutations} from 'vuex'
  import ActivityApi from '../../api/activity'

  export default {
    components: {
      Cell, Group, GroupTitle, XButton, Alert
    },
    data() {
      return {
        activityTime: "",
        address: "",
        registerTime: "",
        selectTime: "",
        chargeRule: "",
        chargeBeginAge: "",
        increment: "",
        wechat: "",
        detail: "",
        isRegistered: false,
        url: '',
        show: false,
        title: '',
        content: ''
      }
    },
    mounted() {
      ActivityApi.checkRegister(this.$route.params.id, this.checkSuccess, this.fail)
      console.log(this.$route)
      ActivityApi.getActivity(this.$route.params.id, this.success, this.fail)
    },
    methods: {
      checkSuccess: function (status, text) {
        if (status === 200) {
          this.isRegistered = true;
        } else if (status === 500) {
          console.log("取消报名活动失败");
          // this.setState("失败", "取消报名活动失败");
        } else if (status === 404) {
          this.isRegistered = false;
          // this.setState("失败", "取消报名活动失败");
        } else if (status === 405) {
          console.log("您还没有报名活动");
          // this.setState("失败", "您尚未报名该活动");
        }
      },
      registerSuccess: function (status, text) {
        if (status === 200) {
          this.isRegistered = true;
          console.log("成功取消活动")
          this.setState("成功", "成功报名该活动");
        } else if (status === 500) {
          console.log("取消报名活动失败");
          this.setState("失败", "取消报名活动失败");
        } else if (status === 404) {
          console.log("抱歉，该活动不存在");
          this.setState("失败", "抱歉，该活动不存在");
        } else if (status === 405) {
          console.log("您还没有报名活动");
          this.setState("失败", "您还没有报名本活动");
        }
      },
      leaveSuccess: function (status, text) {
        if (status === 200) {
          this.isRegistered = false;
          console.log("成功报名活动");
          this.setState("成功", "取消报名活动成功");
        } else if (status === 500) {
          console.log("报名活动失败");
          this.setState("失败", "报名活动失败");
        } else if (status === 404) {
          console.log("抱歉，该活动不存在");
          this.setState("失败", "抱歉，该活动不存在");
        } else if (status === 405) {
          console.log("活动已经报名");
          this.setState("失败", "活动已报名");
        }
      },
      allSuccess: function (status, text) {
        if (status === 200) {
          console.log(JSON.parse(text))
        } else if (status === 500) {
          console.log("获取活动列表失败");
          this.setState("失败", "获取活动列表失败");
        }
      },
      register_activity: function () {
        ActivityApi.registerActivity(this.$route.params.id, this.registerSuccess, this.fail)
      },
      cancel: function () {
        ActivityApi.leaveActivity(this.$route.params.id, this.leaveSuccess, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text);
          console.log(result);
          this.activityTime = result.activityBeginTime + " - " + result.activityEndTime;
          this.address = result.location;
          this.registerTime = result.registerBeginTime + " - " + result.registerEndTime;
          this.selectTime = result.selectBeginTime + " - " + result.selectEndTime;
          this.chargeRule = result.chargeRule;
          this.chargeBeginAge = "男　" + result.boyBeginAge + "/" + "女　" + result.girlBeginAge;
          this.increment = result.increment;
          this.wechat = result.wechat;
          this.detail = result.detail;
          this.url = result.url;
        } else if (status === 500) {
          console.log("获取活动失败");
          this.setState("失败", "获取活动失败");
        } else if (status === 404) {
          console.log("没有该活动");
          this.setState("失败", "没有该活动");
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！");
        console.log(err);
        this.setState("失败", "网络错误");
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      }
    }
  }
</script>

<style lang="less" type="text/less">
  .btn {
  }

  .btn-bottom {
    position: absolute;
    // z-index: 999;
    bottom: 0;
    left: 0;
    width: 100%;
  }

  .bottom {
    height: 100px
  }
</style>
