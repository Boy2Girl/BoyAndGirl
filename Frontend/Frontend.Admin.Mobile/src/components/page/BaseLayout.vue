<template>
  <div>
    <router-view/>
    <Bar/>
  </div>
</template>

<script>
  import Bar from '../common/Bar.vue'

  export default {
    components: {
      Bar
    },
    data() {
      return {
        data: {},
      }
    },
    mounted(){
      console.log('init')
    }
  }
</script>

<style lang="less" type="text/less">
</style>




