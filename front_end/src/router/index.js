import Vue from 'vue';
import Router from 'vue-router';
// import { BootstrapVue } from 'bootstrap-vue';
import homepage from '../components/homepage.vue';
// import voices from '../components/voices.vue';
import whole_page from "@/components/whole_page";

// Vue.use(BootstrapVue);
Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: homepage,
      meta: {
        title: 'Asoul数据监测',
        // icon: '/clip_fire_dragon_sq.png',
      },
    },
    {
      path: '/:live_info',
      name: 'live',
      component: whole_page,
      meta: {
        title: 'Asoul数据监测',
        // icon: '/clip_fire_dragon_sq.png',
      },
    },
  ],
});
