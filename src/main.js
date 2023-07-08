import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import store from './store'
import router from './router'
import {useUserStore} from '@/user'

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(router)
app.use(store)
app.mount('#app')
