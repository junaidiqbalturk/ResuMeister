<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Global SaaS Startup Design System */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

:root {
  --font-primary: 'Outfit', sans-serif;
  --font-heading: 'Space Grotesk', sans-serif;
  --bg-deep: #030712;
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --accent: #6366F1;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-primary);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.1) transparent;
}

/* Custom Scrollbar for Premium Feel */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.05); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.1); }

h1, h2, h3, h4, h5 {
  font-family: var(--font-heading);
  font-weight: 700;
  letter-spacing: -0.02em;
}

/* Global Transition Utility */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* Global Button Fix for SaaS 2.0 */
button, .btn {
  font-family: var(--font-primary);
  cursor: pointer;
  border-radius: 6px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

img { max-width: 100%; display: block; }
</style>
