<template>
  <div class="templates-page">
    <div class="page-header text-center">
      <div class="badge">Professional Templates</div>
      <h1 class="page-title">Stand out with <br><span class="text-gradient">expertly designed</span> resumes.</h1>
      <p class="page-subtitle">Create your new ATS-friendly resume in less than 5 minutes. Browse layouts engineered for high-growth tech, business, and creative roles.</p>
    </div>

    <!-- Category Filter Bar -->
    <div class="category-filters-container">
      <div class="category-filters">
        <button 
          v-for="cat in categories" 
          :key="cat"
          class="filter-btn" 
          :class="{ active: selectedCategory === cat }"
          @click="selectedCategory = cat"
        >
          {{ cat }}
        </button>
      </div>
    </div>

    <!-- Template Grid -->
    <section class="templates-section">
      <transition-group name="grid-fade" tag="div" class="templates-grid">
        <div v-for="template in filteredTemplates" :key="template.id" class="template-card glass-card">
          <div class="card-visual">
            <img :src="template.image" :alt="template.name" class="t-img" />
            
            <div class="t-overlay">
              <button class="btn-use-template" @click="selectTemplate(template.id)">
                Use Blueprint
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="btn-icon">
                  <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            
            <!-- Category Tag floating on image -->
            <div class="t-floating-badge">{{ template.category }}</div>
          </div>
          <div class="card-info">
            <h3>{{ template.name }}</h3>
            <p>{{ template.desc }}</p>
          </div>
        </div>
      </transition-group>
      
      <!-- Empty State -->
      <div v-if="filteredTemplates.length === 0" class="no-results glass-card">
         <p>No templates found for this category.</p>
         <button class="btn-text" @click="selectedCategory = 'All Templates'">View All Templates</button>
      </div>
    </section>
    
    <!-- Benefits Banner -->
    <section class="benefits-banner glass-card">
       <div class="benefit-item">
          <div class="b-icon">✨</div>
          <div class="b-text">
            <h4>ATS-Friendly</h4>
            <p>Pass the screening robots.</p>
          </div>
       </div>
       <div class="benefit-item">
          <div class="b-icon">⚡</div>
          <div class="b-text">
            <h4>5-Minute Builder</h4>
            <p>Generate instantly via AI.</p>
          </div>
       </div>
       <div class="benefit-item">
          <div class="b-icon">🎨</div>
          <div class="b-text">
            <h4>Premium Designs</h4>
            <p>Stand out from the crowd.</p>
          </div>
       </div>
    </section>
  </div>
</template>

<script>
import classicImg from '@/assets/cv-classic.jpg';
import proImg from '@/assets/cv-template-professional.jpg';
import execImg from '@/assets/cv-template-executive.jpg';
import minimalImg from '@/assets/cv-template-minimalistic.jpg';
import modernImg from '@/assets/cv-template-modern.jpg';

export default {
  name: 'ResumeTemplate',
  data() {
    return {
      selectedCategory: 'All Templates',
      categories: ['All Templates', 'Engineering', 'Product', 'Creative', 'Business', 'Tech', 'Management'],
      templates: [
        { id: 1, name: 'The Architect', category: 'Engineering', desc: 'A structure-first layout for senior technical leads.', image: proImg },
        { id: 2, name: 'The Specialist', category: 'Product', desc: 'Focuses on outcome-driven metrics and impact.', image: execImg },
        { id: 3, name: 'The Minimalist', category: 'Creative', desc: 'Clean, Swiss-inspired design for high data density.', image: minimalImg },
        { id: 4, name: 'The Classic', category: 'Business', desc: 'Timeless professional layout for established roles.', image: classicImg },
        { id: 5, name: 'The Modern', category: 'Tech', desc: 'Bold, high-contrast design for the modern workforce.', image: modernImg },
        { id: 6, name: 'The Visionary', category: 'Management', desc: 'Forward-looking structure showcasing leadership initiatives.', image: execImg },
        { id: 7, name: 'The Developer', category: 'Engineering', desc: 'Syntax-highlighted aesthetics tailored for coders.', image: proImg },
        { id: 8, name: 'The Strategist', category: 'Business', desc: 'A dense, analytics-focused layout for strategists.', image: classicImg }
      ]
    };
  },
  computed: {
    filteredTemplates() {
      if (this.selectedCategory === 'All Templates') {
        return this.templates;
      }
      return this.templates.filter(t => t.category === this.selectedCategory);
    }
  },
  methods: {
    selectTemplate(id) {
      this.$router.push(`/resume-template/fill-resume?template=${id}`);
    }
  }
};
</script>

<style scoped>
.templates-page {
  padding: 4rem 2rem 8rem;
  max-width: 1400px;
  margin: 0 auto;
}

/* Header Styles */
.page-header {
  text-align: center;
  margin-bottom: 4rem;
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
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Filter Navigation */
.category-filters-container {
  display: flex;
  justify-content: center;
  margin-bottom: 4rem;
  position: relative;
  z-index: 10;
}

.category-filters {
  display: flex;
  gap: 0.5rem;
  background: rgba(30, 41, 59, 0.4);
  backdrop-filter: blur(12px);
  padding: 0.5rem;
  border-radius: 99px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  overflow-x: auto;
  scrollbar-width: none; /* Firefox */
  max-width: 100%;
}
.category-filters::-webkit-scrollbar { display: none; } /* Chrome */

.filter-btn {
  background: transparent;
  color: var(--text-muted);
  padding: 0.75rem 1.5rem;
  border-radius: 99px;
  font-weight: 600;
  font-size: 0.95rem;
  white-space: nowrap;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.filter-btn:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.05);
}

.filter-btn.active {
  background: var(--text-main);
  color: var(--bg-deep);
  box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15);
}

/* Templates Grid */
.templates-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); 
  gap: 3rem; 
  position: relative;
}

/* List Transitions */
.grid-fade-enter-active, .grid-fade-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.grid-fade-enter-from, .grid-fade-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
.grid-fade-leave-active {
  position: absolute;
}

/* Template Card */
.template-card { 
  border-radius: 20px; 
  overflow: hidden; 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

.template-card:hover { 
  border-color: rgba(99, 102, 241, 0.5); 
  transform: translateY(-8px); 
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 20px rgba(99, 102, 241, 0.15);
}

.card-visual { 
  height: 440px; 
  overflow: hidden; 
  position: relative; 
  background: #0f172a;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.t-img { 
  width: 100%; 
  height: 100%; 
  object-fit: cover; 
  object-position: top;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s; 
  filter: brightness(0.9);
}

.template-card:hover .t-img { 
  transform: scale(1.08); 
  filter: brightness(0.6); 
}

/* Floating Badge inside Image */
.t-floating-badge {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  color: var(--text-main);
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: opacity 0.3s;
  opacity: 1;
}

.template-card:hover .t-floating-badge {
  opacity: 0;
}

/* Hover Overlay */
.t-overlay { 
  position: absolute; 
  top: 0; left: 0; width: 100%; height: 100%; 
  display: flex; align-items: center; justify-content: center; 
  background: rgba(2, 6, 23, 0.4); 
  backdrop-filter: blur(3px); 
  opacity: 0; 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); 
  pointer-events: none;
}

.template-card:hover .t-overlay { 
  opacity: 1; 
  pointer-events: auto;
}

/* Action Button */
.btn-use-template { 
  background: var(--accent);
  color: #fff;
  padding: 1rem 2rem; 
  border-radius: 99px; 
  font-weight: 600; 
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transform: translateY(20px); 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
}

.template-card:hover .btn-use-template { 
  transform: translateY(0); 
}

.btn-use-template:hover {
  background: #4f46e5;
  transform: translateY(-2px) !important;
  box-shadow: 0 15px 40px rgba(99, 102, 241, 0.5);
}

.btn-icon {
  transition: transform 0.3s;
}
.btn-use-template:hover .btn-icon {
  transform: translateX(4px);
}

/* Card Information */
.card-info { 
  padding: 1.75rem; 
  background: linear-gradient(to bottom, rgba(30, 41, 59, 0), rgba(30, 41, 59, 0.3));
}

.card-info h3 { 
  font-size: 1.4rem; 
  font-weight: 700; 
  color: var(--text-main); 
  margin-bottom: 0.5rem;
}

.card-info p { 
  color: var(--text-muted); 
  font-size: 0.95rem; 
  line-height: 1.5; 
}

/* Empty State */
.no-results {
  text-align: center;
  padding: 4rem 2rem;
  border-radius: 24px;
  grid-column: 1 / -1;
}
.no-results p {
  font-size: 1.25rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
}
.btn-text {
  background: none;
  color: var(--accent);
  font-weight: 600;
  font-size: 1rem;
  text-decoration: underline;
  text-underline-offset: 4px;
}
.btn-text:hover { color: #fff; }

/* Benefits Banner */
.benefits-banner {
  margin-top: 6rem;
  padding: 3rem;
  border-radius: 24px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.4), rgba(15, 23, 42, 0.6));
}

.benefit-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.b-icon {
  font-size: 2.5rem;
  background: var(--bg-deep);
  width: 64px; height: 64px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

.b-text h4 {
  font-size: 1.15rem;
  margin-bottom: 0.25rem;
  color: var(--text-main);
}
.b-text p {
  font-size: 0.95rem;
  color: var(--text-muted);
}

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .benefits-banner { grid-template-columns: 1fr; gap: 2rem; }
  .templates-grid { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }
}

@media (max-width: 768px) {
   .page-title { font-size: 2.75rem; }
   .category-filters { border-radius: 16px; padding: 0.75rem; }
   .templates-grid { grid-template-columns: 1fr; }
   .card-visual { height: 400px; }
   .benefits-banner { padding: 2rem; }
}
</style>
