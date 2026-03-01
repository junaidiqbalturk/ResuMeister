<template>
  <div id="app">
    <SiteNavbar v-if="!$route.meta.hideNav" />
    <main class="page-content" :class="{ 'auth-page': $route.meta.hideNav && !$route.meta.isDashboard, 'dashboard-page': $route.meta.isDashboard }">
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <SiteFooter v-if="!$route.meta.hideNav" />
  </div>
</template>

<script>
import SiteNavbar from '@/components/SiteNavbar.vue';
import SiteFooter from '@/components/SiteFooter.vue';

export default {
  name: 'App',
  components: {
    SiteNavbar,
    SiteFooter
  }
};
</script>

<style>
/* Global SaaS Startup Design System */
.page-content {
  min-height: calc(100vh - 400px);
  padding-top: 80px; /* Account for fixed navbar */
}
.page-content.auth-page {
  padding-top: 0;
  min-height: 100vh;
}
.page-content.dashboard-page {
  padding-top: 0;
  min-height: 100vh;
}
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Plus Jakarta Sans', sans-serif;
  --font-secondary: 'Outfit', sans-serif;
  --font-heading: 'Space Grotesk', sans-serif;
  
  /* Modern SaaS Dark Palette */
  --bg-deep: #020617;
  --bg-card: rgba(30, 41, 59, 0.4);
  --border-subtle: rgba(255, 255, 255, 0.08);
  
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  
  /* Brand Colors */
  --accent: #6366F1;
  --accent-glow: rgba(99, 102, 241, 0.15);
  --secondary: #FDBA74;
  --tertiary: #EC4899;
  
  /* Effects */
  --glass-bg: rgba(15, 23, 42, 0.7);
  --glass-blur: blur(12px);
  --glass-border: 1px solid rgba(255, 255, 255, 0.1);
  --shadow-premium: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.1) transparent;
  overflow-x: hidden;
}

/* Custom Scrollbar for Premium Feel */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 99px; border: 2px solid var(--bg-deep); }
::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.2); }

h1, h2, h3, h4, h5 {
  font-family: var(--font-heading);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

/* Global Transition Utility */
.page-enter-active, .page-leave-active {
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.page-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.page-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Global Button & UI Elements */
button, .btn {
  font-family: var(--font-primary);
  cursor: pointer;
  border: none;
  outline: none;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

a {
  color: inherit;
  text-decoration: none;
  transition: 0.3s;
}

img { max-width: 100%; display: block; }

/* Utility Classes */
.text-gradient {
  background: linear-gradient(to right, var(--accent), var(--tertiary), var(--secondary));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.glass-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: var(--glass-border);
  box-shadow: var(--shadow-premium);
}
</style>
