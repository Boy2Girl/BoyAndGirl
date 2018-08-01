<template>
    <div>
      <div class="sub-title">
        个人相册
      </div>
      <group>
        <img :src="source" class="photo"/>
      </group>

      <div class="sub-title">
        基本信息
      </div>
      <group>
        <cell class="cell-font" title="昵称:" :value="form.nickname"/>
        <cell class="cell-font" title="编号:" :value="form.index"/>
        <cell class="cell-font" title="性别:" :value="form.gender"/>
        <cell class="cell-font" title="身高:" :value="form.p_height"/>
        <cell class="cell-font" title="出生日期:" :value="form.birthDate"/>
        <cell class="cell-font" title="婚姻状况:" :value="form.marriage"/>
        <cell class="cell-font" title="交友类型:" :value="form.friend"/>
      </group>

      <div class="sub-title">
        坐标
      </div>
      <group>
        <cell class="cell-font" title="家乡:" :value="form.hometown"/>
        <cell class="cell-font" title="所在城市:" :value="form.city"/>
        <cell class="cell-font" title="居住地点：" :value="form.live"/>
      </group>

      <div class="sub-title">
        学校
      </div>
      <group>
        <cell class="cell-font" title="目前状态:" :value="form.studyState"/>
        <cell class="cell-font" title="本科学校:" :value="form.collageSchool"/>
        <cell class="cell-font" title="硕士学校:" :value="form.masterSchool"/>
        <cell class="cell-font" title="博士学校:" :value="form.doctorSchool"/>
        <cell class="cell-font" title="学历:" :value="form.education"/>
        <cell class="cell-font" title="专业:" :value="form.major"/>
      </group>

      <div class="sub-title">
        工作
      </div>
      <group>
        <cell class="cell-font" title="工作单位:" :value="form.corporation"/>
        <cell class="cell-font" title="工作状况:" :value="form.work_state"/>
        <cell class="cell-font" title="职业：" :value="form.career"/>
        <cell class="cell-font" title="单位类型:" :value="form.corporation_type"/>
        <cell class="cell-font" title="年收入（实际/预期）:" :value="form.income"/>
      </group>

      <div class="sub-title">
        住房/家庭情况
      </div>
      <group>
        <cell class="cell-font" title="住房情况:" :value="form.house_state"/>
        <cell class="cell-font" title="家庭情况:" :value="form.family_state"/>
      </group>

      <div class="sub-title">
        想说的话
      </div>
      <group>
        <cell class="cell-font" title="关于我:" :value="form.about_me"/>
        <cell class="cell-font" title="关于你:" :value="form.about_you"/>
      </group>
    </div>
</template>

<script>
    import { CellFormPreview, Group, Cell } from 'vux'
    import UserApi from '../../api/user' 
    export default {
      components:{
        CellFormPreview, Group, Cell
      },
      data() {
        return {
          source: require('../../assets/background.jpg'),
          form:{
            id: 1,
            avatarUrl:'',
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
            gender: [],
            p_height: '',
            birthDate: '2828',
            marriage: [],
            friend: [],
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
        },
        }
      },
      mounted(){
        UserApi.getUserInfo(1, this.success, this.fail)
      },
      methods:{
        success: function(status, text){
          if(status == 200){
            console.log("成功插入")
          }else if(status == 500){
            console.log("上传用户信息失败")
          }
        },
        fail: function(err){
          console.log("错误发生了！！！")
          console.log(err)
        }
      }
    }
</script>

<style scoped>
  .sub-title{
    background-color: #875927;
    color: white;
    padding: 4px;
    width: 110%;
    height: 110%;
    margin-left: 1%;
    margin-right: 1%;
    margin-top: 20px;
  }

  .cell-font{
    font-size: smaller;
    padding-bottom: 2px;
    padding-top: 2px;
  }

  .photo{
    width: 30%;
    height: 30%;
    margin: 5%;
  }
</style>
