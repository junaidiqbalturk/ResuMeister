<template>
  <div class="templates-page">
    <div class="page-header text-center">
      <div class="badge">Professional Portfolio</div>
      <h1 class="page-title">Design your <span class="text-gradient">edge.</span></h1>
      <p class="page-subtitle">Select a blueprint engineered for high-growth tech and business roles. All templates are ATS-optimized.</p>
    </div>

    <!-- Template Grid -->
    <section class="templates-section">
      <div class="templates-grid">
        <div v-for="template in templates" :key="template.id" class="template-card">
          <div class="card-visual">
            <img :src="template.image" :alt="template.name" class="t-img" />
            <div class="t-overlay">
              <button class="btn-primary-large" @click="selectTemplate(template.id)">Use Blueprint</button>
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
      templates: [
        { 
          id: 1, 
          name: 'The Architect', 
          category: 'Engineering', 
          desc: 'A structure-first layout for senior technical leads.', 
          image: proImg 
        },
        { 
          id: 2, 
          name: 'The Specialist', 
          category: 'Product', 
          desc: 'Focuses on outcome-driven metrics and impact.', 
          image: execImg 
        },
        { 
          id: 3, 
          name: 'The Minimalist', 
          category: 'Creative', 
          desc: 'Clean, Swiss-inspired design for high data density.', 
          image: minimalImg 
        },
        { 
          id: 4, 
          name: 'The Classic', 
          category: 'Business', 
          desc: 'Timeless professional layout for established roles.', 
          image: classicImg 
        },
        { 
          id: 5, 
          name: 'The Modern', 
          category: 'Tech', 
          desc: 'Bold, high-contrast design for the modern workforce.', 
          image: modernImg 
        },
        { 
          id: 6, 
          name: 'The Visionary', 
          category: 'Management', 
          desc: 'Forward-looking structure showcasing leadership initiatives.', 
          image: execImg
        },
        { 
          id: 7, 
          name: 'The Developer', 
          category: 'Engineering', 
          desc: 'Syntax-highlighted aesthetics tailored for coders.', 
          image: proImg 
        },
        { 
          id: 8, 
          name: 'The Strategist', 
          category: 'Business', 
          desc: 'A dense, analytics-focused layout for strategists.', 
          image: classicImg 
        }
      ]
    };
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

.page-header {
  text-align: center;
  margin-bottom: 5rem;
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
  max-width: 700px;
  margin: 0 auto;
}

.templates-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); 
  gap: 3rem; 
}

.template-card { 
  background: var(--bg-card); 
  border: 1px solid rgba(255, 255, 255, 0.08); 
  border-radius: 24px; 
  overflow: hidden; 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

.template-card:hover { 
  border-color: var(--accent); 
  transform: translateY(-8px); 
  box-shadow: 0 30px 60px rgba(0,0,0,0.4);
}

.card-visual { 
  height: 480px; 
  overflow: hidden; 
  position: relative; 
  background: #000;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.t-img { 
  width: 100%; 
  height: 100%; 
  object-fit: cover; 
  object-position: top;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s; 
  opacity: 0.8; 
}

.template-card:hover .t-img { 
  transform: scale(1.05); 
  opacity: 1; 
}

.t-overlay { 
  position: absolute; 
  top: 0; left: 0; width: 100%; height: 100%; 
  display: flex; align-items: center; justify-content: center; 
  background: rgba(15, 23, 42, 0.6); 
  backdrop-filter: blur(4px); 
  opacity: 0; 
  transition: opacity 0.3s; 
}

.template-card:hover .t-overlay { 
  opacity: 1; 
}

.btn-primary-large { 
  background: var(--text-main); 
  color: var(--bg-deep) !important; 
  padding: 1rem 2rem; 
  border-radius: 99px; 
  font-weight: 700; 
  cursor: pointer; 
  transform: translateY(20px); 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px rgba(255,255,255,0.1);
  font-family: var(--font-primary);
  border: none;
}

.btn-primary-large:hover {
  transform: translateY(0) scale(1.05);
  box-shadow: 0 15px 40px rgba(255,255,255,0.2);
}

.template-card:hover .btn-primary-large { 
  transform: translateY(0); 
}

.card-info { 
  padding: 2rem; 
  flex-grow: 1;
}

.info-top { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  margin-bottom: 1rem; 
}

.info-top h3 { 
  font-size: 1.35rem; 
  font-weight: 700; 
  color: var(--text-main); 
}

.t-badge { 
  font-size: 0.75rem; 
  font-weight: 800; 
  text-transform: uppercase; 
  color: var(--accent); 
  background: rgba(99, 102, 241, 0.1); 
  padding: 6px 12px; 
  border-radius: 8px; 
}

.card-info p { 
  color: var(--text-muted); 
  font-size: 1rem; 
  line-height: 1.6; 
}

@media (max-width: 768px) {
   .page-title { font-size: 2.5rem; }
   .templates-grid { grid-template-columns: 1fr; }
   .card-visual { height: 400px; }
}
</style>
