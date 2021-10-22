// Style
import 'sanitize.css'
import '@fortawesome/fontawesome-free/css/all.css'
// Custom Style
import './style/default.styl'
// Import
import { createApp } from 'vue'
import { createStore } from 'vuex'
import { createI18n } from 'vue-i18n'
import { createRouter, createWebHistory } from 'vue-router'
// I18n
import en_US from './locales/en-US.yml'
import zh_CN from './locales/zh-CN.yml'
// Root & Routes
import App from './App.vue'
import Idle from './routes/Idle.vue'
import Login from './routes/Login.vue'
// Stores
import StoreUser from './stores/user'
// Script
const app = createApp(App)
// Store
const store = createStore({
  modules: {
    user: StoreUser
  }
})
app.use(store)
// Router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/idle', component: Idle },
    { path: '/login', component: Login },
  ]
})
app.use(router)
// I18n
const i18n = createI18n({
  locale: 'zh-CN',
  fallbackLocale: 'en-US',
  messages: {
    'en-US': en_US,
    'zh-CN': zh_CN
  }
})
app.use(i18n)
// Mount
app.mount('body')
