<template>
  <personal-info/>
</template>

<script>
  const PersonalInfo = () => import('../../common/PersonalInfo.vue')

  export default {
    components: {
      PersonalInfo
    },
    name: "admin-user-info-page"
  }
</script>

<style scoped>

</style>
