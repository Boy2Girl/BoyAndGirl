<template>
  <div>
    <div>
      <alert v-model="show" :title="title" :content="content" @on-hide="onHide"/>
    </div>
    <div class="sub">个人相册</div>
    <img :src="form.avatar"
         style="width:100px; height:100px; display:inline; padding: 2%"/>
    <!--<img v-for="item in form.photoList" :src="item.source"-->
    <!--style="width:100px; height:100px; display:inline; padding: 2%"/>-->

    <div class="sub">基本信息</div>
    <cell-form-preview class="form-text" :list="[
    {label: '昵称', value: form.name},
    {label: '真实姓名', value: form.realName},
    {label: '编号', value: form.id},
    {label: '性别', value: form.gender},
    {label: '身高（cm）', value: form.p_height},
    {label: '出生日期', value: form.bornDate},
    {label: '婚姻状况', value: form.marriage},
    {label: '交友类型', value: form.friend}]"/>

    <div class="sub">联系方式</div>
    <cell-form-preview class="form-text" v-if="!to_post" :list="[
    {label: '电话', value: form.phone},
    {label: '微信', value: form.wechat}]"/>

    <div class="sub">坐标</div>
    <cell-form-preview class="form-text" :list="[
    {label: '家乡', value: form.hometown},
    {label: '所在城市', value: form.city},
    {label: '工作单位', value: form.company},
    {label: '年收入（实际/预期）', value: form.income}]"/>

    <div class="sub">学历</div>
    <cell-form-preview class="form-text" :list="[
    {label: '本科学校', value: form.collageSchool},
    {label: '硕士学校', value: form.masterSchool},
    {label: '博士学校', value: form.doctorSchool}]"/>

    <div class="sub">住房/家庭情况
    </div>
    <cell-form-preview class="form-text" :list="[
    {label: '住房情况', value: form.housingCondition},
    {label: '家庭情况', value: form.economyCondition}]"/>

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
  import {XTextarea, CellFormPreview, Group, Cell, XButton, Alert} from 'vux'
  import UserApi from '../../api/user'
  import SubTitle from './SubTitle'
  import PostsApi from '../../api/posts'
  import {mapGetters, mapMutations} from 'vuex';
  import check from '../../api/check';
  import router from '../../router/index.js'

  export default {
    components: {
      XTextarea, CellFormPreview, Group, Cell, SubTitle, XButton, Alert
    },
    data() {
      return {
        isChecked: 'False',
        to_post: false,
        disabled: true,
        title: '',
        content: '',
        show: false,
        form: {
          avatar: '',
          personUrl: '',
          studentUrl: '',
          graduateUrl: '',
          otherUrl: '',
          phone: ' ',
          email: ' ',
          qq: '',
          wechat: '',
          name: '',
          realName: '',
          id: '',
          gender: '',
          p_height: '',
          bornDate: '2019-01-01',
          marriage: '',
          friend: '',
          hometown: '',
          city: '',
          livingPlace: '',
          studyState: '',
          collageSchool: '',
          masterSchool: '',
          doctorSchool: '',
          education: '',
          major: '',
          company: '',
          work_state: '',
          job: '',
          corporation_type: '',
          income: '',
          housingCondition: '',
          economyCondition: '',
          about_you: '',
          about_me: '',
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
      // this.form.index = this.getUserID();
      check.check(this.checkSuccess, this.fail);
      // UserApi.getUserInfo(this.form.index, this.isChecked, this.success, this.fail);
    },
    methods: {
      ...mapMutations(['setToken', 'setUserID']),
      ...mapGetters(['getToken', 'getUserID']),
      checkSuccess: function (status, text) {
        console.log(status + text);
        let result = (JSON.parse(text));
        console.log(result['role']);
        if (!result['isReal'] && result['role'] === 'USER') {
          this.setState('失败', '您还没有通过系统审核');
        }

        if (result['isReal'])
          this.isChecked = 'True';
        else
          this.isChecked = 'False';
        UserApi.getUserInfo(this.form.index, this.isChecked, this.success, this.fail);
      },
      success: function (status, text) {
        if (status === 200) {
          console.log("成功插入");
          let result = (JSON.parse(text));
          this.form = result;
          console.log(this.form)
        } else if (status === 500) {
          console.log("上传用户信息失败")
        }
      },
      fail: function (err) {
        console.log("错误发生了！！！")
        console.log(err)
      },
      recruit() {
        console.log("ids:  " + this.form.id)
        PostsApi.recruit_someone(this.form.id, this.success, this.fail)
      },
      setState: function (title, content) {
        this.title = title;
        this.content = content;
        this.show = true;
      },
      onHide: function () {
        this.$router.push('/user/user');
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
