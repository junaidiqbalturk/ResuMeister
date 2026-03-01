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
             <span class="pulse"></span> {{ syncStatus }}
          </div>
          <button class="btn-share-ghost" @click.prevent="saveToCloud">Save Resume</button>
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
                <div class="input-group floating">
                  <input v-model="form.name" type="text" id="fname" placeholder=" " required />
                  <label for="fname">Full Name</label>
                </div>
                <div class="input-group floating">
                  <input v-model="form.title" type="text" id="ftitle" placeholder=" " required />
                  <label for="ftitle">Professional Title</label>
                </div>
              </div>
              <div class="input-grid">
                <div class="input-group floating">
                  <input v-model="form.email" type="email" id="femail" placeholder=" " required />
                  <label for="femail">Email Address</label>
                </div>
                <div class="input-group floating">
                  <input v-model="form.phone" type="text" id="fphone" placeholder=" " />
                  <label for="fphone">Phone Number</label>
                </div>
              </div>
              <div class="input-grid">
                <div class="input-group floating">
                  <input v-model="form.location" type="text" id="floc" placeholder=" " required />
                  <label for="floc">Location</label>
                </div>
                <div class="input-group floating">
                  <input v-model="form.linkedin" type="text" id="flinkedin" placeholder=" " />
                  <label for="flinkedin">LinkedIn Username</label>
                </div>
              </div>
              <div class="input-group floating">
                 <input v-model="form.github" type="text" id="fgithub" placeholder=" " />
                 <label for="fgithub">GitHub / Portfolio Username</label>
              </div>
            </div>

            <!-- Deep Optimization Sections -->
            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">02</span> <h3>Career Objective</h3>
              </div>
              <div class="input-group floating">
                <textarea v-model="form.objective" id="fobj" placeholder=" " rows="3"></textarea>
                <label for="fobj">Translate your career goals into a high-impact narrative...</label>
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
                       <div class="input-group floating">
                          <input v-model="exp.title" :id="'extitle'+index" type="text" placeholder=" " />
                          <label :for="'extitle'+index">Job Title</label>
                       </div>
                       <div class="input-group floating">
                          <input v-model="exp.company" :id="'excomp'+index" type="text" placeholder=" " />
                          <label :for="'excomp'+index">Company</label>
                       </div>
                    </div>
                    <div class="input-grid">
                       <div class="input-group floating">
                          <input v-model="exp.startDate" :id="'exstart'+index" type="text" placeholder=" " />
                          <label :for="'exstart'+index">Start Date (e.g. Jan 2020)</label>
                       </div>
                       <div class="input-group floating">
                          <input v-model="exp.endDate" :id="'exend'+index" type="text" placeholder=" " />
                          <label :for="'exend'+index">End Date (e.g. Present)</label>
                       </div>
                    </div>
                    <div class="input-group floating">
                       <textarea v-model="exp.description" :id="'exdesc'+index" placeholder=" " rows="4"></textarea>
                       <label :for="'exdesc'+index">Description & Achievements</label>
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
                       <div class="input-group floating">
                          <input v-model="edu.degree" :id="'eddeg'+index" type="text" placeholder=" " />
                          <label :for="'eddeg'+index">Degree / Certificate</label>
                       </div>
                       <div class="input-group floating">
                          <input v-model="edu.school" :id="'edsch'+index" type="text" placeholder=" " />
                          <label :for="'edsch'+index">Institution</label>
                       </div>
                    </div>
                    <div class="input-grid">
                       <div class="input-group floating">
                          <input v-model="edu.startDate" :id="'edstart'+index" type="text" placeholder=" " />
                          <label :for="'edstart'+index">Start Date</label>
                       </div>
                       <div class="input-group floating">
                          <input v-model="edu.endDate" :id="'edend'+index" type="text" placeholder=" " />
                          <label :for="'edend'+index">End Date</label>
                       </div>
                    </div>
                 </div>
                 <button type="button" class="btn-add-repeater" @click="addEducation">+ Add Education</button>
              </div>
            </div>

            <div class="form-section reveal-up">
              <div class="section-title">
                <span class="num">05</span> <h3>Core Competencies</h3>
              </div>
               <div class="input-group floating">
                  <input v-model="skillsInput" id="fskills" type="text" placeholder=" " />
                  <label for="fskills">Skills (comma separated, e.g. React, Python)</label>
               </div>
               <div class="input-group floating" style="margin-top: 1rem;">
                  <input v-model="certsInput" id="fcerts" type="text" placeholder=" " />
                  <label for="fcerts">Certifications (comma separated)</label>
               </div>
               <div class="input-grid" style="margin-top: 1rem;">
                 <div class="input-group floating">
                    <input v-model="langsInput" id="flangs" type="text" placeholder=" " />
                    <label for="flangs">Languages (comma separated)</label>
                 </div>
                 <div class="input-group floating">
                    <input v-model="interestsInput" id="finterests" type="text" placeholder=" " />
                    <label for="finterests">Interests (comma separated)</label>
                 </div>
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
              <div v-if="['1', '4', '8'].includes(templateId)" class="template-layout-classic">
                 <div class="canvas-header">
                    <h1>{{ form.name || 'Your Name' }}</h1>
                    <p class="canvas-title">{{ form.title || 'Professional Title' }}</p>
                    <div class="canvas-contact">
                       <span v-if="form.email">{{ form.email }}</span>
                       <span v-if="form.email && form.phone"> | </span>
                       <span v-if="form.phone">{{ form.phone }}</span>
                       <span v-if="(form.email || form.phone) && form.location"> | </span>
                       <span v-if="form.location">{{ form.location }}</span>
                       <span v-if="(form.email || form.phone || form.location) && form.linkedin"> | </span>
                       <span v-if="form.linkedin">{{ String(form.linkedin).replace('https://', '').replace('www.', '') }}</span>
                       <span v-if="(form.email || form.phone || form.location || form.linkedin) && form.github"> | </span>
                       <span v-if="form.github">{{ String(form.github).replace('https://', '').replace('www.', '') }}</span>
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

              <!-- Professional / Graphic Column Layout (Template 3) -->
              <div v-else-if="templateId === '3'" class="template-layout-professional">
                  <div class="prof-top">
                     <!-- Slate block on the top-left edge -->
                     <div class="slate-edge-block"></div>
                     <div class="prof-top-left">
                        <h1>{{ form.name || 'John Doe' }}</h1>
                        <h2>{{ form.title || 'Software Engineer' }}</h2>
                        <p class="prof-summary">{{ form.objective || 'Professional Software Engineer with 3 years of Professional web and Mobile Application Development.' }}</p>
                     </div>
                     <div class="prof-top-center">
                        <div class="prof-avatar">
                           <img :src="'https://ui-avatars.com/api/?name=' + (form.name || 'John+Doe') + '&background=4A7C82&color=fff&size=200'" alt="Avatar"/>
                        </div>
                     </div>
                     <div class="prof-top-right">
                        <div class="prof-contact">
                           <div v-if="form.email">{{ form.email }} <span class="icon">✉</span></div>
                           <div v-if="form.phone">{{ form.phone }} <span class="icon">📱</span></div>
                           <div v-if="form.location">{{ form.location }} <span class="icon">📍</span></div>
                           <div v-if="form.linkedin">{{ String(form.linkedin).replace('https://', '') }} <span class="icon">in</span></div>
                           <div v-if="form.github">{{ String(form.github).replace('https://', '') }} <span class="icon">gh</span></div>
                        </div>
                     </div>
                  </div>
                  
                  <hr class="prof-divider" />
                  
                  <div class="prof-main">
                     <div class="prof-left">
                        <div class="prof-section">
                           <h3 class="prof-section-title">WORK EXPERIENCE</h3>
                           <div v-for="(exp, index) in (form.experience && form.experience.some(e => e.title || e.company) ? form.experience : [{title: 'Senior Software Engineer', company: 'ABC Tech Holding', startDate: '08/2019', endDate: 'Aug ', location: 'Karachi, Pakistan', description: '<ul><li>Design, code and maintain the Oracle/Java Systems based on Established standards.</li><li>Develop Oracle Reports, forms, SQL, PL/SQL & procedures.</li></ul>'}, {title: 'Software Engineer', company: 'Universal Software', startDate: '12/2018', endDate: '08/2019', location: 'Karachi, Pakistan', description: '<ul><li>Develop tools and applications by producing clean, efficient code.</li></ul>'}])" :key="'pexp'+index" class="prof-item">
                              <div class="teal-marker"></div>
                              <div class="prof-item-header">
                                 <h4 class="prof-role">{{ exp.title || 'Job Title' }}</h4>
                                 <h5 class="prof-company">{{ exp.company || 'Company' }}</h5>
                                 <div class="prof-dates-loc">
                                    <span class="prof-dates">{{ exp.startDate }} <span v-if="exp.startDate && exp.endDate">-</span> {{ exp.endDate }}</span>
                                    <span class="prof-loc">{{ exp.location || 'Location' }}</span>
                                 </div>
                              </div>
                              <div class="prof-desc-label" v-if="exp.description">Achievements/Tasks</div>
                              <div class="prof-desc teal-bullets" v-html="formatDescription(exp.description)"></div>
                           </div>
                        </div>
                        
                        <div class="prof-section">
                           <h3 class="prof-section-title">EDUCATION</h3>
                           <div v-for="(edu, index) in (form.education && form.education.some(e => e.degree || e.school) ? form.education : [{degree: 'Bachelors in Electrical Engineering', school: 'University Of Washington DC, United States', startDate: '01/2013', endDate: '09/2017'}])" :key="'pedu'+index" class="prof-item">
                              <div class="teal-marker" style="height: 18px; top: 5px;"></div>
                              <h4 class="prof-role">{{ edu.degree || 'Degree' }}</h4>
                              <h5 class="prof-company">{{ edu.school || 'School' }}</h5>
                              <div class="prof-dates-loc">
                                 <span class="prof-dates">{{ edu.startDate }} <span v-if="edu.startDate && edu.endDate">-</span> {{ edu.endDate }}</span>
                              </div>
                           </div>
                        </div>
                     </div>
                     
                     <div class="prof-right">
                        <div class="prof-section">
                           <h3 class="prof-section-title">SKILLS</h3>
                           <div class="prof-skills-grid">
                              <span v-for="skill in (form.skills.length ? form.skills : ['Data Analysis', 'Data Visualization', 'Firebase', 'Java Spring', 'Java Swing', 'Python'])" :key="'pskill'+skill" class="prof-skill-pill">{{ skill }}</span>
                           </div>
                        </div>
                        
                        <div class="prof-section">
                           <h3 class="prof-section-title">CERTIFICATIONS</h3>
                           <div v-for="(cert, index) in (form.certifications.length ? form.certifications : [{name: 'R Programming', issuer: 'John Hopkins University'}, {name: 'Tools For Data Science', issuer: 'IBM'}])" :key="'pcert'+index" class="prof-cert-item">
                              <h4 class="prof-cert-name">{{ cert.name || 'Certification' }}</h4>
                              <p class="prof-cert-desc">{{ cert.issuer || 'Issuer' }}</p>
                           </div>
                        </div>
                        
                        <div class="prof-section">
                           <h3 class="prof-section-title">LANGUAGES</h3>
                           <div v-for="(lang, index) in (form.languages.length ? form.languages : [{name: 'English', level: 5}, {name: 'Urdu', level: 4}, {name: 'Punjabi', level: 4}])" :key="'plang'+index" class="prof-lang-item">
                              <span class="prof-lang-name">{{ lang.name || 'Language' }}</span>
                              <div class="prof-lang-dots">
                                 <span v-for="n in 5" :key="n" class="lang-dot" :class="{'filled': n <= (lang.level || 5)}"></span>
                              </div>
                           </div>
                        </div>
                        
                        <div class="prof-section">
                           <h3 class="prof-section-title">INTERESTS</h3>
                           <div class="prof-interests-grid">
                              <span v-for="interest in (form.interests.length ? form.interests : ['Photography', 'Travelling', 'Arts', 'Writing'])" :key="'pint'+interest" class="prof-interest-pill">{{ interest }}</span>
                           </div>
                        </div>
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

                    <div class="m-section" v-if="form.email || form.phone || form.location || form.linkedin || form.github">
                       <h3>Contact</h3>
                       <div class="m-contact-item" v-if="form.email">{{ form.email }}</div>
                       <div class="m-contact-item" v-if="form.phone">{{ form.phone }}</div>
                       <div class="m-contact-item" v-if="form.location">{{ form.location }}</div>
                       <div class="m-contact-item" v-if="form.linkedin">{{ String(form.linkedin).replace('https://', '') }}</div>
                       <div class="m-contact-item" v-if="form.github">{{ String(form.github).replace('https://', '') }}</div>
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
import axios from 'axios';
import { debounce } from 'lodash'; // Using lodash or a custom debounce

export default {
  name: 'FillResume',
  data() {
    return {
      templateId: this.$route.query.template || '1',
      resumeId: this.$route.query.id || null, // Track existing resume ID
      form: {
        name: '',
        title: '',
        email: '',
        phone: '',
        location: '',
        linkedin: '',
        github: '',
        objective: '',
        experience: [
           { title: '', company: '', location: '', startDate: '', endDate: '', description: '' }
        ],
        education: [
           { degree: '', school: '', startDate: '', endDate: '' }
        ],
        skills: [],
        certifications: [],
        languages: [],
        interests: []
      },
      skillsInput: '',
      certsInput: '',
      langsInput: '',
      interestsInput: '',
      isGenerating: false,
      isAutoFilled: false,
      syncStatus: 'Saved to cloud' // UI Feedback
    };
  },
  watch: {
     skillsInput(newVal) {
        this.form.skills = newVal.split(',').map(s => s.trim()).filter(s => s);
        this.debouncedSave();
     },
     certsInput(newVal) {
        this.form.certifications = newVal.split(',').map(s => ({ name: s.trim() })).filter(s => s.name);
        this.debouncedSave();
     },
     langsInput(newVal) {
        this.form.languages = newVal.split(',').map(s => ({ name: s.trim(), level: 5 })).filter(s => s.name);
        this.debouncedSave();
     },
     interestsInput(newVal) {
        this.form.interests = newVal.split(',').map(s => s.trim()).filter(s => s);
        this.debouncedSave();
     },
     form: {
       handler() {
         this.debouncedSave();
       },
       deep: true
     }
  },
  created() {
     // Create a debounced save function
     this.debouncedSave = this.createDebounce(() => {
        this.saveToCloud();
     }, 1500);
  },
  async mounted() {
    this.executeAnimations();

    // Load existing resume or auto-fill
    if (this.resumeId) {
       await this.loadResume();
    } else if (store.user) {
      this.autoFillFromProfile();
    }
  },
  methods: {
    createDebounce(func, delay) {
      let timeoutId;
      return (...args) => {
        this.syncStatus = 'Saving...';
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
          func.apply(this, args);
        }, delay);
      };
    },
    autoFillFromProfile() {
      let filledCount = 0;
      if (store.user.fullName) { this.form.name = store.user.fullName; filledCount++; }
      if (store.user.email) { this.form.email = store.user.email; filledCount++; }
      if (store.user.location) { this.form.location = store.user.location; filledCount++; } 
      else if (store.user.address) { this.form.location = store.user.address; filledCount++; }
      if (store.user.professionalTitle) { this.form.title = store.user.professionalTitle; filledCount++; }

      if (filledCount > 0) this.isAutoFilled = true;
    },
    async loadResume() {
      try {
        const response = await axios.get(`http://localhost:5000/api/resumes/${this.resumeId}`, { withCredentials: true });
        if (response.data.resume) {
          const res = response.data.resume;
          this.templateId = res.template_id;
          
          if (res.data) {
             // Reconstruct form backwards compatibility
             this.form.name = res.data.name || '';
             this.form.title = res.data.title || '';
             this.form.email = res.data.email || '';
             this.form.location = res.data.location || '';
             this.form.phone = res.data.phone || '';
             this.form.linkedin = res.data.linkedin || '';
             this.form.github = res.data.github || '';
             this.form.objective = res.data.objective || '';
             this.form.experience = res.data.experience && res.data.experience.length ? res.data.experience : [{ title: '', company: '', location: '', startDate: '', endDate: '', description: '' }];
             this.form.education = res.data.education && res.data.education.length ? res.data.education : [{ degree: '', school: '', startDate: '', endDate: '' }];
             this.form.skills = res.data.skills || [];
             this.skillsInput = this.form.skills.join(', ');
             this.form.certifications = res.data.certifications || [];
             this.certsInput = this.form.certifications.map(c => c.name).join(', ');
             this.form.languages = res.data.languages || [];
             this.langsInput = this.form.languages.map(l => l.name).join(', ');
             this.form.interests = res.data.interests || [];
             this.interestsInput = this.form.interests.join(', ');
          }
        }
      } catch (error) {
        console.error("Failed to load resume", error);
      }
    },
    async saveToCloud() {
      if (!store.isLoggedIn) return; // Prevent saving if not logged in

      const payload = {
         title: this.form.name ? `${this.form.name}'s Resume` : 'Untitled Resume',
         template_id: this.templateId,
         data: this.form
      };

      try {
        if (this.resumeId) {
           // Update existing
           await axios.put(`http://localhost:5000/api/resumes/${this.resumeId}`, payload, { withCredentials: true });
           this.syncStatus = 'Saved to cloud';
        } else {
           // Create new
           const response = await axios.post(`http://localhost:5000/api/resumes`, payload, { withCredentials: true });
           if (response.data.resume) {
              this.resumeId = response.data.resume.id; // Switch to update mode for future saves
              // Update URL without page reload
              this.$router.replace({ query: { ...this.$route.query, id: this.resumeId } });
           }
           this.syncStatus = 'Saved to cloud';
        }
      } catch (error) {
        console.error("Save failed", error);
        this.syncStatus = 'Save failed';
      }
    },
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

.editor-panel {
  width: 500px;
  flex-shrink: 0;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  display: flex;
  flex-direction: column;
}

.panel-scroll {
  flex: 1;
  overflow-y: auto;
  padding: 3rem 2.5rem;
}

.editor-header { margin-bottom: 4rem; }
.editor-header h2 { font-family: 'Space Grotesk', sans-serif; font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem; }
.editor-header p { color: #94A3B8; font-size: 1.1rem; }

.form-section { margin-bottom: 4rem; }
.section-title { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; }
.section-title .num { font-size: 0.8rem; font-weight: 800; color: #6366F1; opacity: 0.5; }
.section-title h3 { font-size: 1.2rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; }

/* Floating Labels */
.floating { position: relative; margin-bottom: 0.5rem; }
.floating input, .floating textarea {
  width: 100%;
  padding: 1.5rem 1rem 0.5rem;
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  color: white;
  font-family: inherit;
  font-size: 1rem;
  transition: all 0.3s;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
}
.floating textarea { min-height: 100px; resize: vertical; }

.floating input:focus, .floating textarea:focus {
  outline: none;
  border-color: rgba(99, 102, 241, 0.4);
  background: rgba(15, 23, 42, 0.8);
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2), inset 0 2px 4px rgba(0,0,0,0.2);
}

.floating label {
  position: absolute;
  top: 1rem;
  left: 1rem;
  color: #64748B;
  font-size: 0.95rem;
  font-weight: 500;
  pointer-events: none;
  transition: 0.2s ease all;
}

.floating input:focus ~ label, .floating input:not(:placeholder-shown) ~ label,
.floating textarea:focus ~ label, .floating textarea:not(:placeholder-shown) ~ label {
  top: 0.4rem;
  font-size: 0.7rem;
  color: #818CF8;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
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
.template-layout-classic { 
  padding: 80px 70px; 
  font-family: var(--font-primary, 'Plus Jakarta Sans', sans-serif);
}
.canvas-header { margin-bottom: 2rem; }
.canvas-header h1 { font-family: var(--font-heading, 'Space Grotesk', sans-serif); font-size: 38px; font-weight: 800; margin-bottom: 4px; letter-spacing: -0.03em; color: #020617; }
.canvas-title { font-size: 18px; color: #6366F1; font-weight: 600; margin-bottom: 12px; letter-spacing: 0.02em; text-transform: uppercase; }
.canvas-contact { font-size: 13px; color: #475569; padding-bottom: 24px; border-bottom: 2px solid #F1F5F9; font-weight: 500; }

.canvas-section { margin-bottom: 32px; }
.canvas-section h3 { font-size: 15px; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 800; color: #0F172A; margin-bottom: 16px; position: relative; display: inline-block; }
.canvas-section h3::after { content: ''; position: absolute; left: 0; bottom: -4px; width: 100%; height: 2px; background: #6366F1; border-radius: 2px; }
.canvas-text { font-size: 14px; line-height: 1.7; color: #334155; font-weight: 400; }

.cv-item { margin-bottom: 24px; page-break-inside: avoid; }
.cv-item-header { display: flex; align-items: baseline; flex-wrap: wrap; margin-bottom: 6px; }
.cv-role { font-weight: 700; font-size: 16px; color: #0F172A; margin-right: 6px; }
.cv-company { font-weight: 500; font-size: 15px; color: #6366F1; }
.cv-dates { margin-left: auto; font-size: 13px; font-weight: 600; color: #64748B; background: #F8FAFC; padding: 4px 10px; border-radius: 6px; border: 1px solid #E2E8F0; }
.cv-desc { margin-top: 8px; font-size: 13.5px; color: #475569; }

.canvas-skills { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
.skill-pill { background: #EEF2FF; padding: 6px 14px; border-radius: 99px; font-size: 12px; font-weight: 600; color: #4F46E5; border: 1px solid rgba(99, 102, 241, 0.2); transition: all 0.2s; }
.skill-pill:hover { background: #4F46E5; color: white; }


/* --- MODERN SPLIT TEMPLATE --- */
.template-layout-modern {
  display: flex;
  height: 100%;
  min-height: 297mm;
  font-family: var(--font-primary, 'Plus Jakarta Sans', sans-serif);
}
.modern-left {
  width: 32%;
  background: #0F172A; /* Slate 900 */
  color: #F8FAFC;
  padding: 50px 35px;
}
.modern-right {
  width: 68%;
  background: #FFFFFF;
  padding: 50px 45px;
}

.m-header { margin-bottom: 45px; }
.m-header h1 { font-family: var(--font-heading, 'Space Grotesk', sans-serif); font-size: 36px; font-weight: 800; line-height: 1.1; margin-bottom: 8px; color: #fff; letter-spacing: -0.02em; }
.m-header h2 { font-size: 16px; font-weight: 500; color: #818CF8; letter-spacing: 0.05em; text-transform: uppercase; }

.m-section { margin-bottom: 40px; }
.m-section h3 { font-size: 14px; text-transform: uppercase; font-weight: 800; letter-spacing: 0.15em; margin-bottom: 20px; }
.modern-left .m-section h3 { color: #fff; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; }
.modern-right .m-section h3 { color: #020617; border-bottom: 2px solid #F1F5F9; padding-bottom: 10px; position: relative; }
.modern-right .m-section h3::after { content: ''; position: absolute; left: 0; bottom: -2px; width: 40px; height: 2px; background: #6366F1; }

.m-contact-item { font-size: 13px; color: #CBD5E1; margin-bottom: 12px; word-break: break-all; display: flex; align-items: center; gap: 8px; }
.m-contact-item::before { content: '→'; color: #6366F1; font-size: 14px; }
.m-skills-list { list-style: none; padding: 0; margin: 0; }
.m-skills-list li { font-size: 13.5px; color: #E2E8F0; margin-bottom: 10px; position: relative; padding-left: 16px; }
.m-skills-list li::before { content: '❖'; position: absolute; left: 0; top: 1px; font-size: 10px; color: #818CF8; }

.m-edu-item { margin-bottom: 20px; }
.m-edu-deg { font-size: 14.5px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.m-edu-sch { font-size: 13px; color: #94A3B8; margin-bottom: 4px; }
.m-edu-date { font-size: 12px; color: #64748B; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }

.m-text { font-size: 14px; line-height: 1.7; color: #334155; }
.m-exp-item { margin-bottom: 30px; position: relative; padding-left: 20px; }
.m-exp-item::before { content: ''; position: absolute; left: 0; top: 6px; bottom: -10px; width: 2px; background: #E2E8F0; }
.m-exp-item:last-child::before { display: none; }
.m-exp-item::after { content: ''; position: absolute; left: -3px; top: 6px; width: 8px; height: 8px; border-radius: 50%; background: #6366F1; border: 2px solid #fff; }

.m-exp-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }
.m-exp-title { font-size: 16px; font-weight: 800; color: #0F172A; }
.m-exp-date { font-size: 12.5px; font-weight: 700; color: #64748B; text-align: right; background: #F8FAFC; padding: 4px 10px; border-radius: 6px; }
.m-exp-company { font-size: 14.5px; font-weight: 600; color: #6366F1; margin-bottom: 12px; }
.m-exp-desc { margin-top: 8px; color: #475569; }

/* --- PROFESSIONAL TEMPLATE (Template 3) --- */
.template-layout-professional {
  font-family: var(--font-primary, 'Plus Jakarta Sans', sans-serif);
  padding: 0;
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 297mm;
  background: white;
}
.prof-top {
  display: flex;
  padding: 50px 60px 30px;
  align-items: center;
  position: relative;
}
.prof-top-left {
  flex: 1;
  position: relative;
  padding-left: 10px;
}
.slate-edge-block {
  position: absolute;
  left: 0;
  top: 30px;
  width: 25px;
  height: 55px;
  background: #3B4B5E;
}
.prof-top-left h1 {
  font-family: var(--font-primary, 'Plus Jakarta Sans', sans-serif);
  font-size: 46px;
  font-weight: 500;
  color: #3B4B5E;
  margin-bottom: 2px;
  line-height: 1;
  letter-spacing: -0.01em;
}
.prof-top-left h2 {
  font-size: 19px;
  font-weight: 500;
  color: #589A9E;
  margin-bottom: 15px;
}
.prof-summary {
  font-size: 13.5px;
  color: #1A202C;
  line-height: 1.5;
  max-width: 95%;
  font-weight: 500;
}
.prof-top-center {
  margin: 0 40px;
}
.prof-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.prof-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.prof-top-right {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}
.prof-contact {
  text-align: right;
  font-size: 12.5px;
  color: #1A202C;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.prof-contact .icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #3B4B5E;
  color: white;
  width: 20px;
  height: 20px;
  border-radius: 2px;
  font-size: 11px;
  margin-left: 10px;
  vertical-align: middle;
}
.prof-divider {
  border: none;
  height: 1px;
  background: #CBD5E1;
  margin: 0;
  width: 100%;
}
.prof-main {
  display: flex;
  padding: 30px 60px 50px;
  gap: 40px;
}
.prof-left {
  flex: 60%;
}
.prof-right {
  flex: 40%;
}
.prof-section {
  margin-bottom: 35px;
}
.prof-section-title {
  font-size: 20px;
  font-weight: 800;
  color: #1A202C;
  text-transform: uppercase;
  margin-bottom: 24px;
  letter-spacing: -0.01em;
}
.prof-item {
  position: relative;
  margin-bottom: 35px;
}
.teal-marker {
  position: absolute;
  left: -60px;
  top: 4px;
  width: 25px;
  height: 48px;
  background: #589A9E;
}
.prof-item-header {
  margin-bottom: 10px;
}
.prof-role {
  font-size: 17px;
  font-weight: 800;
  color: #1A202C;
  margin-bottom: 2px;
}
.prof-company {
  font-size: 16px;
  font-weight: 700;
  color: #1A202C;
  margin-bottom: 4px;
}
.prof-dates-loc {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #589A9E;
  font-style: italic;
  font-weight: 500;
  margin-bottom: 10px;
}
.prof-loc {
  color: #589A9E;
}
.prof-desc-label {
  font-size: 12.5px;
  color: #589A9E;
  font-style: italic;
  font-weight: 500;
  margin-bottom: 4px;
}
.prof-desc {
  font-size: 13px;
  color: #1A202C;
  line-height: 1.6;
  font-weight: 500;
}
.teal-bullets ul {
  padding-left: 18px;
  margin-top: 5px;
  list-style-type: none;
}
.teal-bullets ul li {
  position: relative;
  margin-bottom: 6px;
}
.teal-bullets ul li::before {
  content: '•';
  color: #589A9E;
  font-size: 18px;
  position: absolute;
  left: -15px;
  top: -4px;
}
.prof-skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.prof-skill-pill {
  background: #3B4B5E;
  color: white;
  font-size: 12px;
  font-weight: 500;
  padding: 5px 12px;
  border-radius: 4px;
}
.prof-cert-item {
  margin-bottom: 12px;
}
.prof-cert-name {
  font-size: 13px;
  font-weight: 700;
  color: #1A202C;
  margin-bottom: 2px;
}
.prof-cert-desc {
  font-size: 12px;
  color: #718096;
  font-style: italic;
}
.prof-lang-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding-right: 20px;
}
.prof-lang-name {
  font-size: 13px;
  color: #1A202C;
  font-weight: 500;
}
.prof-lang-dots {
  display: flex;
  gap: 8px;
}
.lang-dot {
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: #E2E8F0;
}
.lang-dot.filled {
  background: #3B4B5E;
}
.prof-interests-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.prof-interest-pill {
  border: 1px solid #A0AEC0;
  color: #1A202C;
  font-size: 12.5px;
  font-weight: 500;
  padding: 5px 14px;
  border-radius: 4px;
}

@media (max-width: 1200px) {
  .workspace-main { flex-direction: column; overflow-y: auto; }
  .editor-panel { width: 100%; height: auto; border-right: none; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
  .preview-panel { width: 100%; height: 600px; }
  .resume-canvas { transform: scale(0.65); transform-origin: top center; }
  .panel-scroll { padding: 2rem 1.5rem; }
  .input-grid { grid-template-columns: 1fr; gap: 1rem; }
}

/* Enhancements for better UX */
.input-group input, .input-group textarea {
  background: rgba(2, 6, 23, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
}
.input-group input:focus, .input-group textarea:focus {
  border-color: #6366F1;
  background: rgba(2, 6, 23, 0.9);
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2), inset 0 2px 4px rgba(0,0,0,0.2);
}
.repeater-item {
  background: rgba(255, 255, 255, 0.02);
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}
.repeater-item:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 255, 255, 0.1);
}
.preview-canvas-container {
  background: #0f172a;
}
</style>
