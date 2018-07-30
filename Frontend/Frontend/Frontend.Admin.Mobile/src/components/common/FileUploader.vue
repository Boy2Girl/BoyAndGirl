<template>
  <div>
    <Upload
      ref="upload"
      :show-upload-list="false"
      :before-upload="handleBeforeUpload"
      multiple
      :data="data"
      action="http://www.injusalon.com/count/file/upload"
      style="display: inline-block;width:58px;">
      <div style="width: 58px;height:58px;line-height: 58px;">
        <icon type="camera" size="20"/>
      </div>
    </Upload>
  </div>
</template>
<script>
  import {Icon} from "vux";
  import {Upload} from 'iview';

  export default {
    components: {
      Upload, Icon
    },
    data() {
      return {
        data: {
          fileName: '11',
          rID: '2'
        },
      }
    },
    methods: {
      handleBeforeUpload(file) {
        console.log(file)
        this.data.fileName = file.name;
        this.data.rID = "2";
        return true;
      }
    },
    mounted() {
      this.uploadList = this.$refs.upload.fileList;
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
