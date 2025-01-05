import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from "@/views/Dashboard.vue";
import Glide from '@glidejs/glide';
import '@glidejs/glide/dist/css/glide.core.min.css';
import ResumeTemplate from "@/views/ResumeTemplate.vue";
import FillResume from "@/views/FillResume.vue"; // Ensure Glide CSS is imported

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/Dashboard', component: Dashboard },
  { path: '/resume-template', component: ResumeTemplate},
  { path: '/resume-template/fill-resume', component: FillResume},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app');
