<template>
<div>
    <file-uploader :url="url" :params = "params">

    </file-uploader>
</div>
</template>

<script>
    import FileUploader from '../../common/FileUploader'
    import {mapGetters, mapMutations} from 'vuex'
    import UserApi from '../../../api/user' 
    export default {
        components: {
            FileUploader
        },
        data(){
            return{
                url: "http://127.0.0.1:5000/api/test",
                params: {"aaa":"aaa"}
            }
        },
        mounted(){
            UserApi.signIn("123", "12345634", UserApi.ROLE.USER, this.success, this.fail)
            this.setToken("2222")
            console.log(this.getToken())
        },
        methods: {
            ...mapMutations(['setToken']),
            ...mapGetters(['getToken']),
            success: function (status, text) {
                console.log('请求结果')
                console.log(text+" "+ status)
            },
            fail: function (e) {
                console.log("发现错误！！！！")
                console.log(e)
            }
        }
        
    }
</script>

<style scoped>

</style>
