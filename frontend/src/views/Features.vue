<template>
  <div class="features-page">
    <div class="page-header text-center">
      <div class="badge">Platform Features</div>
      <h1 class="page-title">Everything you need to <br/><span class="text-gradient">stand out.</span></h1>
      <p class="page-subtitle">We automated the tedious parts of writing a resume so you can focus on landing your dream role. Stand out from the crowd with our comprehensive suite of career tools.</p>
    </div>

    <!-- Feature Block 1: AI Assistant -->
    <section class="feature-block">
      <div class="feature-text">
        <h2 class="feature-heading">AI Content Generator</h2>
        <p class="feature-desc">Writer's block is a thing of the past. Let our AI trained on thousands of successful tech and business resumes write your summary, bullet points, and cover letter variations in seconds.</p>
        <ul class="feature-list">
          <li><span class="icon-check">✓</span> Over 1,000+ industry-specific prompts</li>
          <li><span class="icon-check">✓</span> Grammar and punctuation auto-fix</li>
          <li><span class="icon-check">✓</span> Tone adjustment (Professional, Creative, Direct)</li>
        </ul>
      </div>
      <div class="feature-visual tilt-right">
        <div class="mockup-ui glass-card">
          <div class="ui-header"><span class="mr-2">✨</span> AI Suggester</div>
          <div class="ui-body">
            <div class="ui-suggestion">"Spearheaded a cross-functional team of 12 to deliver a new SaaS product..."</div>
            <div class="ui-suggestion active">
               <span class="floating-sparkle">✨</span>
               "Automated CI/CD pipelines, reducing deployment times by 40%..."
            </div>
            <div class="ui-suggestion">"Managed an annual marketing budget of $1.5M..."</div>
          </div>
        </div>
        <!-- Decorative Glow -->
        <div class="visual-glow glow-accent"></div>
      </div>
    </section>

    <!-- Feature Block 2: ATS Scanner -->
    <section class="feature-block reverse">
      <div class="feature-visual tilt-left">
         <div class="mockup-ui ats-scanner glass-card">
          <div class="ring-wrapper">
             <div class="ring-chart">
               <span>94<small>%</small></span>
             </div>
             <div class="ring-glow"></div>
          </div>
          <div class="ats-stats">
            <div class="stat-row"><span class="status green">●</span> <span>Keywords Match</span> <span class="ml-auto font-bold text-green">Good</span></div>
            <div class="stat-row"><span class="status yellow">●</span> <span>Action Verbs</span> <span class="ml-auto font-bold text-yellow">Needs tuning</span></div>
            <div class="stat-row"><span class="status green">●</span> <span>Format Check</span> <span class="ml-auto font-bold text-green">Passed</span></div>
          </div>
        </div>
        <!-- Decorative Glow -->
        <div class="visual-glow glow-secondary"></div>
      </div>
      <div class="feature-text">
        <h2 class="feature-heading">Real-time ATS Scoring</h2>
        <p class="feature-desc">Don't guess if your resume will pass the Applicant Tracking Systems. Paste your target job description and get an instant score and actionable feedback based on real recruitment data.</p>
        <ul class="feature-list">
          <li><span class="icon-check">✓</span> Keyword gap analysis</li>
          <li><span class="icon-check">✓</span> Hard skills vs Soft skills matching</li>
          <li><span class="icon-check">✓</span> Formatting & readability checks</li>
        </ul>
      </div>
    </section>

    <!-- Feature Block 3: Export & Tracking -->
    <section class="feature-block">
      <div class="feature-text">
        <h2 class="feature-heading">Instant PDF Rendering</h2>
        <p class="feature-desc">No more wrestling with Word document margins. Choose a premium template, populate your data, and export to a flawless, crisp PDF instantly. Every generated file is optimized for web and print.</p>
      </div>
      <div class="feature-visual bento-style">
        <div class="bento-sm glass-card group">
            <span class="text-2xl mb-2 block transition-transform group-hover:scale-110">📄</span>
            PDF Download
        </div>
        <div class="bento-sm glass-card group">
            <span class="text-2xl mb-2 block transition-transform group-hover:scale-110">🔗</span>
            Clean URLs
        </div>
        <div class="bento-sm wide glass-card group relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-r from-indigo-500/10 to-transparent"></div>
            <span class="text-2xl mb-2 block transition-transform group-hover:scale-110">📈</span>
            Multi-version tracking
        </div>
      </div>
    </section>

  </div>
</template>

<script>
export default {
  name: 'FeaturesView'
}
</script>

<style scoped>
.features-page {
  padding: 4rem 2rem 8rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin: 2rem auto 8rem;
  max-width: 800px;
  animation: fadeUp 0.8s ease-out;
}

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

.page-title {
  font-size: clamp(3rem, 5vw, 4.5rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
  font-weight: 800;
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  line-height: 1.6;
}

/* Base Feature Block Styles */
.feature-block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: center;
  margin-bottom: 10rem;
}

.feature-block.reverse {
  /* No actual reverse in flex because it's grid, but we can reverse order property if we swap DOM or use grid areas */
  grid-template-areas: "visual text";
}
.feature-block.reverse .feature-visual { grid-area: visual; }
.feature-block.reverse .feature-text { grid-area: text; }

.feature-heading {
  font-size: clamp(2rem, 3vw, 2.75rem);
  margin-bottom: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.feature-desc {
  font-size: 1.15rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.feature-list {
  list-style: none;
  font-size: 1.1rem;
}

.feature-list li {
  margin-bottom: 1.2rem;
  display: flex;
  align-items: center;
  gap: 16px;
  color: var(--text-main);
  opacity: 0.95;
  font-weight: 500;
}

.icon-check {
  color: #fff;
  background: var(--accent);
  border-radius: 50%;
  width: 24px; height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  box-shadow: 0 4px 10px rgba(99, 102, 241, 0.4);
}

/* Mockup UI Component Styling */
.feature-visual {
  position: relative;
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.visual-glow {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 80%; height: 80%;
  border-radius: 50%;
  filter: blur(80px);
  z-index: -1;
  opacity: 0.6;
}
.glow-accent { background: var(--accent); }
.glow-secondary { background: var(--secondary); }

.tilt-right { transform: perspective(1000px) rotateY(-8deg) rotateX(4deg); }
.tilt-right:hover { transform: perspective(1000px) rotateY(0deg) rotateX(0deg); }

.tilt-left { transform: perspective(1000px) rotateY(8deg) rotateX(4deg); }
.tilt-left:hover { transform: perspective(1000px) rotateY(0deg) rotateX(0deg); }

.mockup-ui {
  width: 100%;
  max-width: 500px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(16px);
}

/* AI Suggester Specifics */
.ui-header {
  padding: 1.25rem 1.5rem;
  background: rgba(255,255,255,0.03);
  font-weight: 600;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  display: flex;
  align-items: center;
  font-size: 1.05rem;
}

.mr-2 { margin-right: 8px; }

.ui-body { padding: 1.5rem; display: flex; flex-direction: column; gap: 1rem; }

.ui-suggestion {
  padding: 1.25rem;
  border: 1px dashed rgba(255,255,255,0.15);
  border-radius: 12px;
  font-size: 0.95rem;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
}

.ui-suggestion:hover {
  background: rgba(255,255,255,0.02);
  border-color: rgba(255,255,255,0.3);
}

.ui-suggestion.active {
  border-color: var(--accent);
  border-style: solid;
  color: var(--text-main);
  background: rgba(99, 102, 241, 0.15);
  transform: translateX(10px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.floating-sparkle {
  position: absolute;
  top: -10px;
  right: -10px;
  font-size: 1.25rem;
  animation: pulseGlow 2s infinite alternate;
}

/* ATS Scanner Specifics */
.ats-scanner {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 2rem;
  gap: 2.5rem;
}

.ring-wrapper {
  position: relative;
}

.ring-chart {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  border: 12px solid #10B981; /* Green success */
  border-right-color: rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  font-weight: 800;
  transform: rotate(-45deg);
  background: rgba(16, 185, 129, 0.05);
  position: relative;
  z-index: 2;
}

.ring-chart span {
  transform: rotate(45deg);
  font-family: var(--font-heading);
}

.ring-chart small {
  font-size: 1.25rem;
  color: var(--text-muted);
}

.ring-glow {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 100%; height: 100%;
  border-radius: 50%;
  box-shadow: 0 0 40px rgba(16, 185, 129, 0.4);
  z-index: 1;
}

.ats-stats {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  padding: 0 1rem;
}

.stat-row {
  display: flex;
  align-items: center;
  background: rgba(255,255,255,0.03);
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.05);
  font-size: 0.95rem;
}

.status { margin-right: 12px; font-size: 1rem; }
.status.green { color: #10B981; text-shadow: 0 0 10px rgba(16,185,129,0.5); }
.status.yellow { color: #F59E0B; text-shadow: 0 0 10px rgba(245,158,11,0.5); }

.ml-auto { margin-left: auto; }
.font-bold { font-weight: 700; }
.text-green { color: #10B981; }
.text-yellow { color: #F59E0B; }

/* Bento Style Visual (Feature 3) */
.bento-style {
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  min-height: auto;
  transform: none; /* No tilt here */
}

.bento-sm {
  border-radius: 20px;
  padding: 2.5rem 1rem;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  text-align: center;
  cursor: default;
}

.bento-sm:hover {
  color: var(--text-main);
  transform: translateY(-8px);
  border-color: rgba(99, 102, 241, 0.4);
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}

.bento-sm.wide { 
  grid-column: span 2; 
  flex-direction: row;
  gap: 1rem;
  padding: 2rem;
}

.text-2xl { font-size: 2rem; }
.mb-2 { margin-bottom: 0.5rem; }
.block { display: block; }
.transition-transform { transition: transform 0.3s; }

/* Utility Classes used in HTML */
.group:hover .group-hover\:scale-110 { transform: scale(1.1); }
.relative { position: relative; }
.absolute { position: absolute; }
.inset-0 { top: 0; right: 0; bottom: 0; left: 0; }
.overflow-hidden { overflow: hidden; }

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlow {
  from { opacity: 0.6; filter: drop-shadow(0 0 5px rgba(255,255,255,0.5)); }
  to { opacity: 1; filter: drop-shadow(0 0 15px rgba(255,255,255,1)); }
}

@media (max-width: 1024px) {
  .feature-block {
    grid-template-columns: 1fr;
    gap: 4rem;
    grid-template-areas: "text" "visual" !important;
    text-align: center;
  }
  
  .feature-list li {
    justify-content: center;
  }
  
  .feature-visual {
    min-height: 350px;
  }
  
  .tilt-left, .tilt-right {
    transform: none; /* Disable 3d tilts on smaller devices */
  }
  
  .tilt-left:hover, .tilt-right:hover {
    transform: translateY(-5px);
  }
}
</style>
