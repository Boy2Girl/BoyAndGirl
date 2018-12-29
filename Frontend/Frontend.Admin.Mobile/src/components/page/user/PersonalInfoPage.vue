<template>
  <div>
    <info/>
  </div>
</template>

<script>
  // import Info from '../../common/PersonalInfo.vue';

  const Info = () => import('../../common/PersonalInfo.vue')
  export default {
    components: {
      Info
    }
  }
</script>

<style scoped>

</style>
