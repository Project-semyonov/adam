import Vue from 'vue';
import Router from 'vue-router';
import TempSensor from '@/components/TempSensor';
import Home from '@/components/Home';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/temp/all',
      name: 'TempAll',
      component: TempSensor,
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
  ],
});
