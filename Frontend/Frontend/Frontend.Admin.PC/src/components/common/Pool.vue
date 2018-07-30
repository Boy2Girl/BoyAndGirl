<template>
    <div style="margin: 5%;">
        <Collapse v-model="district">
            <Panel v-for="item in pools">
                {{item.name}}
                <div slot="content">
                    <ul>
                        <li style="list-style-type: none" v-for="subItem in item.content">
                            <Card>
                                <h3 style="display: inline">{{ subItem.value }}</h3>
                                <div style="float: right">
                                    <div style="display:inline">
                                        <h5 style="display:inline;color:#3f6dff">{{subItem.numOfMan}}</h5>
                                    </div>
                                    /
                                    <div style="display:inline">
                                        <h5 style="display:inline;color:pink;">{{subItem.numOfWoman}}</h5>
                                    </div>
                                </div>
                            </Card>
                        </li>
                    </ul>
                    <div @click="isShow=true">
                        <Card>
                            <h3 style="text-align: center">新增交友池</h3>
                        </Card>
                    </div>
                </div>
            </Panel>
        </Collapse>
        <Modal
                v-model="isShow"
                title="新增交友池"
                @on-ok="ok"
                @on-cancel="cancel">
            <!--<Input v-model="username" size="large" :placeholder="accountLoginUsername" style="padding:20px"/>-->
            <!--<Input v-model="password" size="large" type="password" :placeholder="accountLoginPassword"-->
            <!--style="padding:20px"/>-->
        </Modal>
    </div>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator';

    interface PoolInfo {
        value: string,
        numOfMan: number,
        numOfWoman: number
    }

    interface Item {
        name: string,
        content: PoolInfo[]
    }

    @Component
    export default class Pool extends Vue {
        district: string;
        isShow: boolean;
        pools: Item[] = [
            {
                name: "南京",
                content: [
                    {
                        value: "仙林地区",
                        numOfMan: 20,
                        numOfWoman: 30
                    },
                    {
                        value: "鼓楼地区",
                        numOfMan: 10,
                        numOfWoman: 20
                    }
                ],
            },
            {
                name: "北京",
                content: [
                    {
                        value: "朝阳区",
                        numOfMan: 5,
                        numOfWoman: 20
                    },
                    {
                        value: "修士",
                        numOfMan: 7,
                        numOfWoman: 28
                    }
                ]
            }
        ];
    }
</script>

<style scoped>

</style>