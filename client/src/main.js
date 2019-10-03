import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import GlobalEvents from 'vue-global-events';
import VModal from 'vue-js-modal';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.use(VModal);
Vue.component('GlobalEvents', GlobalEvents);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
