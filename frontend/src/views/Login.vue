<template>
  <div class="auth-layout">
    <div class="auth-side visual-side">
      <div class="visual-content">
        <router-link to="/" class="logo mb-5">
          <div class="logo-icon">R</div>
          <span>ResuMeister</span>
        </router-link>
        
        <h2>Welcome back.</h2>
        <p>Access your resume dashboard and continue your career journey.</p>
        
        <div class="testimonial-card">
          <p>"ResuMeister helped me land a Senior Dev role at a FAANG company completely stress-free."</p>
          <div class="author">- Alex D., Software Engineer</div>
        </div>
      </div>
      <div class="pattern-overlay"></div>
    </div>
    
    <div class="auth-side form-side">
      <div class="form-wrapper">
        <div class="mobile-logo">
          <div class="logo-icon">R</div> ResuMeister
        </div>
        
        <h1 class="auth-title">Log In</h1>
        <p class="auth-subtitle">Don't have an account? <router-link to="/register" class="link">Sign up</router-link></p>

        <button class="social-btn">
          <span class="g-icon">G</span> Continue with Google
        </button>
        <button class="social-btn">
          <span class="g-icon">in</span> Continue with LinkedIn
        </button>

        <div class="divider"><span>or sign in with email</span></div>

        <form @submit.prevent="handleLogin" class="auth-form">
          <div class="input-group floating">
            <input type="email" id="email" v-model="email" placeholder=" " required />
            <label for="email">Email address</label>
          </div>
          
          <div class="input-group floating">
            <input type="password" id="password" v-model="password" placeholder=" " required />
            <label for="password">Password</label>
          </div>

          <div v-if="errorMessage" class="error-msg">
            {{ errorMessage }}
          </div>

          <div class="form-actions">
            <label class="checkbox-wrapper">
              <input type="checkbox" /> Keep me signed in
            </label>
            <a href="#" class="link forgot">Forgot password?</a>
          </div>

          <button type="submit" class="btn-primary-large full-width" :disabled="isLoading">
            {{ isLoading ? 'Signing In...' : 'Sign In' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { store } from '@/store.js';

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
      isLoading: false
    }
  },
  methods: {
    async handleLogin() {
      this.errorMessage = '';
      this.isLoading = true;

      try {
        const response = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        });
        
        if (response.data.success) {
          // Fake fetching additional profile data from this login endpoint for now
          // We can expand the backend to return literal DB values (Name, phone, etc.)
          store.login({
            email: this.email,
            username: this.email.split('@')[0], 
            // In a real scenario, the backend might return `id`, `fullName`, `phone`, `address` here
          });
          
          this.$router.push('/dashboard');
        } else {
          this.errorMessage = response.data.message || 'Invalid credentials';
        }
      } catch (err) {
        if (err.response && err.response.data) {
          this.errorMessage = err.response.data.message || 'Invalid credentials';
        } else {
          this.errorMessage = 'Network error. Please ensure backend is running.';
        }
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>

<style scoped>
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

/* Visual Side */
.visual-side {
  background: linear-gradient(135deg, var(--bg-deep) 0%, #0f172a 100%);
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
  margin-bottom: 4rem;
}

.testimonial-card {
  background: rgba(255,255,255,0.03);
  border-left: 4px solid var(--accent);
  padding: 1.5rem;
  border-radius: 0 12px 12px 0;
}

.testimonial-card p {
  font-size: 0.95rem;
  font-style: italic;
  margin-bottom: 0.5rem;
  color: var(--text-main);
}

.author {
  font-size: 0.85rem;
  color: var(--text-dim);
  font-weight: 600;
}

.pattern-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
  background-size: 30px 30px;
  opacity: 0.4;
  z-index: 1;
}

/* Form Side */
.form-side {
  background: var(--bg-deep);
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
}

.form-wrapper {
  width: 100%;
  max-width: 420px;
}

.mobile-logo {
  display: none;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-heading);
  font-weight: bold;
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

.auth-title {
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
}

.auth-subtitle {
  color: var(--text-muted);
  margin-bottom: 2.5rem;
}

.link {
  color: var(--accent);
  font-weight: 500;
  text-decoration: none;
}
.link:hover { text-decoration: underline; }

.social-btn {
  width: 100%;
  padding: 1rem;
  border-radius: 12px;
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-main);
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.social-btn:hover {
  background: rgba(255,255,255,0.05);
}

.g-icon { background: white; color: black; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }

.divider {
  display: flex;
  align-items: center;
  margin: 2rem 0;
  color: var(--text-dim);
  font-size: 0.85rem;
}
.divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid rgba(255,255,255,0.1); }
.divider span { padding: 0 1rem; }

/* Floating Labels */
.floating {
  position: relative;
  margin-bottom: 1.5rem;
}

.floating input {
  width: 100%;
  padding: 1.25rem 1rem 0.6rem;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  color: white;
  font-size: 1rem;
  transition: all 0.3s;
}

.floating input:focus {
  outline: none;
  border-color: var(--accent);
  background: rgba(15, 23, 42, 0.9);
}

.floating label {
  position: absolute;
  top: 50%;
  left: 1rem;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 1rem;
  pointer-events: none;
  transition: 0.2s ease all;
}

.floating input:focus ~ label,
.floating input:not(:placeholder-shown) ~ label {
  top: 12px;
  font-size: 0.75rem;
  color: var(--accent);
}

.form-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  font-size: 0.9rem;
}

.checkbox-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-muted);
  cursor: pointer;
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1rem;
  border-radius: 12px;
  font-weight: bold;
  font-size: 1.05rem;
}

@media (max-width: 900px) {
  .visual-side { display: none; }
  .mobile-logo { display: flex; }
}
</style>