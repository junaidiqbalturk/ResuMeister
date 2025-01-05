<template>
  <div class="resume-template-page">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="container">
        <a href="/" class="logo">ResuMeister</a>
        <ul class="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/about">About Us</a></li>
          <li><a href="/contact">Contact Us</a></li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>Discover the Perfect Resume Template</h1>
        <p>Stand out in the job market with a professionally designed resume.</p>
        <button class="cta-btn">Explore Templates</button>
      </div>
    </section>

    <!-- Resume Templates Grid -->
    <section class="templates-grid">
      <div class="container">
        <h2>Our Top Resume Templates</h2>
        <div class="templates">
          <div
            v-for="template in templates"
            :key="template.id"
            class="template-card"
            @mouseover="animateCard"
            @mouseleave="resetCard"
          >
            <div class="template-image-wrapper">
              <img
                :src="template.image"
                alt="Template Preview"
                class="template-image"
              />
              <div class="template-overlay">
                <h3>{{ template.name }}</h3>
                <p>{{ template.description }}</p>
                <button class="btn">Use This Template</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div class="container">
        <p>&copy; 2025 ResuMeister | All Rights Reserved</p>
        <div class="social-links">
          <a href="https://facebook.com" target="_blank">Facebook</a>
          <a href="https://twitter.com" target="_blank">Twitter</a>
          <a href="https://linkedin.com" target="_blank">LinkedIn</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      templates: [
        { id: 1, name: 'Professional', description: 'A clean, corporate-style resume.', image: '/cv-template-professional.jpg' },
        { id: 2, name: 'Creative', description: 'A vibrant, eye-catching resume template.', image: '/images/creative.jpg' },
        { id: 3, name: 'Minimalist', description: 'A sleek, minimal design to highlight your skills.', image: '/cv-template-minimalistic.jpg' },
        { id: 4, name: 'Modern', description: 'A modern design for a modern job seeker.', image: '/cv-template-modern.jpg' },
        { id: 5, name: 'Executive', description: 'A high-end resume design for top-level professionals.', image: '/cv-template-executive.jpg' },
        { id: 6, name: 'Classic', description: 'A timeless, professional layout for any career.', image: '/cv-classic.jpg' }
      ]
    };
  },
  methods: {
    animateCard(event) {
      const card = event.currentTarget;
      card.classList.add('animate-card');
    },
    resetCard(event) {
      const card = event.currentTarget;
      card.classList.remove('animate-card');
    }
  }
};
</script>

<style scoped>
/* General Styles */
body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #f4f4f9;
}

.container {
  width: 90%;
  margin: 0 auto;
}

/* Navbar Styles */
.navbar {
  background: #001f3f;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 10;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar .logo {
  font-size: 2rem;
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;
}

.navbar .logo:hover {
  color: #e84393;
}

.navbar .nav-links {
  list-style: none;
  display: flex;
}

.navbar .nav-links li {
  margin-left: 1.5rem;
}

.navbar .nav-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;
}

.navbar .nav-links a:hover {
  color: #e84393;
}

/* Hero Section */
.hero-section {
  background: url('@/assets/hero-bg.jpeg') no-repeat center center fixed;
  background-size: cover;
  color: white;
  padding: 7rem 0;
  text-align: center;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 1;
}

.hero-section::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: -1;
}

.hero-section h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
  animation: fadeInUp 1s ease-in-out;
}

.hero-section p {
  font-size: 1.4rem;
  margin-top: 0;
  animation: fadeInUp 1.5s ease-in-out;
}

.cta-btn {
  padding: 1.2rem 3rem;
  background-color: #e84393;
  color: white;
  border: none;
  font-size: 1.4rem;
  border-radius: 30px;
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
}

.cta-btn:hover {
  background-color: #d63031;
  transform: scale(1.05);
}

/* Resume Templates Grid */
.templates-grid {
  padding: 4rem 0;
  background-color: #ffffff;
  box-shadow: 0 -6px 12px rgba(0, 0, 0, 0.1);
}

.templates-grid h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #2d3436;
  font-weight: bold;
}

.templates {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
}

.template-card {
  background-color: #ecf0f1;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transform: scale(1);
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  cursor: pointer;
  position: relative;
}

.template-card:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
  background-color: #dfe6e9;
}

.template-image-wrapper {
  position: relative;
  overflow: hidden;
}

.template-image {
  width: 100%;
  height: auto;
  transition: transform 0.4s ease;
}

.template-card:hover .template-image {
  transform: scale(1.1);
}

/* Overlay for Name and Button */
.template-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.template-card:hover .template-overlay {
  opacity: 1;
}

.template-overlay h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.template-overlay .btn {
  padding: 0.8rem 1.5rem;
  background-color: #6c5ce7;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
}

.template-overlay .btn:hover {
  background-color: #a29bfe;
  transform: scale(1.05);
}

/* Template Info Styles */
.template-info {
  padding: 1.5rem;
  text-align: center;
}

.template-info p {
  font-size: 1rem;
  margin-bottom: 1.5rem;
  color: #636e72;
}

/* Footer Styles */
footer {
  background-color: #2c3e50;
  color: white;
  padding: 3rem 0;
  text-align: center;
}

footer p {
  margin-bottom: 1rem;
}

footer .social-links a {
  color: white;
  text-decoration: none;
  margin: 0 1.5rem;
  font-size: 1.2rem;
  transition: color 0.3s ease;
}

footer .social-links a:hover {
  color: #e84393;
}

/* Keyframe Animations */
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar .nav-links {
    display: none;
  }

  .hero-section h1 {
    font-size: 3rem;
  }

  .templates {
    grid-template-columns: 1fr;
  }
}
</style>
