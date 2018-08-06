<template>
  <div>
    <div>
      <alert v-model="show" :title="title"
             @on-show="onShow" @on-hide="onHide">
        {{ content }}
      </alert>
    </div>
    <div v-if="isLogIn" class="content content-front"
         :style="'width: 100%; height: 170%; background: url(' + require('../../assets/login.jpg') + '; background-repeat:no-repeat;'">
      <div class="title" style="margin-top: 70px; margin-bottom: -80px;">登&nbsp&nbsp陆</div>
      <card style="border-radius: 5%;margin: 35% 5% 5%; border: 4px solid #ffffff; box-shadow: -4px 4px 2px #dddddd;">
        <div style="margin: 5%" slot="content">
          <x-input placeholder="手机号" v-model="username" :max="13" is-type="china-mobile" class="input">
            <Icon slot="label" type="person" size="27" color="#6A005F" style="margin-right: 15px;"/>
          </x-input>
          <x-input title="" placeholder="密码" v-model="password" class="input" type="password">
            <Icon slot="label" type="locked" size="27" color="#6A005F" style="margin-right: 15px;"/>
          </x-input>
          <div class="middle">
          </div>
          <x-button class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="signIn" style="margin-top: 10px;">
            登陆
          </x-button>
          <x-button class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="changeState"
                    style="margin-top: 3px;">注册
          </x-button>
        </div>
      </card>

    </div>
    <div v-else class="content content-front"
         :style="'width: 100%; height: 170%; background: url(' + require('../../assets/login.jpg') + '; background-repeat:no-repeat;'">
      <div class="title" style="margin-top: 60px; margin-bottom: -100px;">
        注&nbsp&nbsp册
      </div>
      <card style="border-radius: 5%;margin: 35% 5% 5%; border: 4px solid #f5f5f5; box-shadow: -4px 4px 2px #dddddd;">
        <div style="margin: 3%" slot="content">
          <x-input placeholder="手机号" v-model="username" :max="13" is-type="china-mobile" class="input">
            <Icon slot="label" type="person" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <x-input title="" placeholder="密码" v-model="password" class="input" type="password">
            <Icon slot="label" type="locked" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <x-input title="" placeholder="再次输入密码" v-model="password2" class="input" type="password">
            <Icon slot="label" type="locked" size="27" color="#6A005F" style="margin-right: 15px;"></Icon>
          </x-input>
          <x-input placeholder="验证码" class="input">
            <x-button slot="right" type="primary" mini>发送验证码</x-button>
          </x-input>
          <div class="middle">
          </div>
          <x-button class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="signUp" style="margin-top: 10px;">
            注册
          </x-button>
          <x-button class='button1' :gradients="['#43aaa7','#55bdd9']" @click.native="changeState"
                    style="margin-top: 3px;">返回登录
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
  import router from '../../router/index.js'

  export default {
    components: {
      Card, XInput, Group, XButton, Alert
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
        content: 'hhh'
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

          UserApi.getUserInfo(this.getUserID(), this.userInfoSuccess, this.fail);
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
        else if (this.password === this.password2)
          UserApi.signUp(this.username, this.password, this.getRole(), this.signupSuccess, this.fail);
        else
          this.setState("错误", "您两次输入的密码不一致");
      },
      changeState: function () {
        this.isLogIn = !this.isLogIn
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

      },
      onHide: function () {
        if (this.title === "成功") {
          this.isLogIn = true
        }
      },
      getpath: function () {
        let js = document.scripts;
        //js[js.length - 1] 就是当前的js文件的路径
        js = js[js.length - 1].src.substring(0, js[js.length - 1].src.lastIndexOf("/") + 1);

        return js;
      }
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

