<template>
  <div class="ats-scanner-container relative-bg">
    <!-- Ambient Background Lighting -->
    <div class="ambient-blob blob-purple"></div>
    <div class="ambient-blob blob-blue"></div>
    <div class="ambient-blob blob-pink"></div>

    <div class="ats-wrapper">
      
      <!-- Header -->
      <div class="ats-header">
        <h1 class="text-gradient hover-glow">Intelligent ATS Scanner</h1>
        <p class="subtitle">
          Test your resume against any job description. Our advanced AI model reveals your exact matching probability before you apply.
        </p>
      </div>

      <!-- Main Content Grid -->
      <div class="ats-grid">
        
        <!-- Input Form Section -->
        <div class="glass-card ats-panel">
          <h2 class="panel-title">
            <span class="icon-box">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </span>
            Analyze Application
          </h2>
          
          <form @submit.prevent="scanResume" class="ats-form">
            
            <!-- Job Description -->
            <div class="form-group">
              <label>Job Description</label>
              <textarea 
                v-model="jobDescription" 
                rows="6" 
                class="custom-input custom-scrollbar"
                placeholder="Paste the target job description here..."
                required
              ></textarea>
            </div>

            <!-- Resume Upload -->
            <div class="form-group">
              <label>Upload Resume (PDF/DOCX)</label>
              
              <div 
                class="file-dropzone"
                @click="triggerFileInput"
              >
                <input 
                  type="file" 
                  ref="fileInput" 
                  @change="handleFileUpload" 
                  class="hidden-input" 
                  accept=".pdf,.docx" 
                  required
                />
                <div class="dropzone-content">
                  <svg xmlns="http://www.w3.org/2000/svg" class="upload-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                  <div>
                    <span v-if="!cvFile" class="dropzone-text">Click to browse or drag and drop</span>
                    <span v-else class="dropzone-text highlight">{{ cvFile.name }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="error" class="error-box">
              {{ error }}
            </div>

            <!-- Submit Button -->
            <button 
              type="submit" 
              class="btn bg-gradient-btn"
              :disabled="loading || !jobDescription || !cvFile"
            >
              <span class="btn-content">
                <svg v-if="loading" class="spinner" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                {{ loading ? 'Analyzing Resume...' : 'Scan Now' }}
              </span>
            </button>
            
          </form>
        </div>

        <!-- Results Section -->
        <div class="results-column">
          
          <!-- Empty State -->
          <div v-if="!result && !loading" class="glass-card empty-state">
            <svg xmlns="http://www.w3.org/2000/svg" class="empty-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p>Your analysis results will appear here after scanning.</p>
          </div>

          <!-- Loading Skeleton -->
          <div v-if="loading" class="glass-card skeleton-panel">
            <div class="skeleton-circle pulse"></div>
            <div class="skeleton-lines">
              <div class="sk-line pulse" style="width: 75%"></div>
              <div class="sk-line pulse" style="width: 50%"></div>
              <div class="sk-line pulse" style="width: 85%"></div>
            </div>
          </div>

          <!-- Score Card -->
          <template v-if="result && !loading">
            
            <div class="results-header d-flex justify-content-between align-items-center mb-3">
              <h2 class="results-title mb-0">Analysis Complete</h2>
              <div class="header-actions" style="display: flex; gap: 10px;">
                <button @click="resetScan" class="btn btn-primary btn-sm print-btn" style="padding: 0.5rem 1rem;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline; margin-right:6px; vertical-align:text-bottom;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
                  New Scan
                </button>
                <button @click="downloadReport" class="btn btn-secondary btn-sm print-btn" style="padding: 0.5rem 1rem;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline; margin-right:6px; vertical-align:text-bottom;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                  Download PDF
                </button>
              </div>
            </div>

            <div class="glass-card score-card">
              <!-- Score Circle -->
              <div class="progress-circle-container" :data-color="scoreTheme(result.overall_score)">
                <svg class="progress-ring" viewBox="0 0 160 160">
                  <circle class="ring-bg" cx="80" cy="80" r="70" />
                  <circle class="ring-progress" cx="80" cy="80" r="70" 
                    :stroke-dasharray="440" 
                    :stroke-dashoffset="440 - (result.overall_score / 100) * 440" />
                </svg>
                <div class="progress-text">
                  <span class="score-number">{{ Math.round(result.overall_score) }}<span>%</span></span>
                  <span class="score-label">Match</span>
                </div>
              </div>
              
              <div class="score-details">
                 <div class="assessment-box">
                    <h3>Overall Assessment</h3>
                    <p>{{ assessmentText(result.overall_score) }}</p>
                 </div>
                 
                 <div class="sub-scores">
                   <div class="sub-score-item">
                     <div class="sub-score-header">
                       <span>Semantic Context Match</span>
                       <span class="sub-number" :class="scoreColorText(result.semantic_score)">{{ Math.round(result.semantic_score) }}%</span>
                     </div>
                     <div class="progress-bar-bg">
                       <div class="progress-bar-fill" :class="scoreColorBg(result.semantic_score)" :style="{ width: result.semantic_score + '%' }"></div>
                     </div>
                   </div>

                   <div class="sub-score-item">
                     <div class="sub-score-header">
                       <span>Keyword Coverage</span>
                       <span class="sub-number" :class="scoreColorText(result.keyword_score)">{{ Math.round(result.keyword_score) }}%</span>
                     </div>
                     <div class="progress-bar-bg">
                       <div class="progress-bar-fill" :class="scoreColorBg(result.keyword_score)" :style="{ width: result.keyword_score + '%' }"></div>
                     </div>
                   </div>

                   <!-- NEW YoE Metric Area -->
                   <div class="sub-score-item mt-3" v-if="result.required_yoe > 0">
                     <div class="sub-score-header mb-1">
                       <span>Years of Experience (YoE)</span>
                       <span class="sub-number" :class="result.candidate_yoe >= result.required_yoe ? 'text-success' : 'text-danger'">
                         {{ result.candidate_yoe }} / {{ result.required_yoe }} yrs
                       </span>
                     </div>
                     <div class="progress-bar-bg" style="height: 4px;">
                       <div class="progress-bar-fill" 
                            :class="result.candidate_yoe >= result.required_yoe ? 'bg-success' : 'bg-danger'" 
                            :style="{ width: Math.min((result.candidate_yoe / result.required_yoe) * 100, 100) + '%' }">
                        </div>
                     </div>
                     <p class="yoe-hint" v-if="result.candidate_yoe < result.required_yoe">Candidate is {{ result.required_yoe - result.candidate_yoe }} years short of the requirement.</p>
                     <p class="yoe-hint" v-else-if="result.candidate_yoe > result.required_yoe">Candidate exceeds the YoE requirement by {{ result.candidate_yoe - result.required_yoe }} years!</p>
                     <p class="yoe-hint" v-else>Candidate perfectly matches the YoE requirement!</p>
                   </div>

                 </div>
              </div>
            </div>

            <!-- Keyword Breakdown -->
            <div class="glass-card ats-panel" style="margin-top:1.5rem">
              <h3 class="panel-subtitle">
                <span class="gradient-bar"></span>
                Keyword Intelligence
              </h3>
              
              <div class="keyword-groups">
                <div class="keyword-section">
                  <h4 class="success-heading">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    Identified Strengths
                  </h4>
                  <div class="chips">
                    <span v-for="kw in result.matched_keywords" :key="kw" class="chip chip-success">
                      {{ kw }}
                    </span>
                    <span v-if="!result.matched_keywords.length" class="empty-chips">No matching keywords found.</span>
                  </div>
                </div>

                <div class="keyword-section">
                  <h4 class="error-heading">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
                    Missing Requirements
                  </h4>
                  <div class="chips">
                    <span v-for="kw in missingKeywords" :key="kw" class="chip chip-error">
                      {{ kw }}
                    </span>
                    <span v-if="!missingKeywords.length" class="empty-chips">You hit all required keywords!</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Actionable Insights -->
            <div class="glass-card ats-panel" style="margin-top:1.5rem" v-if="result.actionable_insights && result.actionable_insights.length > 0">
              <h3 class="panel-subtitle">
                <span class="gradient-bar bg-accent-gradient"></span>
                Actionable Insights
              </h3>
              
              <div class="insights-container">
                <div v-for="(insight, index) in result.actionable_insights" :key="index" class="insight-card" :class="`insight-${insight.type}`">
                  
                  <div class="insight-icon">
                    <svg v-if="insight.type === 'keywords'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" /></svg>
                    <svg v-else-if="insight.type === 'experience'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <svg v-else-if="insight.type === 'structure'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" /></svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  </div>

                  <div class="insight-content">
                    <p class="insight-msg">{{ insight.message }}</p>
                    <p v-if="insight.projection" class="insight-proj">
                      <strong>Projection:</strong> {{ insight.projection }}
                    </p>
                  </div>

                </div>
              </div>
            </div>

          </template>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ATSScanner",
  data() {
    return {
      jobDescription: '',
      cvFile: null,
      loading: false,
      error: null,
      result: null
    };
  },
  computed: {
    missingKeywords() {
      if (!this.result) return [];
      const matched = new Set(this.result.matched_keywords.map(k => k.toLowerCase()));
      return this.result.required_keywords.filter(k => !matched.has(k.toLowerCase()));
    }
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.cvFile = file;
      }
    },
    async scanResume() {
      if (!this.jobDescription || !this.cvFile) return;

      this.loading = true;
      this.error = null;
      this.result = null;

      const formData = new FormData();
      formData.append('job_description', this.jobDescription);
      formData.append('cv_file', this.cvFile);

      try {
        const response = await axios.post('http://localhost:5000/api/ats-scan', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          withCredentials: true
        });

        if (response.data.success) {
          this.result = response.data.result;
        } else {
          this.error = response.data.message || 'Scanning failed.';
        }
      } catch (err) {
        this.error = err.response?.data?.message || 'Server error tracking scan.';
      } finally {
        this.loading = false;
      }
    },
    resetScan() {
      this.result = null;
      this.cvFile = null;
      this.jobDescription = '';
      this.error = null;
      if (this.$refs.fileInput) {
        this.$refs.fileInput.value = '';
      }
    },
    downloadReport() {
      window.print();
    },
    scoreTheme(score) {
      if (score >= 80) return 'success';
      if (score >= 40) return 'warning';
      return 'danger';
    },
    scoreColorText(score) {
      if (score >= 80) return 'text-success';
      if (score >= 40) return 'text-warning';
      return 'text-danger';
    },
    scoreColorBg(score) {
      if (score >= 80) return 'bg-success';
      if (score >= 40) return 'bg-warning';
      return 'bg-danger';
    },
    assessmentText(score) {
      if (score >= 85) return 'Exceptional Candidate Match. You are highly likely to pass the automated screening.';
      if (score >= 70) return 'Strong Match. Consider adding a few more specific keywords missing in the breakdown.';
      if (score >= 50) return 'Moderate Match. Heavy re-tailoring of your experiences to the JD is recommended.';
      return 'Low Match. The semantic engine does not correlate your timeline deeply with this specific role.';
    }
  }
};
</script>

<style scoped>
.ats-scanner-container {
  min-height: 100vh;
  padding-bottom: 5rem;
  color: var(--text-main);
  background-color: var(--bg-deep);
}

.relative-bg {
  position: relative;
  overflow: hidden;
}

/* Ambient Lighting */
.ambient-blob {
  position: absolute;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  filter: blur(80px);
  mix-blend-mode: multiply;
  opacity: 0.15;
  animation: blobMotion 8s infinite alternate;
  z-index: 0;
  pointer-events: none;
}
.blob-purple { background: var(--accent); top: -10%; left: -5%; animation-delay: 0s; }
.blob-blue   { background: #3b82f6; top: -5%; right: -5%; animation-delay: 2s; }
.blob-pink   { background: var(--tertiary); bottom: -10%; left: 20%; animation-delay: 4s; }

@keyframes blobMotion {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(30px, 40px) scale(1.1); }
}

.ats-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
  position: relative;
  z-index: 10;
}

.ats-header {
  text-align: center;
  margin-bottom: 4rem;
}

.ats-header h1 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 1rem;
}
.ats-header .subtitle {
  color: var(--text-muted);
  font-size: 1.1rem;
  max-width: 700px;
  margin: 0 auto;
}

.ats-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2.5rem;
}
@media (min-width: 900px) {
  .ats-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.ats-panel {
  padding: 2.5rem;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
}

.panel-title {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.icon-box {
  background: var(--accent-glow);
  color: var(--accent);
  padding: 0.5rem;
  border-radius: 8px;
  display: flex;
}

.ats-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 0.5rem;
}

.custom-input {
  width: 100%;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem;
  color: var(--text-main);
  font-family: inherit;
  font-size: 1rem;
  resize: vertical;
  transition: 0.3s;
}
.custom-input:focus {
  border-color: var(--accent);
  outline: none;
  background: rgba(255, 255, 255, 0.05);
}

.hidden-input {
  display: none;
}

.file-dropzone {
  border: 2px dashed rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 2.5rem 1rem;
  text-align: center;
  cursor: pointer;
  transition: 0.3s;
  background: rgba(255,255,255,0.01);
}
.file-dropzone:hover {
  border-color: var(--accent);
  background: rgba(255,255,255,0.03);
}
.dropzone-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
.upload-icon {
  width: 48px;
  height: 48px;
  color: var(--text-dim);
  transition: color 0.3s;
}
.file-dropzone:hover .upload-icon {
  color: var(--accent);
}
.dropzone-text {
  color: var(--text-muted);
  font-size: 0.95rem;
}
.dropzone-text.highlight {
  color: var(--accent);
  font-weight: 600;
}

.error-box {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  color: #f87171;
  padding: 1rem;
  border-radius: 12px;
  font-size: 0.9rem;
}

.bg-gradient-btn {
  background: linear-gradient(135deg, var(--accent), var(--tertiary));
  color: white !important;
  font-size: 1.1rem;
  font-weight: 700;
  padding: 1rem;
  border-radius: 12px;
  margin-top: 1rem;
  position: relative;
  overflow: hidden;
}
.bg-gradient-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

/* Spinner Core */
.spinner {
  width: 20px;
  height: 20px;
  color: white;
  animation: spin 1s linear infinite;
}
.opacity-25 { opacity: 0.25; }
.opacity-75 { opacity: 0.75; }
@keyframes spin { 100% { transform: rotate(360deg); } }

/* Results Column Empty/Loading */
.results-column {
  display: flex;
  flex-direction: column;
}
.empty-state {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 3rem;
  border-radius: 20px;
  border: 2px dashed rgba(255,255,255,0.05);
  color: var(--text-dim);
}
.empty-icon {
  width: 64px;
  height: 64px;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.skeleton-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 3rem;
  border-radius: 20px;
}
.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: .5; }
}
.skeleton-circle {
  width: 140px; height: 140px;
  border-radius: 50%;
  border: 8px solid rgba(255,255,255,0.05);
}
.skeleton-lines {
  width: 100%; display: flex; flex-direction: column; gap: 1rem; align-items: center;
}
.sk-line {
  height: 12px; border-radius: 6px; background: rgba(255,255,255,0.05);
}

/* Real Score Card */
.score-card {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2.5rem;
  padding: 2.5rem;
  border-radius: 20px;
}
@media (max-width: 600px) {
  .score-card {
    flex-direction: column;
    text-align: center;
  }
}

.progress-circle-container {
  position: relative;
  width: 160px;
  height: 160px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.progress-ring {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
  position: absolute;
  top: 0; left: 0;
}
.ring-bg {
  stroke: rgba(255,255,255,0.05);
  stroke-width: 10;
  fill: transparent;
}
.ring-progress {
  stroke-width: 10;
  fill: transparent;
  stroke-linecap: round;
  transition: stroke-dashoffset 1.5s ease-out;
}

.progress-text {
  text-align: center;
  z-index: 2;
}
.score-number {
  font-size: 2.5rem;
  font-weight: 800;
  font-family: var(--font-heading);
  line-height: 1;
  display: block;
}
.score-number span {
  font-size: 1.25rem;
}
.score-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--text-dim);
  font-weight: 600;
}

/* Score Data Colors */
.progress-circle-container[data-color="success"] .ring-progress { stroke: #10B981; }
.progress-circle-container[data-color="success"] .score-number { color: #34D399; }

.progress-circle-container[data-color="warning"] .ring-progress { stroke: #F59E0B; }
.progress-circle-container[data-color="warning"] .score-number { color: #FBBF24; }

.progress-circle-container[data-color="danger"] .ring-progress { stroke: #EF4444; }
.progress-circle-container[data-color="danger"] .score-number { color: #F87171; }

.score-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.assessment-box h3 { font-size: 1.5rem; margin-bottom: 0.25rem; }
.assessment-box p { color: var(--text-muted); font-size: 0.95rem; }

.sub-score-item { margin-bottom: 1rem; }
.sub-score-header { display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.4rem; color: var(--text-muted); }
.sub-number { font-weight: 700; }
.progress-bar-bg { width: 100%; height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; overflow: hidden; }
.progress-bar-fill { height: 100%; border-radius: 4px; transition: width 1s ease-out; }

/* Utility colors */
.text-success { color: #34D399; }
.bg-success { background: #10B981; }
.text-warning { color: #FBBF24; }
.bg-warning { background: #F59E0B; }
.text-danger { color: #F87171; }
.bg-danger { background: #EF4444; }

.mb-1 { margin-bottom: 0.25rem !important; }
.mt-3 { margin-top: 1rem !important; }
.yoe-hint { font-size: 0.75rem !important; color: var(--text-dim) !important; margin-top: 0.4rem; font-style: italic;}

/* Keywords */
.panel-subtitle {
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}
.gradient-bar {
  width: 6px;
  height: 24px;
  background: linear-gradient(to bottom, var(--accent), var(--tertiary));
  border-radius: 3px;
}
.keyword-groups {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.success-heading { color: #34D399; display: flex; align-items: center; gap: 0.5rem; font-size: 0.95rem; margin-bottom: 0.75rem;}
.error-heading { color: #F87171; display: flex; align-items: center; gap: 0.5rem; font-size: 0.95rem; margin-bottom: 0.75rem;}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.chip {
  padding: 0.35rem 0.85rem;
  border-radius: 99px;
  font-size: 0.75rem;
  font-weight: 600;
  border: 1px solid transparent;
}
.chip-success { background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.2); color: #6EE7B7; }
.chip-error { background: rgba(239, 68, 68, 0.1); border-color: rgba(239, 68, 68, 0.2); color: #FCA5A5; }
.empty-chips { color: var(--text-dim); font-size: 0.85rem; }

/* Actionable Insights */
.bg-accent-gradient { background: linear-gradient(to bottom, #8B5CF6, #EC4899); }
.insights-container { display: flex; flex-direction: column; gap: 1.25rem; }

.insight-card {
  display: flex;
  gap: 1.25rem;
  padding: 1.25rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  transition: transform 0.2s, background 0.2s;
}
.insight-card:hover { transform: translateY(-2px); background: rgba(255,255,255,0.04); }

.insight-icon {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.insight-keywords .insight-icon { background: rgba(245, 158, 11, 0.15); color: #FBBF24; }
.insight-experience .insight-icon { background: rgba(59, 130, 246, 0.15); color: #60A5FA; }
.insight-structure .insight-icon { background: rgba(236, 72, 153, 0.15); color: #F472B6; }
.insight-success .insight-icon { background: rgba(16, 185, 129, 0.15); color: #34D399; }

.insight-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.insight-msg { font-size: 0.95rem; color: var(--text-main); margin-bottom: 0.4rem; line-height: 1.5; }
.insight-proj { font-size: 0.85rem; color: var(--accent); font-weight: 500; }
.insight-proj strong { color: var(--text-muted); text-transform: uppercase; font-size: 0.7rem; letter-spacing: 1px; margin-right: 4px; }

/* Print Styles for ATS Report Download */
@media print {
  /* Hide Navbar, Site Footer, Inputs, Buttons */
  nav, .site-navbar, .site-footer, .input-column, .print-btn, .header {
    display: none !important;
  }
  
  /* Reset layout for full page width */
  @page {
    margin: 1.5cm;
    size: auto;
  }
  
  .ats-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
  }
  
  .scanner-layout {
    display: block !important;
    gap: 0 !important;
  }
  
  .results-column {
    width: 100% !important;
    margin: 0 auto !important;
  }
  
  /* Change dark theme to light for printing to save ink */
  body, html {
    background: white !important;
    color: black !important;
  }
  
  .page-content {
      padding-top: 0 !important;
      min-height: auto !important;
  }
  
  .glass-card {
    background: transparent !important;
    border: 1px solid #ccc !important;
    box-shadow: none !important;
    color: black !important;
    margin-bottom: 20px !important;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  
  .score-number { color: black !important; }
  .text-main, .text-muted, .text-dim { color: black !important; }
  .gradient-text { background: none !important; -webkit-text-fill-color: black !important; font-weight: bold; }
  
  /* Make insights stand out on paper */
  .insight-card {
    border: 1px solid #eee !important;
    background: #fdfdfd !important;
  }
  
  /* Ensure backgrounds print for progress bars / chips */
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
}

</style>

