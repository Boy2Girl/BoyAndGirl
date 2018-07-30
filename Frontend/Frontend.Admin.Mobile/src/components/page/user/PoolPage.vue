<template>
<div>
    <file-uploader :url="url" :params = "params">

    </file-uploader>
</div>
</template>

<script>
    import FileUploader from '../../common/FileUploader'
    export default {
        components: {
            FileUploader
        },
        data(){
            return{
                url: "http://127.0.0.1:5000/api/test",
                params: {"aaa":"aaa"}
            }
        }
    }
</script>

<style scoped>

</style>
