<template>
  <div>
    <div class="demo-upload-list" v-for="item in uploadList">
      <img :src="item">
      <div class="demo-upload-list-cover">
        <img src="../../assets/eye.png" @click="handleView(item)"/>
        <img src="../../assets/trash.png" @click="handleRemove(item)"/>
      </div>
    </div>
    <div>
      <Upload
        ref="upload"
        :show-upload-list="false"
        :before-upload="handleBeforeUpload"
        :on-success="handleSuccess"
        multiple
        :action="url"
        style="display: inline-block; width:58px; padding-left: 10px; margin-bottom: 10px;">
        <div>
          <Button>上传图片</Button>
        </div>
      </Upload>
    </div>
    <Modal title="查看详情" v-model="visible">
      <img :src="imgUrl" v-if="visible" style="width: 100%">
    </Modal>
  </div>
</template>
<script>
  import {Upload, Button, Modal} from 'iview';
  import baseUrl from '../../api/basequery';

  export default {

    components: {
      Modal,
      Upload, Button},
    props: {
      url: String
    },
    data() {
      return {
        uploadList: [],
        visible: false
      }
    },
    methods: {
      handleView (url) {
        this.imgUrl = url;
        this.visible = true;
      },
      handleRemove(url) {
        this.uploadList.splice(this.uploadList.indexOf(url), 1);
      },
      handleBeforeUpload(file) {
        console.log(file);
        this.$emit('child-say', file.name);
        return true;
      },
      handleSuccess(res) {
        console.log(res);
        let pictureurl = baseUrl.baseUrl.split('api')[0] + 'static/' + res;
        console.log(pictureurl);
        //this.uploadList = [];
        this.uploadList.push(pictureurl);

        this.$emit('child-say', pictureurl);
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
    margin: 2px 10px;
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

  .demo-upload-list-cover img {
    width: 30%;
    height: 30%;
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
