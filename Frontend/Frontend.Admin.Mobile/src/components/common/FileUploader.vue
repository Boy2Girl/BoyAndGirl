<template>
  <div>
    <Upload
      ref="upload"
      :show-upload-list="false"
      :before-upload="handleBeforeUpload"
      :on-success="handleSuccess"
      multiple
      :action="url"
      style="display: inline-block;width:58px; padding-left: 10px; margin-bottom: 10px;">
      <div>
        <Button>上传图片</Button>
      </div>
    </Upload>
  </div>
</template>
<script>
  import {Upload,Button} from 'iview';
  import baseUrl from '../../api/basequery';
  export default {
    components: {Upload,Button},
    props: {
      url: String
    },
    data() {
      return {}
    },
    methods: {
      handleBeforeUpload(file) {
        console.log(file)
        this.$emit('child-say', file.name);
        return true;
      },
      handleSuccess(res) {
        console.log(res)
        this.$emit('child-say', baseUrl.split('api')[0] + '/static/' + res);
      }
    }

  }
</script>
<style>

</style>
