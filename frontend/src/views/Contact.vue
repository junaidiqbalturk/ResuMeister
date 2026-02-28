<template>
  <div class="contact-page">
    <div class="container">
      <div class="contact-grid">
        <div class="contact-info">
          <div class="badge">Contact Us</div>
          <h1 class="page-title">We'd love to <br/><span class="text-gradient">hear from you.</span></h1>
          <p class="subtitle mb-5">Whether you have a question about features, pricing, or anything else, our team is ready to answer all your questions.</p>
          
          <div class="info-blocks">
            <div class="info-block glass-card">
              <div class="icon-wrap">📧</div>
              <div>
                <h3>Chat to Sales</h3>
                <p>Speak to our friendly team.</p>
                <a href="mailto:sales@resumeister.com">sales@resumeister.com</a>
              </div>
            </div>
            
            <div class="info-block glass-card">
              <div class="icon-wrap">💬</div>
              <div>
                <h3>Chat to Support</h3>
                <p>We're here to help you.</p>
                <a href="mailto:support@resumeister.com">support@resumeister.com</a>
              </div>
            </div>

            <div class="info-block glass-card">
              <div class="icon-wrap">📍</div>
              <div>
                <h3>Visit Us</h3>
                <p>Visit our office HQ.</p>
                <span>100 Innovation Drive, Tech City, 90210</span>
              </div>
            </div>
          </div>
        </div>

        <div class="contact-form-wrapper glass-card">
          <form @submit.prevent="submitForm">
            <div class="form-row">
              <div class="input-group">
                <label>First Name</label>
                <input type="text" placeholder="First name" required />
              </div>
              <div class="input-group">
                <label>Last Name</label>
                <input type="text" placeholder="Last name" required />
              </div>
            </div>
            
            <div class="input-group">
              <label>Email</label>
              <input type="email" placeholder="you@company.com" required />
            </div>

            <div class="input-group">
              <label>Phone Number (Optional)</label>
              <input type="tel" placeholder="+1 (555) 000-0000" />
            </div>

            <div class="input-group">
              <label>Message</label>
              <textarea rows="5" placeholder="Leave us a message..." required></textarea>
            </div>

            <button type="submit" class="btn-primary flex-center full-width">Send Message</button>
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
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.subtitle {
  font-size: 1.1rem;
  color: var(--text-muted);
  line-height: 1.6;
}

.mb-5 { margin-bottom: 3rem; }

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
}

.info-blocks {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-block {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem;
  border-radius: 16px;
  align-items: flex-start;
}

.icon-wrap {
  background: rgba(255,255,255,0.05);
  font-size: 1.5rem;
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.info-block h3 {
  font-size: 1.1rem;
  margin-bottom: 0.25rem;
}

.info-block p {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}

.info-block a, .info-block span {
  color: var(--text-main);
  font-weight: 600;
  font-size: 0.95rem;
}

.info-block a:hover {
  color: var(--accent);
}

.contact-form-wrapper {
  padding: 3rem;
  border-radius: 24px;
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
  font-weight: 500;
  margin-bottom: 0.5rem;
  color: var(--text-main);
}

input, textarea {
  width: 100%;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 0.9rem 1rem;
  color: white;
  font-family: var(--font-primary);
  font-size: 1rem;
  transition: all 0.3s;
}

input:focus, textarea:focus {
  outline: none;
  border-color: var(--accent);
  background: rgba(15, 23, 42, 0.9);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.btn-primary {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.05rem;
  margin-top: 1rem;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255,255,255,0.1);
}

.full-width { width: 100%; }
.flex-center { display: flex; align-items: center; justify-content: center; }

@media (max-width: 900px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 4rem;
  }
  .form-row { grid-template-columns: 1fr; }
  .contact-form-wrapper { padding: 2rem; }
}
</style>
