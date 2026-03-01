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
              <div class="repeater-wrapper">
                 <div v-for="(exp, index) in form.experience" :key="index" class="repeater-item">
                    <div class="repeater-header">
                       <h4>Experience {{ index + 1 }}</h4>
                       <button type="button" class="btn-remove" @click="removeExperience(index)" v-if="form.experience.length > 1">×</button>
                    </div>
                    <div class="input-grid">
                       <div class="input-group">
                          <label>Job Title</label>
                          <input v-model="exp.title" type="text" placeholder="Senior Developer" />
                       </div>
                       <div class="input-group">
                          <label>Company</label>
                          <input v-model="exp.company" type="text" placeholder="TechCorp Inc." />
                       </div>
                    </div>
                    <div class="input-grid">
                       <div class="input-group">
                          <label>Start Date</label>
                          <input v-model="exp.startDate" type="text" placeholder="Jan 2020" />
                       </div>
                       <div class="input-group">
                          <label>End Date</label>
                          <input v-model="exp.endDate" type="text" placeholder="Present" />
                       </div>
                    </div>
                    <div class="input-group">
                       <label>Description & Achievements</label>
                       <textarea v-model="exp.description" placeholder="• Led development of... &#10;• Increased performance by 40%..." rows="4"></textarea>
                    </div>
                 </div>
                 <button type="button" class="btn-add-repeater" @click="addExperience">+ Add Experience</button>
              </div>
            </div>
            
            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">04</span> <h3>Education Stack</h3>
              </div>
              <div class="repeater-wrapper">
                 <div v-for="(edu, index) in form.education" :key="index" class="repeater-item">
                    <div class="repeater-header">
                       <h4>Education {{ index + 1 }}</h4>
                       <button type="button" class="btn-remove" @click="removeEducation(index)" v-if="form.education.length > 1">×</button>
                    </div>
                    <div class="input-grid">
                       <div class="input-group">
                          <label>Degree / Certificate</label>
                          <input v-model="edu.degree" type="text" placeholder="B.S. Computer Science" />
                       </div>
                       <div class="input-group">
                          <label>Institution</label>
                          <input v-model="edu.school" type="text" placeholder="University of Technology" />
                       </div>
                    </div>
                    <div class="input-grid">
                       <div class="input-group">
                          <label>Start Date</label>
                          <input v-model="edu.startDate" type="text" placeholder="2016" />
                       </div>
                       <div class="input-group">
                          <label>End Date</label>
                          <input v-model="edu.endDate" type="text" placeholder="2020" />
                       </div>
                    </div>
                 </div>
                 <button type="button" class="btn-add-repeater" @click="addEducation">+ Add Education</button>
              </div>
            </div>

            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">05</span> <h3>Skill Calibration</h3>
              </div>
               <div class="input-group">
                  <input v-model="skillsInput" type="text" placeholder="React, Python, AWS, Design Ops (comma separated)" />
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
              <!-- Classic / Standard Layout (Template 1, 4, etc) -->
              <div v-if="['1', '3', '4', '8'].includes(templateId)" class="template-layout-classic">
                 <div class="canvas-header">
                    <h1>{{ form.name || 'Your Name' }}</h1>
                    <p class="canvas-title">{{ form.title || 'Professional Title' }}</p>
                    <div class="canvas-contact">
                       <span v-if="form.email">{{ form.email }}</span>
                       <span v-if="form.email && form.location"> | </span>
                       <span v-if="form.location">{{ form.location }}</span>
                    </div>
                 </div>
                 
                 <div class="canvas-section" v-if="form.objective">
                    <h3>Objective</h3>
                    <p class="canvas-text">{{ form.objective }}</p>
                 </div>

                 <div class="canvas-section" v-if="form.experience && form.experience.some(e => e.title || e.company)">
                    <h3>Experience</h3>
                    <div v-for="(exp, index) in form.experience" :key="'exp'+index" class="cv-item">
                       <div v-if="exp.title || exp.company" class="cv-item-header">
                          <span class="cv-role">{{ exp.title || 'Job Title' }}</span>
                          <span class="cv-company"><span v-if="exp.title && exp.company"> at </span>{{ exp.company }}</span>
                          <span class="cv-dates">{{ exp.startDate }} <span v-if="exp.startDate && exp.endDate">-</span> {{ exp.endDate }}</span>
                       </div>
                       <div class="canvas-text cv-desc" v-html="formatDescription(exp.description)"></div>
                    </div>
                 </div>

                 <div class="canvas-section" v-if="form.education && form.education.some(e => e.degree || e.school)">
                    <h3>Education</h3>
                    <div v-for="(edu, index) in form.education" :key="'edu'+index" class="cv-item">
                       <div v-if="edu.degree || edu.school" class="cv-item-header">
                          <span class="cv-role">{{ edu.degree || 'Degree' }}</span>
                          <span class="cv-company"><span v-if="edu.degree && edu.school">, </span>{{ edu.school }}</span>
                          <span class="cv-dates">{{ edu.startDate }} <span v-if="edu.startDate && edu.endDate">-</span> {{ edu.endDate }}</span>
                       </div>
                    </div>
                 </div>

                 <div class="canvas-section" v-if="form.skills && form.skills.length > 0">
                    <h3>Skills</h3>
                    <div class="canvas-skills">
                       <span v-for="skill in form.skills" :key="skill" class="skill-pill">{{ skill }}</span>
                    </div>
                 </div>
              </div>

              <!-- Modern / Split Column Layout (Template 2, 5, etc) -->
              <div v-else class="template-layout-modern">
                 <div class="modern-left">
                    <div class="m-header">
                       <h1>{{ form.name || 'Your Name' }}</h1>
                       <h2>{{ form.title || 'Professional Title' }}</h2>
                    </div>

                    <div class="m-section" v-if="form.email || form.location">
                       <h3>Contact</h3>
                       <div class="m-contact-item" v-if="form.email">{{ form.email }}</div>
                       <div class="m-contact-item" v-if="form.location">{{ form.location }}</div>
                    </div>

                    <div class="m-section" v-if="form.skills && form.skills.length > 0">
                       <h3>Skills</h3>
                       <ul class="m-skills-list">
                          <li v-for="skill in form.skills" :key="'m'+skill">{{ skill }}</li>
                       </ul>
                    </div>
                    
                    <div class="m-section" v-if="form.education && form.education.some(e => e.degree || e.school)">
                       <h3>Education</h3>
                       <div v-for="(edu, index) in form.education" :key="'medu'+index" class="m-edu-item">
                          <div class="m-edu-deg">{{ edu.degree || 'Degree' }}</div>
                          <div class="m-edu-sch">{{ edu.school || 'Institution' }}</div>
                          <div class="m-edu-date">{{ edu.startDate }} <span v-if="edu.startDate && edu.endDate">-</span> {{ edu.endDate }}</div>
                       </div>
                    </div>
                 </div>
                 
                 <div class="modern-right">
                    <div class="m-section" v-if="form.objective">
                       <h3>Profile</h3>
                       <p class="m-text">{{ form.objective }}</p>
                    </div>

                    <div class="m-section" v-if="form.experience && form.experience.some(e => e.title || e.company)">
                       <h3>Work Experience</h3>
                       <div v-for="(exp, index) in form.experience" :key="'mexp'+index" class="m-exp-item">
                          <div class="m-exp-header">
                             <div class="m-exp-title">{{ exp.title || 'Job Title' }}</div>
                             <div class="m-exp-date">{{ exp.startDate }} <span v-if="exp.startDate && exp.endDate">-</span> {{ exp.endDate }}</div>
                          </div>
                          <div class="m-exp-company">{{ exp.company }}</div>
                          <div class="m-text m-exp-desc" v-html="formatDescription(exp.description)"></div>
                       </div>
                    </div>
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
import { store } from '@/store.js';

export default {
  name: 'FillResume',
  data() {
    return {
      templateId: this.$route.query.template || '1',
      form: {
        name: '',
        title: '',
        email: '',
        location: '',
        objective: '',
        experience: [
           { title: '', company: '', startDate: '', endDate: '', description: '' }
        ],
        education: [
           { degree: '', school: '', startDate: '', endDate: '' }
        ],
        skills: []
      },
      skillsInput: '',
      isGenerating: false,
      isAutoFilled: false
    };
  },
  watch: {
     skillsInput(newVal) {
        this.form.skills = newVal.split(',').map(s => s.trim()).filter(s => s);
     }
  },
  mounted() {
    this.executeAnimations();

    // Auto-fill from global user store if logged in
    if (store.user) {
      let filledCount = 0;
      if (store.user.fullName) { this.form.name = store.user.fullName; filledCount++; }
      if (store.user.email) { this.form.email = store.user.email; filledCount++; }
      if (store.user.location) { this.form.location = store.user.location; filledCount++; } 
      else if (store.user.address) { this.form.location = store.user.address; filledCount++; }
      if (store.user.professionalTitle) { this.form.title = store.user.professionalTitle; filledCount++; }

      if (filledCount > 0) this.isAutoFilled = true;
    }
  },
  methods: {
    addExperience() {
       this.form.experience.push({ title: '', company: '', startDate: '', endDate: '', description: '' });
    },
    removeExperience(index) {
       this.form.experience.splice(index, 1);
    },
    addEducation() {
       this.form.education.push({ degree: '', school: '', startDate: '', endDate: '' });
    },
    removeEducation(index) {
       this.form.education.splice(index, 1);
    },
    formatDescription(text) {
       if (!text) return '';
       // Convert newlines to breaks for simple formatting, or handle bullets
       return text.replace(/\n/g, '<br/>');
    },
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

/* Repeater Styles */
.repeater-wrapper { display: flex; flex-direction: column; gap: 1.5rem; }
.repeater-item {
  background: rgba(15, 23, 42, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 1.5rem;
  position: relative;
}
.repeater-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.repeater-header h4 { font-size: 0.9rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.05em; }
.btn-remove { background: rgba(239, 68, 68, 0.1); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.2); width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; cursor: pointer; transition: all 0.2s; }
.btn-remove:hover { background: rgba(239, 68, 68, 0.2); color: #fff; }

.btn-add-repeater {
  background: transparent;
  border: 1px dashed rgba(99, 102, 241, 0.4);
  color: #818CF8;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
}
.btn-add-repeater:hover { background: rgba(99, 102, 241, 0.1); border-style: solid; box-shadow: 0 0 15px rgba(99, 102, 241, 0.2); }

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
  box-shadow: 0 40px 80px -20px rgba(0,0,0,0.4);
  transform-origin: top center;
  overflow: hidden;
}

/* --- CLASSIC TEMPLATE (Padding controlled inside wrapper) --- */
.template-layout-classic { padding: 60px; }
.canvas-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.02em; }
.canvas-title { font-size: 18px; color: #6366F1; font-weight: 700; margin-bottom: 12px; }
.canvas-contact { font-size: 14px; color: #64748B; margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px; }

.canvas-section { margin-bottom: 30px; }
.canvas-section h3 { font-size: 14px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 900; color: #111827; margin-bottom: 12px; border-bottom: 2px solid #111827; padding-bottom: 4px; width: fit-content; }
.canvas-text { font-size: 14px; line-height: 1.6; color: #334155; }

.cv-item { margin-bottom: 16px; page-break-inside: avoid; }
.cv-item-header { display: flex; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px; }
.cv-role { font-weight: 800; font-size: 15px; color: #111827; margin-right: 6px; }
.cv-company { font-weight: 600; font-size: 14px; color: #475569; }
.cv-dates { margin-left: auto; font-size: 13px; font-weight: 600; color: #64748B; background: #F8FAFC; padding: 2px 8px; border-radius: 4px; }
.cv-desc { margin-top: 4px; }

.canvas-skills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.skill-pill { background: #F1F5F9; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; color: #475569; border: 1px solid #E2E8F0; }


/* --- MODERN SPLIT TEMPLATE --- */
.template-layout-modern {
  display: flex;
  height: 100%;
  min-height: 297mm;
}
.modern-left {
  width: 32%;
  background: #1E293B; /* Slate 800 */
  color: #F8FAFC;
  padding: 40px 30px;
}
.modern-right {
  width: 68%;
  background: #FFFFFF;
  padding: 40px 40px;
}

.m-header { margin-bottom: 40px; }
.m-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; line-height: 1.1; margin-bottom: 8px; color: #fff; }
.m-header h2 { font-size: 16px; font-weight: 400; color: #94A3B8; }

.m-section { margin-bottom: 35px; }
.m-section h3 { font-size: 15px; text-transform: uppercase; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 16px; }
.modern-left .m-section h3 { color: #fff; border-bottom: 2px solid #334155; padding-bottom: 6px; }
.modern-right .m-section h3 { color: #0F172A; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; }

.m-contact-item { font-size: 13px; color: #CBD5E1; margin-bottom: 8px; word-break: break-all; }
.m-skills-list { list-style: none; padding: 0; margin: 0; }
.m-skills-list li { font-size: 13px; color: #CBD5E1; margin-bottom: 6px; position: relative; padding-left: 12px; }
.m-skills-list li::before { content: '•'; position: absolute; left: 0; color: #6366F1; }

.m-edu-item { margin-bottom: 16px; }
.m-edu-deg { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.m-edu-sch { font-size: 13px; color: #94A3B8; margin-bottom: 4px; }
.m-edu-date { font-size: 12px; color: #64748B; }

.m-text { font-size: 14px; line-height: 1.6; color: #334155; }
.m-exp-item { margin-bottom: 24px; }
.m-exp-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }
.m-exp-title { font-size: 16px; font-weight: 700; color: #0F172A; }
.m-exp-date { font-size: 13px; font-weight: 600; color: #64748B; text-align: right; }
.m-exp-company { font-size: 14px; font-weight: 600; color: #6366F1; margin-bottom: 8px; }
.m-exp-desc { margin-top: 8px; }

@media (max-width: 1200px) {
  .workspace-main { flex-direction: column; overflow-y: auto; }
  .editor-panel, .preview-panel { width: 100%; height: auto; }
  .resume-canvas { transform: scale(0.8); }
}
</style>
