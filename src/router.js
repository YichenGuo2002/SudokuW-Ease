import Vue from 'vue'
import { createRouter,createWebHistory} from 'vue-router'

export default createRouter({
  history: createWebHistory(process.env.BASE_URL),
  /*base: process.env.BASE_URL,*/
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/find',
      name: 'Find',
      component: () => import('./views/Find.vue')
    },
    {
      path: '/upload',
      name: 'Upload',
      component: () => import('./views/Upload.vue')
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('./views/About.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('./views/Register.vue')
    },
    {
      path: '/user',
      name: 'User',
      component: () => import('./views/User.vue')
    },
  ]
})