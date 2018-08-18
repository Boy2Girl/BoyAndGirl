<template>
<div>
  <pool-people-tab/>
  <pool-people-list/>
</div>
</template>

<script>
// import PoolPeopleTab from '../../common/PoolPeopleTab';
  // import PoolPeopleList from '../../common/PoolPeopleList';

  const PoolPeopleTab = () => import('../../common/PoolPeopleTab')
  const PoolPeopleList = () => import('../../common/PoolPeopleList')
  export default {
    components: {
      PoolPeopleList,PoolPeopleTab
    }
  }
</script>

<style scoped>

</style>
