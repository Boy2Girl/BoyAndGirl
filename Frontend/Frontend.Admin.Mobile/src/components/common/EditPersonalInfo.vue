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
      <cell class="cell-font" title="昵称:" v-model="form.nickname"/>
      <cell class="cell-font" title="编号:" v-model="form.index"/>
      <popup-picker title="性别" class="cell-font" :data="list_gender" value-text-align="right" v-model="form.gender"/>
      <x-input class="cell-font" title="身高(cm):" text-align="right" v-model="form.p_height"/>
      <datetime class="cell-font" title="出生日期:" v-model="form.birthDate" value-text-align="right"/>
      <popup-picker class="cell-font" title="婚姻状况:" :data="list_state" value-text-align="right"
                    v-model="form.marriage"/>
      <popup-picker class="cell-font" title="交友类型:" :data="list_type" value-text-align="right" v-model="form.friend"/>
      <x-input class="cell-font" title="电话:" text-align="right" v-model="form.phone"/>
      <x-input class="cell-font" title="邮箱:" text-align="right" v-model="form.email"/>
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
      <popup-picker class="cell-font" title="学历:" :data="list_education" value-text-align="right" v-model="form.education"/>
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
  import FileUPloader from './FileUploader'
  import UserApi from '../../api/user'
  import SubTitle from './SubTitle'
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
        form:{
          avatarUrl:'',
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
          gender: [],
          p_height: '',
          birthDate: '',
          marriage: [],
          friend: [],
          hometown: '',
          city: '',
          live: '',
          studyState: '',
          collageSchool: '',
          masterSchool: '',
          doctorSchool: '',
          education: [],
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
        console.log(this.form);
        UserApi.addUserInfo(this.form, this.success, this.fail)
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入")
          // 返回
          this.$router.go(-1);
        } else if (status === 500) {
          console.log("上传用户信息失败")
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
      }
    }
  }
</script>

<style scoped>
  .subtitle{
    margin-top: 10px;
  }

  .cell-font{
    font-size: smaller;
  }

  .group-type{
    margin-top: 5px;
  }
</style>
