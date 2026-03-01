<template>
  <div class="contact-page">
    <div class="container">
      <div class="contact-grid">
        <div class="contact-info">
          <div class="badge glow-pulse">Contact Us</div>
          <h1 class="page-title">We'd love to <br/><span class="text-gradient">hear from you.</span></h1>
          <p class="subtitle mb-8">Whether you have a question about features, pricing, or anything else, our team is ready to answer all your questions.</p>
          
          <div class="info-blocks">
            <div class="info-block glass-card group">
              <div class="icon-wrap transition-colors group-hover:bg-accent group-hover:text-white">📧</div>
              <div>
                <h3 class="text-white font-semibold text-lg">Chat to Sales</h3>
                <p class="text-muted text-sm mb-1 mt-1">Speak to our friendly team.</p>
                <a href="mailto:sales@resumeister.com" class="contact-link">sales@resumeister.com</a>
              </div>
            </div>
            
            <div class="info-block glass-card group">
              <div class="icon-wrap transition-colors group-hover:bg-accent group-hover:text-white">💬</div>
              <div>
                <h3 class="text-white font-semibold text-lg">Chat to Support</h3>
                <p class="text-muted text-sm mb-1 mt-1">We're here to help you.</p>
                <a href="mailto:support@resumeister.com" class="contact-link">support@resumeister.com</a>
              </div>
            </div>

            <div class="info-block glass-card group">
              <div class="icon-wrap transition-colors group-hover:bg-accent group-hover:text-white">📍</div>
              <div>
                <h3 class="text-white font-semibold text-lg">Visit Us</h3>
                <p class="text-muted text-sm mb-1 mt-1">Visit our office HQ.</p>
                <span class="contact-link cursor-default">100 Innovation Drive, Tech City, 90210</span>
              </div>
            </div>
          </div>
        </div>

        <div class="contact-form-wrapper glass-card form-glow-bg relative">
          <!-- Subtle glow behind the form -->
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/5 to-pink-500/5 rounded-3xl pointer-events-none"></div>
          
          <form @submit.prevent="submitForm" class="relative z-10">
            <h3 class="text-2xl font-bold text-white mb-6">Send us a message</h3>
            <div class="form-row">
              <div class="input-group">
                <label>First Name</label>
                <input type="text" placeholder="Jane" required class="premium-input" />
              </div>
              <div class="input-group">
                <label>Last Name</label>
                <input type="text" placeholder="Doe" required class="premium-input" />
              </div>
            </div>
            
            <div class="input-group">
              <label>Email</label>
              <input type="email" placeholder="jane@company.com" required class="premium-input" />
            </div>

            <div class="input-group">
              <label>Phone Number <span class="text-muted font-normal">(Optional)</span></label>
              <input type="tel" placeholder="+1 (555) 000-0000" class="premium-input" />
            </div>

            <div class="input-group">
              <label>Message</label>
              <textarea rows="5" placeholder="How can we help you?" required class="premium-input"></textarea>
            </div>

            <button type="submit" class="btn-primary-large full-width mt-4">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  methods: {
    submitForm() {
      // In a real app, this would use a toast notification instead of alert
      alert("Thanks for your message! Our team will get back to you soon.");
    }
  }
}
</script>

<style scoped>
.contact-page {
  padding: 4rem 2rem 8rem;
  max-width: 1200px;
  margin: 0 auto;
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
  animation: fadeUp 0.8s ease-out;
}

.glow-pulse {
  animation: fadeUp 0.8s ease-out, pulseGlow 2s infinite;
}

@keyframes pulseGlow {
  0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
  100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
}

.page-title {
  font-size: clamp(3rem, 5vw, 4.5rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
  font-weight: 800;
  animation: fadeUp 1s ease-out;
}

.subtitle {
  font-size: 1.2rem;
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 500px;
  animation: fadeUp 1s ease-out 0.2s backwards;
}

.mb-8 { margin-bottom: 2rem; }
.mb-6 { margin-bottom: 1.5rem; }
.mb-1 { margin-bottom: 0.25rem; }
.mt-1 { margin-top: 0.25rem; }
.mt-4 { margin-top: 1rem; }
.text-white { color: #fff; }
.text-muted { color: var(--text-muted); }
.text-sm { font-size: 0.875rem; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.text-lg { font-size: 1.125rem; }
.text-2xl { font-size: 1.5rem; }
.cursor-default { cursor: default; }

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 6rem;
  align-items: start;
}

.info-blocks {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  animation: fadeUp 1s ease-out 0.4s backwards;
}

.info-block {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem 2rem;
  border-radius: 20px;
  align-items: flex-start;
  transition: transform 0.3s, background 0.3s;
}

.info-block:hover {
  transform: translateX(10px);
  background: rgba(30, 41, 59, 0.6);
  border-color: rgba(99, 102, 241, 0.3);
}

.icon-wrap {
  background: rgba(255,255,255,0.05);
  font-size: 1.5rem;
  width: 52px;
  height: 52px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255,255,255,0.1);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.info-block:hover .icon-wrap {
  background: var(--accent);
  color: white;
  border-color: var(--accent);
  transform: scale(1.1) rotate(5deg);
  box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
}

.contact-link {
  color: var(--accent);
  font-weight: 600;
  font-size: 0.95rem;
  transition: color 0.3s;
  display: inline-block;
}

.contact-link:hover {
  color: var(--tertiary);
}

/* Form Styling */
.contact-form-wrapper {
  padding: 3.5rem 3rem;
  border-radius: 24px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.4);
  animation: fadeUp 1.2s ease-out 0.5s backwards;
}

.form-glow-bg::before {
  content: '';
  position: absolute;
  top: -50px; right: -50px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
  z-index: 0;
  opacity: 0.5;
  pointer-events: none;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.input-group label {
  display: block;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #fff;
}

.premium-input {
  width: 100%;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  color: white;
  font-family: var(--font-primary);
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.premium-input::placeholder {
  color: rgba(255,255,255,0.3);
}

.premium-input:focus {
  outline: none;
  border-color: var(--accent);
  background: rgba(15, 23, 42, 0.95);
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15), 0 10px 20px rgba(0,0,0,0.2);
  transform: translateY(-2px);
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1.1rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1.05rem;
  border: none;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-primary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(255,255,255,0.2);
}

.full-width { width: 100%; }

/* Utilities used in HTML */
.relative { position: relative; }
.absolute { position: absolute; }
.inset-0 { inset: 0; }
.pointer-events-none { pointer-events: none; }
.z-10 { z-index: 10; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 960px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 4rem;
  }
  .form-row { grid-template-columns: 1fr; }
  .contact-form-wrapper { padding: 2.5rem 2rem; }
}
</style>
