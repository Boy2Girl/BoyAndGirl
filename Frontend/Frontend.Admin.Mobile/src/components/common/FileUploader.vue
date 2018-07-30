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
  .demo-upload-list {
    display: inline-block;
    width: 60px;
    height: 60px;
    text-align: center;
    line-height: 60px;
    border: 1px solid transparent;
    border-radius: 4px;
    overflow: hidden;
    background: #fff;
    position: relative;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .2);
    margin-right: 4px;
  }

  .demo-upload-list img {
    width: 100%;
    height: 100%;
  }

  .demo-upload-list-cover {
    display: none;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, .6);
  }

  .demo-upload-list:hover .demo-upload-list-cover {
    display: block;
  }

  .demo-upload-list-cover i {
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    margin: 0 2px;
  }
</style>
