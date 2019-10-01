import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Test from './components/Test.vue';
import Base from './components/Base.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Base',
      component: Base,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ],
});
