import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/index',
      name: 'index',
      component: require('@/components/index').default
    },
    {
      path: '/page1',
      component: require('@/components/demo/page1').default
    },
    {
      path: '/page2',
      component: require('@/components/demo/page2').default
    },
    {
      path: '/test',
      name: 'test',
      component: require('@/components/test').default
    },
    {
      path: '*',
      redirect: '/index'
    }
  ]
})

// 渲染进程接收主进程的传参
const { ipcRenderer } = require('electron');

ipcRenderer.on('href', (event, arg) => {
  if (arg) {
    router.push({ path: arg });
  }
});

export default router