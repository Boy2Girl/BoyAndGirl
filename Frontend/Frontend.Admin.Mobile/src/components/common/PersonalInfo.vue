<template>
  <div>
    <div class="sub">个人相册</div>
    <img v-for="item in form.photoList" :src="item.source"
         style="width:100px; height:100px; display:inline; padding: 2%"/>

    <div class="sub">基本信息</div>
    <cell-form-preview class="form-text" :list="[
    {label: '昵称', value: form.nickname},
    {label: '编号', value: form.index},
    {label: '性别', value: form.gender},
    {label: '身高（cm）', value: form.p_height},
    {label: '出生日期', value: form.birthDate},
    {label: '婚姻状况', value: form.marriage},
    {label: '交友类型', value: form.friend}]"/>

    <div class="sub">联系方式</div>
    <cell-form-preview class="form-text" v-if="!to_post" :list="[
    {label: '电话', value: form.phone},
    {label: '邮箱', value: form.email},
    {label: 'qq', value: form.qq},
    {label: '微信', value: form.wechat}]"/>

    <div class="sub">坐标</div>
    <cell-form-preview class="form-text" :list="[
    {label: '家乡', value: form.hometown},
    {label: '所在城市', value: form.city},
    {label: '居住地点', value: form.live}]"/>

    <div class="sub">学习情况</div>
    <cell-form-preview class="form-text" :list="[
    {label: '目前状态', value: form.studyState},
    {label: '本科学校', value: form.collageSchool},
    {label: '硕士学校', value: form.masterSchool},
    {label: '博士学校', value: form.doctorSchool},
    {label: '学历', value: form.education},
    {label: '专业', value: form.major}]"/>

    <div class="sub">工作</div>
    <cell-form-preview class="form-text" :list="[
    {label: '工作单位', value: form.corporation},
    {label: '工作状况', value: form.work_state},
    {label: '职业', value: form.career},
    {label: '单位类型', value: form.corporation_type},
    {label: '年收入（实际/预期）', value: form.income}]"/>

    <div class="sub">住房/家庭情况</div>
    <cell-form-preview class="form-text" :list="[
    {label: '住房情况', value: form.house_state},
    {label: '家庭情况', value: form.family_state}]"/>

    <div class="sub">想说的话</div>
    <x-textarea :disabled='disabled' class="cell-font" title="关于我:" :value="form.about_me"/>
    <x-textarea :disabled='disabled' style="margin-bottom: 48px; " class="cell-font" title="关于你:"
                :value="form.about_you"/>


    <x-button class='button1' style="margin-bottom: 48px" v-if="to_post" type="primary"
              @click.native="recruit">应征某人
    </x-button>
  </div>
</template>

<script>
  import {XTextarea, CellFormPreview, Group, Cell, XButton} from 'vux'
  import UserApi from '../../api/user'
  import SubTitle from './SubTitle'
  import PostsApi from '../../api/posts'
  import {mapGetters, mapMutations} from 'vuex';

  export default {
    components: {
      XTextarea, CellFormPreview, Group, Cell, SubTitle, XButton
    },
    data() {
      return {
        to_post: false,
        disabled: true,
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
          gender: '',
          p_height: '',
          birthDate: '',
          marriage: '',
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
          about_you: '',
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
      this.form.index = id;
    },
    mounted() {
      this.form.index = this.getUserID();
      UserApi.getUserInfo(this.form.index , this.success, this.fail);
    },
    methods: {
      ...mapMutations(['setToken', 'setUserID']),
      ...mapGetters(['getToken', 'getUserID']),
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
      recruit() {
        PostsApi.recruit_someone(3, this.success, this.fail)
      }
    }
  }
</script>

<style scoped>
  .sub {
    background-color: #6732af;
    color: white;
    padding: 4px;
    height: 30px;
    margin-left: 5px;
    margin-right: 5px;
    margin-top: 5px;
  }

  .cell-font {
    font-size: 14px;
    padding-bottom: 2px;
    padding-top: 2px;
    border-style: hidden;
  }

  .form-text {
    font-size: 14px;
    color: #292929;
    font-color: #292929;
  }

</style>
