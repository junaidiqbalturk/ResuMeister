<template>
  <div class="templates-wrapper">
    <!-- Atmosphere -->
    <div class="atmosphere">
      <div class="aura aura-1"></div>
      <div class="aura aura-2"></div>
    </div>

    <!-- SaaS Navbar -->
    <nav class="navbar-saas">
      <div class="container nav-content">
        <a href="/" class="logo-link">
          <img src="/resumeister.png" alt="ResuMeister" class="logo-img">
          <span class="logo-text">ResuMeister</span>
        </a>
        <div class="nav-links">
           <a href="/" class="nav-link">Home</a>
           <a href="/Dashboard" class="nav-link">Dashboard</a>
        </div>
        <div class="nav-actions">
           <a href="/login" class="btn-ghost">Login</a>
           <a href="/register" class="btn-saas-primary">Get Started</a>
        </div>
      </div>
    </nav>

    <!-- Template Hero -->
    <header class="template-hero reveal-up">
      <div class="container">
        <h1>Design your <span class="text-gradient">edge.</span></h1>
        <p>Select a blueprint engineered for high-growth technical roles.</p>
      </div>
    </header>

    <!-- Template Grid -->
    <section class="templates-section container">
      <div class="templates-grid">
        <div v-for="template in templates" :key="template.id" class="template-card-saas reveal-up">
          <div class="card-visual">
            <img :src="template.image" :alt="template.name" class="t-img">
            <div class="t-overlay">
              <button class="btn-saas-select" @click="selectTemplate(template.id)">Use Blueprint</button>
            </div>
          </div>
          <div class="card-info">
            <div class="info-top">
               <h3>{{ template.name }}</h3>
               <span class="t-badge">{{ template.category }}</span>
            </div>
            <p>{{ template.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer-saas container">
      <div class="footer-bottom">
        <p>© 2024 ResuMeister Labs. All blueprints are ATS-optimized by default.</p>
        <div class="status-badge">
           <span class="status-dot"></span> System Operational
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { gsap } from 'gsap';

export default {
  name: 'ResumeTemplate',
  data() {
    return {
      templates: [
        { id: 1, name: 'The Architect', category: 'Engineering', desc: 'A structure-first layout for senior technical leads.', image: 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?q=80&w=2070&auto=format&fit=crop' },
        { id: 2, name: 'The Specialist', category: 'Product', desc: 'Focuses on outcome-driven metrics and impact.', image: 'https://images.unsplash.com/photo-1626197031507-c17099753214?q=80&w=2070&auto=format&fit=crop' },
        { id: 3, name: 'The Minimalist', category: 'Creative', desc: 'Clean, Swiss-inspired design for high density.', image: 'https://images.unsplash.com/photo-1512485694743-9c9538b4e6e0?q=80&w=2070&auto=format&fit=crop' }
      ]
    };
  },
  mounted() {
    this.executeAnimations();
  },
  methods: {
    executeAnimations() {
      gsap.from('.reveal-up', {
        y: 30,
        opacity: 0,
        duration: 0.8,
        stagger: 0.1,
        ease: 'power3.out'
      });
    },
    selectTemplate(id) {
      this.$router.push(`/fill-resume/${id}`);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.templates-wrapper {
  min-height: 100vh;
  background-color: #030712;
  color: #F8FAFC;
  font-family: 'Outfit', sans-serif;
  overflow-x: hidden;
  position: relative;
}

.atmosphere {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
}
.aura { position: absolute; border-radius: 50%; filter: blur(140px); opacity: 0.1; }
.aura-1 { width: 800px; height: 800px; background: #6366F1; top: -10%; left: -10%; }
.aura-2 { width: 600px; height: 600px; background: #EC4899; bottom: -5%; right: -5%; }

.navbar-saas { padding: 2rem 0; z-index: 100; position: relative; }
.nav-content { display: flex; justify-content: space-between; align-items: center; }
.logo-link { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.logo-img { height: 28px; }
.logo-text { font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff; }

.nav-links { display: flex; gap: 2rem; }
.nav-link { color: #64748B; text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.3s; }
.nav-link:hover { color: #fff; }

.btn-ghost { color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; margin-right: 1.5rem; }
.btn-saas-primary { background: #fff; color: #030712; padding: 0.6rem 1.4rem; border-radius: 99px; font-weight: 700; text-decoration: none; font-size: 0.9rem; transition: all 0.3s; }
.btn-saas-primary:hover { transform: scale(1.05); box-shadow: 0 10px 40px rgba(255, 255, 255, 0.2); }

.container { max-width: 1200px; margin: 0 auto; padding: 0 2rem; position: relative; z-index: 10; }

.template-hero { padding: 6rem 0; text-align: center; }
.template-hero h1 { font-family: 'Space Grotesk', sans-serif; font-size: clamp(3rem, 6vw, 4.5rem); font-weight: 800; margin-bottom: 1rem; }
.text-gradient { background: linear-gradient(to right, #6366F1, #FDBA74); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.template-hero p { font-size: 1.25rem; color: #94A3B8; max-width: 600px; margin: 0 auto; }

.templates-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 2rem; padding-bottom: 8rem; }

.template-card-saas { background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 24px; overflow: hidden; transition: all 0.4s; }
.template-card-saas:hover { border-color: rgba(99, 102, 241, 0.3); transform: translateY(-8px); }

.card-visual { height: 480px; overflow: hidden; position: relative; background: #000; }
.t-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s; opacity: 0.8; }
.template-card-saas:hover .t-img { transform: scale(1.05); opacity: 1; }

.t-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.4); backdrop-filter: blur(4px); opacity: 0; transition: opacity 0.3s; }
.template-card-saas:hover .t-overlay { opacity: 1; }

.btn-saas-select { background: #fff; color: #030712; border: none; padding: 1rem 2rem; border-radius: 99px; font-weight: 800; cursor: pointer; transform: translateY(10px); transition: all 0.3s; }
.template-card-saas:hover .btn-saas-select { transform: translateY(0); }

.card-info { padding: 2rem; }
.info-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.info-top h3 { font-size: 1.25rem; font-weight: 700; color: #fff; }
.t-badge { font-size: 0.7rem; font-weight: 800; text-transform: uppercase; color: #6366F1; background: rgba(99, 102, 241, 0.1); padding: 4px 10px; border-radius: 4px; }
.card-info p { color: #64748B; font-size: 0.95rem; line-height: 1.6; }

.footer-bottom { border-top: 1px solid rgba(255, 255, 255, 0.05); padding: 4rem 0; display: flex; justify-content: space-between; align-items: center; font-size: 0.9rem; color: #475569; }
.status-badge { display: flex; align-items: center; gap: 8px; font-weight: 600; }
.status-dot { width: 8px; height: 8px; background: #10B981; border-radius: 50%; box-shadow: 0 0 10px #10B981; }

@media (max-width: 768px) {
   .nav-links { display: none; }
   .template-hero h1 { font-size: 2.5rem; }
   .templates-grid { grid-template-columns: 1fr; }
   .card-visual { height: 350px; }
}
</style>
