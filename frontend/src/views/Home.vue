<template>
  <div class="home-page">
    
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <div class="badge glow-pulse">🚀 The #1 AI Resume Builder</div>
        <h1 class="hero-title">
          Land your dream job with a <br/>
          <span class="text-gradient highlight-text">standout resume.</span>
        </h1>
        <p class="hero-subtitle">
          Create professional, ATS-friendly resumes in minutes. Our AI technology ensures you beat the bots and get noticed by top recruiters.
        </p>
        <div class="hero-cta">
          <router-link to="/register" class="btn-primary-large group">
            Build Your Resume — Free
            <span class="arrow-icon">→</span>
          </router-link>
          <router-link to="/templates" class="btn-outline-large">View Templates</router-link>
        </div>
        <p class="hero-micro mt-6 tracking-wide">NO CREDIT CARD REQUIRED • ATS-OPTIMIZED FORMATS • 100K+ BUILT</p>
      </div>

      <div class="hero-mockup-wrapper">
        <div class="floating-mockup">
           <img :src="heroImage" alt="ResuMeister Dashboard Mockup" class="mockup-img" />
           <div class="mockup-glow"></div>
           
           <!-- Decorative floating UI elements -->
           <div class="float-ui ui-1 glass-card">
              <span class="ui-icon">✨</span> AI Summary Generated
           </div>
           <div class="float-ui ui-2 glass-card">
              <span class="ui-icon">📈</span> ATS Score 94%
           </div>
        </div>
      </div>
    </section>

    <!-- Trusted By / Logos -->
    <section class="logos-section">
      <p class="logos-title text-gradient">TRUSTED BY PROFESSIONALS HIRED AT</p>
      <div class="logo-grid">
        <div class="company-logo">Google</div>
        <div class="company-logo">Amazon</div>
        <div class="company-logo">Microsoft</div>
        <div class="company-logo">Netflix</div>
        <div class="company-logo">Meta</div>
      </div>
    </section>

    <!-- Feature Highlights - Bento Grid -->
    <section class="features-section">
      <div class="section-header">
        <div class="badge">Platform Features</div>
        <h2>Everything you need to <span class="text-gradient">get hired.</span></h2>
        <p>A powerful suite of tools designed to accelerate your career growth.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-card glass-card x-large group-card">
          <div class="bento-content">
            <h3>AI-Powered Templates</h3>
            <p>Generate bullet points, summaries, and cover letters effortlessly with our smart AI assistant. We analyze thousands of successful profiles to suggest the perfect phrasing for your role.</p>
            <div class="inline-cta mt-4">Explore AI Features <span>→</span></div>
          </div>
          <div class="bento-visual bg-gradient-1"></div>
        </div>
        
        <div class="bento-card glass-card">
          <div class="bento-content">
            <div class="icon-wrap">🤖</div>
            <h3>ATS-Friendly</h3>
            <p>Rigorously tested layouts to pass Applicant Tracking Systems.</p>
          </div>
          <div class="bento-visual bg-pattern"></div>
        </div>
        
        <div class="bento-card glass-card">
          <div class="bento-content">
            <div class="icon-wrap">📄</div>
            <h3>1-Click PDF Export</h3>
            <p>Download your polished resume in pixel-perfect PDF format instantly.</p>
          </div>
        </div>
        
        <div class="bento-card glass-card large group-card">
          <div class="bento-content">
            <h3>Multi-Profile Management</h3>
            <p>Tailor your resume for different roles seamlessly. Duplicate, edit, and keep track of all your applications in one centralized dashboard.</p>
          </div>
          <div class="bento-visual bento-grid-mini">
            <span v-for="i in 4" :key="i" class="mini-card outline-glow"></span>
          </div>
        </div>
      </div>
    </section>

    <!-- Simple Try Now Banner -->
    <section class="cta-section">
      <div class="cta-banner-content glass-card premium-shadow">
        <h2>Ready to upgrade your career?</h2>
        <p>Join thousands of successful job seekers today and land your dream job faster.</p>
        <router-link to="/register" class="btn-cta-massive">
          Get Started For Free
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
import heroImg from '@/assets/hero-bg.jpeg';

export default {
  name: 'HomeView',
  data() {
    return {
      heroImage: heroImg
    };
  }
}
</script>

<style scoped>
.home-page {
  padding-bottom: 4rem;
  overflow-x: hidden;
}

/* Helpers */
.mt-4 { margin-top: 1rem; }
.mt-6 { margin-top: 1.5rem; }
.tracking-wide { letter-spacing: 0.05em; font-weight: 700; color: var(--text-dim) !important; }

.badge {
  display: inline-block;
  padding: 0.5rem 1.25rem;
  background: var(--accent-glow);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 99px;
  color: var(--accent);
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.1);
}

.glow-pulse {
  animation: pulseGlow 2s infinite;
}

@keyframes pulseGlow {
  0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
  100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
}

/* Hero Section */
.hero-section {
  min-height: 95vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 6rem 2rem 0;
  text-align: center;
  position: relative;
  overflow: visible; /* to allow glows to escape */
}

/* Animated Background Blob */
.hero-section::before {
  content: '';
  position: absolute;
  top: -10%;
  left: 50%;
  transform: translateX(-50%);
  width: 900px;
  height: 900px;
  background: radial-gradient(circle, rgba(99,102,241,0.2) 0%, rgba(236,72,153,0.1) 40%, transparent 70%);
  z-index: -1;
  pointer-events: none;
  animation: floatOrb 10s ease-in-out infinite alternate;
}

@keyframes floatOrb {
  0% { transform: translate(-50%, 0) scale(1); }
  100% { transform: translate(-50%, 20px) scale(1.05); }
}

.hero-title {
  font-size: clamp(3.5rem, 6vw, 5.5rem);
  line-height: 1.1;
  margin-bottom: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  animation: fadeUp 0.8s ease-out;
}

.highlight-text {
  position: relative;
  display: inline-block;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  max-width: 650px;
  margin: 0 auto 3rem;
  line-height: 1.6;
  animation: fadeUp 0.8s ease-out 0.1s backwards;
}

.hero-cta {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  align-items: center;
  animation: fadeUp 0.8s ease-out 0.2s backwards;
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1rem 2.25rem;
  border-radius: 99px;
  font-weight: 700;
  font-size: 1.1rem;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 10px 30px rgba(255,255,255,0.15);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-primary-large:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 40px rgba(255,255,255,0.3);
}

.arrow-icon {
  transition: transform 0.3s;
}
.btn-primary-large:hover .arrow-icon {
  transform: translateX(4px);
}

.btn-outline-large {
  background: rgba(30, 41, 59, 0.5);
  backdrop-filter: blur(8px);
  color: var(--text-main) !important;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 1rem 2.25rem;
  border-radius: 99px;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-outline-large:hover {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.4);
  transform: translateY(-4px);
}

.hero-micro {
  font-size: 0.8rem;
  color: var(--text-dim);
  animation: fadeUp 0.8s ease-out 0.3s backwards;
}

/* Advanced Hero Visual */
.hero-mockup-wrapper {
  margin-top: 6rem;
  width: 100%;
  max-width: 1100px;
  perspective: 1000px;
  animation: fadeUp 1.2s ease-out 0.5s backwards;
  position: relative;
}

.floating-mockup {
  position: relative;
  border-radius: 20px;
  transform: rotateX(8deg) rotateY(-2deg) scale(0.95);
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  transform-style: preserve-3d;
}

.floating-mockup:hover {
  transform: rotateX(0deg) rotateY(0deg) scale(1);
}

.mockup-img {
  width: 100%;
  height: auto;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 30px 80px rgba(0,0,0,0.6), 0 0 40px var(--accent-glow);
  filter: brightness(0.95) contrast(1.1);
}

.mockup-glow {
  position: absolute;
  top: 50%; left: 50%;
  width: 80%; height: 80%;
  transform: translate(-50%, -50%);
  background: radial-gradient(ellipse, var(--accent-glow) 0%, transparent 70%);
  z-index: -1;
}

/* Floating UI Elements */
.float-ui {
  position: absolute;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  transform: translateZ(50px);
  animation: float 6s ease-in-out infinite;
}

.ui-icon { font-size: 1.25rem; }

.ui-1 {
  top: 15%; right: -5%;
  border-left: 3px solid var(--tertiary);
  animation-delay: 0s;
}

.ui-2 {
  bottom: 20%; left: -8%;
  border-left: 3px solid #10B981;
  animation-delay: -3s;
}

@keyframes float {
  0% { transform: translateY(0px) translateZ(50px); }
  50% { transform: translateY(-15px) translateZ(50px); }
  100% { transform: translateY(0px) translateZ(50px); }
}

/* Logos Section */
.logos-section {
  padding: 5rem 2rem;
  text-align: center;
  position: relative;
  z-index: 10;
}

.logos-title {
  font-size: 0.85rem;
  font-weight: 800;
  margin-bottom: 2.5rem;
  letter-spacing: 0.1em;
}

.logo-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 4rem;
  opacity: 0.5;
  transition: opacity 0.4s;
}
.logos-section:hover .logo-grid { opacity: 0.8; }

.company-logo {
  font-family: var(--font-heading);
  font-size: 1.7rem;
  font-weight: 700;
  color: white;
  filter: grayscale(100%);
  transition: filter 0.4s, transform 0.4s;
  cursor: default;
}

.company-logo:hover {
  filter: grayscale(0%);
  transform: scale(1.1);
  text-shadow: 0 0 20px rgba(255,255,255,0.3);
}

/* Features - Bento Grid */
.features-section {
  max-width: 1200px;
  margin: 6rem auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  margin-bottom: 1rem;
}
.section-header p {
  color: var(--text-muted);
  font-size: 1.15rem;
  max-width: 600px;
  margin: 0 auto;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 280px;
  gap: 1.5rem;
}

.bento-card {
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  position: relative;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s;
}

.bento-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(99,102,241,0.2);
}

.bento-card.x-large {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-card.large {
  grid-column: span 2;
}

.icon-wrap {
  width: 48px; height: 48px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}

.bento-content h3 {
  font-size: 1.6rem;
  margin-bottom: 0.75rem;
  color: var(--text-main);
  z-index: 2;
  position: relative;
}

.bento-content p {
  color: var(--text-muted);
  font-size: 1rem;
  line-height: 1.6;
  z-index: 2;
  position: relative;
}

.x-large .bento-content h3 {
  font-size: 2.8rem;
  margin-bottom: 1rem;
}
.x-large .bento-content p {
  font-size: 1.15rem;
  max-width: 80%;
}

.inline-cta {
  color: var(--accent);
  font-weight: 700;
  font-size: 1.05rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: 0.3s;
}
.group-card:hover .inline-cta { color: var(--text-main); }
.group-card:hover .inline-cta span { transform: translateX(5px); }
.inline-cta span { transition: transform 0.3s; }

.bento-visual {
  position: absolute;
  bottom: 0; right: 0; left: 0; top: 0;
  z-index: 1;
  opacity: 0.15;
  transition: opacity 0.5s;
}

.bento-card:hover .bento-visual {
  opacity: 0.4;
}

.bg-gradient-1 {
  background: radial-gradient(circle at bottom right, var(--accent) 0%, transparent 60%);
}

.bg-pattern {
  background-image: radial-gradient(rgba(255,255,255,0.2) 1px, transparent 1px);
  background-size: 20px 20px;
  bottom: -50px; right: -50px;
}

/* CTA Banner */
.cta-section {
  padding: 6rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.cta-banner-content {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.4), rgba(236, 72, 153, 0.2));
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 32px;
  padding: 5rem 3rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.cta-banner-content::before {
  content: '';
  position: absolute;
  top: -50%; left: -50%; width: 200%; height: 200%;
  background: radial-gradient(ellipse at center, rgba(255,255,255,0.1) 0%, transparent 50%);
  pointer-events: none;
}

.cta-banner-content h2 {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  margin-bottom: 1rem;
  color: #fff;
}

.cta-banner-content p {
  color: rgba(255,255,255,0.8);
  font-size: 1.25rem;
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto; margin-right: auto;
}

.btn-cta-massive {
  background: #fff;
  color: var(--accent) !important;
  padding: 1.25rem 3rem;
  border-radius: 99px;
  font-weight: 800;
  font-size: 1.25rem;
  display: inline-block;
  box-shadow: 0 15px 30px rgba(0,0,0,0.3);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-cta-massive:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 20px 40px rgba(99, 102, 241, 0.4);
}

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 960px) {
  .hero-section { padding-top: 4rem; }
  .bento-grid {
    grid-template-columns: 1fr;
    grid-auto-rows: minmax(220px, auto);
  }
  .bento-card.x-large, .bento-card.large {
    grid-column: span 1;
    grid-row: span 1;
  }
  .x-large .bento-content p { max-width: 100%; }
  .ui-1, .ui-2 { display: none; }
  .hero-cta { flex-direction: column; }
  .btn-primary-large, .btn-outline-large { width: 100%; justify-content: center; }
  .cta-banner-content { padding: 4rem 2rem; }
}
</style>
