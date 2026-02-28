<template>
  <div class="blog-page">
    <div class="page-header text-center">
      <div class="badge">Resources & Insights</div>
      <h1 class="page-title">Career <span class="text-gradient">Advancement.</span></h1>
      <p class="page-subtitle">Expert advice on resumes, interviews, and navigating the modern job market.</p>
    </div>

    <div class="categories-nav">
      <button class="cat-btn active">All Posts</button>
      <button class="cat-btn">Resume Tips</button>
      <button class="cat-btn">Interview Prep</button>
      <button class="cat-btn">Career Growth</button>
      <button class="cat-btn">ATS Secrets</button>
    </div>

    <!-- Featured Post -->
    <div class="featured-post glass-card">
      <div class="featured-img" style="background-image: url('https://source.unsplash.com/random/800x600/?office')"></div>
      <div class="featured-content">
        <div class="post-meta">
          <span class="post-tag">Resume Tips</span>
          <span class="post-date">Oct 12, 2026</span>
        </div>
        <h2>How to write a developer resume that passes the 6-second test</h2>
        <p>Recruiters spend an average of 6 seconds skimming your resume. Here is how to ensure your most important achievements stand out instantly...</p>
        <button class="btn-read-more">Read Article →</button>
      </div>
    </div>

    <!-- Blog Grid -->
    <div class="blog-grid">
      <div class="blog-card" v-for="i in 6" :key="i">
        <div class="blog-img bg-gradient-1"></div>
        <div class="blog-card-content">
          <div class="post-meta">
            <span class="post-tag">Interview Prep</span>
            <span class="post-date">Oct 10, 2026</span>
          </div>
          <h3>Top 10 Behavioral Interview Questions</h3>
          <p>Master the STAR method to ace your next remote interview with these proven examples.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blog-page {
  padding: 4rem 2rem 8rem;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 4rem;
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

.categories-nav {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 4rem;
}

.cat-btn {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  color: var(--text-muted);
  padding: 0.6rem 1.25rem;
  border-radius: 99px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s;
}

.cat-btn:hover {
  background: rgba(255,255,255,0.1);
  color: var(--text-main);
}

.cat-btn.active {
  background: var(--text-main);
  color: var(--bg-deep);
  border-color: var(--text-main);
  font-weight: 600;
}

.featured-post {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  overflow: hidden;
  margin-bottom: 4rem;
  transition: transform 0.3s;
}

.featured-post:hover {
  transform: translateY(-5px);
}

.featured-img {
  background-size: cover;
  background-position: center;
  min-height: 400px;
}

.featured-content {
  padding: 3rem 4rem 3rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.post-meta {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1.5rem;
  font-size: 0.85rem;
}

.post-tag {
  background: rgba(99, 102, 241, 0.15);
  color: var(--accent);
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  font-weight: 600;
}

.post-date {
  color: var(--text-dim);
}

.featured-content h2 {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.featured-content p {
  color: var(--text-muted);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.btn-read-more {
  background: transparent;
  border: none;
  color: var(--text-main);
  font-weight: 600;
  font-size: 1rem;
  padding: 0;
  display: inline-flex;
  align-items: center;
  align-self: flex-start;
  transition: 0.3s;
}

.btn-read-more:hover {
  color: var(--accent);
  transform: translateX(5px);
}

.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2.5rem;
}

.blog-card {
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s;
  cursor: pointer;
}

.blog-card:hover {
  transform: translateY(-5px);
  background: rgba(30, 41, 59, 0.6);
}

.blog-img {
  height: 200px;
  background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(236,72,153,0.2));
}

.blog-card-content {
  padding: 2rem;
}

.blog-card-content h3 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.blog-card-content p {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.6;
}

@media (max-width: 900px) {
  .featured-post {
    grid-template-columns: 1fr;
    gap: 0;
  }
  .featured-img { min-height: 250px; }
  .featured-content { padding: 2rem; }
}
</style>
