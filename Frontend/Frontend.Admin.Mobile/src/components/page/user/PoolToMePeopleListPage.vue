<template>
  <pool-people-tab/>
  <pool-people-list/>
</template>

<script>
  const PoolPeopleTab = () => import('../../common/PoolPeopleTab')
  const PoolPeopleList = () => import('../../common/PoolPeopleList')
  export default {
    components: {
      PoolPeopleList,PoolPeopleTab
    },
    name: "pool-to-me-people-list-page"

  }
</script>

<style scoped>

</style>
