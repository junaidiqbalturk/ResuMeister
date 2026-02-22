import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from "@/views/Dashboard.vue";
import ResumeTemplate from "@/views/ResumeTemplate.vue";
import FillResume from "@/views/FillResume.vue";

const routes = [
  { name: 'Home', path: '/', component: Home },
  { name: 'Login', path: '/login', component: Login },
  { name: 'Register', path: '/register', component: Register },
  { name: 'Dashboard', path: '/Dashboard', component: Dashboard },
  { name: 'ResumeTemplate', path: '/resume-template', component: ResumeTemplate },
  { name: 'FillResume', path: '/resume-template/fill-resume', component: FillResume },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app');
