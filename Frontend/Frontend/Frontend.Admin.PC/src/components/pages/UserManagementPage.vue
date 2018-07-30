<template>
    <layout>
        <user-list></user-list>
    </layout>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator';
    import UserList from '../common/UserList.vue';

    @Component({
        components: {UserList}
    })

    export default class ActivityPage extends Vue {
    }
</script>

<style scoped>
</style>