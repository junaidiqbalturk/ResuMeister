<template>
  <div class="home-page">
    
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <div class="badge">🚀 The #1 AI Resume Builder</div>
        <h1 class="hero-title">
          Land your dream job with a <br/>
          <span class="text-gradient">standout resume.</span>
        </h1>
        <p class="hero-subtitle">
          Create professional, ATS-friendly resumes in minutes. Our AI technology ensures you beat the bots and get noticed by top recruiters.
        </p>
        <div class="hero-cta">
          <router-link to="/register" class="btn-primary-large">Build Your Resume — Free</router-link>
          <router-link to="/templates" class="btn-outline-large">View Templates</router-link>
        </div>
        <p class="hero-micro">No credit card required. Over 100k+ resumes built.</p>
      </div>

      <div class="hero-mockup-wrapper">
        <div class="mockup-frame">
          <div class="mockup-header">
            <span></span><span></span><span></span>
          </div>
          <img src="https://source.unsplash.com/random/1200x800/?dashboard" alt="ResuMeister Dashboard Mockup" class="mockup-img" />
          <div class="mockup-overlay"></div>
        </div>
      </div>
    </section>

    <!-- Trusted By / Logos -->
    <section class="logos-section">
      <p>Trusted by professionals hired at</p>
      <div class="logo-grid">
        <div class="company-logo">Google</div>
        <div class="company-logo">Amazon</div>
        <div class="company-logo">Microsoft</div>
        <div class="company-logo">Netflix</div>
        <div class="company-logo">Meta</div>
      </div>
    </section>

    <!-- Feature Highlights -->
    <section class="features-section">
      <div class="section-header">
        <h2>Everything you need to <span class="text-gradient">get hired.</span></h2>
        <p>A powerful suite of tools designed to accelerate your career growth.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-card x-large">
          <div class="bento-content">
            <h3>AI-Powered Templates</h3>
            <p>Generate bullet points, summaries, and cover letters effortlessly with our smart AI assistant.</p>
          </div>
          <div class="bento-visual bg-gradient-1"></div>
        </div>
        <div class="bento-card">
          <div class="bento-content">
            <h3>ATS-Friendly</h3>
            <p>Our templates are rigorously tested to pass Applicant Tracking Systems.</p>
          </div>
          <div class="bento-visual bg-pattern"></div>
        </div>
        <div class="bento-card">
          <div class="bento-content">
            <h3>1-Click PDF Export</h3>
            <p>Download your polished resume in pixel-perfect PDF format instantly.</p>
          </div>
        </div>
        <div class="bento-card large">
          <div class="bento-content">
            <h3>Multi-Profile Management</h3>
            <p>Tailor your resume for different roles seamlessly.</p>
          </div>
          <div class="bento-visual bento-grid-mini">
            <span v-for="i in 4" :key="i"></span>
          </div>
        </div>
      </div>
    </section>

    <!-- Simple Try Now Banner -->
    <section class="cta-banner">
      <div class="cta-banner-content">
        <h2>Ready to upgrade your career?</h2>
        <p>Join thousands of successful job seekers today.</p>
        <router-link to="/register" class="btn-primary-large">Get Started Now</router-link>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
.home-page {
  padding-bottom: 4rem;
}

/* Hero Section */
.hero-section {
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: -20%;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
  z-index: -1;
  pointer-events: none;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(99, 102, 241, 0.1);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 99px;
  color: var(--accent);
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 2rem;
  animation: fadeDown 0.8s ease-out;
}

.hero-title {
  font-size: clamp(3rem, 6vw, 5rem);
  line-height: 1.1;
  margin-bottom: 1.5rem;
  animation: fadeUp 1s ease-out;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto 3rem;
  animation: fadeUp 1s ease-out 0.2s backwards;
}

.hero-cta {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem;
  animation: fadeUp 1s ease-out 0.4s backwards;
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1rem 2rem;
  border-radius: 99px;
  font-weight: 700;
  font-size: 1.1rem;
  box-shadow: 0 10px 30px rgba(255,255,255,0.1);
  transition: all 0.3s;
}

.btn-primary-large:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 40px rgba(255,255,255,0.2);
}

.btn-outline-large {
  background: transparent;
  color: var(--text-main) !important;
  border: 1px solid rgba(255,255,255,0.2);
  padding: 1rem 2rem;
  border-radius: 99px;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s;
}

.btn-outline-large:hover {
  background: rgba(255,255,255,0.05);
  border-color: rgba(255,255,255,0.5);
}

.hero-micro {
  font-size: 0.85rem;
  color: var(--text-dim);
  animation: fadeUp 1s ease-out 0.6s backwards;
}

.hero-mockup-wrapper {
  margin-top: 5rem;
  width: 100%;
  max-width: 1100px;
  perspective: 1000px;
  animation: fadeUp 1.2s ease-out 0.8s backwards;
}

.mockup-frame {
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--shadow-premium);
  transform: rotateX(5deg);
  transition: transform 0.5s;
}

.mockup-frame:hover {
  transform: rotateX(0deg);
}

.mockup-header {
  background: rgba(0,0,0,0.3);
  padding: 1rem;
  display: flex;
  gap: 8px;
}

.mockup-header span {
  width: 12px; height: 12px; border-radius: 50%;
}
.mockup-header span:nth-child(1) { background: #FF5F56; }
.mockup-header span:nth-child(2) { background: #FFBD2E; }
.mockup-header span:nth-child(3) { background: #27C93F; }

.mockup-img {
  width: 100%;
  height: auto;
  opacity: 0.8;
  filter: brightness(0.9) contrast(1.1);
}

/* Logos Section */
.logos-section {
  padding: 4rem 2rem;
  text-align: center;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.logos-section p {
  color: var(--text-dim);
  margin-bottom: 2rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.85rem;
}

.logo-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 3rem;
  opacity: 0.6;
}

.company-logo {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  filter: grayscale(100%);
  transition: filter 0.3s, opacity 0.3s;
}

.company-logo:hover {
  filter: grayscale(0%);
  opacity: 1;
}

/* Features */
.features-section {
  max-width: 1200px;
  margin: 8rem auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.section-header p {
  color: var(--text-muted);
  font-size: 1.15rem;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 250px;
  gap: 1.5rem;
}

.bento-card {
  background: var(--bg-card);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  position: relative;
  transition: transform 0.3s, background 0.3s;
}

.bento-card:hover {
  transform: translateY(-5px);
  background: rgba(30, 41, 59, 0.6);
  border-color: rgba(255, 255, 255, 0.15);
}

.bento-card.x-large {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-card.large {
  grid-column: span 2;
}

.bento-content h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-main);
  z-index: 2;
  position: relative;
}

.bento-content p {
  color: var(--text-muted);
  font-size: 0.95rem;
  z-index: 2;
  position: relative;
}

.x-large .bento-content h3 {
  font-size: 2.5rem;
}

.bento-visual {
  position: absolute;
  bottom: 0; right: 0; left: 0; top: 0;
  z-index: 1;
  opacity: 0.3;
  transition: opacity 0.3s;
}

.bento-card:hover .bento-visual {
  opacity: 0.6;
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
.cta-banner {
  margin: 6rem 2rem;
}

.cta-banner-content {
  background: linear-gradient(135deg, var(--accent), var(--tertiary));
  max-width: 1000px;
  margin: 0 auto;
  border-radius: 24px;
  padding: 4rem 2rem;
  text-align: center;
  box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3);
}

.cta-banner-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: white;
}

.cta-banner-content p {
  color: rgba(255,255,255,0.8);
  font-size: 1.1rem;
  margin-bottom: 2.5rem;
}

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 900px) {
  .bento-grid {
    grid-template-columns: 1fr;
    grid-auto-rows: minmax(200px, auto);
  }
  .bento-card.x-large, .bento-card.large {
    grid-column: span 1;
    grid-row: span 1;
  }
  .hero-cta { flex-direction: column; }
  .btn-primary-large, .btn-outline-large { width: 100%; text-align: center; }
}
</style>
