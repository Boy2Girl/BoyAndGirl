<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"
             @on-show="onShow" @on-hide="onHide"/>
    </div>
    <div class="content content-front"
         :style="'width: 100%; height: 170%; background: url(' + require('../../assets/login.jpg') + ';'">
      <div class="title" style="margin-top: 40px; margin-bottom: -80px;">{{titleText}}</div>
      <card style="border-radius: 5%;margin: 35% 5% 5%; border: 4px solid #ffffff; box-shadow: -4px 4px 2px #dddddd;">
        <div slot="content">
          <x-input placeholder="手机号" v-model="username" :max="13" is-type="china-mobile" class="input">
            <Icon slot="label" type="person" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <x-input title="" placeholder="密码" v-model="password" class="input" type="password">
            <Icon slot="label" type="locked" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <div class="middle">
          </div>
          <x-input v-if="!isLogIn" title="" placeholder="再次输入密码" v-model="password2" class="input" type="password">
            <Icon slot="label" type="locked" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <x-input v-if="!isLogIn" placeholder="验证码" class="input">
            <x-button slot="right" type="primary" mini>发送验证码</x-button>
          </x-input>
          <x-button v-if="isLogIn" class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="signIn"
                    style="margin-top: 10px;">
            登陆
          </x-button>
          <x-button v-if="!isLogIn" class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="signUp"
                    style="margin-top: 10px;">
            注册
          </x-button>
          <x-button class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="changeState"
                    style="margin-top: 3px; margin-bottom: 10px">{{buttonText}}
          </x-button>

        </div>
      </card>

    </div>
  </div>
</template>

<script>
  import {Card, XInput, Group, XButton, Alert} from 'vux';
  import {mapGetters, mapMutations} from 'vuex'
  import UserApi from '../../api/user'
  import {Icon} from 'iview';


  export default {
    components: {
      Card, XInput, Group, XButton, Alert,Icon
    },
    data() {
      return {
        username: '',　// phone number
        password: '',
        password2: '',
        code: '',
        isLogIn: true,
        show: false,
        title: '',
        content: 'hhh',
        buttonText: '注册',
        titleText: '登  录'
      }
    },
    mounted() {

    },
    methods: {
      ...mapMutations(['setToken', 'setUserID']),
      ...mapGetters(['getToken', 'getUserID']),
      signinSuccess: function (status, text) {
        console.log('请求结果');
        console.log(text + " " + status);
        if (status === 200) {
          let token = JSON.parse(text);
          this.setToken(token.token);
          this.setUserID(token.id);

          if (this.getRole() === UserApi.ROLE.ADMIN && this.isLogIn === true) {
            if (this.$router.redirect === location.hostname) {
              this.$router.go(-1);
            }
            else {
              this.$router.push('/admin/activity');
            }
            //router.push('admin/activity');
          }
          else if (this.getRole() === UserApi.ROLE.USER && this.isLogIn === true) {
            if (this.$router.redirect === location.hostname) {
              this.$router.go(-1);
            }
            else {
              this.$router.push('/user/activity');
            }
            //router.push('user/activity');
          }
          //UserApi.getUserInfo(this.getUserID(), this.userInfoSuccess, this.fail);
        } else if (status === 404) {
          this.setState("失败", "该用户不存在");
        } else if (status === 403) {
          this.setState("失败", "用户名或者密码错误");
        }
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      },
      signupSuccess: function (status, text) {
        console.log('请求结果');
        console.log(text + " " + status);
        if (status === 200) {
          let token = JSON.parse(text);
          this.setToken(token.token);

          window.location.href =
            "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxcf058ebab08beee9&redirect_uri=http%3a%2f%2fwww.injusalon.com%2f%23%2fuser%2factivity&response_type=code&scope=snsapi_base&state=123#wechat_redirect";

          this.setState("成功", "恭喜您注册成功");
        } else if (status === 405) {
          this.setState("错误", "该用户已经存在");
        }
      },
      userInfoSuccess: function (status, text) {
        if (status === 200) {
          console.log(JSON.parse(text))
        } else if (status === 404) {
          this.setState("错误", "该用户还没有进行实名认证");
        }
      },
      fail: function (e) {
        console.log("发现错误！！！");
        console.log(e)
      },
      signIn: function () {
        UserApi.signIn(this.username, this.password, this.getRole(), this.signinSuccess, this.fail)
      },
      signUp: function () {
        if (this.username === '' || this.password === '')
          this.setState("错误", "用户名或者密码不能为空");
        else if (this.password === this.password2) {
          if(!/^1[34578]\d{9}$/.test(this.username)){
            this.setState('错误', '请输入正确的手机号码');
          }
          else
            UserApi.signUp(this.username, this.password, this.getRole(), this.signupSuccess, this.fail);
        }
        else
          this.setState("错误", "您两次输入的密码不一致");
      },
      changeState: function () {
        this.isLogIn = !this.isLogIn
        if (this.isLogIn) {
          this.buttonText = '注册';
          this.titleText = '登  录';
        }
        else {
          this.buttonText = '返回登录';
          this.titleText = '注  册';
        }
      },
      getRole: function () {
        let role = '';
        if (this.$route.path.split('/')[this.$route.path.split('/').length - 1] === 'admin') {
          role = UserApi.ROLE.ADMIN
        } else {
          role = UserApi.ROLE.USER
        }
        return role
      },
      onShow: function () {
        // if (this.getRole() === UserApi.ROLE.ADMIN && this.isLogIn === true) {
        //   if (this.$router.redirect === location.hostname) {
        //     this.$router.go(-1);
        //   }
        //   else {
        //     this.$router.push('/admin/activity');
        //   }
        //   //router.push('admin/activity');
        // }
        // else if (this.getRole() === UserApi.ROLE.USER && this.isLogIn === true) {
        //   if (this.$router.redirect === location.hostname) {
        //     this.$router.go(-1);
        //   }
        //   else {
        //     this.$router.push('/user/activity');
        //   }
        //   //router.push('user/activity');
        // }

      },
      onHide: function () {
        if (this.title === "成功") {
          this.isLogIn = true
        }
      },
    }
  }
</script>

<style scoped>
  .content-front {
    position: absolute;
    text-align: center;
  }

  .button1 {
    width: 85%;
  }

  .input {
    width: 90%;
    padding-left: 4px;
    border-bottom: 1px solid #797979;
    margin-left: 5%;
  }

  .title {
    -webkit-text-fill-color: #ffffff; /*伪空心的文字，与背景色有关*/
    -webkit-text-stroke-color: #9e9e9e;
    -webkit-text-stroke-width: 1px;
    /*W3C标准*/
    text-fill-color: #d1d1d1;
    text-stroke-color: #9e9e9e;
    text-stroke-width: 1px;

    font-weight: bolder;
    font-size: 40px;

    text-shadow: -5px 5px 5px #313131, -0px 0px 2px #d77c35, -2px 2px 3px #0b807d; /**/
  }
</style>

