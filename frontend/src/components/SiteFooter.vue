<template>
  <footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand">
        <router-link to="/" class="logo">
          <div class="logo-icon">R</div>
          <span>ResuMeister</span>
        </router-link>
        <p class="brand-desc">Build a professional, ATS-friendly resume in minutes. Start landing more interviews today.</p>
        <div class="social-links">
          <a href="#" class="social-icon">𝕏</a>
          <a href="#" class="social-icon">In</a>
          <a href="#" class="social-icon">GH</a>
        </div>
      </div>
      
      <div class="footer-links">
        <div class="link-group">
          <h4>Product</h4>
          <router-link to="/features">Features</router-link>
          <router-link to="/resume-template">Templates</router-link>
          <router-link to="/pricing">Pricing</router-link>
        </div>
        <div class="link-group">
          <h4>Company</h4>
          <router-link to="/about">About Us</router-link>
          <router-link to="/blog">Blog</router-link>
          <router-link to="/contact">Contact</router-link>
        </div>
        <div class="link-group">
          <h4>Legal</h4>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>

      <div class="footer-newsletter">
        <h4>Stay Updated</h4>
        <p>Get career tips and product updates delivered to your inbox.</p>
        <form @submit.prevent class="newsletter-form">
          <input type="email" placeholder="Enter your email" required />
          <button type="submit" class="btn-subscribe">→</button>
        </form>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; {{ new Date().getFullYear() }} ResuMeister. All rights reserved.</p>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  background: #020617; /* Var fallback */
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding: 5rem 2rem 2rem;
  color: var(--text-muted);
}

.footer-top {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 3fr 1.5fr;
  gap: 4rem;
  padding-bottom: 4rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.5rem;
  color: var(--text-main);
  margin-bottom: 1rem;
}

.logo-icon {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--accent), var(--secondary));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  color: white;
}

.brand-desc {
  line-height: 1.6;
  margin-bottom: 2rem;
  max-width: 300px;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.social-icon:hover {
  background: var(--text-main);
  color: var(--bg-deep);
}

.footer-links {
  display: flex;
  justify-content: space-between;
}

.link-group h4 {
  color: var(--text-main);
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.link-group a {
  display: block;
  margin-bottom: 0.8rem;
  transition: color 0.3s;
}

.link-group a:hover {
  color: var(--text-main);
}

.footer-newsletter h4 {
  color: var(--text-main);
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.footer-newsletter p {
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.newsletter-form {
  display: flex;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.5rem;
  border-radius: 99px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.newsletter-form input {
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-main);
  padding: 0.5rem 1rem;
  width: 100%;
}

.btn-subscribe {
  background: var(--text-main);
  color: var(--bg-deep);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
  font-size: 0.9rem;
}

@media (max-width: 900px) {
  .footer-top {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  .footer-links {
    flex-wrap: wrap;
    gap: 2rem;
  }
  .link-group {
    width: calc(50% - 1rem);
  }
}
</style>
