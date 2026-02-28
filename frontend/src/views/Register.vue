<template>
  <div class="auth-layout">
    <div class="auth-side visual-side">
      <div class="visual-content">
        <router-link to="/" class="logo mb-5">
          <div class="logo-icon">R</div>
          <span>ResuMeister</span>
        </router-link>
        
        <h2>Start your career <br/>upgrade today.</h2>
        <p>Join thousands of professionals landing their dream jobs faster than ever.</p>
        
        <div class="feature-ticks">
           <div class="tick"><span>✓</span> Free 14-day trial on Pro features</div>
           <div class="tick"><span>✓</span> Instant PDF & DOCX downloads</div>
           <div class="tick"><span>✓</span> Real-time ATS optimization</div>
        </div>
      </div>
      <div class="pattern-overlay"></div>
    </div>
    
    <div class="auth-side form-side">
      <div class="form-wrapper">
        <div class="mobile-logo">
          <div class="logo-icon">R</div> ResuMeister
        </div>
        
        <h1 class="auth-title">Create an Account</h1>
        <p class="auth-subtitle">Already have an account? <router-link to="/login" class="link">Log in</router-link></p>

        <form @submit.prevent="handleRegister" class="auth-form">
          
          <div class="input-group floating">
            <input type="text" id="name" v-model="name" placeholder=" " required />
            <label for="name">Full Name</label>
          </div>

          <div class="input-group floating">
            <input type="email" id="email" v-model="email" placeholder=" " required />
            <label for="email">Email address</label>
          </div>
          
          <div class="input-group floating">
            <input type="password" id="password" v-model="password" placeholder=" " required />
            <label for="password">Password</label>
            <div class="password-strength" v-if="password.length > 0">
              <div class="str-meter" :class="{ 'good': password.length > 5, 'strong': password.length > 8 }"></div>
              <span>{{ password.length > 8 ? 'Strong' : password.length > 5 ? 'Good' : 'Weak' }}</span>
            </div>
          </div>

          <button type="submit" class="btn-primary-large full-width">Create Account</button>
          
          <p class="terms">By creating an account, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.</p>
        </form>

        <div class="divider"><span>or sign up with</span></div>

        <div class="social-row">
          <button class="social-btn"><span class="g-icon">G</span> Google</button>
          <button class="social-btn"><span class="g-icon">in</span> LinkedIn</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterView',
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      console.log('Registering', this.email);
      this.$router.push('/dashboard');
    }
  }
}
</script>

<style scoped>
/* Inherit base structures from login via duplicate or global if needed, but scoped here for isolation */
.auth-layout {
  display: flex;
  min-height: 100vh;
  width: 100%;
}

.auth-side {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.visual-side {
  background: linear-gradient(135deg, var(--bg-deep) 0%, rgba(99, 102, 241, 0.1) 100%);
  position: relative;
  overflow: hidden;
  padding: 4rem;
  justify-content: center;
  border-right: 1px solid rgba(255,255,255,0.05);
}

.visual-content {
  position: relative;
  z-index: 2;
  max-width: 480px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.5rem;
  color: var(--text-main);
}

.logo-icon {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, var(--accent), var(--secondary));
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: white;
}

.mb-5 { margin-bottom: 4rem; }

.visual-side h2 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.visual-side p {
  color: var(--text-muted);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 3rem;
}

.feature-ticks { display: flex; flex-direction: column; gap: 1rem; }
.tick { display: flex; align-items: center; gap: 12px; font-weight: 500; font-size: 1.05rem; }
.tick span { color: #10B981; background: rgba(16, 185, 129, 0.1); padding: 4px; border-radius: 50%; font-size: 0.8rem; display: flex;}

.pattern-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
  background-size: 30px 30px;
  opacity: 0.4;
  z-index: 1;
}

.form-side {
  background: var(--bg-deep);
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
}

.form-wrapper { width: 100%; max-width: 420px; }

.mobile-logo { display: none; align-items: center; gap: 0.5rem; font-family: var(--font-heading); font-weight: bold; font-size: 1.5rem; margin-bottom: 2rem; }

.auth-title { font-size: 2.2rem; margin-bottom: 0.5rem; }

.auth-subtitle { color: var(--text-muted); margin-bottom: 2.5rem; }

.link { color: var(--accent); font-weight: 500; text-decoration: none; }
.link:hover { text-decoration: underline; }

.floating { position: relative; margin-bottom: 1.5rem; }
.floating input {
  width: 100%; padding: 1.25rem 1rem 0.6rem;
  background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; color: white; font-size: 1rem; transition: all 0.3s;
}
.floating input:focus { outline: none; border-color: var(--accent); background: rgba(15, 23, 42, 0.9); }
.floating label {
  position: absolute; top: 50%; left: 1rem; transform: translateY(-50%);
  color: var(--text-muted); font-size: 1rem; pointer-events: none; transition: 0.2s ease all;
}
.floating input:focus ~ label, .floating input:not(:placeholder-shown) ~ label { top: 12px; font-size: 0.75rem; color: var(--accent); }

.password-strength {
  display: flex; align-items: center; gap: 10px; margin-top: 8px; font-size: 0.8rem; color: var(--text-dim);
}
.str-meter { flex: 1; height: 4px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; position: relative;}
.str-meter::after { content:''; position: absolute; top:0;left:0;height:100%; width: 33%; background: #EF4444; transition: 0.3s;}
.str-meter.good::after { width: 66%; background: #F59E0B; }
.str-meter.strong::after { width: 100%; background: #10B981; }

.btn-primary-large { background: var(--text-main); color: var(--bg-deep) !important; padding: 1rem; border-radius: 12px; font-weight: bold; font-size: 1.05rem; }
.full-width { width: 100%; }

.terms { font-size: 0.8rem; color: var(--text-dim); text-align: center; margin-top: 1rem; }
.terms a { color: var(--text-muted); text-decoration: underline; }

.divider { display: flex; align-items: center; margin: 2rem 0; color: var(--text-dim); font-size: 0.85rem; }
.divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid rgba(255,255,255,0.1); }
.divider span { padding: 0 1rem; }

.social-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.social-btn {
  padding: 0.8rem; border-radius: 12px; background: var(--bg-card); border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-main); font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem;
}
.social-btn:hover { background: rgba(255,255,255,0.05); }
.g-icon { background: white; color: black; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }

@media (max-width: 900px) { .visual-side { display: none; } .mobile-logo { display: flex; } }
</style>
