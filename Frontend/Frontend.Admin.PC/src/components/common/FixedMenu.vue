<template>
    <Menu mode="horizontal" theme="light" active-name="1">
        <div class="layout-logo-text">
            <MenuItem name="0">
                <img class="layout-logo" src="../../assets/logo.jpg"/>
                <h3 class="layout-text">{{logoName}}</h3>
            </MenuItem>
        </div>
        <div class="layout-nav">
            <router-link :to="{path: '/'}">
                <MenuItem name="1">
                    <Icon type="map"></Icon>
                    {{menuBar1}}
                </MenuItem>
            </router-link>
            <router-link :to="{path: '/pool'}">
                <MenuItem name="2">
                    <Icon type="stats-bars"></Icon>
                    {{menuBar2}}
                </MenuItem>
            </router-link>
            <router-link :to="{path: '/user'}">
                <MenuItem name="3">
                    <Icon type="ios-people"></Icon>
                    {{menuBar3}}
                </MenuItem>
            </router-link>
        </div>
        <div class="layout-user">
            <Button type="ghost" icon="person" size="large" shape="circle" @click="isShow = true"></Button>
        </div>
        <Modal
                v-model="isShow"
                :title="accountLogin"
                @on-ok="ok"
                @on-cancel="cancel">
            <Input v-model="username" size="large" :placeholder="accountLoginUsername" style="padding:20px"/>
            <Input v-model="password" size="large" type="password" :placeholder="accountLoginPassword"
                   style="padding:20px"/>
        </Modal>
    </Menu>
</template>
<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";
    import SENTENCES from "../../assets/sentences/index";

    @Component
    export default class FixedMenu extends Vue {
        menuBar1: string = SENTENCES.MENU.ACTIVITY;
        menuBar2: string = SENTENCES.MENU.POOL;
        menuBar3: string = SENTENCES.MENU.USER_MANAGEMENT;
        logoName: string = SENTENCES.MENU.LOGO_NAME;
        accountLogin: string = SENTENCES.ACCOUNT.LOGIN.TITLE;
        accountLoginUsername: string = SENTENCES.ACCOUNT.LOGIN.USERNAME;
        accountLoginPassword: string = SENTENCES.ACCOUNT.LOGIN.PASSWORD;

        isShow: boolean = false;
        username: string = "";
        password: string = "";

    }
</script>

<style scoped>
    .layout-logo-text {
        margin-left: 15px;
        margin-right: 15px;
    }

    .layout-logo {
        width: auto;
        height: 30px;
        background: #6d3770;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 13px;
        left: 20px;
        margin-right: 25px;
    }

    .layout-text {
        display: table;
        color: #6d3770;
    }

    .layout-nav {
        width: auto;
        margin: 0 0 0 auto;
    }

    .layout-user {
        text-align: right;
        margin-right: 15px;
    }
</style>