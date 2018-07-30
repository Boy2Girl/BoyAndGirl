<template>
    <div style="margin: 5%;">
        <file-uploader route="profile" :params=params v-on:getFileName="getFileName"></file-uploader>
    </div>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator';
    import FileUploader from 'FileUploader.vue';

    @Component({
        components: {FileUploader}
    })

    export default class Activity extends Vue {
        params = {
            fileName: "jjj"
        };

        mounted() {
            console.log("hello");
        }

        getFileName(fileName) {

        }

    }
</script>

<style scoped>

</style>