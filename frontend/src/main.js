import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from "@/views/Dashboard.vue";
import ResumeTemplate from "@/views/ResumeTemplate.vue";
import FillResume from "@/views/FillResume.vue";

import Features from "@/views/Features.vue";
import About from "@/views/About.vue";
import Pricing from "@/views/Pricing.vue";
import Blog from "@/views/Blog.vue";
import Contact from "@/views/Contact.vue";

import { store } from './store.js';
import axios from 'axios';

// Configure Axios globally to send cookies
axios.defaults.withCredentials = true;

// Initialize global user state
store.init();

import ATSScanner from "@/views/ATSScanner.vue";

const routes = [
  { name: 'Home', path: '/', component: Home },
  { name: 'Features', path: '/features', component: Features },
  { name: 'Pricing', path: '/pricing', component: Pricing },
  { name: 'About', path: '/about', component: About },
  { name: 'Blog', path: '/blog', component: Blog },
  { name: 'Contact', path: '/contact', component: Contact },
  { name: 'Login', path: '/login', component: Login, meta: { hideNav: true } },
  { name: 'Register', path: '/register', component: Register, meta: { hideNav: true } },
  { name: 'Dashboard', path: '/Dashboard', component: Dashboard, meta: { requiresAuth: true, hideNav: true, isDashboard: true } },
  { name: 'ResumeTemplate', path: '/resume-template', component: ResumeTemplate },
  { name: 'FillResume', path: '/resume-template/fill-resume', component: FillResume, meta: { hideNav: true } },
  { name: 'ATSScanner', path: '/ats-scanner', component: ATSScanner, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Basic Navigation Guard to prevent non-logged-in users from seeing dashboard
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !store.isLoggedIn) {
    next('/login');
  } else {
    next();
  }
});

createApp(App).use(router).mount('#app');
