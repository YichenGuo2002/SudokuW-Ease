import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  /*mode: 'history',*/
  /*base: process.env.BASE_URL,*/
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import(/* webpackChunkName: "create" */ './views/Home.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (create.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "create" */ './views/About.vue')
    },
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