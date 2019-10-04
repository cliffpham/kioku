import Vue from 'vue';
import Router from 'vue-router';
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
  ],
});
