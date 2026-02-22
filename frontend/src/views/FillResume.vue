<template>
  <div class="workspace-wrapper">
    <!-- Atmosphere Layer -->
    <div class="atmosphere">
      <div class="aura aura-1"></div>
      <div class="aura aura-2"></div>
    </div>

    <!-- Persistent App Header -->
    <nav class="app-header">
      <div class="container-fluid header-content">
        <div class="header-left">
          <a href="/Dashboard" class="btn-icon-ghost">
             <span class="icon">◂</span> Dashboard
          </a>
          <span class="divider"></span>
          <div class="document-info">
            <span class="doc-badge">Draft</span>
            <span class="doc-name">Untitled Resume v1</span>
          </div>
        </div>
        <div class="header-right">
          <div class="status-indicator">
             <span class="pulse"></span> Saved to cloud
          </div>
          <button class="btn-share-ghost">Share</button>
          <button class="btn-export-saas" @click="generateResume">Export PDF</button>
        </div>
      </div>
    </nav>

    <!-- Main Workspace: IDE-style -->
    <main class="workspace-main">
      <!-- Left: Editor Panel -->
      <section class="editor-panel">
        <div class="panel-scroll">
          <div class="editor-header reveal-up">
            <h2>Design Workspace</h2>
            <p>Engineer your professional narrative with AI precision.</p>
          </div>

          <form @submit.prevent="generateResume" class="saas-form">
            <!-- Basic Info Section -->
            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">01</span> <h3>Identity Hub</h3>
              </div>
              <div class="input-grid">
                <div class="input-group">
                  <label>Full Name</label>
                  <input v-model="form.name" type="text" placeholder="Johnathan Doe" required />
                </div>
                <div class="input-group">
                  <label>Professional Title</label>
                  <input v-model="form.title" type="text" placeholder="Principal Software Engineer" required />
                </div>
              </div>
              <div class="input-grid">
                <div class="input-group">
                  <label>Email</label>
                  <input v-model="form.email" type="email" placeholder="john@company.com" required />
                </div>
                <div class="input-group">
                  <label>Location</label>
                  <input v-model="form.location" type="text" placeholder="San Francisco, CA" required />
                </div>
              </div>
            </div>

            <!-- Deep Optimization Sections -->
            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">02</span> <h3>Career Objective</h3>
              </div>
              <div class="input-group">
                <textarea v-model="form.objective" placeholder="Translate your career goals into high-impact narrative..." rows="3"></textarea>
              </div>
            </div>

            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">03</span> <h3>Experience Stack</h3>
              </div>
              <div class="input-group">
                <div class="control-box">
                  <textarea v-model="experience" placeholder="Describe your missions, achievements, and impact..." rows="6"></textarea>
                  <div class="ai-helper">
                    <span>✨ AI Optimize</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">04</span> <h3>Skill Calibration</h3>
              </div>
               <div class="input-group">
                  <input v-model="skills" type="text" placeholder="React, Python, AWS, Design Ops (comma separated)" />
               </div>
            </div>

            <div class="workspace-actions">
               <p class="data-usage">Transmitting via 256-bit encrypted channel</p>
            </div>
          </form>
        </div>
      </section>

      <!-- Right: Live Preview Panel -->
      <section class="preview-panel">
        <div class="preview-chrome">
           <div class="zoom-controls">
              <span>View: 100%</span>
           </div>
        </div>
        <div class="preview-canvas-container">
           <div class="resume-canvas reveal-zoom">
              <!-- Live Preview Content -->
              <div class="canvas-header">
                 <h1>{{ form.name || 'Your Name' }}</h1>
                 <p class="canvas-title">{{ form.title || 'Professional Title' }}</p>
                 <div class="canvas-contact">
                    <span>{{ form.email || 'Email' }}</span> | <span>{{ form.location || 'Location' }}</span>
                 </div>
              </div>
              
              <div class="canvas-section" v-if="form.objective">
                 <h3>Objective</h3>
                 <p>{{ form.objective }}</p>
              </div>

              <div class="canvas-section">
                 <h3>Experience</h3>
                 <div class="canvas-text">{{ experience || 'Detailed achievements will appear here...' }}</div>
              </div>

              <div class="canvas-section">
                 <h3>Skills</h3>
                 <div class="canvas-skills">
                    <span v-for="skill in skillsArr" :key="skill" class="skill-pill">{{ skill }}</span>
                 </div>
              </div>
           </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import { gsap } from 'gsap';

export default {
  name: 'FillResume',
  data() {
    return {
      templateId: this.$route.params.templateId,
      form: {
        name: '',
        title: '',
        email: '',
        location: '',
        objective: ''
      },
      experience: '',
      skills: '',
      isGenerating: false
    };
  },
  computed: {
     skillsArr() {
        return this.skills ? this.skills.split(',').map(s => s.trim()).filter(s => s) : [];
     }
  },
  mounted() {
    this.executeAnimations();
  },
  methods: {
    executeAnimations() {
       gsap.from('.reveal-up', {
         y: 20,
         opacity: 0,
         duration: 0.8,
         stagger: 0.1,
         ease: 'power3.out'
       });
       gsap.from('.preview-panel', {
          x: 40,
          opacity: 0,
          duration: 1.2,
          ease: 'expo.out'
       });
    },
    async generateResume() {
      this.isGenerating = true;
      // Mock transmission
      setTimeout(() => {
        alert('Generation initiated. Transmitting to high-orbit render server...');
        this.isGenerating = false;
        this.$router.push('/Dashboard');
      }, 2000);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.workspace-wrapper {
  height: 100vh;
  background-color: #030712;
  color: #F8FAFC;
  font-family: 'Outfit', sans-serif;
  overflow: hidden;
  display: flex;
  flex-direction: column;
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

.aura { position: absolute; border-radius: 50%; filter: blur(120px); opacity: 0.1; }
.aura-1 { width: 600px; height: 600px; background: #6366F1; top: -10%; left: -10%; }
.aura-2 { width: 400px; height: 400px; background: #EC4899; bottom: 10%; right: 10%; }

/* App Header Chrome */
.app-header {
  height: 64px;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  z-index: 100;
}

.header-content {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1.5rem;
}

.header-left { display: flex; align-items: center; gap: 1.5rem; }
.btn-icon-ghost { color: #94A3B8; text-decoration: none; font-size: 0.9rem; font-weight: 500; display: flex; align-items: center; gap: 8px; transition: color 0.3s; }
.btn-icon-ghost:hover { color: #fff; }
.divider { width: 1px; height: 24px; background: rgba(255,255,255,0.1); }

.document-info { display: flex; align-items: center; gap: 12px; }
.doc-badge { padding: 3px 8px; background: rgba(253, 186, 116, 0.1); border: 1px solid rgba(253, 186, 116, 0.2); border-radius: 4px; font-size: 0.7rem; font-weight: 700; color: #FDBA74; text-transform: uppercase; }
.doc-name { font-weight: 600; font-size: 0.95rem; }

.header-right { display: flex; align-items: center; gap: 1.5rem; }
.status-indicator { font-size: 0.8rem; color: #64748B; display: flex; align-items: center; gap: 8px; }
.pulse { width: 6px; height: 6px; background: #10B981; border-radius: 50%; }

.btn-share-ghost { background: transparent; border: 1px solid rgba(255,255,255,0.1); color: #fff; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer; }
.btn-export-saas { background: #fff; color: #030712; border: none; padding: 0.5rem 1.2rem; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: transform 0.2s; }
.btn-export-saas:hover { transform: scale(1.02); }

/* Main Workspace */
.workspace-main {
  flex: 1;
  display: flex;
  overflow: hidden;
  position: relative;
  z-index: 10;
}

/* Editor Panel */
.editor-panel {
  width: 45%;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  background: rgba(15, 23, 42, 0.2);
  display: flex;
  flex-direction: column;
}

.panel-scroll {
  flex: 1;
  overflow-y: auto;
  padding: 4rem;
}

.editor-header { margin-bottom: 4rem; }
.editor-header h2 { font-family: 'Space Grotesk', sans-serif; font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem; }
.editor-header p { color: #94A3B8; font-size: 1.1rem; }

.form-section { margin-bottom: 4rem; }
.section-title { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.section-title .num { font-size: 0.8rem; font-weight: 800; color: #6366F1; opacity: 0.5; }
.section-title h3 { font-size: 1.2rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; }

.input-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem; }
.input-group { display: flex; flex-direction: column; gap: 10px; }
.input-group label { font-size: 0.85rem; font-weight: 600; color: #475569; }
.input-group input, .input-group textarea {
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 1rem 1.2rem;
  color: #fff;
  font-family: inherit;
  font-size: 1rem;
  transition: all 0.3s;
}
.input-group input:focus, .input-group textarea:focus {
  outline: none;
  border-color: rgba(99, 102, 241, 0.4);
  background: rgba(15, 23, 42, 0.8);
}

.control-box { position: relative; }
.ai-helper { position: absolute; bottom: 1rem; right: 1rem; background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.2); padding: 5px 12px; border-radius: 99px; font-size: 0.75rem; font-weight: 700; color: #818CF8; cursor: pointer; transition: all 0.3s; }
.ai-helper:hover { background: rgba(99, 102, 241, 0.2); transform: scale(1.05); }

.data-usage { font-size: 0.8rem; color: #475569; margin-top: 2rem; }

/* Preview Panel */
.preview-panel {
  flex: 1;
  background: #0F172A;
  position: relative;
  display: flex;
  flex-direction: column;
}

.preview-chrome { padding: 12px 2rem; background: rgba(255,255,255,0.02); display: flex; justify-content: flex-end; }
.zoom-controls { font-size: 0.75rem; color: #475569; font-weight: 600; }

.preview-canvas-container {
  flex: 1;
  overflow: auto;
  padding: 4rem;
  background: #111827;
  display: flex;
  justify-content: center;
}

.resume-canvas {
  width: 210mm;
  min-height: 297mm;
  background: #fff;
  color: #111827;
  padding: 60px;
  box-shadow: 0 40px 80px -20px rgba(0,0,0,0.4);
  transform-origin: top center;
}

.canvas-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.02em; }
.canvas-title { font-size: 18px; color: #6366F1; font-weight: 700; margin-bottom: 12px; }
.canvas-contact { font-size: 14px; color: #64748B; margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px; }

.canvas-section { margin-bottom: 30px; }
.canvas-section h3 { font-size: 14px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 900; color: #111827; margin-bottom: 12px; border-bottom: 2px solid #111827; padding-bottom: 4px; width: fit-content; }
.canvas-text { font-size: 14px; line-height: 1.6; color: #334155; }

.canvas-skills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.skill-pill { background: #F1F5F9; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; color: #475569; border: 1px solid #E2E8F0; }

@media (max-width: 1200px) {
  .workspace-main { flex-direction: column; overflow-y: auto; }
  .editor-panel, .preview-panel { width: 100%; height: auto; }
  .resume-canvas { transform: scale(0.8); }
}
</style>
