import Vue from 'vue';
import Router from 'vue-router';
import TempSensor from '@/components/TempSensor';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/temp/all',
      name: 'TempAll',
      component: TempSensor,
    },
  ],
});
