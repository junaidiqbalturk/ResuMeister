<template>
  <nav class="navbar" :class="{ 'scrolled': isScrolled }">
    <div class="nav-container">
      <router-link to="/" class="logo">
        <div class="logo-icon">R</div>
        <span>ResuMeister</span>
      </router-link>

      <div class="menu-toggle" @click="toggleMenu" :class="{ 'active': isMenuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div class="nav-links" :class="{ 'open': isMenuOpen }">
        <router-link to="/features" @click="closeMenu">Features</router-link>
        <router-link to="/resume-template" @click="closeMenu">Templates</router-link>
        <router-link to="/pricing" @click="closeMenu">Pricing</router-link>
        <router-link to="/about" @click="closeMenu">About Us</router-link>
        <router-link to="/blog" @click="closeMenu">Blog</router-link>
        <router-link to="/contact" @click="closeMenu">Contact</router-link>
        
        <div class="nav-actions">
          <router-link to="/login" class="nav-link-subtle" @click="closeMenu">Log in</router-link>
          <router-link to="/register" class="btn-primary" @click="closeMenu">Get Started</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'SiteNavbar',
  data() {
    return {
      isScrolled: false,
      isMenuOpen: false
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  unmounted() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 20;
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    }
  }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  transition: all 0.3s ease;
  padding: 1.5rem 0;
  border-bottom: 1px solid transparent;
}

.navbar.scrolled {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(12px);
  padding: 1rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.5rem;
  color: var(--text-main);
}

.logo-icon {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--accent), var(--secondary));
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  color: white;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.nav-links a {
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--text-muted);
  position: relative;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  color: var(--text-main);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-left: 1rem;
}

.nav-link-subtle {
  color: var(--text-main) !important;
  font-weight: 600 !important;
}

.btn-primary {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 0.6rem 1.25rem;
  border-radius: 99px;
  font-weight: 600 !important;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255, 255, 255, 0.1);
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
}

.menu-toggle span {
  width: 28px;
  height: 2px;
  background: var(--text-main);
  transition: 0.3s;
}

@media (max-width: 900px) {
  .menu-toggle {
    display: flex;
  }
  
  .nav-links {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: var(--bg-deep);
    flex-direction: column;
    padding: 2rem;
    gap: 1.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
    transition: clip-path 0.4s ease-in-out;
  }
  
  .nav-links.open {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  }
  
  .nav-actions {
    flex-direction: column;
    width: 100%;
    margin-left: 0;
    margin-top: 1rem;
  }
  
  .btn-primary {
    width: 100%;
    text-align: center;
  }

  .menu-toggle.active span:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
  }
  .menu-toggle.active span:nth-child(2) {
    opacity: 0;
  }
  .menu-toggle.active span:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
  }
}
</style>
