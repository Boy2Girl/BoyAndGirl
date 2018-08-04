<template>
  <div>
    <sub-title value="个人相册"/>
    <img v-for="item in form.photoList" :src="item.source" style="width:100px; height:100px; display:inline; padding: 2%"/>

    <sub-title value="基本信息"/>
    <group>
      <cell class="cell-font" title="昵称:" :value="form.nickname"/>
      <cell class="cell-font" title="编号:" :value="form.index"/>
      <cell class="cell-font" title="性别:" :value="form.gender"/>
      <cell class="cell-font" title="身高:" :value="form.p_height"/>
      <cell class="cell-font" title="出生日期:" :value="form.birthDate"/>
      <cell class="cell-font" title="婚姻状况:" :value="form.marriage"/>
      <cell class="cell-font" title="交友类型:" :value="form.friend"/>
      <cell class="cell-font" v-if="!to_post" title="电话:" text-align="right" v-model="form.phone"/>
      <cell class="cell-font" v-if="!to_post"  title="邮箱:" text-align="right" v-model="form.email"/>
      <cell class="cell-font" v-if="!to_post" title="qq:" text-align="right" v-model="form.qq"/>
      <cell class="cell-font" v-if="!to_post" title="微信:" text-align="right" v-model="form.wechat"/>
    </group>

    <sub-title value="坐标"/>
    <group>
      <cell class="cell-font" title="家乡:" :value="form.hometown"/>
      <cell class="cell-font" title="所在城市:" :value="form.city"/>
      <cell class="cell-font" title="居住地点：" :value="form.live"/>
    </group>

    <sub-title value="学校"/>
    <group>
      <cell class="cell-font" title="目前状态:" :value="form.studyState"/>
      <cell class="cell-font" title="本科学校:" :value="form.collageSchool"/>
      <cell class="cell-font" title="硕士学校:" :value="form.masterSchool"/>
      <cell class="cell-font" title="博士学校:" :value="form.doctorSchool"/>
      <cell class="cell-font" title="学历:" :value="form.education"/>
      <cell class="cell-font" title="专业:" :value="form.major"/>
    </group>

    <sub-title value="工作"/>
    <group>
      <cell class="cell-font" title="工作单位:" :value="form.corporation"/>
      <cell class="cell-font" title="工作状况:" :value="form.work_state"/>
      <cell class="cell-font" title="职业：" :value="form.career"/>
      <cell class="cell-font" title="单位类型:" :value="form.corporation_type"/>
      <cell class="cell-font" title="年收入（实际/预期）:" :value="form.income"/>
    </group>

    <sub-title value="住房/家庭情况"/>
    <group>
      <cell class="cell-font" title="住房情况:" :value="form.house_state"/>
      <cell class="cell-font" title="家庭情况:" :value="form.family_state"/>
    </group>

    <sub-title value="想说的话"/>
    <group>
      <x-textarea :disabled='disabled' class="cell-font" title="关于我:" :value="form.about_me"/>
      <x-textarea :disabled='disabled' style="margin-bottom: 48px; " class="cell-font" title="关于你:" :value="form.about_you"/>
    </group>

    <x-button class='button1' style="margin-bottom: 48px" v-if="to_post" :gradients="['#a66dcb','#e015fa']" @click.native="recruit">应征某人</x-button>
  </div>
</template>

<script>
  import {XTextarea, CellFormPreview, Group, Cell, XButton} from 'vux'
  import UserApi from '../../api/user'
  import SubTitle from './SubTitle'
  import PostsApi from '../../api/posts'

  export default {
    components: {
      XTextarea, CellFormPreview, Group, Cell, SubTitle, XButton
    },
    data() {
      return {
        to_post: false,
        disabled: true,
        form: {
          id: 1,
          avatarUrl: '',
          personUrl: '',
          studentUrl: '',
          graduateUrl: '',
          otherUrl: '',
          phone: ' ',
          email: ' ',
          qq: '',
          wechat: '',
          nickname: ' ',
          index: '',
          gender: '',
          p_height: '',
          birthDate: '2828',
          marriage: '未婚',
          friend: '',
          hometown: '',
          city: '',
          live: '',
          studyState: '',
          collageSchool: '',
          masterSchool: '',
          doctorSchool: '',
          education: '',
          major: '',
          corporation: '',
          work_state: '',
          career: '',
          corporation_type: '',
          income: '',
          house_state: '',
          family_state: '',
          about_you: 'adsjkfbdjksfbjksdhfjkhsdjkfhjksdhfjkhsahdjhasdhkkhjksdfjkjekg',
          about_me: '',
          photoList: [
            {
              id: 1,
              source: require('../../assets/background.jpg')
            },
            {
              id: 2,
              source: require('../../assets/background.jpg')
            }
          ]
        },
      }
    },
    created() {
      let to_post = this.$route.params.toPost;
      let id = this.$route.params.id;
      this.to_post = to_post;
      this.form.id = id;
      console.log(this.to_post + '是否加载aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    },
    mounted() {
      UserApi.getUserInfo(1, this.success, this.fail);
    },
    methods: {
      success: function (status, text) {
        if (status == 200) {
          console.log("成功插入")
          let result = (JSON.parse(text))
          this.form = result
        } else if (status == 500) {
          console.log("上传用户信息失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
      },
      recruit(){
        PostsApi.recruit_someone(3,this.success,this.fail)
      }
    }
  }
</script>

<style scoped>
  .sub-title {
    background-color: #FF66FF;
    color: white;
    padding: 4px;
    width: 110%;
    height: 110%;
    margin-left: 1%;
    margin-right: 1%;
    margin-top: 20px;
  }

  .cell-font {
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
  }

</style>
