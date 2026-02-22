<template>
  <div class="auth-wrapper">
    <!-- Atmosphere -->
    <div class="atmosphere">
      <div class="aura aura-1"></div>
      <div class="aura aura-2"></div>
    </div>

    <!-- Minimal Back Nav -->
    <nav class="auth-nav container">
      <a href="/" class="logo-link reveal-up">
        <img src="/resumeister.png" alt="ResuMeister" class="logo-img">
        <span class="logo-text">ResuMeister</span>
      </a>
    </nav>

    <div class="container auth-content">
      <div class="auth-card reveal-up">
        <div class="auth-header">
           <h1>Welcome back</h1>
           <p>Access your professional engineering workspace.</p>
        </div>

        <form @submit.prevent="handleLogin" class="saas-form">
          <div class="form-group">
            <label>Email Address</label>
            <input v-model="email" type="email" placeholder="name@company.com" required />
          </div>
          <div class="form-group">
            <div class="label-row">
               <label>Password</label>
               <a href="#" class="forgot-link">Forgot?</a>
            </div>
            <input v-model="password" type="password" placeholder="••••••••" required />
          </div>
          
          <button type="submit" class="btn-auth-primary" :disabled="loading">
            <span v-if="!loading">Login to Workspace</span>
            <span v-else>Verifying Credentials...</span>
          </button>
        </form>

        <div class="auth-footer">
           <p>New to ResuMeister? <a href="/register">Create an account</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { gsap } from 'gsap';

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      loading: false
    };
  },
  mounted() {
    this.executeAnimations();
  },
  methods: {
    executeAnimations() {
      gsap.from('.reveal-up', {
        y: 30,
        opacity: 0,
        duration: 1,
        stagger: 0.15,
        ease: 'power3.out'
      });
    },
    handleLogin() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        this.$router.push('/Dashboard');
      }, 1500);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.auth-wrapper {
  min-height: 100vh;
  background-color: #030712;
  color: #F8FAFC;
  font-family: 'Outfit', sans-serif;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.atmosphere {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
}
.aura { position: absolute; border-radius: 50%; filter: blur(140px); opacity: 0.1; }
.aura-1 { width: 800px; height: 800px; background: #6366F1; top: -10%; left: -10%; }
.aura-2 { width: 600px; height: 600px; background: #EC4899; bottom: -5%; right: -5%; }

.auth-nav { padding: 2.5rem 0; z-index: 10; }
.logo-link { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.logo-img { height: 28px; }
.logo-text { font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff; }

.auth-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  padding-bottom: 5rem;
}

.auth-card {
  width: 100%;
  max-width: 440px;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 32px;
  padding: 3.5rem;
  box-shadow: 0 40px 100px -20px rgba(0,0,0,0.5);
}

.auth-header { text-align: center; margin-bottom: 3rem; }
.auth-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 2rem; font-weight: 700; color: #fff; margin-bottom: 0.75rem; }
.auth-header p { color: #94A3B8; font-size: 1rem; }

.saas-form { display: flex; flex-direction: column; gap: 1.75rem; }
.form-group { display: flex; flex-direction: column; gap: 10px; }
.label-row { display: flex; justify-content: space-between; align-items: center; }
.label-row label { margin-bottom: 0; }
.form-group label { font-size: 0.85rem; font-weight: 600; color: #475569; }

.forgot-link { font-size: 0.8rem; color: #6366F1; text-decoration: none; font-weight: 600; }

.form-group input {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  color: #fff;
  font-family: inherit;
  font-size: 1rem;
  transition: all 0.3s;
}
.form-group input:focus { outline: none; border-color: rgba(99, 102, 241, 0.5); background: rgba(15, 23, 42, 0.9); }

.btn-auth-primary {
  margin-top: 1rem;
  background: #fff;
  color: #030712;
  border: none;
  padding: 1.1rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}
.btn-auth-primary:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(255,255,255,0.15); }
.btn-auth-primary:disabled { opacity: 0.5; cursor: not-allowed; }

.auth-footer { margin-top: 2.5rem; text-align: center; font-size: 0.9rem; color: #475569; }
.auth-footer a { color: #fff; text-decoration: none; font-weight: 700; margin-left: 5px; }

@media (max-width: 480px) {
  .auth-card { padding: 2.5rem; border-radius: 0; height: 100vh; max-width: 100%; border: none; background: transparent; backdrop-filter: none; box-shadow: none; }
  .auth-nav { display: none; }
}
</style>