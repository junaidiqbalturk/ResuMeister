<template>
  <div class="features-page">
    <div class="page-header text-center">
      <div class="badge">Platform Features</div>
      <h1 class="page-title">Everything you need to <br/><span class="text-gradient">stand out.</span></h1>
      <p class="page-subtitle">We automated the tedious parts of writing a resume so you can focus on landing your dream role.</p>
    </div>

    <!-- Feature Block 1: AI Asssitant -->
    <section class="feature-block">
      <div class="feature-text">
        <h2 class="feature-heading">AI Content Generator</h2>
        <p class="feature-desc">Writer's block is a thing of the past. Let our AI trained on thousands of successful tech and business resumes write your summary, bullet points, and cover letter variations in seconds.</p>
        <ul class="feature-list">
          <li><span>✓</span> Over 1,000+ industry-specific prompts</li>
          <li><span>✓</span> Grammar and punctuation auto-fix</li>
          <li><span>✓</span> Tone adjustment (Professional, Creative, Direct)</li>
        </ul>
      </div>
      <div class="feature-visual tilt-right">
        <div class="mockup-ui">
          <div class="ui-header">AI Suggester ✨</div>
          <div class="ui-body">
            <div class="ui-suggestion">"Spearheaded a cross-functional team of 12 to deliver a new SaaS product..."</div>
            <div class="ui-suggestion active">"Automated CI/CD pipelines, reducing deployment times by 40%..."</div>
            <div class="ui-suggestion">"Managed an annual marketing budget of $1.5M..."</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Feature Block 2: ATS Scanner -->
    <section class="feature-block reverse">
      <div class="feature-visual tilt-left">
         <div class="mockup-ui ats-scanner">
          <div class="ring-chart">
            <span>94%</span>
          </div>
          <div class="ats-stats">
            <div><span class="status green">●</span> Keywords Found</div>
            <div><span class="status yellow">●</span> Optimization Needed</div>
            <div><span class="status green">●</span> Format Passed</div>
          </div>
        </div>
      </div>
      <div class="feature-text">
        <h2 class="feature-heading">Real-time ATS Scoring</h2>
        <p class="feature-desc">Don't guess if your resume will pass the Applicant Tracking Systems. Paste your target job description and get an instant score and actionable feedback.</p>
        <ul class="feature-list">
          <li><span>✓</span> Keyword gap analysis</li>
          <li><span>✓</span> Hard skills vs Soft skills matching</li>
          <li><span>✓</span> Formatting checks</li>
        </ul>
      </div>
    </section>

    <!-- Feature Block 3: Export & Tracking -->
    <section class="feature-block">
      <div class="feature-text">
        <h2 class="feature-heading">Instant PDF Rendering</h2>
        <p class="feature-desc">No more wrestling with Word document margins. Choose a premium template, populate your data, and export to a flawless, crisp PDF instantly.</p>
      </div>
      <div class="feature-visual bento-style">
        <div class="bento-sm">PDF Download</div>
        <div class="bento-sm">Clean URLs</div>
        <div class="bento-sm wide">Multi-version tracking</div>
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
  padding: 2rem 2rem 6rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin: 4rem auto 8rem;
  max-width: 800px;
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
  margin-bottom: 1.5rem;
}

.page-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
}

.feature-block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: center;
  margin-bottom: 8rem;
}

.feature-block.reverse {
  /* No actual reverse in flex because it's grid, but we can reverse order property if we swap DOM or use grid areas */
  grid-template-areas: "visual text";
}
.feature-block.reverse .feature-visual { grid-area: visual; }
.feature-block.reverse .feature-text { grid-area: text; }

.feature-heading {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

.feature-desc {
  font-size: 1.1rem;
  color: var(--text-muted);
  line-height: 1.8;
  margin-bottom: 2rem;
}

.feature-list {
  list-style: none;
  font-size: 1.05rem;
}

.feature-list li {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-main);
  opacity: 0.9;
}

.feature-list span {
  color: var(--accent);
  font-weight: bold;
}

/* Mockup UI Component Styling */
.feature-visual {
  position: relative;
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  padding: 2rem;
  min-height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 30px 60px rgba(0,0,0,0.5);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.tilt-right { transform: perspective(1000px) rotateY(-5deg) rotateX(5deg); }
.tilt-right:hover { transform: perspective(1000px) rotateY(0deg) rotateX(0deg); }

.tilt-left { transform: perspective(1000px) rotateY(5deg) rotateX(5deg); }
.tilt-left:hover { transform: perspective(1000px) rotateY(0deg) rotateX(0deg); }

.mockup-ui {
  width: 100%;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  overflow: hidden;
}

.ui-header {
  padding: 1rem;
  background: rgba(255,255,255,0.05);
  font-weight: 600;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.ui-body { padding: 1.5rem; display: flex; flex-direction: column; gap: 1rem; }

.ui-suggestion {
  padding: 1rem;
  border: 1px dashed rgba(255,255,255,0.2);
  border-radius: 8px;
  font-size: 0.9rem;
  color: var(--text-muted);
  cursor: pointer;
  transition: 0.3s;
}

.ui-suggestion:hover, .ui-suggestion.active {
  border-color: var(--accent);
  color: var(--text-main);
  background: rgba(99, 102, 241, 0.1);
  transform: translateX(10px);
}

.ats-scanner {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2.5rem;
  gap: 2rem;
}

.ring-chart {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 10px solid var(--accent);
  border-right-color: rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  transform: rotate(-45deg);
}

.ring-chart span {
  transform: rotate(45deg);
}

.ats-stats {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  width: 100%;
}

.status { margin-right: 8px; font-size: 1rem; }
.status.green { color: #10B981; }
.status.yellow { color: #F59E0B; }

.bento-style {
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.bento-sm {
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 2rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  transition: 0.3s;
}

.bento-sm:hover {
  background: rgba(30, 41, 59, 0.8);
  color: var(--text-main);
  transform: translateY(-5px);
}

.bento-sm.wide { grid-column: span 2; }

@media (max-width: 900px) {
  .feature-block {
    grid-template-columns: 1fr;
    gap: 4rem;
    grid-template-areas: "text" "visual" !important;
  }
}
</style>
