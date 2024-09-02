import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from "@/views/Dashboard.vue";
import Glide from '@glidejs/glide';
import '@glidejs/glide/dist/css/glide.core.min.css'; // Ensure Glide CSS is imported

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/Dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app');
