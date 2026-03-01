<template>
  <div class="d-minimal-wrapper">
    
    <!-- Top Header Navigation -->
    <header class="d-header-nav">
      <div class="d-nav-container">
        
        <!-- Brand / Identity -->
        <div class="d-brand" @click="activeTab = 'overview'" role="button">
          <img src="/resumeister.png" alt="ResuMeister" class="d-logo" />
          <span class="d-brand-text">ResuMeister</span>
        </div>

        <!-- Right Side Nav -->
        <div class="d-nav-right">
          
          <div class="d-nav-links">
             <button class="d-nav-link" :class="{ 'active': activeTab === 'overview' }" @click="activeTab = 'overview'">Overview</button>
             <button class="d-nav-link" :class="{ 'active': activeTab === 'settings' }" @click="activeTab = 'settings'">Settings</button>
             <div class="d-divider"></div>
             <button class="d-nav-link d-text-error" @click="handleLogout">Logout</button>
          </div>

          <!-- User Profile -->
          <div class="d-user-profile">
            <div class="d-avatar">{{ userInitials }}</div>
            <div class="d-user-info">
              <span class="d-user-name">{{ store.user?.fullName || store.user?.username || 'Guest' }}</span>
              <span class="d-user-plan">Pro Plan</span>
            </div>
          </div>

        </div>
      </div>
    </header>

    <!-- Main Workspace -->
    <main class="d-main-content">
      <div class="d-workspace-container">
        
        <!-- Welcome Header -->
        <div class="d-page-header">
           <h1 v-if="activeTab === 'overview'">Overview</h1>
           <h1 v-else>Account Settings</h1>
           <p v-if="activeTab === 'overview'">Welcome back, {{ store.user?.username || 'User' }}. Here is a summary of your workspace.</p>
           <p v-else>Manage your personal information and default resume details.</p>
           <div class="d-ph-glow"></div>
        </div>

        <!-- Overview Content -->
        <div v-if="activeTab === 'overview'" class="d-fade-enter">
          
          <div class="d-card-grid">
            
            <!-- Create New Resume Card -->
            <div class="d-card d-create-card" @click="$router.push('/resume-template')">
               <div class="d-card-header">
                  <div class="d-icon-ring"><i class="ph-plus">+</i></div>
               </div>
               <div class="d-card-body">
                  <h3>Create New Resume</h3>
                  <p>Start a new document with our AI builder.</p>
               </div>
            </div>

            <!-- Profile Completion Card -->
            <div class="d-card">
               <div class="d-card-header d-flex-between">
                  <span class="d-label">Profile Strength</span>
                  <span class="d-pct-text">{{ profileCompletion }}%</span>
               </div>
               <div class="d-card-body mt-auto">
                 <div class="d-progress-track">
                    <div class="d-progress-fill" :style="{ width: profileCompletion + '%' }"></div>
                 </div>
                 <p class="d-sub-text mt-3">Complete your <a href="#" @click.prevent="activeTab = 'settings'" class="d-link">Settings</a> to increase your score.</p>
               </div>
            </div>

            <!-- Statistics Grid (Inner) -->
            <div class="d-card-subgrid">
               <!-- Total Resumes -->
               <div class="d-card d-sm-card">
                  <span class="d-label">Total Resumes</span>
                  <span class="d-value mt-auto">0</span>
               </div>
               
               <!-- Subscription -->
               <div class="d-card d-sm-card">
                  <span class="d-label">Plan</span>
                  <span class="d-value d-text-gradient mt-auto">Pro</span>
               </div>
            </div>

          </div>

          <!-- Documents Section -->
          <div class="d-section mt-12">
             <div class="d-section-header">
                <h2>Recent Documents</h2>
             </div>
             
             <div class="d-empty-state">
                <div class="d-empty-icon">📄</div>
                <p>No narratives found in your workspace.</p>
                <button class="d-btn-primary mt-4" @click="$router.push('/resume-template')">Create Document</button>
             </div>
          </div>
          
          <!-- ATS Scan History Section -->
          <div class="d-section mt-12">
             <div class="d-section-header d-flex justify-content-between align-items-center">
                <h2 class="mb-0">My ATS Scans</h2>
                <button class="d-btn-secondary btn-sm" @click="$router.push('/ats-scanner')" style="padding: 0.4rem 0.8rem; font-size: 0.85rem;">
                   <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline; margin-right:4px; vertical-align:text-bottom;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                   New Scan
                </button>
             </div>
             
             <div v-if="atsHistory.length === 0" class="d-empty-state">
                <div class="d-empty-icon">🔍</div>
                <p>No ATS scans found. Upload a resume and job description to get started.</p>
                <button class="d-btn-primary mt-4" @click="$router.push('/ats-scanner')">Try ATS Scanner</button>
             </div>
             
             <div v-else class="ats-table-container">
               <table class="ats-table">
                 <thead>
                   <tr>
                     <th>Date</th>
                     <th>Resume File</th>
                     <th>Job Target</th>
                     <th>Overall Score</th>
                     <th>Action</th>
                   </tr>
                 </thead>
                 <tbody>
                   <tr v-for="scan in atsHistory" :key="scan.id">
                     <td>{{ formatDate(scan.created_at) }}</td>
                     <td class="file-cell">{{ scan.cv_filename }}</td>
                     <td class="desc-cell">{{ scan.job_description }}</td>
                     <td>
                        <div class="score-badge" :class="getScoreClass(scan.overall_score)">
                          {{ Math.round(scan.overall_score) }}%
                        </div>
                     </td>
                     <td>
                        <button class="d-btn-secondary" @click="viewScanDetails(scan)">Details</button>
                     </td>
                   </tr>
                 </tbody>
               </table>
             </div>
          </div>
          
        </div>

        <!-- Settings Content -->
        <div v-else-if="activeTab === 'settings'" class="d-fade-enter">
           <div class="d-card d-settings-card">
              <form @submit.prevent="saveProfile" class="d-form">
                 <div class="d-form-row">
                    <div class="d-input-group">
                       <label>Full Name</label>
                       <input type="text" v-model="profileForm.fullName" placeholder="John Doe" />
                    </div>
                    <div class="d-input-group">
                       <label>Email Address</label>
                       <input type="email" :value="store.user?.email" disabled class="d-input-disabled" />
                    </div>
                 </div>
                 
                 <div class="d-form-row mt-6">
                    <div class="d-input-group">
                       <label>Phone Number</label>
                       <input type="tel" v-model="profileForm.phone" placeholder="+1 (555) 000-0000" />
                    </div>
                    <div class="d-input-group">
                       <label>Location</label>
                       <input type="text" v-model="profileForm.address" placeholder="City, State" />
                    </div>
                 </div>

                 <div class="d-form-row mt-6">
                    <div class="d-input-group">
                       <label>GitHub Profile</label>
                       <input type="text" v-model="profileForm.githubProfile" placeholder="https://github.com/..." />
                    </div>
                    <div class="d-input-group">
                       <label>LinkedIn Profile</label>
                       <input type="text" v-model="profileForm.linkedinProfile" placeholder="https://linkedin.com/in/..." />
                    </div>
                 </div>

                 <div class="d-form-row mt-6">
                    <div class="d-input-group w-50">
                       <label>Discord Username</label>
                       <input type="text" v-model="profileForm.discord" placeholder="username#1234" />
                    </div>
                 </div>

                 <div class="d-form-actions mt-8">
                    <button type="submit" class="d-btn-primary ml-auto">Save Changes</button>
                 </div>
              </form>
           </div>
        </div>

      </div>
    </main>

    <!-- Toast Notification -->
    <transition name="toast-slide">
      <div v-if="toast.visible" class="d-toast" :class="'d-toast-' + toast.type">
        <div class="d-toast-icon">
          <span v-if="toast.type === 'success'">✓</span>
          <span v-else>!</span>
        </div>
        <div class="d-toast-content">
          <div class="d-toast-title">{{ toast.title }}</div>
          <div class="d-toast-msg">{{ toast.message }}</div>
        </div>
        <button class="d-toast-close" @click="toast.visible = false">&times;</button>
      </div>
    </transition>

  </div>
</template>

<script>
import { store } from '@/store';
import axios from 'axios';

export default {
  name: 'Dashboard',
  data() {
    return {
      store,
      activeTab: 'overview',
      toast: { visible: false, type: 'success', title: '', message: '' },
      toastTimer: null,
      atsHistory: [],
      profileForm: {
        fullName: store.user?.fullName || '',
        phone: store.user?.phone || '',
        address: store.user?.address || '',
        githubProfile: store.user?.githubProfile || '',
        linkedinProfile: store.user?.linkedinProfile || '',
        discord: store.user?.discord || ''
      }
    }
  },
  computed: {
    userInitials() {
      if (!this.store.user) return 'U';
      const nameObj = this.store.user;
      let displayName = nameObj.fullName || nameObj.username || nameObj.email || 'User';
      if (typeof displayName === 'string' && displayName.length > 0) {
         return displayName.charAt(0).toUpperCase();
      }
      return 'U';
    },
    profileCompletion() {
      const form = this.profileForm;
      let filled = 0;
      const totalFields = 7;
      if (this.store.user?.email) filled++;
      if (form.fullName && form.fullName.trim()) filled++;
      if (form.phone && form.phone.trim()) filled++;
      if (form.address && form.address.trim()) filled++;
      if (form.githubProfile && form.githubProfile.trim()) filled++;
      if (form.linkedinProfile && form.linkedinProfile.trim()) filled++;
      if (form.discord && form.discord.trim()) filled++;
      
      return Math.round((filled / totalFields) * 100);
    }
  },
  mounted() {
    this.fetchProfile();
    this.fetchATSHistory();
  },
  methods: {
    async fetchProfile() {
      if (store.user?.id) {
        try {
          const response = await axios.get(`http://localhost:5000/account/details/${store.user.id}`);
          if (response.data.success) {
             const data = response.data.data;
             this.profileForm.fullName = data.full_name || store.user.fullName || '';
             this.profileForm.phone = data.phone || store.user.phone || '';
             this.profileForm.address = data.address || store.user.address || '';
             this.profileForm.githubProfile = data.github_profile || store.user.githubProfile || '';
             this.profileForm.linkedinProfile = data.linkedin_profile || store.user.linkedinProfile || '';
             this.profileForm.discord = data.discord || store.user.discord || '';
             store.updateProfile(this.profileForm);
          }
        } catch (err) {
          console.error("Could not fetch profile", err);
        }
      }
    },
    showToast(type, title, message) {
      if(this.toastTimer) clearTimeout(this.toastTimer);
      this.toast = { visible: true, type, title, message };
      this.toastTimer = setTimeout(() => {
        this.toast.visible = false;
      }, 4000);
    },
    async saveProfile() {
      try {
        if (!store.user?.id) {
          this.showToast('error', 'Authentication Error', 'Please login first.');
          return;
        }
        const response = await axios.post(`http://localhost:5000/account/details/${store.user.id}`, this.profileForm);
        if (response.data.success) {
          store.updateProfile(this.profileForm);
          this.showToast('success', 'Profile Updated', 'Your settings have been saved successfully.');
        } else {
          this.showToast('error', 'Update Failed', 'Failed to save changes. Please try again.');
        }
      } catch (err) {
        console.error("Error updating profile", err);
        this.showToast('error', 'Server Error', 'Could not connect to the server.');
      }
    },
    handleLogout() {
      store.logout();
      this.$router.push('/');
    },
    async fetchATSHistory() {
      if (store.user?.id) {
        try {
          const response = await axios.get(`http://localhost:5000/api/ats-history`, { withCredentials: true });
          if (response.data.success) {
            this.atsHistory = response.data.history;
          }
        } catch (err) {
          console.error("Could not fetch ATS history", err);
        }
      }
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    getScoreClass(score) {
      if (score >= 80) return 'score-success';
      if (score >= 40) return 'score-warning';
      return 'score-danger';
    },
    viewScanDetails(scan) {
      // In a real app, this might open a modal or navigate to a detailed view
      this.showToast('success', 'Scan Overview', `Overall: ${Math.round(scan.overall_score)}% | Semantic: ${Math.round(scan.semantic_score)}% | Keywords: ${Math.round(scan.keyword_score)}%`);
    }
  }
};
</script>

<style scoped>
/* Base Reset & Variables for Dashboard Theme using Global SaaS tokens */
.d-minimal-wrapper {
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-primary);
  box-sizing: border-box;
}

* { box-sizing: border-box; }

/* Top Header Navigation */
.d-header-nav {
  position: sticky;
  top: 0;
  width: 100%;
  height: 72px;
  background: rgba(2, 6, 23, 0.7); /* Deep dark background with high transparency */
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
  z-index: 50;
  display: flex;
  align-items: center;
}

.d-nav-container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.d-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}
.d-logo { height: 24px; filter: invert(1); }
.d-brand-text { font-family: var(--font-heading); font-weight: 700; font-size: 1.25rem; letter-spacing: -0.02em; color: var(--text-main); }

.d-nav-right {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.d-nav-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.d-nav-link {
  background: none; border: none; color: var(--text-muted); font-size: 0.95rem; font-weight: 600;
  cursor: pointer; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); font-family: var(--font-primary);
}
.d-nav-link:hover, .d-nav-link.active { color: var(--text-main); text-shadow: 0 0 10px rgba(255,255,255,0.3); }
.d-text-error { color: #f87171; }
.d-text-error:hover { color: #ef4444; text-shadow: 0 0 10px rgba(239, 68, 68, 0.4); }

.d-divider { width: 1px; height: 16px; background: var(--border-subtle); }

.d-user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 16px 6px 6px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  transition: all 0.3s;
}
.d-user-profile:hover { background: rgba(255, 255, 255, 0.08); border-color: rgba(255, 255, 255, 0.2); }
.d-avatar {
  width: 34px; height: 34px; border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--tertiary));
  display: flex; justify-content: center; align-items: center;
  font-size: 1rem; font-weight: 700; color: #fff; text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}
.d-user-info { display: flex; flex-direction: column; }
.d-user-name { font-size: 0.9rem; font-weight: 700; line-height: 1; margin-bottom: 3px; font-family: var(--font-secondary); }
.d-user-plan { font-size: 0.7rem; color: var(--accent); font-weight: 600; line-height: 1; text-transform: uppercase; letter-spacing: 0.05em; }

/* Main Workspace */
.d-main-content {
  padding: 5rem 2rem 8rem;
}
.d-workspace-container {
  max-width: 1050px;
  margin: 0 auto;
}

/* Typography & Headers */
.d-page-header { margin-bottom: 4rem; position: relative; }
.d-page-header h1 { font-family: var(--font-heading); font-size: 3rem; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 0.5rem; text-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.d-page-header p { color: var(--text-muted); font-size: 1.1rem; max-width: 600px; font-weight: 400; }
.d-ph-glow {
  position: absolute; top: -100px; left: -50px; width: 300px; height: 300px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%); filter: blur(40px); border-radius: 50%; pointer-events: none; z-index: -1;
}

/* Cards System */
.d-card-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.d-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: var(--glass-border);
  box-shadow: var(--shadow-premium);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
}
.d-card::before {
  content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 100%); pointer-events: none;
}
.d-card:hover { transform: translateY(-5px); border-color: rgba(255,255,255,0.2); box-shadow: 0 30px 60px rgba(0,0,0,0.6), 0 0 30px var(--accent-glow); }

/* Specific Cards */
.d-create-card {
  cursor: pointer;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(236, 72, 153, 0.1) 100%);
  border: 1px solid rgba(99, 102, 241, 0.3);
}
.d-create-card:hover { border-color: rgba(99, 102, 241, 0.6); }
.d-icon-ring {
  width: 60px; height: 60px; border-radius: 50%; background: #ffffff;
  display: flex; align-items: center; justify-content: center; font-size: 2rem; color: #000;
  margin-bottom: 2rem; transition: all 0.4s; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}
.d-create-card:hover .d-icon-ring { transform: rotate(90deg) scale(1.1); box-shadow: 0 0 30px rgba(255,255,255,0.6); }
.d-card-body h3 { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 700; margin-bottom: 0.35rem; }
.d-card-body p { font-size: 1rem; color: var(--text-main); opacity: 0.8; }

/* Subgrid for smaller metrics */
.d-card-subgrid { display: grid; grid-template-rows: 1fr 1fr; gap: 2rem; }
.d-sm-card { padding: 1.75rem; }

/* Elements within cards */
.d-label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--text-muted); font-weight: 700; }
.d-value { font-family: var(--font-heading); font-size: 2.8rem; font-weight: 700; letter-spacing: -0.03em; line-height: 1; }
.d-text-gradient { background: linear-gradient(135deg, var(--accent), var(--tertiary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.d-pct-text { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; }

.d-progress-track { width: 100%; height: 8px; background: rgba(0,0,0,0.3); border-radius: 99px; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.5); }
.d-progress-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--tertiary)); border-radius: 99px; transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 0 10px var(--accent-glow); }
.d-sub-text { font-size: 0.9rem; color: var(--text-muted); }
.d-link { color: var(--accent); text-decoration: none; font-weight: 600; transition: color 0.3s; }
.d-link:hover { color: var(--text-main); text-shadow: 0 0 10px var(--accent-glow); }

.d-flex-between { display: flex; justify-content: space-between; align-items: center; }

/* Sections */
.d-section-header h2 { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; margin-bottom: 2rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem; }
.d-empty-state {
  background: var(--glass-bg); backdrop-filter: var(--glass-blur); border: 1px dashed var(--border-subtle);
  border-radius: 20px; padding: 5rem 2rem; text-align: center; color: var(--text-muted);
}
.d-empty-icon { font-size: 3rem; margin-bottom: 1.5rem; opacity: 0.7; }
.d-btn-primary { 
  background: linear-gradient(135deg, var(--accent), var(--tertiary)); color: #fff; border: none; 
  padding: 0.85rem 1.75rem; border-radius: 12px; font-size: 1rem; font-weight: 600; 
  cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
  font-family: var(--font-primary);
}
.d-btn-primary:hover { box-shadow: 0 8px 25px rgba(236, 72, 153, 0.5); transform: translateY(-2px); }

.d-btn-secondary {
  background: rgba(255,255,255,0.05); color: var(--text-main); border: 1px solid var(--border-subtle);
  padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; font-family: var(--font-primary);
}
.d-btn-secondary:hover { background: rgba(255,255,255,0.1); border-color: var(--accent); }

/* ATS Table Styles */
.ats-table-container {
  width: 100%;
  overflow-x: auto;
  border-radius: 12px;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border-subtle);
}
.ats-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}
.ats-table th {
  padding: 1rem 1.5rem;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border-subtle);
  font-weight: 600;
}
.ats-table td {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,0.03);
  font-size: 0.95rem;
  color: var(--text-main);
  vertical-align: middle;
}
.ats-table tbody tr:last-child td { border-bottom: none; }
.ats-table tbody tr:hover td { background: rgba(255,255,255,0.02); }

.file-cell { font-family: var(--font-secondary); font-weight: 500; color: var(--accent); }
.desc-cell { color: var(--text-dim); max-width: 300px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

.score-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.35rem 0.75rem;
  border-radius: 99px;
  font-weight: 700;
  font-size: 0.85rem;
}
.score-success { background: rgba(16, 185, 129, 0.15); color: #34D399; }
.score-warning { background: rgba(245, 158, 11, 0.15); color: #FBBF24; }
.score-danger { background: rgba(239, 68, 68, 0.15); color: #F87171; }

/* Forms */
.d-settings-card { max-width: 850px; padding: 3rem; }
.d-form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.d-input-group { display: flex; flex-direction: column; gap: 8px; }
.d-input-group label { font-size: 0.85rem; font-weight: 600; color: var(--text-muted); letter-spacing: 0.05em; text-transform: uppercase; }
.d-input-group input { 
  background: rgba(0,0,0,0.3); border: 1px solid var(--border-subtle); padding: 0.85rem 1rem; 
  border-radius: 8px; color: var(--text-main); font-family: var(--font-primary); font-size: 1rem;
  transition: all 0.3s;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
}
.d-input-group input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent), 0 0 15px var(--accent-glow); background: rgba(0,0,0,0.5); }
.d-input-disabled { opacity: 0.5; cursor: not-allowed; }

.w-50 { grid-column: span 1; }
.d-form-actions { display: flex; align-items: center; justify-content: flex-end; border-top: 1px solid var(--border-subtle); padding-top: 2rem;}
.ml-auto { margin-left: auto; }

/* Utilities */
.mt-3 { margin-top: 0.75rem; }
.mt-4 { margin-top: 1.25rem; }
.mt-6 { margin-top: 1.75rem; }
.mt-8 { margin-top: 2.25rem; }
.mt-10 { margin-top: 2.75rem; }
.mt-12 { margin-top: 3.5rem; }
.mt-auto { margin-top: auto; }

/* Animations */
.d-fade-enter { animation: fade 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; }
@keyframes fade { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

/* Toast Notification */
.d-toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 9999;
}
.d-toast-success { border-bottom: 2px solid #10B981; }
.d-toast-error { border-bottom: 2px solid #EF4444; }

.d-toast-icon {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 0.9rem;
  color: #fff;
}
.d-toast-success .d-toast-icon { background: rgba(16, 185, 129, 0.2); color: #10B981; }
.d-toast-error .d-toast-icon { background: rgba(239, 68, 68, 0.2); color: #EF4444; }

.d-toast-content { display: flex; flex-direction: column; }
.d-toast-title { font-weight: 700; font-size: 0.95rem; color: var(--text-main); margin-bottom: 2px; }
.d-toast-msg { font-size: 0.85rem; color: var(--text-muted); }

.d-toast-close {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 1.2rem;
  cursor: pointer;
  margin-left: 0.5rem;
  transition: color 0.2s;
}
.d-toast-close:hover { color: var(--text-main); }

.toast-slide-enter-active, .toast-slide-leave-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.toast-slide-enter-from, .toast-slide-leave-to { opacity: 0; transform: translateY(20px) scale(0.95); }

/* Mobile */
@media(max-width: 768px) {
  .d-card-grid { grid-template-columns: 1fr; }
  .d-card-subgrid { grid-template-columns: 1fr 1fr; grid-template-rows: auto; }
  .d-nav-links { display: none; }
  .d-form-row { grid-template-columns: 1fr; }
  .d-main-content { padding: 3rem 1.5rem 5rem; }
  .d-nav-right { gap: 1rem; }
}
</style>
