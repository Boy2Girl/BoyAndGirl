<template>
    <Footer class="layout-footer-center">
        <Row>
            <Col span="8">
            <div>
                <h3>{{footer1Title}}</h3>
                <div>
                    <h4 class="footer-line">{{footer1Content1}}</h4>
                    <h4 class="footer-line">{{footer1Content2}}</h4>
                </div>
            </div>
            </Col>
            <Col span="8">
            <div>
                <h3>{{footer2Title}}</h3>
                <div>
                    <h4 class="footer-line">{{footer2Content1}}</h4>
                    <h4 class="footer-line">{{footer2Content2}}</h4>
                </div>
            </div>
            </Col>
            <Col span="8">
            </Col>
        </Row>
    </Footer>
</template>
<script lang="ts">
    import {Component, Emit, Inject, Model, Prop, Provide, Vue, Watch} from 'vue-property-decorator';
    import SENTENCES from "../../assets/sentences/index";

    @Component
    export default class FixedFooter extends Vue {
        footer1Title: string = SENTENCES.FOOTER.TECHNIQUE.TITLE;
        footer1Content1: string = SENTENCES.FOOTER.TECHNIQUE.POWER1;
        footer1Content2: string = SENTENCES.FOOTER.TECHNIQUE.POWER2;
        footer2Title: string = SENTENCES.FOOTER.CONTACT.TITLE;
        footer2Content1: string = SENTENCES.FOOTER.CONTACT.PHONE;
        footer2Content2: string = SENTENCES.FOOTER.CONTACT.NAME;
    }
</script>

<style scoped>
    .layout-footer-center {
        background-color: #6d3770;
        text-align: center;
        color: white;
    }

    .footer-line {
        display: inline;
    }
</style>