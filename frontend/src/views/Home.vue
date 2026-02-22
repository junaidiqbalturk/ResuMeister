<template>
  <div class="home-wrapper">
    <!-- Rich Atmosphere Background -->
    <div class="atmosphere">
      <div class="aura aura-1"></div>
      <div class="aura aura-2"></div>
      <div class="aura aura-3"></div>
      <div class="aura aura-4"></div>
    </div>

    <!-- Navigation -->
    <nav class="navbar" :class="{ 'navbar-scrolled': scrolled }">
      <div class="container nav-content">
        <div class="logo">
          <a href="/" class="logo-link">
            <img src="/resumeister.png" alt="ResuMeister" class="logo-img">
            <span class="logo-text">ResuMeister</span>
          </a>
        </div>
        <div class="nav-links" v-if="!isMobile">
          <a href="#features" class="nav-link">Product</a>
          <a href="#process" class="nav-link">Process</a>
          <a href="/resume-template" class="nav-link">Blueprints</a>
        </div>
        <div class="nav-actions">
          <a href="/login" class="btn-ghost">Login</a>
          <a href="/register" class="btn-saas-primary">Start Building</a>
        </div>
      </div>
    </nav>

    <!-- HERO: Compact & Full -->
    <section class="hero-full">
      <div class="container hero-grid">
        <div class="hero-left">
          <div class="hero-badge fade-in">
            <span class="badge-dot"></span> 
            ResuMeister Labs v2.5
          </div>
          <h1 class="hero-h1 fade-in">
            Engineering <br/>
            <span class="text-gradient">world-class</span> <br/>
            careers.
          </h1>
          <p class="hero-p fade-in">
            A high-fidelity workspace designed for precision. We combine AI-driven logic with silicon-valley design to help you land at top-tier companies.
          </p>
          <div class="hero-btns fade-in">
            <a href="/register" class="btn-vibrant">Get Started</a>
            <a href="#features" class="btn-ghost-vibrant">View Logic</a>
          </div>
        </div>

        <!-- HERO VISUAL: Rich Dashboard (Not Blank) -->
        <div class="hero-visual zoom-in">
           <div class="v-chrome">
              <div class="v-dots"><span></span><span></span><span></span></div>
           </div>
           <div class="v-body">
              <div class="v-sidebar">
                 <div class="v-s-item" style="width: 80%"></div>
                 <div class="v-s-item" style="width: 60%"></div>
                 <div class="v-s-item" style="width: 40%"></div>
              </div>
              <div class="v-main">
                 <div class="v-m-header">
                    <div class="v-m-card red"></div>
                    <div class="v-m-card blue"></div>
                    <div class="v-m-card purple"></div>
                 </div>
                 <div class="v-m-editor">
                    <!-- Removing the "blank white box" -->
                    <div class="v-m-line title"></div>
                    <div class="v-m-line text"></div>
                    <div class="v-m-line text" style="width: 60%"></div>
                    <div class="v-m-line head"></div>
                    <div class="v-m-line text"></div>
                 </div>
              </div>
           </div>
           <div class="v-overlay"></div>
        </div>
      </div>
    </section>

    <!-- LOGO STRIP -->
    <section class="logo-strip">
       <div class="container strip-flex">
          <span class="strip-text">HIRED AT</span>
          <div class="logo-v">LINΞAR</div>
          <div class="logo-v">VΞRCΞL</div>
          <div class="logo-v">STRIPΞ</div>
          <div class="logo-v">FIGMA</div>
       </div>
    </section>

    <!-- FEATURES: Dense & Visible -->
    <section id="features" class="features-section">
      <div class="container">
        <div class="section-hdr">
          <h2>Built for Performance.</h2>
          <p>The infrastructure behind the world's most successful resumes.</p>
        </div>

        <div class="bento-grid">
          <div class="bento-card b-lg">
             <div class="bento-icon">⚡</div>
             <h3>AI Optimization Engine</h3>
             <p>Our neural network analyzes job descriptions to rewrite your achievements for 99.9% ATS compatibility in seconds.</p>
          </div>
          <div class="bento-card">
             <div class="bento-icon">💎</div>
             <h3>Precision Design</h3>
             <p>Every pixel is engineered for professional clarity and impact.</p>
          </div>
          <div class="bento-card">
             <div class="bento-icon">📊</div>
             <h3>ATS Scoring</h3>
             <p>Instant feedback on how well your resume parses across major HR systems.</p>
          </div>
          <div class="bento-card b-wd">
             <div class="bento-icon">🚀</div>
             <h3>High-Density Workspace</h3>
             <p>The only builder that feels like a professional IDE. Real-time rendering, collaborative tools, and one-click PDF deployments to high-orbit render servers.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- PROCESS: Clear & Full -->
    <section id="process" class="process-section">
       <div class="container">
          <div class="section-hdr">
             <h2>The Strategy.</h2>
          </div>
          <div class="process-grid">
             <div class="p-card">
                <div class="p-num">01</div>
                <h3>Blueprint</h3>
                <p>Choose a mathematically balanced template ready for high-growth roles.</p>
             </div>
             <div class="p-card">
                <div class="p-num">02</div>
                <h3>Narrative</h3>
                <p>Input your career missions and achievements into our precision workspace.</p>
             </div>
             <div class="p-card">
                <div class="p-num">03</div>
                <h3>Deploy</h3>
                <p>Generate a world-class PDF that commands attention from the best in tech.</p>
             </div>
          </div>
       </div>
    </section>

    <!-- CTA -->
    <section class="cta-section container">
       <div class="cta-card">
          <h2>Ready to launch?</h2>
          <p>Join the next generation of industry leaders.</p>
          <div class="cta-btns">
             <a href="/register" class="btn-vibrant">Start Now</a>
             <a href="/resume-template" class="btn-ghost-vibrant">View All</a>
          </div>
       </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
       <div class="container footer-flex">
          <div class="f-info">
             <div class="logo">
                <img src="/resumeister.png" alt="ResuMeister" class="logo-img">
                <span class="logo-text">ResuMeister</span>
             </div>
             <p>The career catalyst for technical innovators.</p>
          </div>
          <div class="f-nav">
             <a href="/resume-template">Templates</a>
             <a href="/register">Builder</a>
             <a href="/login">Login</a>
          </div>
       </div>
       <div class="container f-bottom">
          <p>© 2024 ResuMeister Labs. All systems operational.</p>
       </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      scrolled: false,
      isMobile: false
    };
  },
  mounted() {
    this.handleResize();
    window.addEventListener('resize', this.handleResize);
    window.addEventListener('scroll', this.handleScroll);
  },
  unmounted() {
    window.removeEventListener('resize', this.handleResize);
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleResize() {
      this.isMobile = window.innerWidth < 1024;
    },
    handleScroll() {
      this.scrolled = window.scrollY > 10;
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Outfit:wght@400;600;700;800&display=swap');

.home-wrapper {
  background: #030712;
  color: #fff;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
  position: relative;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 2rem; position: relative; z-index: 10; }

/* Atmosphere */
.atmosphere { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; }
.aura { position: absolute; border-radius: 50%; filter: blur(120px); opacity: 0.15; }
.aura-1 { width: 600px; height: 600px; background: #6366F1; top: -100px; left: -100px; }
.aura-2 { width: 500px; height: 500px; background: #FDBA74; bottom: -50px; right: 100px; }
.aura-3 { width: 400px; height: 400px; background: #EC4899; top: 30%; left: 30%; }

/* Navbar */
.navbar { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; padding: 1.5rem 0; transition: 0.3s; }
.navbar-scrolled { background: rgba(3, 7, 18, 0.9); backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255,255,255,0.05); padding: 1rem 0; }
.nav-content { display: flex; justify-content: space-between; align-items: center; }
.logo-link { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.logo-img { height: 28px; }
.logo-text { font-family: 'Outfit', sans-serif; color: #fff; font-size: 1.25rem; font-weight: 800; letter-spacing: -0.02em; }
.nav-links { display: flex; gap: 2rem; }
.nav-link { color: #94A3B8; text-decoration: none; font-size: 0.9rem; font-weight: 600; transition: 0.2s; }
.nav-link:hover { color: #fff; }
.btn-saas-primary { background: #fff; color: #030712; padding: 0.6rem 1.4rem; border-radius: 99px; text-decoration: none; font-weight: 700; font-size: 0.9rem; }
.btn-ghost { color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; margin-right: 1rem; }

/* HERO: Fixed Gaps & Rich Content */
.hero-full { padding: 160px 0 6rem; }
.hero-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 4rem; align-items: center; }
.hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 99px; font-size: 0.8rem; font-weight: 700; color: #818CF8; margin-bottom: 2rem; }
.badge-dot { width: 6px; height: 6px; background: #6366F1; border-radius: 50%; box-shadow: 0 0 10px #6366F1; }
.hero-h1 { font-size: clamp(3rem, 6vw, 4.5rem); font-weight: 900; line-height: 1; letter-spacing: -0.05em; margin-bottom: 2rem; }
.text-gradient { background: linear-gradient(to right, #6366F1, #FDBA74, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-p { font-size: 1.25rem; color: #94A3B8; line-height: 1.6; margin-bottom: 3rem; }
.hero-btns { display: flex; gap: 1rem; }
.btn-vibrant { background: #fff; color: #030712; padding: 1rem 2.5rem; border-radius: 99px; font-weight: 800; text-decoration: none; font-size: 1.1rem; }
.btn-ghost-vibrant { background: rgba(255,255,255,0.05); color: #fff; padding: 1rem 2.5rem; border-radius: 99px; font-weight: 800; text-decoration: none; border: 1px solid rgba(255,255,255,0.1); font-size: 1.1rem; }

/* Dashboard Visual: Dark & Detailed (No White Blank) */
.hero-visual { background: #0F172A; border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; overflow: hidden; position: relative; box-shadow: 0 50px 100px rgba(0,0,0,0.6); }
.v-chrome { background: #1E293B; padding: 12px 20px; display: flex; gap: 8px; border-bottom: 1px solid rgba(255,255,255,0.05); }
.v-dots span { width: 10px; height: 10px; border-radius: 50%; background: #334155; display: inline-block; margin-right: 4px; }
.v-body { height: 400px; display: flex; padding: 1.5rem; gap: 1.5rem; }
.v-sidebar { width: 25%; background: rgba(255,255,255,0.03); border-radius: 12px; padding: 1.5rem; display: flex; flex-direction: column; gap: 1.5rem; }
.v-s-item { height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; }
.v-main { flex: 1; display: flex; flex-direction: column; gap: 1.5rem; }
.v-m-header { display: flex; gap: 10px; }
.v-m-card { height: 60px; flex: 1; border-radius: 8px; opacity: 0.2; }
.v-m-card.red { background: #EF4444; }
.v-m-card.blue { background: #3B82F6; }
.v-m-card.purple { background: #8B5CF6; }
.v-m-editor { flex: 1; background: #1A202C; border-radius: 12px; padding: 2rem; display: flex; flex-direction: column; gap: 1rem; border: 1px solid rgba(255,255,255,0.05); }
.v-m-line { height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; }
.v-m-line.title { height: 20px; width: 40%; background: rgba(255,255,255,0.1); margin-bottom: 0.5rem; }
.v-m-line.head { height: 12px; width: 25%; background: rgba(255,255,255,0.07); }
.v-overlay { position: absolute; top:0; left:0; width:100%; height:100%; background: radial-gradient(circle at center, rgba(99,102,241,0.1), transparent); pointer-events: none; }

/* Logo Strip */
.logo-strip { padding: 3rem 0; background: rgba(0,0,0,0.2); border-top: 1px solid rgba(255,255,255,0.02); }
.strip-flex { display: flex; justify-content: center; align-items: center; gap: 4rem; flex-wrap: wrap; text-align: center; }
.strip-text { font-size: 0.7rem; font-weight: 800; color: #475569; letter-spacing: 0.1em; }
.logo-v { font-size: 1.25rem; font-weight: 900; color: #fff; opacity: 0.2; letter-spacing: 0.1em; }

/* Sections */
.features-section, .process-section { padding: 6rem 0; }
.section-hdr { text-align: center; margin-bottom: 4rem; }
.section-hdr h2 { font-family: 'Outfit', sans-serif; font-size: 3rem; font-weight: 800; margin-bottom: 1rem; }
.section-hdr p { font-size: 1.1rem; color: #94A3B8; max-width: 600px; margin: 0 auto; }

.bento-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.bento-card { background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3rem; }
.b-lg { grid-column: span 2; }
.b-wd { grid-column: span 3; }
.bento-icon { font-size: 2.5rem; margin-bottom: 1.5rem; display: block; }
.bento-card h3 { font-size: 1.5rem; margin-bottom: 1rem; color: #fff; }
.bento-card p { color: #94A3B8; line-height: 1.6; }

.process-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.p-card { background: rgba(15, 23, 42, 0.2); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3rem; position: relative; }
.p-num { font-size: 3rem; font-weight: 900; color: rgba(255,255,255,0.05); position: absolute; top: 1.5rem; right: 2rem; }
.p-card h3 { font-size: 1.4rem; color: #fff; margin-bottom: 1rem; }
.p-card p { color: #64748B; font-size: 0.95rem; line-height: 1.6; }

/* CTA */
.cta-section { padding: 4rem 0; }
.cta-card { background: linear-gradient(135deg, #1E1B4B 0%, #030712 100%); border: 1px solid rgba(99,102,241,0.2); border-radius: 32px; padding: 6rem; text-align: center; }
.cta-card h2 { font-size: 3rem; font-weight: 900; margin-bottom: 1rem; }
.cta-card p { font-size: 1.2rem; color: #94A3B8; margin-bottom: 3rem; }
.cta-btns { display: flex; justify-content: center; gap: 1.5rem; }

/* Footer */
.footer { padding: 6rem 0 3rem; border-top: 1px solid rgba(255,255,255,0.05); }
.footer-flex { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4rem; }
.f-info { max-width: 300px; }
.f-info p { margin-top: 1.5rem; color: #475569; font-size: 0.9rem; }
.f-nav { display: flex; gap: 2rem; }
.f-nav a { color: #475569; text-decoration: none; font-size: 0.9rem; font-weight: 600; transition: 0.2s; }
.f-nav a:hover { color: #fff; }
.f-bottom { border-top: 1px solid rgba(255,255,255,0.05); padding-top: 2rem; color: #475569; font-size: 0.85rem; text-align: center; }

@media (max-width: 1024px) {
  .hero-grid { grid-template-columns: 1fr; text-align: center; }
  .hero-btns { justify-content: center; }
  .hero-visual { display: none; }
  .bento-grid, .process-grid { grid-template-columns: 1fr; }
  .b-lg, .b-wd { grid-column: span 1; }
  .footer-flex { flex-direction: column; gap: 3rem; text-align: center; }
  .f-info { margin: 0 auto; }
  .f-nav { margin: 0 auto; }
}
</style>
