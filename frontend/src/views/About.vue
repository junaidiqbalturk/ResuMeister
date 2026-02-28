<template>
  <div class="about-page">
    <div class="page-header text-center">
      <div class="badge">Our Mission</div>
      <h1 class="page-title">We believe everyone <br/><span class="text-gradient">deserves a great career.</span></h1>
      <p class="page-subtitle max-w-2xl">We're on a mission to democratize the job hunt by providing accessible, professional tools that help talented individuals get noticed.</p>
    </div>

    <!-- Story Section -->
    <section class="story-section">
      <div class="story-image">
        <img src="https://source.unsplash.com/random/800x1000/?teamwork" alt="Our Team" class="glass-card round-img" />
      </div>
      <div class="story-text">
        <h2>The ResuMeister Story</h2>
        <p>It started with a simple observation: highly qualified candidates were being rejected because their resumes couldn't pass automated screening software. The hiring process was broken.</p>
        <p>We built ResuMeister to level the playing field. By combining cutting-edge AI with recruiter-approved design principles, we've created a platform that ensures your true potential shines through.</p>
        
        <div class="stats-grid mt-4">
          <div class="stat-item">
            <span class="stat-num">100k+</span>
            <span class="stat-label">Active Users</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">94%</span>
            <span class="stat-label">Interview Rate</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">50+</span>
            <span class="stat-label">Pro Templates</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <h2 class="text-center mb-4">Meet the Crew</h2>
      <p class="text-center mb-5 subtitle">Passionate engineers, designers, and career experts.</p>
      
      <div class="team-grid">
        <div class="team-card" v-for="i in 4" :key="i">
          <div class="member-img bg-gradient-1"></div>
          <h3>Jane Doe</h3>
          <p class="role">Co-Founder & CEO</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about-page {
  padding: 4rem 2rem 8rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 6rem;
  display: flex;
  flex-direction: column;
  align-items: center;
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
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
}

.max-w-2xl { max-width: 700px; }
.mb-4 { margin-bottom: 2rem; }
.mb-5 { margin-bottom: 4rem; }
.mt-4 { margin-top: 2rem; }
.text-center { text-align: center; }

.story-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: center;
  margin-bottom: 8rem;
}

.round-img {
  border-radius: 24px;
  object-fit: cover;
  width: 100%;
  height: 500px;
}

.story-text h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

.story-text p {
  font-size: 1.1rem;
  color: var(--text-muted);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-num {
  font-size: 2rem;
  font-weight: 700;
  font-family: var(--font-heading);
  color: var(--text-main);
}

.stat-label {
  color: var(--text-dim);
  font-size: 0.9rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.team-card {
  text-align: center;
  padding: 2rem;
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 20px;
  transition: transform 0.3s;
}

.team-card:hover {
  transform: translateY(-5px);
  background: rgba(30, 41, 59, 0.6);
}

.member-img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin: 0 auto 1.5rem;
}

.bg-gradient-1 { background: linear-gradient(135deg, var(--accent), var(--secondary)); }

.team-card h3 {
  font-size: 1.25rem;
  margin-bottom: 0.25rem;
}

.role {
  color: var(--accent);
  font-size: 0.9rem;
  font-weight: 500;
}

@media (max-width: 900px) {
  .story-section {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}
</style>
