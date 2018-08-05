<template>
  <div>
    <personal-info/>
    <br>
    <br>
    <br>
    <x-button type="primary" style="position: fixed; bottom: 47px; width: 50%; margin-left: 50%">审核通过</x-button>
    <x-button type="warn" style="position: fixed; bottom: 47px; width: 50%">审核不通过</x-button>
  </div>
</template>

<script>
  import PersonalInfo from '../../common/PersonalInfo.vue';
  import {XButton} from 'vux';

  export default {
    components: {
      PersonalInfo, XButton
    }
  }
</script>

<style scoped>

</style>
