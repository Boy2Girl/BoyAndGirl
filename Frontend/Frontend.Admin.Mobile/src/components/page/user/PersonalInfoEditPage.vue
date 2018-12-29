<template>
  <div>
    <EditPersonalInfo/>
  </div>
</template>

<script>
  // import EditPersonalInfo from '../../common/EditPersonalInfo.vue'

  const EditPersonalInfo = () => import('../../common/EditPersonalInfo.vue')
  export default {
    components: {
      EditPersonalInfo
    },
    name: "personal-info-edit-page"
  }
</script>

<style scoped>

</style>
