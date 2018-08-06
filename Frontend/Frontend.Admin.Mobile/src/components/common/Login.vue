<template>
  <div>
    <div>
      <alert v-model="show" :title="title"
             @on-show="onShow" @on-hide="onHide">
        {{ content }}
      </alert>
    </div>
    <div v-if="isLogIn" class="content content-front">
      <Group>
        <card :header="{title: '用户登陆',style:'font-size:20px;' }" style="border-radius: 5%;margin: 40% 5% 5%;">
          <div style="margin: 5%" slot="content">
            <x-input placeholder="  手机号" v-model="username" :max="13" is-type="china-mobile" class="input">
              <Icon slot="label" type="person" size="27" color="#6A005F"/>
            </x-input>
            <x-input title="" placeholder="  密码" v-model="password" class="input">
              <Icon slot="label" type="locked" size="27" color="#6A005F"/>
            </x-input>
            <div class="middle">
            </div>
            <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="signIn">登陆</x-button>
            <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="changeState">注册</x-button>
          </div>
        </card>
      </Group>
    </div>
    <div v-else class="content content-front">
      <Group>
        <card :header="{title: '用户注册',style:'font-size:20px;' }" style="border-radius: 5%;margin: 40% 5% 5%;">
          <div style="margin: 5%" slot="content">
            <x-input placeholder="  手机号" v-model="username" :max="13" is-type="china-mobile" class="input">
              <Icon slot="label" type="person" size="27" color="#6A005F"></Icon>
            </x-input>
            <x-input title="" placeholder="  密码" v-model="password" class="input" type="password">
              <Icon slot="label" type="locked" size="27" color="#6A005F"></Icon>
            </x-input>
            <x-input title="" placeholder="  再次输入密码" v-model="password2" class="input" type="password">
              <Icon slot="label" type="locked" size="27" color="#6A005F"></Icon>
            </x-input>
            <x-input placeholder="  验证码" class="input">
              <x-button slot="right" type="primary" mini>发送验证码</x-button>
            </x-input>
            <div class="middle">
            </div>
            <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="signUp">注册</x-button>
            <x-button class='button1' :gradients="['#a66dcb','#e015fa']" @click.native="changeState">返回登录</x-button>
          </div>
        </card>
      </Group>
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
        content: ''
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
      }
    }
  }
</script>

<style scoped>
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
</style>

