<template>
  <div>
    <!-- <h1>111</h1> -->
    <user-list/>
  </div>
</template>

<script>
  // import UserList from '../../common/UserList';
  const UserList = () => import('../../common/UserList')
  export default {
    components: {
      UserList
    },
  }
</script>

<style scoped>

</style>
