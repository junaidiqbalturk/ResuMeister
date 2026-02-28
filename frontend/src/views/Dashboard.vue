<template>
  <div class="dashboard-wrapper">
    <!-- Atmosphere -->
    <div class="atmosphere">
      <div class="aura aura-1"></div>
      <div class="aura aura-2"></div>
    </div>

    <!-- Dashboard App Shell -->
    <div class="app-shell">
      <!-- Sidebar Chrome -->
      <aside class="sidebar reveal-left">
        <div class="sidebar-brand">
          <img src="/resumeister.png" alt="ResuMeister" class="s-logo" />
          <span>ResuMeister</span>
        </div>
        
        <nav class="sidebar-nav">
          <a href="#" class="s-nav-link" :class="{ active: activeTab === 'overview' }" @click.prevent="activeTab = 'overview'">
            <span class="s-icon">▤</span> Overview
          </a>
          <a href="/resume-template" class="s-nav-link">
            <span class="s-icon">⚡</span> New Resume
          </a>
          <a href="#" class="s-nav-link" :class="{ active: activeTab === 'settings' }" @click.prevent="activeTab = 'settings'">
            <span class="s-icon">⚙</span> Settings
          </a>
          <a href="#" class="s-nav-link mt-auto s-logout" @click.prevent="handleLogout">
            <span class="s-icon">↩</span> Logout
          </a>
        </nav>

        <div class="sidebar-footer">
          <div class="user-profile">
            <div class="avatar">{{ userInitials }}</div>
            <div class="u-info">
              <p class="u-name">{{ store.user?.fullName || store.user?.username || 'Guest' }}</p>
              <p class="u-plan">Pro Plan</p>
            </div>
          </div>
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="dashboard-main">
        <header class="dash-header container reveal-up">
           <div class="h-left">
              <h1 v-if="activeTab === 'overview'">Workspace Overview</h1>
              <h1 v-else>Account Settings</h1>
              <p v-if="activeTab === 'overview'">Welcome back, {{ store.user?.username || 'Commander' }}. Your career engine is optimal.</p>
              <p v-else>Manage your profile and default resume data.</p>
           </div>
           <div class="h-right">
              <button class="btn-create-saas" @click="$router.push('/resume-template')">
                <span>+</span> New Strategy
              </button>
           </div>
        </header>

        <section class="container scroll-area">
           <!-- Tab: Overview -->
           <div v-if="activeTab === 'overview'">
             <!-- Statistics Bento -->
             <div class="bento-grid">
                <div class="bento-item stat-card reveal-up">
                   <p class="label">Total Resumes</p>
                   <div class="val-group">
                      <span class="value">12</span>
                      <span class="trend">+2 this week</span>
                   </div>
                </div>
                <div class="bento-item stat-card reveal-up">
                   <p class="label">ATS Optimization</p>
                   <div class="val-group">
                      <span class="value">94%</span>
                      <span class="trend pos">Deep-sync active</span>
                   </div>
                </div>
                <div class="bento-item bento-wide activity-card reveal-up">
                   <h3>Recent Activity</h3>
                   <div class="activity-list">
                      <div class="act-item">
                         <span class="act-dot"></span>
                         <p>Resume <strong>"Software_Eng_v2"</strong> exported as PDF</p>
                         <span class="act-time">2h ago</span>
                      </div>
                      <div class="act-item">
                         <span class="act-dot"></span>
                         <p>Mock Interview <strong>"Google_PM"</strong> session completed</p>
                         <span class="act-time">Yesterday</span>
                      </div>
                   </div>
                </div>
                <div class="bento-item promo-card reveal-up">
                   <img src="/resumeister.png" alt="" class="p-logo">
                   <h3>Unlock AI Design</h3>
                   <p>Get access to our neural-link design suggestions.</p>
                   <button class="btn-sm-primary">Upgrade</button>
                </div>
             </div>

             <!-- Resume Repository -->
             <div class="repo-section reveal-up">
                <div class="section-title">
                   <h2>Active Narratives</h2>
                   <a href="#" class="view-all">View All</a>
                </div>
                <div class="resume-list">
                   <div class="resume-row" v-for="i in 3" :key="i">
                      <div class="r-info">
                         <div class="r-icon">📄</div>
                         <div>
                            <p class="r-name">Principal_Software_Strategist_0{{i}}</p>
                            <p class="r-meta">Modified Feb 21, 2024 • 2:45 PM</p>
                         </div>
                      </div>
                      <div class="r-actions">
                         <button class="btn-row-ghost" @click="$router.push('/resume-template/fill-resume?template=1')">Edit</button>
                         <button class="btn-row-ghost">Export</button>
                      </div>
                   </div>
                </div>
             </div>
           </div>

           <!-- Tab: Settings -->
           <div v-else-if="activeTab === 'settings'" class="settings-view reveal-up">
              <div class="settings-card bento-item">
                 <h3>Contact Information</h3>
                 <p class="mb-4 text-muted">This data will automatically pre-fill when you create a new resume.</p>
                 
                 <form @submit.prevent="saveProfile" class="profile-form">
                    <div class="form-row">
                      <div class="input-group">
                        <label>Full Name</label>
                        <input type="text" v-model="profileForm.fullName" placeholder="John Doe" />
                      </div>
                      <div class="input-group">
                        <label>Email Address</label>
                        <input type="email" v-bind:value="store.user?.email" disabled class="disabled-input"/>
                      </div>
                    </div>
                    
                    <div class="form-row">
                      <div class="input-group">
                        <label>Phone Number</label>
                        <input type="tel" v-model="profileForm.phone" placeholder="+1 (555) 000-0000" />
                      </div>
                      <div class="input-group">
                        <label>Location / Address</label>
                        <input type="text" v-model="profileForm.address" placeholder="San Francisco, CA" />
                      </div>
                    </div>

                    <div v-if="saveMessage" class="save-msg mb-4">{{ saveMessage }}</div>

                    <div class="form-actions mt-4">
                      <button type="submit" class="btn-create-saas">Save Changes</button>
                    </div>
                 </form>
              </div>
           </div>

        </section>
      </main>
    </div>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import { store } from '@/store';

export default {
  name: 'Dashboard',
  data() {
    return {
      store,
      activeTab: 'overview',
      saveMessage: '',
      profileForm: {
        fullName: store.user?.fullName || '',
        phone: store.user?.phone || '',
        address: store.user?.address || ''
      }
    }
  },
  computed: {
    userInitials() {
      const name = this.store.user?.fullName || this.store.user?.username || 'G';
      return name.charAt(0).toUpperCase();
    }
  },
  mounted() {
    this.executeAnimations();
  },
  methods: {
    executeAnimations() {
      gsap.from('.reveal-left', { x: -50, opacity: 0, duration: 1, ease: 'expo.out' });
      gsap.from('.reveal-up', { y: 20, opacity: 0, duration: 0.8, stagger: 0.1, ease: 'power3.out' });
    },
    saveProfile() {
      store.updateProfile({
        fullName: this.profileForm.fullName,
        phone: this.profileForm.phone,
        address: this.profileForm.address
      });
      this.saveMessage = 'Profile updated successfully!';
      setTimeout(() => this.saveMessage = '', 3000);
    },
    handleLogout() {
      store.logout();
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.dashboard-wrapper {
  height: 100vh;
  background-color: #030712;
  color: #F8FAFC;
  font-family: 'Outfit', sans-serif;
  overflow: hidden;
  position: relative;
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
.aura { position: absolute; border-radius: 50%; filter: blur(120px); opacity: 0.08; }
.aura-1 { width: 600px; height: 600px; background: #6366F1; top: -10%; left: -10%; }
.aura-2 { width: 500px; height: 500px; background: #EC4899; bottom: -10%; right: -10%; }

.app-shell {
  display: flex;
  height: 100%;
  position: relative;
  z-index: 10;
}

/* Sidebar */
.sidebar {
  width: 280px;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(20px);
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  flex-direction: column;
  padding: 2.5rem;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 4rem;
}
.s-logo { height: 24px; filter: brightness(100); }
.sidebar-brand span { font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; font-weight: 700; }

.sidebar-nav { flex: 1; display: flex; flex-direction: column; gap: 10px; }
.s-nav-link {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 12px 16px;
  color: #64748B;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.3s;
}
.s-nav-link:hover { color: #fff; background: rgba(255,255,255,0.03); }
.s-nav-link.active { color: #fff; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.05); }
.s-icon { font-size: 1rem; opacity: 0.7; }

.sidebar-footer { border-top: 1px solid rgba(255,255,255,0.05); padding-top: 2rem; }
.user-profile { display: flex; align-items: center; gap: 12px; }
.avatar { width: 40px; height: 40px; background: #6366F1; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.8rem; }
.u-name { font-weight: 600; font-size: 0.9rem; }
.u-plan { font-size: 0.75rem; color: #64748B; font-weight: 500; }

/* Main Area */
.dashboard-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.container { max-width: 1000px; margin: 0 auto; padding: 0 4rem; }

.dash-header { padding-top: 5rem; padding-bottom: 3.5rem; display: flex; justify-content: space-between; align-items: flex-end; }
.dash-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; }
.dash-header p { color: #94A3B8; font-size: 1.1rem; }

.btn-create-saas {
  background: #fff;
  color: #030712;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.3s;
}
.btn-create-saas:hover { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(255,255,255,0.15); }

/* Bento Grid */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 4rem;
}

.bento-item {
  background: rgba(15, 23, 42, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 24px;
  padding: 2rem;
  transition: all 0.3s;
}
.bento-item:hover { border-color: rgba(255,255,255,0.1); background: rgba(15, 23, 42, 0.4); }

.stat-card .label { font-size: 0.8rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1.5rem; }
.val-group { display: flex; flex-direction: column; gap: 5px; }
.value { font-size: 2.2rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; }
.trend { font-size: 0.75rem; color: #64748B; font-weight: 600; }
.trend.pos { color: #10B981; }

.bento-wide { grid-column: span 2; }
.bento-wide h3 { font-size: 1.1rem; margin-bottom: 2rem; }
.activity-list { display: flex; flex-direction: column; gap: 1.5rem; }
.act-item { display: flex; align-items: center; gap: 1rem; font-size: 0.95rem; }
.act-dot { width: 6px; height: 6px; background: #6366F1; border-radius: 50%; }
.act-time { margin-left: auto; font-size: 0.8rem; color: #475569; }

.promo-card { background: linear-gradient(135deg, #6366F1, #EC4899); border: none; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 15px; }
.p-logo { height: 24px; filter: brightness(100); }
.promo-card h3 { font-size: 1.2rem; font-weight: 700; color: #fff; }
.promo-card p { font-size: 0.85rem; color: rgba(255,255,255,0.8); }
.btn-sm-primary { background: #fff; border: none; padding: 6px 16px; border-radius: 6px; font-weight: 700; font-size: 0.75rem; cursor: pointer; }

/* Repository */
.repo-section { margin-bottom: 8rem; }
.section-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
.section-title h2 { font-size: 1.4rem; font-weight: 700; }
.view-all { font-size: 0.85rem; color: #6366F1; font-weight: 600; text-decoration: none; }

.resume-list { display: flex; flex-direction: column; gap: 12px; }
.resume-row {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.04);
  padding: 1.25rem 2rem;
  border-radius: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s;
}
.resume-row:hover { background: rgba(255, 255, 255, 0.04); border-color: rgba(255, 255, 255, 0.1); }

.r-info { display: flex; align-items: center; gap: 1.5rem; }
.r-icon { font-size: 1.2rem; }
.r-name { font-weight: 600; font-size: 1rem; margin-bottom: 4px; }
.r-meta { font-size: 0.8rem; color: #475569; }

.r-actions { display: flex; gap: 10px; }
.btn-row-ghost { background: transparent; border: 1px solid rgba(255,255,255,0.06); color: #94A3B8; padding: 6px 14px; border-radius: 6px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: all 0.3s; }
.btn-row-ghost:hover { color: #fff; border-color: rgba(255,255,255,0.2); background: rgba(255,255,255,0.02); }

@media (max-width: 1024px) {
  .sidebar { display: none; }
  .dash-header { padding-top: 3rem; flex-direction: column; align-items: flex-start; gap: 2rem; }
  .bento-grid { grid-template-columns: 1fr; }
  .bento-wide { grid-column: span 1; }
  .resume-row { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
  .r-actions { width: 100%; display: grid; grid-template-columns: 1fr 1fr; }
}

/* Settings View Elements */
.settings-view { margin-bottom: 8rem; }
.settings-card { max-width: 800px; }
.settings-card h3 { font-size: 1.4rem; font-weight: 700; margin-bottom: 0.5rem; }
.text-muted { color: #94A3B8; font-size: 0.95rem; }
.mb-4 { margin-bottom: 2rem; }
.mt-4 { margin-top: 2rem; }

.profile-form { display: flex; flex-direction: column; gap: 2rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }

.input-group { display: flex; flex-direction: column; gap: 8px; }
.input-group label { font-size: 0.85rem; font-weight: 600; color: #E2E8F0; }
.input-group input { 
  background: rgba(15, 23, 42, 0.6); 
  border: 1px solid rgba(255,255,255,0.1); 
  padding: 12px 16px; 
  border-radius: 8px; 
  color: #F8FAFC; 
  font-family: 'Outfit', sans-serif;
  transition: all 0.3s;
}
.input-group input:focus { outline: none; border-color: #6366F1; background: rgba(15, 23, 42, 0.9); }
.disabled-input { background: rgba(0,0,0,0.2) !important; color: #64748B !important; cursor: not-allowed; }

.save-msg { color: #10B981; font-weight: 600; font-size: 0.9rem; padding: 10px 14px; background: rgba(16, 185, 129, 0.1); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.2); }
.s-logout:hover { color: #EF4444 !important; background: rgba(239, 68, 68, 0.1) !important; }
</style>
