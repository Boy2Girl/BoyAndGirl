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
        <cell class="cell-font" title="昵称:" :value="birthDate"/>
        <cell class="cell-font" title="编号:" :value="index"/>
        <cell class="cell-font" title="性别:" :value="gender"/>
        <cell class="cell-font" title="身高:" :value="p_height"/>
        <cell class="cell-font" title="出生日期:" :value="birthDate"/>
        <cell class="cell-font" title="婚姻状况:" :value="state"/>
        <cell class="cell-font" title="交友类型:" :value="type"/>
      </group>

      <div class="sub-title">
        坐标
      </div>
      <group>
        <cell class="cell-font" title="家乡:" :value="hometown"/>
        <cell class="cell-font" title="所在城市:" :value="city"/>
        <cell class="cell-font" title="居住地点：" :value="live"/>
      </group>

      <div class="sub-title">
        学校
      </div>
      <group>
        <cell class="cell-font" title="目前状态:" :value="studyState"/>
        <cell class="cell-font" title="本科学校:" :value="collageSchool"/>
        <cell class="cell-font" title="硕士学校:" :value="masterSchool"/>
        <cell class="cell-font" title="博士学校:" :value="doctorSchool"/>
        <cell class="cell-font" title="学历:" :value="education"/>
        <cell class="cell-font" title="专业:" :value="major"/>
      </group>

      <div class="sub-title">
        工作
      </div>
      <group>
        <cell class="cell-font" title="工作单位:" :value="corporation"/>
        <cell class="cell-font" title="工作状况:" :value="work_state"/>
        <cell class="cell-font" title="职业：" :value="career"/>
        <cell class="cell-font" title="单位类型:" :value="corporation_type"/>
        <cell class="cell-font" title="年收入（实际/预期）:" :value="income"/>
      </group>

      <div class="sub-title">
        住房/家庭情况
      </div>
      <group>
        <cell class="cell-font" title="住房情况:" :value="house_state"/>
        <cell class="cell-font" title="家庭情况:" :value="family_state"/>
      </group>

      <div class="sub-title">
        想说的话
      </div>
      <group>
        <cell class="cell-font" title="关于我:" :value="about_me"/>
        <cell class="cell-font" title="关于你:" :value="about_you"/>
      </group>
    </div>
</template>

<script>
    import { CellFormPreview, Group, Cell } from 'vux'
    export default {
      components:{
        CellFormPreview, Group, Cell
      },
      data() {
        return {
          source: require('../../assets/background.jpg'),
          nickname: ' ',
          index: '',
          gender: '',
          p_height: '',
          birthDate: '2828',
          state: '',
          type: '',
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
