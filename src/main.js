import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import store from './store'

const pinia = createPinia()
const app = createApp(App)
app.use(router);
app.use(store)
app.use(pinia)
app.mount('#app')
