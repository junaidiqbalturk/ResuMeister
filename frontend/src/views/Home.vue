<template>
  <div class="home">
    <!-- Navbar -->
    <header class="navbar">
      <div class="container">
        <div class="navbar-content">
          <!-- Logo -->
          <div class="logo">
            <router-link to="/">ResuMeister</router-link>
          </div>
          <!-- Navigation Items -->
          <nav class="nav-items">
            <router-link to="/">Home</router-link>
            <router-link to="/about">About Us</router-link>
            <router-link to="/templates">Resume Templates</router-link>
            <router-link to="/contact">Contact Us</router-link>
          </nav>
          <!-- Action Buttons -->
          <div class="action-buttons">
            <router-link to="/login" class="btn btn-primary" style="background-color: green;">Log In</router-link>
            <router-link to="/register" class="btn btn-primary">Register Now</router-link>
          </div>
        </div>
      </div>
    </header>

    <!-- Slider Section -->
    <section class="slider">
      <div class="container">
        <h1>Craft Your Perfect Resume</h1>
        <p>Professional templates and easy-to-use tools to help you stand out.</p>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <div class="container">
        <div class="feature-item">
          <i class="fas fa-cogs"></i>
          <h3>Customizable Templates</h3>
          <p>Choose from a variety of modern, customizable templates.</p>
        </div>
        <div class="feature-item">
          <i class="fas fa-user-tie"></i>
          <h3>Professional Design</h3>
          <p>Ensure your resume looks professional and is ATS-friendly.</p>
        </div>
        <div class="feature-item">
          <i class="fas fa-check-circle"></i>
          <h3>Easy & Fast</h3>
          <p>Create and download your resume in minutes with ease.</p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div class="container">
        <p>&copy; 2024 ResuMeister. All rights reserved.</p>
        <nav>
          <router-link to="/privacy">Privacy Policy</router-link>
          <router-link to="/terms">Terms of Service</router-link>
        </nav>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
/* Global Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  box-sizing: border-box;
}

/* Navbar Styles */
.navbar {
  background-color: #333;
  color: #fff;
  padding: 15px 20px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1000;

}

.navbar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar .navbar-content {
  display: flex;
  align-items: center;
  width: 100%;
}

.navbar .logo a {
  font-size: 1.5em;
  color: #fff;
  text-decoration: none;
}

.navbar .nav-items {
  display: flex;
  gap: 20px;
  flex: 1;
  justify-content: center;
}

.navbar .nav-items a {
  color: #fff;
  text-decoration: none;
  font-size: 1em;
}

.navbar .action-buttons {
  display: flex;
  gap: 10px;
  margin-right: 49px;
}

.navbar .btn {
  padding: 10px 20px;
  border-radius: 25px;
  font-size: 0.9em;
  text-decoration: none;
  display: inline-block;
  border: 2px solid transparent;
}

.btn-outline {
  background-color: transparent;
  border-color: #fff;
  color: #fff;
}

.btn-primary {
  background-color: #667eea;
  color: #fff;
  border-color: #667eea;
}

/* Slider Section */
.slider {
  background: url('@/assets/slider-bg.jpeg') no-repeat center center/cover;
  color: #fff;
  text-align: center;
  padding: 100px 20px;
  margin-top: 70px; /* To make space for the fixed navbar */
  width: 100%;
  position: relative;
  margin-left: -8px;
}

.slider h1 {
  font-size: 3em;
  margin-bottom: 20px;
}

.slider p {
  font-size: 1.25em;
  margin-bottom: 30px;
}

/* Features Section */
.features {
  padding: 60px 20px;
  background-color: #fff;
  text-align: center;
}

.features .container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.feature-item {
  max-width: 300px;
  margin: 20px;
  text-align: center;
}

.feature-item i {
  font-size: 3em;
  color: #667eea;
  margin-bottom: 15px;
}

.feature-item h3 {
  font-size: 1.5em;
  margin-bottom: 10px;
}

.feature-item p {
  font-size: 1.1em;
  color: #666;
}

/* Footer */
footer {
  padding: 24px 0;
  background-color: #333;
  color: #fff;
  text-align: center;

}

footer nav {
  margin: 20px 0;
}

footer nav a {
  color: #fff;
  margin: 0 15px;
  text-decoration: none;
}

footer p {
  font-size: 0.9em;
  margin-bottom: 0;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar .nav-items {
    flex-direction: column;
    align-items: center;
  }

  .navbar .action-buttons {
    flex-direction: column;
    align-items: center;
  }

  .slider h1 {
    font-size: 2em;
  }

  .slider p {
    font-size: 1em;
  }

  .features {
    padding: 40px 20px;
  }

  .feature-item {
    margin: 10px;
  }
}
</style>
