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
        <h1>Choose Your Perfect Resume Template</h1>
        <p>Find a template that suits your career and make your resume stand out!</p>
      </div>
    </section>

    <!-- Resume Templates Grid -->
    <section class="templates-grid">
      <div class="container">
        <h2>Our Top Resume Templates</h2>
        <div class="templates">
          <div v-for="template in templates" :key="template.id" class="template-card">
            <img :src="template.image" alt="Template Preview" class="template-image" />
            <div class="template-info">
              <h3>{{ template.name }}</h3>
              <p>{{ template.description }}</p>
              <button class="btn">Use This Template</button>
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
        { id: 1, name: 'Professional', description: 'A clean, corporate-style resume.', image: '/images/professional.jpg' },
        { id: 2, name: 'Creative', description: 'A vibrant, eye-catching resume template.', image: '/images/creative.jpg' },
        { id: 3, name: 'Minimalist', description: 'A sleek, minimal design to highlight your skills.', image: '/images/minimalist.jpg' },
        { id: 4, name: 'Modern', description: 'A modern design for a modern job seeker.', image: '/images/modern.jpg' },
        { id: 5, name: 'Executive', description: 'A high-end resume design for top-level professionals.', image: '/images/executive.jpg' },
        { id: 6, name: 'Classic', description: 'A timeless, professional layout for any career.', image: '/images/classic.jpg' }
      ]
    };
  }
};
</script>

<style scoped>
/* General Styles */
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  width: 90%;
  margin: 0 auto;
}

/* Navbar Styles */
.navbar {
  background-color: #2c3e50;
  padding: 1rem;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar .logo {
  font-size: 1.8rem;
  color: white;
  text-decoration: none;
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
}

/* Hero Section */
.hero-section {
  background-color: #34495e;
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-section h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1.2rem;
  margin-top: 0;
}

/* Resume Templates Grid */
.templates-grid {
  padding: 4rem 0;
}

.templates-grid h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 2rem;
}

.templates {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.template-card {
  background-color: #ecf0f1;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.template-card:hover {
  transform: scale(1.05);
}

.template-image {
  width: 100%;
  height: auto;
}

.template-info {
  padding: 1rem;
  text-align: center;
}

.template-info h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.template-info p {
  font-size: 1rem;
  margin-bottom: 1rem;
}

.btn {
  padding: 0.8rem 1.5rem;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #c0392b;
}

/* Footer Styles */
footer {
  background-color: #2c3e50;
  color: white;
  padding: 2rem 0;
  text-align: center;
}

footer p {
  margin-bottom: 1rem;
}

footer .social-links a {
  color: white;
  text-decoration: none;
  margin: 0 1rem;
}

footer .social-links a:hover {
  color: #e74c3c;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar .nav-links {
    display: none;
  }

  .hero-section h1 {
    font-size: 2.5rem;
  }

  .templates {
    grid-template-columns: 1fr;
  }
}
</style>
