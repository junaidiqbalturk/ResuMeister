<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar">
      <div class="container">
        <div class="logo">
          <a href="#">ResuMeister</a>
        </div>
        <div class="nav-items">
          <a href="#">Home</a>
          <a href="#">About Us</a>
          <a href="#">Resume Templates</a>
          <a href="#">Contact Us</a>
        </div>
        <div class="action-buttons">
          <a href="#" class="btn btn-outline">Login</a>
          <a href="#" class="btn btn-primary">Register Now</a>
        </div>
      </div>
    </nav>

    <!-- Slider -->
    <section class="slider">
      <swiper :slides-per-view="1" autoplay loop>
        <swiper-slide v-for="(slide, index) in slides" :key="index" class="slider-content">
          <div class="slider-inner">
            <h1>{{ slide.title }}</h1>
            <p>{{ slide.description }}</p>
            <a href="#" class="btn btn-primary">Get Started</a>
          </div>
        </swiper-slide>
      </swiper>
    </section>

    <!-- Features Section -->
    <section class="features">
      <div class="container">
        <div class="feature-item" v-for="feature in features" :key="feature.id">
          <i :class="feature.icon"></i>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <nav>
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Service</a>
        <a href="#">Contact Us</a>
      </nav>
      <p>&copy; 2024 ResuMeister. All rights reserved.</p>
    </footer>
  </div>
</template>


<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/swiper-bundle.css';
export default {
  name: 'Home',
  components: {
    Swiper,
    SwiperSlide
  },
data() {
    return {
      slides: [
        {
          title: 'Create Professional Resumes',
          description: 'Design and customize your resume with ease.'
        },
        {
          title: 'Showcase Your Skills',
          description: 'Highlight your expertise and achievements.'
        },
        {
          title: 'Get Hired Faster',
          description: 'Land your dream job with a top-notch resume.'
        }
      ],
      features: [
        {
          id: 1,
          icon: 'fas fa-file-alt',
          title: 'Beautiful Templates',
          description: 'Choose from a variety of professional templates.'
        },
        {
          id: 2,
          icon: 'fas fa-user-edit',
          title: 'Easy Customization',
          description: 'Personalize your resume to suit your needs.'
        },
        {
          id: 3,
          icon: 'fas fa-share-alt',
          title: 'One-Click Sharing',
          description: 'Share your resume directly with employers.'
        }
      ]
    };
  }
};
</script>

<style scoped>
/* Global Styles */
body {
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  box-sizing: border-box;
  overflow-x: hidden;
}

/* Navbar Styles */
.navbar {
  background-color: #222;
  color: #fff;
  padding: 20px 50px;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.navbar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar .logo a {
  font-size: 1.8em;
  font-weight: bold;
  color: #fff;
  text-decoration: none;
}

.navbar .nav-items {
  display: flex;
  gap: 25px;
}

.navbar .nav-items a {
  color: #fff;
  text-decoration: none;
  font-size: 1.1em;
  transition: color 0.3s ease;
}

.navbar .nav-items a:hover {
  color: #ff6347;
}

.navbar .action-buttons {
  display: flex;
  gap: 15px;
}

.navbar .btn {
  padding: 10px 25px;
  border-radius: 30px;
  font-size: 1em;
  text-decoration: none;
  border: 2px solid transparent;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}

.btn-outline {
  background-color: transparent;
  border-color: #fff;
  color: #fff;
}

.btn-outline:hover {
  background-color: #fff;
  color: #222;
}

.btn-primary {
  background-color: #ff6347;
  color: #fff;
  border-color: #ff6347;
}

.btn-primary:hover {
  background-color: #ff4500;
  border-color: #ff4500;
}

/* Slider Section */
.slider {
  background-color: #222;
  padding: 0;
  width: 100%;
  margin-top: 80px;
  height: 80vh;
  display: flex;
  align-items: center;
}

.slider-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.slider-inner {
  text-align: center;
  color: #fff;
}

.slider h1 {
  font-size: 3.5em;
  margin-bottom: 20px;
}

.slider p {
  font-size: 1.5em;
  margin-bottom: 30px;
}

/* Features Section */
.features {
  padding: 60px 50px;
  background-color: #f4f4f4;
}

.features .container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 30px;
}

.feature-item {
  max-width: 300px;
  text-align: center;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-10px);
}

.feature-item i {
  font-size: 3em;
  color: #ff6347;
  margin-bottom: 15px;
}

.feature-item h3 {
  font-size: 1.6em;
  margin-bottom: 10px;
}

.feature-item p {
  font-size: 1.1em;
  color: #666;
}

/* Footer */
footer {
  padding: 30px 50px;
  background-color: #222;
  color: #fff;
  text-align: center;
  margin-top: 50px;
}

footer nav {
  margin: 20px 0;
}

footer nav a {
  color: #fff;
  margin: 0 15px;
  text-decoration: none;
  font-size: 1em;
  transition: color 0.3s ease;
}

footer nav a:hover {
  color: #ff6347;
}

footer p {
  font-size: 1em;
  margin-bottom: 0;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar .container {
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar .nav-items {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    margin-top: 15px;
  }

  .navbar .action-buttons {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    margin-top: 15px;
  }

  .slider h1 {
    font-size: 2.5em;
  }

  .slider p {
    font-size: 1.2em;
  }

  .features .container {
    flex-direction: column;
    align-items: center;
  }
}
</style>
