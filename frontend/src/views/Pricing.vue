<template>
  <div class="pricing-page">
    <div class="page-header text-center">
      <div class="badge">Simple Pricing</div>
      <h1 class="page-title">Invest in your <span class="text-gradient">future.</span></h1>
      <p class="page-subtitle">Choose the perfect plan to accelerate your job search. No hidden fees.</p>
    </div>

    <div class="pricing-grid">
      <!-- Free Plan -->
      <div class="pricing-card">
        <h3 class="plan-name">Starter</h3>
        <p class="plan-desc">Perfect for students and entry-level.</p>
        <div class="plan-price">$0<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span>✓</span> 1 Basic Resume</li>
          <li><span>✓</span> PDF Export (watermarked)</li>
          <li><span>✓</span> Standard Templates</li>
          <li class="disabled"><span>✕</span> AI Content Generation</li>
          <li class="disabled"><span>✕</span> ATS Scoring</li>
        </ul>
        <router-link to="/register" class="btn-outline-large full-width">Get Started</router-link>
      </div>

      <!-- Pro Plan - Popular -->
      <div class="pricing-card popular">
        <div class="popular-badge">Most Popular</div>
        <h3 class="plan-name">Pro</h3>
        <p class="plan-desc">For ambitious professionals.</p>
        <div class="plan-price">$12<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span>✓</span> Unlimited Resumes</li>
          <li><span>✓</span> PDF & DOCX Export</li>
          <li><span>✓</span> Premium Templates</li>
          <li><span>✓</span> AI Content Generation</li>
          <li><span>✓</span> Basic ATS Analysis</li>
        </ul>
        <router-link to="/register" class="btn-primary-large full-width">Start Free Trial</router-link>
      </div>

      <!-- Premium Plan -->
      <div class="pricing-card">
        <h3 class="plan-name">Premium</h3>
        <p class="plan-desc">For executives and power users.</p>
        <div class="plan-price">$29<span class="price-period">/month</span></div>
        <ul class="plan-features">
          <li><span>✓</span> Everything in Pro</li>
          <li><span>✓</span> Unlimited Cover Letters</li>
          <li><span>✓</span> Advanced ATS Scoring (100+)</li>
          <li><span>✓</span> Interview Prep Bot</li>
          <li><span>✓</span> Priority Support</li>
        </ul>
        <router-link to="/register" class="btn-outline-large full-width">Upgrade</router-link>
      </div>
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
  margin-bottom: 6rem;
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

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  align-items: center;
}

.pricing-card {
  background: var(--bg-card);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  padding: 3rem 2.5rem;
  position: relative;
  transition: transform 0.3s, box-shadow 0.3s;
}

.pricing-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.pricing-card.popular {
  background: rgba(30, 41, 59, 0.8);
  border-color: var(--accent);
  box-shadow: 0 10px 40px rgba(99, 102, 241, 0.2);
  transform: scale(1.05);
}

.pricing-card.popular:hover {
  transform: scale(1.05) translateY(-10px);
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
  font-weight: 700;
  box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
}

.plan-name {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.plan-desc {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 2rem;
  min-height: 45px;
}

.plan-price {
  font-size: 3rem;
  font-weight: 700;
  font-family: var(--font-heading);
  margin-bottom: 2rem;
  color: var(--text-main);
}

.price-period {
  font-size: 1rem;
  color: var(--text-muted);
  font-weight: 500;
}

.plan-features {
  list-style: none;
  margin-bottom: 3rem;
}

.plan-features li {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-main);
  opacity: 0.9;
}

.plan-features li span {
  color: #10B981;
  font-weight: bold;
}

.plan-features li.disabled {
  opacity: 0.4;
}

.plan-features li.disabled span {
  color: var(--text-dim);
}

.btn-primary-large, .btn-outline-large {
  display: block;
  text-align: center;
  width: 100%;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 600;
  transition: 0.3s;
}

.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
}

.btn-outline-large {
  background: transparent;
  color: var(--text-main) !important;
  border: 1px solid rgba(255,255,255,0.2);
}

.btn-primary-large:hover, .btn-outline-large:hover {
  transform: translateY(-2px);
}

@media (max-width: 900px) {
  .pricing-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  .pricing-card.popular {
    transform: scale(1);
  }
  .pricing-card.popular:hover {
    transform: translateY(-5px);
  }
}
</style>
