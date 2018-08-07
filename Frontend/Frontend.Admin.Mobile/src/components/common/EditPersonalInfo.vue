<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content"/>
    </div>
    <sub-title class="sub-title" value="头像"/>
    <group class="group-type">
      <FileUPloader :url="actionUrl" v-on:child-say="getAvatar"/>
      <!-- <img :src="source" class="photo"/> -->
      <!-- <img src="../../assets/add.png" class="photo"/> -->
    </group>

    <sub-title class="subtitle" value="基本信息"/>
    <group>
      <x-input class="cell-font" title="昵称:" text-align="right" v-model="form.nickname"/>
      <x-input class="cell-font" title="姓名:" text-align="right" v-model="form.name"/>
      <cell class="cell-font" title="编号:" v-model="form.index"/>
      <popup-picker title="性别" class="cell-font" :data="list_gender" value-text-align="right" v-model="form.gender"/>
      <x-input class="cell-font" title="身高(cm):" :required="true" text-align="right" v-model="form.p_height"/>
      <datetime class="cell-font" title="出生日期:" v-model="form.birthDate" value-text-align="right"/>
      <popup-picker class="cell-font" title="婚姻状况:" :data="list_state" value-text-align="right"
                    v-model="form.marriage"/>
      <popup-picker class="cell-font" title="交友类型:" :data="list_type" value-text-align="right" v-model="form.friend"/>
      <x-input class="cell-font" title="电话:" text-align="right" is-type="china-mobile" v-model="form.phone"/>
      <x-input class="cell-font" title="邮箱:" text-align="right" is-type="email" v-model="form.email"/>
      <x-input class="cell-font" title="qq:" text-align="right" v-model="form.qq"/>
      <x-input class="cell-font" title="微信:" text-align="right" v-model="form.wechat"/>
    </group>


    <sub-title class="subtitle" value="坐标"/>
    <group>
      <x-input class="cell-font" title="家乡:" text-align="right" v-model="form.hometown"/>
      <x-input class="cell-font" title="所在城市:" text-align="right" v-model="form.city"/>
      <x-input class="cell-font" title="居住地点：" text-align="right" v-model="form.live"/>
    </group>

    <sub-title class="subtitle" value="学校"/>
    <group>
      <x-input class="cell-font" title="目前状态:" text-align="right" v-model="form.studyState"/>
      <x-input class="cell-font" title="本科学校:" text-align="right" v-model="form.collageSchool"/>
      <x-input class="cell-font" title="硕士学校:" text-align="right" v-model="form.masterSchool"/>
      <x-input class="cell-font" title="博士学校:" text-align="right" v-model="form.doctorSchool"/>
      <popup-picker class="cell-font" title="学历:" :data="list_education" value-text-align="right"
                    v-model="form.education"/>
      <x-input class="cell-font" title="专业:" text-align="right" v-model="form.major"/>
    </group>

    <sub-title class="subtitle" value="工作"/>
    <group>
      <x-input class="cell-font" title="工作单位:" text-align="right" v-model="form.corporation"/>
      <x-input class="cell-font" title="工作状况:" text-align="right" v-model="form.work_state"/>
      <x-input class="cell-font" title="职业：" text-align="right" v-model="form.career"/>
      <x-input class="cell-font" title="单位类型:" text-align="right" v-model="form.corporation_type"/>
      <x-input class="cell-font" title="年收入（实际/预期）:" label-width="180px" text-align="right" v-model="form.income"/>
    </group>

    <sub-title class="subtitle" value="住房/家庭情况"/>
    <group>
      <x-input class="cell-font" title="住房情况:" text-align="right" v-model="form.house_state"/>
      <x-input class="cell-font" title="家庭情况:" text-align="right" v-model="form.family_state"/>
    </group>

    <sub-title class="subtitle" value="想说的话"/>
    <group>
      <x-textarea class="cell-font" title="关于我:" v-model="form.about_me"/>
      <x-textarea class="cell-font" title="关于你:" v-model="form.about_you"/>
    </group>

    <sub-title value="身份证"/>
    <FileUPloader :url="actionUrl" v-on:child-say="getPerson"/>

    <sub-title value="学生证"/>
    <FileUPloader :url="actionUrl" v-on:child-say="getStudent"/>

    <sub-title value="本科毕业证"/>
    <FileUPloader :url="actionUrl" v-on:child-say="getGraduate"/>

    <sub-title value="其他身份学历及证明"/>
    <group>
      <FileUPloader :url="actionUrl" v-on:child-say="getOthers"/>
    </group>

    <x-button style="margin-bottom: 48px" type="primary" @click.native="save_info">保存</x-button>
    <x-button style="bottom: 48px; position: fixed" type="primary" @click.native="save_info">保存</x-button>
  </div>
</template>

<script>
  import FileUPloader from './FileUploader';
  import UserApi from '../../api/user';
  import SubTitle from './SubTitle';
  import {mapGetters, mapMutations} from 'vuex';
  import CheckApi from '../../api/check';

  import {
    XButton,
    GroupTitle,
    Group,
    Cell,
    XInput,
    Selector,
    PopupPicker,
    Datetime,
    XNumber,
    ChinaAddressData,
    XAddress,
    XTextarea,
    XSwitch,
    Alert
  } from 'vux'

  export default {
    components: {
      SubTitle,
      FileUPloader,
      XButton,
      Group,
      GroupTitle,
      Cell,
      XInput,
      Selector,
      PopupPicker,
      XAddress,
      Datetime,
      XNumber,
      XTextarea,
      XSwitch,
      Alert
    },
    data() {
      return {
        actionUrl: "http://127.0.0.1:5000/api/test",
        source: require('../../assets/background.jpg'),
        form: {
          avatarUrl: '',
          personUrl: '',
          studentUrl: '',
          graduateUrl: '',
          otherUrl: '',
          phone: ' ',
          email: ' ',
          qq: '',
          wechat: '',
          nickname: '',
          index: '',
          gender: ['男'],
          p_height: '',
          birthDate: '',
          marriage: ['未婚'],
          friend: ['恋爱'],
          hometown: '',
          city: '',
          live: '',
          studyState: '',
          collageSchool: '',
          masterSchool: '',
          doctorSchool: '',
          education: ['本科'],
          major: '',
          corporation: '',
          work_state: '',
          career: '',
          corporation_type: '',
          income: '',
          house_state: '',
          family_state: '',
          about_you: '',
          about_me: '',
        },
        list_gender: [['男', '女']],
        list_state: [['未婚', '离婚未育', '离异子女判给对方', '离异子女跟自己', '丧偶未育', '丧偶子女跟自己', '丧偶子女不跟自己', '其他']],
        list_type: [['恋爱', '结婚']],
        list_education: [['小学', '初中', '高中', '大专', '本科', '硕士', '博士']],
        show: false,
        title: '',
        content: ''
      }
    },
    methods: {
      ...mapMutations(['setToken', 'setUserID']),
      ...mapGetters(['getToken', 'getUserID']),
      getAvatar(url) {
        this.form.avatarUrl = url;
      },
      getPerson(url) {
        this.form.personUrl = url
      },
      getStudent(url) {
        this.form.studentUrl = url
      },
      getGraduate(url) {
        this.form.studentUrl = url
      },
      getOthers(url) {
        this.form.otherUrl = url
      },
      save_info() {
        console.log('保存数据了');
        UserApi.addUserInfo(this.form, this.success, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
          // 返回
          this.$router.go(-1);
        } else if (status === 500) {
          this.setState("错误", "上传用户信息失败");
        }
      },
      fail: function (err) {
        this.setState("错误", "网络错误");
        console.log("错误发生了！！！");
        console.log(err)
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      },
      loadSuccess: function (status, text) {
        var result = (JSON.parse(text));
        if (status === 200) {
          this.form.index = result['id'];
          this.form.phone = result['phone'];
          this.form.email = result['email'];
          this.form.gender = [result['gender']];
          this.form.nickname = result['name'];
          this.form.name = result['realName'];
          this.form.avatarUrl = result['avatar'];
          this.form.personUrl = result['personalUrl'];
          this.form.studentUrl = result['studentUrl'];
          this.form.graduateUrl = result['graduateUrl'];
          this.form.otherUrl = result['otherUrl'];
          this.form.qq = result['qq'];
          this.form.wechat = result['wechat'];
          this.form.p_height = result['p_height'];
          this.form.birthDate = result['bornDate'];
          this.form.marriage = [result['marriage']];
          this.form.friend = [result['friend']];
          this.form.hometown = result['hometown'];
          this.form.city = result['city'];
          this.form.live = result['livingPlace'];
          this.form.studyState = result['studyState'];
          this.form.collageSchool = result['collageSchool'];
          this.form.masterSchool = result['masterSchool'];
          this.form.doctorSchool = result['doctorSchool'];
          this.form.education = [result['education']];
          this.form.major = result['major'];
          this.form.corporation = result['company'];
          this.form.work_state = result['work_state'];
          this.form.career = result['job'];
          this.form.corporation_type = result['corporation_type'];
          this.form.income = result['income'];
          this.form.house_state = result['housingCondition'];
          this.form.family_state = result['economyCondition'];
          this.form.about_you = result['about_you'];
          this.form.about_me = result['about_me'];
        }
      },
      loadFail: function (status, text) {

      },
      checkSuccess: function (status, text) {
        if (status === 200) {
          let result = JSON.parse(text)
          if (result.isReal == false) {
            UserApi.getUserInfo(this.form.index, 'False', this.loadSuccess, this.loadFail);
          } else {
            UserApi.getUserInfo(this.form.index, 'True', this.loadSuccess, this.loadFail);
          }
        }
      },
    },
    mounted() {
      this.form.index = this.getUserID();
      CheckApi.check(this.checkSuccess, this.fail)
    }
  }
</script>

<style scoped>
  .subtitle {
    margin-top: 10px;
  }

  .cell-font {
    font-size: smaller;
  }

  .group-type {
    margin-top: 5px;
  }
</style>
