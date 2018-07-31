<template>
  <div>
    <Upload
      ref="upload"
      :show-upload-list="false"
      :before-upload="handleBeforeUpload"
      multiple
      :data="params"
      :action="url"
      style="display: inline-block;width:58px;">
      <div>
        <Button>上传图片</Button>
      </div>
    </Upload>
  </div>
</template>
<script>

  export default {
    props: {
      url: String,
      params: Object,
    },
    data() {
      return {
        
      }
    },
    methods: {
      handleBeforeUpload(file) {
        return true;
      }
    }

  }
</script>
<style>
  
</style>
