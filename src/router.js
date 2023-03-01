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
      path: '/about',
      name: 'about',
      component: () => import('./views/About.vue')
    },
    // route level code-splitting
      // this generates a separate chunk (create.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
    /*
    {
      path: '/product',
      name: 'product',
      props: true,
      component: () => import( './views/Product.vue')
    },
    */
  ]
})