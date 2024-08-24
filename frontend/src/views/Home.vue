<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar">
      <div class="container">
        <div class="logo">
          <a href="#">
            <img src="/resumeister.png" alt="ResuMeister Logo" class="logo-img">
          </a>
        </div>
        <div class="nav-items">
          <a href="#">Home</a>
          <a href="#">About Us</a>
          <a href="#">Resume Templates</a>
          <a href="#">Contact Us</a>
        </div>
        <div class="action-buttons">
          <a href="/login" class="btn btn-outline">Login</a>
          <a href="/register" class="btn btn-primary">Register Now</a>
        </div>
      </div>
    </nav>

    <!-- Slider -->
    <section class="slider">
      <swiper :slides-per-view="1" autoplay loop>
        <swiper-slide v-for="(slide, index) in slides" :key="index" class="slider-content">
          <div class="slider-inner" :style="{ backgroundImage: `url(${slide.image})` }">
            <h1>{{ slide.title }}</h1>
            <p>{{ slide.description }}</p>
            <a href="#" class="btn btn-primary">Get Started</a>
          </div>
        </swiper-slide>
      </swiper>
    </section>

    <!-- Features Section -->
    <section class="features">
      <h2>Why Choose ResuMeister?</h2>
      <div class="container">
        <div class="feature-item" v-for="feature in features" :key="feature.id">
          <i :class="feature.icon"></i>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works">
      <h2>How It Works</h2>
      <div class="steps-container">
        <div class="step" v-for="step in steps" :key="step.id">
          <i :class="step.icon"></i>
          <h3>{{ step.title }}</h3>
          <p>{{ step.description }}</p>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
      <h2>What Our Users Say</h2>
      <div class="testimonials-container">
        <div class="testimonial" v-for="testimonial in testimonials" :key="testimonial.id">
          <img :src="testimonial.photo" alt="User Photo" class="testimonial-photo">
          <p class="testimonial-text">“{{ testimonial.feedback }}”</p>
          <p class="testimonial-author">{{ testimonial.name }}, {{ testimonial.jobTitle }}</p>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="cta">
      <h2>Ready to Land Your Dream Job?</h2>
      <p>Sign up today and start building your professional resume with ResuMeister.</p>
      <a href="#" class="btn btn-primary">Create Your Resume</a>
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
import { Autoplay } from 'swiper';
import 'swiper/css';
import 'swiper/css/autoplay';
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
          description: 'Design and customize your resume with ease.',
          image: '/slide1.jpg'
        },
        {
          title: 'Showcase Your Skills',
          description: 'Highlight your expertise and achievements.',
          image: '/slide2.jpg'
        },
        {
          title: 'Get Hired Faster',
          description: 'Land your dream job with a top-notch resume.',
          image: '/slide3.jpg'
        }
      ],
      features: [
        {
          id: 1,
          icon: 'fas fa-star',
          title: 'Easy to Use',
          description: 'Our user-friendly interface lets you create your resume with just a few clicks.'
        },
        {
          id: 2,
          icon: 'fas fa-briefcase',
          title: 'Professional Templates',
          description: 'Choose from a variety of templates designed by experts.'
        },
        {
          id: 3,
          icon: 'fas fa-cogs',
          title: 'Customizable',
          description: 'Tailor your resume to your unique style and profession.'
        },
        {
          id: 4,
          icon: 'fas fa-check',
          title: 'ATS Friendly',
          description: 'Our resumes are optimized to get past Applicant Tracking Systems.'
        }
      ],
      steps: [
        {
          id: 1,
          icon: 'fas fa-template',
          title: 'Select a Template',
          description: 'Choose from a range of professional templates.'
        },
        {
          id: 2,
          icon: 'fas fa-user',
          title: 'Enter Your Details',
          description: 'Fill in your personal information, work experience, and skills.'
        },
        {
          id: 3,
          icon: 'fas fa-paint-brush',
          title: 'Customize',
          description: 'Adjust the layout, colors, and fonts to your preference.'
        },
        {
          id: 4,
          icon: 'fas fa-download',
          title: 'Download',
          description: 'Save your resume as a PDF or share it directly with employers.'
        }
      ],
      testimonials: [
        {
          id: 1,
          photo: '/slide1.jpg',
          feedback: 'ResuMeister helped me land my dream job! The templates are top-notch and easy to use.',
          name: 'Jane Doe',
          jobTitle: 'Marketing Specialist'
        },
        {
          id: 2,
          photo: '/slide2.jpg',
          feedback: 'I love the customization options. My resume looks fantastic!',
          name: 'John Smith',
          jobTitle: 'Software Engineer'
        },
        {
          id: 3,
          photo: '/slide3.jpg',
          feedback: 'The ATS-friendly feature is a game-changer. I got more interviews after using ResuMeister.',
          name: 'Emily Johnson',
          jobTitle: 'Graphic Designer'
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
  font-family: 'Inter', sans-serif;
  box-sizing: border-box;
  overflow-x: hidden;
  width: 100%;
  height: 100%;
}
.logo-img {
  max-width: 150px;
  max-height: 150px; /* Ensures the logo doesn't exceed this height */
  height: auto;
}

.container {
  width: 100%;
  max-width: 1200px; /* Or any max-width suitable for your design */
  margin: 0 auto; /* Center the container */
  padding: 0 15px; /* Add some padding if needed */
}
section, .feature-item, .step, .testimonial {
  box-sizing: border-box;
}
.navbar, .slider, .features, .how-it-works, .testimonials, .cta, footer {
  width: 100%;
  box-sizing: border-box;
}
.slider {
  width: 100vw;
  height: 80vh;
}
body {
  overflow-x: hidden;
}


/* Navbar Styles */
.navbar {
  background-color: brown;
  color: #fff;
  padding: 7px 28px;
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
  text-align: center;
}

.features h2 {
  font-size: 2.5em;
  margin-bottom: 30px;
  color: #333;
}

.features .container {
  display: flex;
  justify-content: center;
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
  font-size: 2em;
  color: #ff6347;
  margin-bottom: 15px;
}

.feature-item h3 {
  font-size: 1.4em;
  margin-bottom: 10px;
}

.feature-item p {
  font-size: 1em;
  color: #666;
}

/* How It Works Section */
.how-it-works {
  padding: 60px 50px;
  background-color: #fff;
  text-align: center;
}

.how-it-works h2 {
  font-size: 2.5em;
  margin-bottom: 30px;
  color: #333;
}

.steps-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 30px;
}

.step {
  max-width: 250px;
  text-align: center;
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.step:hover {
  transform: translateY(-10px);
}

.step i {
  font-size: 2.5em;
  color: #ff6347;
  margin-bottom: 15px;
}

.step h3 {
  font-size: 1.4em;
  margin-bottom: 10px;
}

.step p {
  font-size: 1em;
  color: #666;
}

/* Testimonials Section */
.testimonials {
  padding: 60px 50px;
  background-color: #f4f4f4;
  text-align: center;
}

.testimonials h2 {
  font-size: 2.5em;
  margin-bottom: 30px;
  color: #333;
}

.testimonials-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 30px;
}

.testimonial {
  max-width: 350px;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  text-align: center;
}

.testimonial:hover {
  transform: translateY(-10px);
}

.testimonial-photo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 15px;
}

.testimonial-text {
  font-size: 1em;
  color: #666;
  margin-bottom: 10px;
}

.testimonial-author {
  font-size: 1.1em;
  font-weight: bold;
  color: #333;
}

/* Call to Action Section */
.cta {
  padding: 60px 50px;
  background-color: #ff6347;
  color: #fff;
  text-align: center;
}

.cta h2 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.cta p {
  font-size: 1.2em;
  margin-bottom: 30px;
}

.cta .btn {
  padding: 15px 30px;
  font-size: 1.2em;
  border-radius: 30px;
  background-color: #fff;
  color: #ff6347;
  border-color: #fff;
}

.cta .btn:hover {
  background-color: #f4f4f4;
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

  .steps-container {
    flex-direction: column;
  }

  .testimonials-container {
    flex-direction: column;
  }
}
</style>
