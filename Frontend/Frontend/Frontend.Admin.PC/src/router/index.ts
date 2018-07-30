import Vue from 'vue';
import Router from 'vue-router';
import ActivityPage from '@/components/pages/ActivityPage.vue';
import PoolPage from '@/components/pages/PoolPage.vue';
import UserManagementPage from '@/components/pages/UserManagementPage.vue';
import BaseLayout from '../components/pages/BaseLayout.vue';

Vue.use(Router);

const routes = [
    {
        path: '/',
        component: BaseLayout,
        children: [
            {
                path: '',
                component: ActivityPage
            },
            {
                path: 'pool',
                component: PoolPage
            },
            {
                path: 'user',
                component: UserManagementPage
            }
        ]
    }
];

Vue.component('base-layout', BaseLayout);

export default new Router({
    routes
});
