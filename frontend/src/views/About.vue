<template>
  <div class="about-page">
    <div class="page-header text-center">
      <div class="badge">Our Mission</div>
      <h1 class="page-title">We believe everyone <br/><span class="text-gradient">deserves a great career.</span></h1>
      <p class="page-subtitle max-w-2xl">We're on a mission to democratize the job hunt by providing accessible, professional tools that help talented individuals get noticed.</p>
    </div>

    <!-- Story Section -->
    <section class="story-section">
      <div class="story-visual">
         <div class="image-wrapper glass-card">
           <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=800" alt="Our Team Collaboration" class="main-img" />
           <div class="image-overlay"></div>
         </div>
         <!-- Floating Stats purely for visual flair over the image -->
         <div class="float-stat stat-1 glass-card">
           <span class="text-accent font-bold text-xl">100k+</span> users
         </div>
      </div>
      
      <div class="story-text">
        <h2 class="text-gradient">The ResuMeister Story</h2>
        <p>It started with a simple observation: highly qualified candidates were being rejected because their resumes couldn't pass automated screening software. The hiring process was broken.</p>
        <p>We built ResuMeister to level the playing field. By combining cutting-edge AI with recruiter-approved design principles, we've created a platform that ensures your true potential shines through.</p>
        
        <div class="stats-grid mt-8">
          <div class="stat-item glass-card p-4 text-center rounded-2xl">
            <span class="stat-num">100k+</span>
            <span class="stat-label">Active Users</span>
          </div>
          <div class="stat-item glass-card p-4 text-center rounded-2xl">
            <span class="stat-num text-green">94%</span>
            <span class="stat-label">Interview Rate</span>
          </div>
          <div class="stat-item glass-card p-4 text-center rounded-2xl">
            <span class="stat-num text-accent">50+</span>
            <span class="stat-label">Pro Templates</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <div class="text-center mb-12">
        <div class="badge glow-pulse mb-4">The Team</div>
        <h2>Meet the <span class="text-gradient">Crew</span></h2>
        <p class="text-muted text-lg mt-2">Passionate engineers, designers, and career experts.</p>
      </div>
      
      <div class="team-grid">
        <div class="team-card glass-card group" v-for="i in 4" :key="i">
          <div class="member-img-wrap">
            <div class="member-img bg-gradient-1"></div>
            <!-- Social links reveal on hover -->
            <div class="social-links">
               <span class="social-icon">in</span>
               <span class="social-icon">tw</span>
            </div>
          </div>
          <h3>Jane Doe</h3>
          <p class="role">Co-Founder & CEO</p>
        </div>
      </div>
    </section>
    
    <!-- Join Us CTA -->
    <section class="join-cta mt-24 glass-card text-center p-12 relative overflow-hidden">
       <div class="absolute inset-0 bg-gradient-to-r from-indigo-500/10 to-transparent pointer-events-none"></div>
       <h2 class="text-3xl font-bold mb-4 relative z-10">Want to join our mission?</h2>
       <p class="text-muted text-lg mb-8 relative z-10">We're always looking for talented individuals to help us build the future of hiring.</p>
       <button class="btn-primary-large inline-block relative z-10">View Open Positions</button>
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

.page-title {
  font-size: clamp(3rem, 5vw, 4.5rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
  font-weight: 800;
}

.page-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  line-height: 1.6;
}

.max-w-2xl { max-width: 700px; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }
.text-3xl { font-size: 1.875rem; }
.mb-4 { margin-bottom: 1rem; }
.mb-8 { margin-bottom: 2rem; }
.mb-12 { margin-bottom: 3rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-8 { margin-top: 2rem; }
.mt-24 { margin-top: 6rem; }
.p-4 { padding: 1rem; }
.p-12 { padding: 3rem; }
.text-center { text-align: center; }
.font-bold { font-weight: 700; }
.text-accent { color: var(--accent); }
.text-green { color: #10B981; }
.rounded-2xl { border-radius: 1rem; }
.inline-block { display: inline-block; }

.story-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: center;
  margin-bottom: 10rem;
}

/* Story Visual */
.story-visual {
  position: relative;
  perspective: 1000px;
}

.image-wrapper {
  border-radius: 24px;
  overflow: hidden;
  position: relative;
  transform: rotateY(5deg) rotateX(5deg);
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s;
  box-shadow: 0 30px 60px rgba(0,0,0,0.5);
}

.image-wrapper:hover {
  transform: rotateY(0deg) rotateX(0deg);
  box-shadow: 0 40px 80px rgba(99, 102, 241, 0.2);
}

.main-img {
  width: 100%;
  height: 550px;
  object-fit: cover;
  display: block;
  filter: brightness(0.9) contrast(1.1);
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(15, 23, 42, 0.8), transparent 50%);
  pointer-events: none;
}

.float-stat {
  position: absolute;
  padding: 1rem 1.5rem;
  border-radius: 16px;
  background: rgba(30, 41, 59, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  transform: translateZ(50px);
  animation: float 6s ease-in-out infinite;
  display: flex;
  align-items: baseline;
  gap: 8px;
  color: var(--text-muted);
}

.stat-1 {
  bottom: 10%;
  left: -5%;
}

@keyframes float {
  0% { transform: translateY(0px) translateZ(50px); }
  50% { transform: translateY(-15px) translateZ(50px); }
  100% { transform: translateY(0px) translateZ(50px); }
}

/* Story Text */
.story-text h2 {
  font-size: clamp(2rem, 3vw, 2.75rem);
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.story-text p {
  font-size: 1.15rem;
  color: var(--text-muted);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  transition: transform 0.3s;
}

.stat-item:hover {
  transform: translateY(-5px);
  background: rgba(255,255,255,0.05);
}

.stat-num {
  font-size: 2.2rem;
  font-weight: 800;
  font-family: var(--font-heading);
  color: var(--text-main);
  margin-bottom: 0.25rem;
}

.stat-label {
  color: var(--text-dim);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}

/* Team Grid */
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.team-card {
  text-align: center;
  padding: 3rem 2rem;
  border-radius: 24px;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s;
}

.team-card:hover {
  transform: translateY(-8px);
  background: rgba(30, 41, 59, 0.6);
  border-color: rgba(255,255,255,0.15);
}

.member-img-wrap {
  position: relative;
  width: 140px; height: 140px;
  margin: 0 auto 1.5rem;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255,255,255,0.1);
  transition: border-color 0.3s;
}

.team-card:hover .member-img-wrap {
  border-color: var(--accent);
}

.member-img {
  width: 100%; height: 100%;
  border-radius: 50%;
  transition: transform 0.5s;
}

.team-card:hover .member-img {
  transform: scale(1.1);
}

.bg-gradient-1 { background: linear-gradient(135deg, var(--accent), var(--secondary)); }

.social-links {
  position: absolute;
  inset: 0;
  background: rgba(15, 23, 42, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  opacity: 0;
  transition: opacity 0.3s;
}

.team-card:hover .social-links {
  opacity: 1;
}

.social-icon {
  width: 36px; height: 36px;
  background: var(--text-main);
  color: var(--bg-deep);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem;
  font-weight: bold;
  cursor: pointer;
  transform: translateY(10px);
  transition: transform 0.3s 0.1s, background 0.3s;
}

.team-card:hover .social-icon { transform: translateY(0); }
.social-icon:hover { background: var(--accent); color: white; }

.team-card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.25rem;
  font-weight: 700;
}

.role {
  color: var(--accent);
  font-size: 0.95rem;
  font-weight: 600;
}

/* Join CTA */
.btn-primary-large {
  background: var(--text-main);
  color: var(--bg-deep) !important;
  padding: 1rem 2.5rem;
  border-radius: 99px;
  font-weight: 700;
  font-size: 1.1rem;
  transition: all 0.3s;
  border: none;
  cursor: pointer;
}

.btn-primary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(255,255,255,0.15);
}

/* Animations */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 900px) {
  .story-section {
    grid-template-columns: 1fr;
    gap: 4rem;
    text-align: center;
  }
  .float-stat { display: none; }
  .image-wrapper { transform: none; }
  .image-wrapper:hover { transform: translateY(-5px); }
  .main-img { height: 400px; }
}
</style>
