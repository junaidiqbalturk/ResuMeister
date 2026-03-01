<template>
  <div class="pricing-page">
    <div class="page-header text-center">
      <div class="badge glow-pulse">Simple Pricing</div>
      <h1 class="page-title">Invest in your <span class="text-gradient">future.</span></h1>
      <p class="page-subtitle">Choose the perfect plan to accelerate your job search. No hidden fees. Cancel anytime.</p>
    </div>

    <!-- Pricing Toggle (Monthly/Yearly) Placeholder for visual balance -->
    <div class="billing-toggle">
       <span class="font-semibold text-main">Monthly</span>
       <div class="toggle-switch"></div>
       <span class="text-muted">Annually <span class="discount-badge">Save 20%</span></span>
    </div>

    <div class="pricing-grid">
      <!-- Free Plan -->
      <div class="pricing-card glass-card group">
        <h3 class="plan-name">Starter</h3>
        <p class="plan-desc">Perfect for students and early-stage professionals building their first resume.</p>
        <div class="plan-price">$0<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span class="icon-check">✓</span> 1 Basic Resume</li>
          <li><span class="icon-check">✓</span> PDF Export (watermarked)</li>
          <li><span class="icon-check">✓</span> Standard Templates</li>
          <li class="disabled"><span class="icon-cross">✕</span> AI Content Generation</li>
          <li class="disabled"><span class="icon-cross">✕</span> ATS Scoring</li>
        </ul>
        <router-link to="/register" class="btn-outline-large full-width">Get Started for Free</router-link>
      </div>

      <!-- Pro Plan - Popular -->
      <div class="pricing-card popular group">
        <div class="popular-glow"></div>
        <div class="popular-badge">Most Popular</div>
        <h3 class="plan-name text-gradient">Pro</h3>
        <p class="plan-desc">For ambitious professionals actively applying to multiple targeted roles.</p>
        <div class="plan-price text-white">$12<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span class="icon-check accent-bg">✓</span> Unlimited Resumes</li>
          <li><span class="icon-check accent-bg">✓</span> PDF & DOCX Export</li>
          <li><span class="icon-check accent-bg">✓</span> Premium Templates</li>
          <li><span class="icon-check accent-bg">✓</span> AI Content Generation</li>
          <li><span class="icon-check accent-bg">✓</span> Basic ATS Analysis</li>
        </ul>
        <router-link to="/register" class="btn-primary-large full-width">Start 7-Day Free Trial</router-link>
      </div>

      <!-- Premium Plan -->
      <div class="pricing-card glass-card group">
        <h3 class="plan-name">Premium</h3>
        <p class="plan-desc">For executives and power users who need complete career toolsets.</p>
        <div class="plan-price">$29<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span class="icon-check">✓</span> Everything in Pro</li>
          <li><span class="icon-check">✓</span> Unlimited Cover Letters</li>
          <li><span class="icon-check">✓</span> Advanced ATS Scoring (100+)</li>
          <li><span class="icon-check">✓</span> Interview Prep Bot</li>
          <li><span class="icon-check">✓</span> Priority 24/7 Support</li>
        </ul>
        <router-link to="/register" class="btn-outline-large full-width">Upgrade to Premium</router-link>
      </div>
    </div>
    
    <!-- Enterprise Banner -->
    <div class="enterprise-banner glass-card mt-12">
       <div>
         <h4 class="text-xl font-bold text-white mb-2">Need a plan for your team or university?</h4>
         <p class="text-muted">We offer custom deployment, priority support, and volume discounts.</p>
       </div>
       <button class="btn-outline-large w-auto">Contact Sales</button>
    </div>
  </div>
</template>

<style scoped>
.pricing-page {
  padding: 4rem 2rem 8rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 3rem;
  animation: fadeUp 0.8s ease-out;
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
}

.glow-pulse {
  animation: pulseGlow 2s infinite;
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
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto;
}

/* Billing Toggle */
.billing-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 5rem;
  animation: fadeUp 0.8s ease-out 0.2s backwards;
}

.toggle-switch {
  width: 56px; height: 32px;
  background: rgba(255,255,255,0.1);
  border-radius: 99px;
  position: relative;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,0.05);
  transition: 0.3s;
}

.toggle-switch::after {
  content: '';
  position: absolute;
  top: 4px; left: 4px;
  width: 22px; height: 22px;
  background: var(--accent);
  border-radius: 50%;
  transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 10px rgba(99, 102, 241, 0.4);
}

.toggle-switch:hover { background: rgba(255,255,255,0.15); }

.discount-badge {
  background: rgba(16, 185, 129, 0.15);
  color: #10B981;
  padding: 0.25rem 0.6rem;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-left: 0.5rem;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

/* Pricing Grid */
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  align-items: stretch;
  animation: fadeUp 1s ease-out 0.4s backwards;
}

.pricing-card {
  border-radius: 24px;
  padding: 3rem 2.5rem;
  position: relative;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s;
  display: flex;
  flex-direction: column;
}

.pricing-card:hover {
  transform: translateY(-8px);
  border-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}

/* Popular Tier */
.pricing-card.popular {
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
  border: 1px solid var(--accent);
  box-shadow: 0 20px 50px rgba(99, 102, 241, 0.25);
  transform: scale(1.05);
  z-index: 2;
}

.pricing-card.popular:hover {
  transform: scale(1.05) translateY(-8px);
  box-shadow: 0 30px 60px rgba(99, 102, 241, 0.35);
}

.popular-glow {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.15), transparent 70%);
  border-radius: 24px;
  pointer-events: none;
}

.popular-badge {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, var(--accent), var(--tertiary));
  color: white;
  padding: 0.5rem 1.5rem;
  border-radius: 99px;
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  box-shadow: 0 5px 15px rgba(99, 102, 241, 0.5);
  border: 1px solid rgba(255,255,255,0.2);
}

/* Plan Details */
.plan-name {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
}

.plan-desc {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 2rem;
  line-height: 1.5;
  min-height: 65px;
}

.plan-price {
  font-size: 3.5rem;
  font-weight: 800;
  font-family: var(--font-heading);
  margin-bottom: 2.5rem;
  color: var(--text-main);
  display: flex;
  align-items: baseline;
}

.price-period {
  font-size: 1.1rem;
  color: var(--text-muted);
  font-weight: 500;
  font-family: var(--font-primary);
  margin-left: 4px;
}

/* Features List */
.plan-features {
  list-style: none;
  margin-bottom: 3rem;
  flex-grow: 1;
}

.plan-features li {
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-main);
  font-weight: 500;
  font-size: 0.95rem;
}

.icon-check, .icon-cross {
  width: 20px; height: 20px;
  border-radius: 50%;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 0.7rem;
  font-weight: bold;
}

.icon-check {
  color: #10B981;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
}

.icon-check.accent-bg {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
  box-shadow: 0 2px 8px rgba(99,102,241,0.4);
}

.icon-cross {
  color: var(--text-dim);
  background: rgba(255,255,255,0.05);
}

.plan-features li.disabled {
  opacity: 0.5;
}

/* Buttons */
.btn-primary-large, .btn-outline-large {
  display: block;
  text-align: center;
  width: 100%;
  padding: 1.1rem;
  border-radius: 16px;
  font-weight: 700;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  font-size: 1.05rem;
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  box-shadow: 0 10px 20px rgba(255,255,255,0.1);
}

.btn-outline-large {
  background: rgba(255,255,255,0.03);
  color: var(--text-main) !important;
  border: 1px solid rgba(255,255,255,0.15);
}

.btn-primary-large:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 30px rgba(255,255,255,0.2);
  background: #fff;
}

.btn-outline-large:hover {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.3);
  transform: translateY(-2px);
}

/* Enterprise Banner */
.enterprise-banner {
  margin-top: 5rem;
  padding: 3rem;
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  background: linear-gradient(to right, rgba(30, 41, 59, 0.4), rgba(15, 23, 42, 0.6));
  animation: fadeUp 1s ease-out 0.6s backwards;
}

/* Utilities */
.text-main { color: var(--text-main); }
.text-muted { color: var(--text-muted); }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.text-xl { font-size: 1.25rem; }
.text-white { color: #fff; }
.mb-2 { margin-bottom: 0.5rem; }
.w-auto { width: auto; padding-left: 2rem; padding-right: 2rem; }

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 1024px) {
  .pricing-grid {
    grid-template-columns: 1fr;
    gap: 4rem;
    max-width: 500px;
    margin: 0 auto;
  }
  .pricing-card.popular {
    transform: scale(1);
  }
  .pricing-card.popular:hover {
    transform: translateY(-8px);
  }
  .enterprise-banner {
    flex-direction: column;
    text-align: center;
  }
}
</style>
