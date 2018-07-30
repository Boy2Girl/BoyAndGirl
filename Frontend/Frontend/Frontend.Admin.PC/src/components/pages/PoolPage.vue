<template>
    <layout>
        <pool></pool>
    </layout>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator';
    import Pool from '../common/Pool.vue';

    @Component({
        components: {Pool}
    })

    export default class PoolPage extends Vue {
    }
</script>

<style scoped>
</style>