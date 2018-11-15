import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import TempSensor from './components/TempSensor.vue'
import Camera from './components/Camera.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/camera',
      name: 'camera',
      component: Camera
    },
    {
      path: '/temp',
      name: 'temp',
      component: TempSensor
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
