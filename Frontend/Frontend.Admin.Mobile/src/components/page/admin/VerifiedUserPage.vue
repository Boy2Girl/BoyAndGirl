<template>
  <div>
    <personal-info/>
  </div>
</template>

<script>
  // import PersonalInfo from '../../common/PersonalInfo.vue';
  const PersonalInfo = () => import('../../common/PersonalInfo.vue')
  import {XButton} from 'vux';
  import UserApi from '../../../api/user';
  import router from "../../../router";

  export default {
    components: {
      PersonalInfo, XButton
    },
    methods: {
    }
  }
</script>

<style scoped>

</style>
