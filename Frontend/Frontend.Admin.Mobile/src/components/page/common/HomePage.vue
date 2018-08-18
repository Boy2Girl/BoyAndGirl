<template>
  <div>
    <div class="bg bg-blur"></div>
    <Login/>
  </div>
</template>

<script>
  // import Login from '../../common/Login.vue'
  const Login = () => import('../../common/Login.vue')
  
  export default {
    components: {
      Login
    },
    mounted(){

    },

  }
</script>

<style scoped>
  .bg {
    background: url('../../../assets/background.jpg');
    height: 1000px;
    text-align: center;
    line-height: 600px;
  }

  .bg-blur {
    float: left;
    width: 100%;
    background: no-repeat center;
    background-size: cover;
    -webkit-filter: blur(35px);
    -moz-filter: blur(35px);
    -o-filter: blur(35px);
    -ms-filter: blur(35px);
    filter: blur(35px);
  }
</style>
