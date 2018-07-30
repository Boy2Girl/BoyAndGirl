<template>
  <div>
    <div class="content content-front">
      <card :header="{title: '用户登陆',style:'font-size:20px;' }" style="border-radius: 5%;margin: 40% 5% 5%;">
        <div style="margin: 5%" slot="content">
          <x-input placeholder="  手机号" v-model="phone" :max="13" is-type="china-mobile" class="input">
            <icon slot="label" type="person" size="27" color="#6A005F"/>
          </x-input>
          <x-input title="" placeholder="  密码" v-model="password" class="input">
            <icon slot="label" type="locked" size="27" color="#6A005F"/>
          </x-input>
          <x-input placeholder="  验证码" class="input">
            <x-button slot="right" type="primary" mini>发送验证码</x-button>
          </x-input>
          <div class="middle">
          </div>
          <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="handle">登陆</x-button>
        </div>
      </card>
    </div>
  </div>
</template>

<script>

  import {Card, Icon, XInput, Group, XButton} from 'vux';

  export default {
    components: {
      Card, Icon, XInput, Group, XButton
    },
    data() {
      return {
        userName: '',
        passWord: '',
        code: '',
        phone: '',
        password: ''
      }
    },
    mounted() {
      this.name = this.$route.query.redirect;
      if (this.name === undefined || this.name === "") {
        this.name = "academy"
      }
      console.log("name  " + this.name)
      console.log(this.$store)
    },
    methods: {}
  }
</script>

<style scoped>
  .content {
    color: #ffffff;
  }

  .content-front {
    position: absolute;
    left: 10px;
    right: 10px;
    text-align: center;
  }

  .button1 {
    width: 85%;
  }

  .input {
    width: 85%;
  }

  .middle {
    height: 50px;
  }
</style>

