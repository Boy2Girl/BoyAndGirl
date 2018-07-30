<template>
    <div style="margin:5%">
        <Input style="margin-bottom:5%" size="large" search enter-button placeholder="输入用户名以搜索用户"/>
        <Table border stripe :columns="userList" :data="userData"></Table>
    </div>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator';
    import {Role} from "../../models/User";

    interface Column {
        title: string;
        key: string;
        render?: any;
        align?: string,
    }

    interface Item {
        uID: string;
        username: string;
        password: string;
        sex: string;
        role: Role
    }

    @Component
    export default class UserList extends Vue {
        userList: Column[] = [
            {
                title: 'ID',
                key: 'uID',
            },
            {
                title: '用户名',
                key: 'username'
            },
            {
                title: '密码',
                key: 'password'
            },
            {
                title: '性别',
                key: 'sex'
            },
            {
                title: '操作',
                key: 'action',
                align: 'center',
                render: (h, params) => {
                    console.log(params.index);
                    if (this.userData[params.index].role == Role.USER) {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'large'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {

                                    }
                                }
                            }, '给予权限')
                        ]);
                    }
                    else {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'large'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {

                                    }
                                }
                            }, '剥夺权限')
                        ]);
                    }
                }
            }
        ];
        userData: Item[] = [
            {
                uID: '1312312312',
                username: '123',
                password: '123',
                sex: '男',
                role: Role.USER
            },
            {
                uID: '2',
                username: '1234',
                password: '1235',
                sex: '男',
                role: Role.PUBLISHER
            },
            {
                uID: '3',
                username: '1238',
                password: '1239',
                sex: '男',
                role: Role.ADMIN
            },
            {
                uID: '4',
                username: '54',
                password: '46',
                sex: '男',
                role: Role.USER
            }];
    }
</script>

<style scoped>
</style>