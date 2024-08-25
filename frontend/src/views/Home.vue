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
    <!-- Slider -->
    <section class="slider">
      <swiper-container
        :slides-per-view="1"
        :autoplay="{ delay: 3000 }"
        loop
        pagination
        class="swiper-container"
      >
        <swiper-slide v-for="(slide, index) in slides" :key="index">
          <div class="slide-content" :style="{ backgroundImage: `url(${slide.image})` }">
            <h1>{{ slide.title }}</h1>
            <p>{{ slide.description }}</p>
            <button class="get-started-button">Get Started</button>
          </div>
        </swiper-slide>
      </swiper-container>
    </section>


    <section class="why-choose">
      <div class="heading-container">
        <h2 class="section-heading">Why Choose ResuMeister</h2>
      </div>
    <div class="card-container">
      <div class="card feature-item" v-for="feature in features" :key="feature.id">
        <div class="icon">{{ feature.icon }}</div>
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
      </div>
    </div>
  </section>
    <!-- second try -->
  <section class="how-it-workss">
    <h2 class="section-titles">How ResuMeister Works</h2>
    <div class="steps-containers">
      <div class="steps" v-for="(step, index) in steps" :key="index">
        <div class="step-number-containers">
          <div class="step-number-wrapper">
            <svg class="step-numbers" viewBox="0 0 100 100">
              <defs>
                <linearGradient id="circle-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#FF99CC" />
                  <stop offset="100%" stop-color="#FF3399" />
                </linearGradient>
              </defs>
              <circle class="outer-circle" cx="50" cy="50" r="48" fill="url(#circle-gradient)" />
              <circle class="inner-circle" cx="50" cy="50" r="44" fill="#FF66B2" />
              <text class="step-text" x="50" y="65" text-anchor="middle">{{ step.id }}</text>
            </svg>
          </div>
      </div>
        <div class="step-contents">
          <div class="step-titles">{{ step.title }}</div>
          <div class="step-descriptions">{{ step.description }}</div>
        </div>
        <!-- Display arrow unless it's the last step -->
        <div class="curved-arrows" v-if="index < steps.length - 1">
          <svg viewBox="0 0 100 50">
            <path
              class="arrow-path"
              d="M0 40 C 20 40, 20 10, 90 10"
              fill="none"
              stroke="#fff"
              stroke-width="2"
              stroke-dasharray="4,2"
            />
            <polygon
                class="arrow-head"
              points="85,5 85,15 95,10"
              fill="#fff"
            />
          </svg>
        </div>
      </div>
    </div>
  </section>
<!-- ends here-->
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
          icon: '🚀',
          title: 'Easy to Use',
          description: 'Our user-friendly interface lets you create your resume with just a few clicks.'
        },
        {
          id: 2,
          icon: '🎨',
          title: 'Professional Templates',
          description: 'Choose from a variety of templates designed by experts.'
        },
        {
          id: 3,
          icon: '🔒',
          title: 'Customizable',
          description: 'Tailor your resume to your unique style and profession.'
        },
        {
          id: 4,
          icon: '💬',
          title: 'ATS Friendly',
          description: 'Our resumes are optimized to get past Applicant Tracking Systems.'
        }
      ],
      steps: [
        {
          id: 1,
          icon: '🔍',
          title: 'Select a Template',
          description: 'Choose from a range of professional templates.'
        },
        {
          id: 2,
          icon: '📝',
          title: 'Enter Your Details',
          description: 'Fill in your personal information, work experience, and skills.'
        },
        {
          id: 3,
          icon: '✏️',
          title: 'Customize',
          description: 'Adjust the layout, colors, and fonts to your preference.'
        },
        {
          id: 4,
          icon: '📥',
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
/* swiper slider*/

/* Swiper Styles */
.swiper-container {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  background-size: cover;
  background-position: center;
}

.slide-content {
  text-align: center;
  color: #fff;
}


/* ends here */



/* New Try here ends here*/
.how-it-workss {
  background-color: #5B2DC7;
  padding: 50px 20px;
  color: white;
  text-align: center;
}

.section-titles {
  font-size: 2.5rem;
  margin-bottom: 40px;
  font-weight: bold;
  font-family: 'Poppins', sans-serif;
}

.steps-containers {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

.steps {
  text-align: center;
  margin: 0 20px;
  position: relative;
  flex: 1;
}

.step-number-containers {
  position: relative;
  margin-bottom: 20px;
}

.step-number-wrapper {
  perspective: 1000px;
  transition: transform 0.3s ease;
}

.step-number-wrapper:hover {
  transform: scale(1.05);
}

.step-numbers {
  width: 100px;
  height: 100px;
  margin: 0 auto;
  filter: drop-shadow(3px 3px 2px rgba(0, 0, 0, 0.3));
  transition: transform 0.3s ease;
}

.step-number-wrapper:hover .step-numbers {
  transform: rotateY(10deg) rotateX(10deg);
}

.outer-circle {
  transition: fill 0.3s ease;
}

.step-number-wrapper:hover .outer-circle {
  fill: url(#circle-gradient-hover);
}

.inner-circle {
  fill: #FF66B2;
  transition: fill 0.3s ease;
}

.step-number-wrapper:hover .inner-circle {
  fill: #FF3399;
}

.step-text {
  font-size: 48px;
  font-weight: bold;
  fill: black;
  stroke: black;
  stroke-width: 1px;
  paint-order: stroke;
  stroke-dasharray: 3 3;
  text-shadow: 2px 2px 1px rgba(255, 255, 255, 0.5);
  transition: transform 0.3s ease;
}

.step-number-wrapper:hover .step-text {
  transform: scale(1.1) rotate(-5deg);
}

.step-contents {
  margin-top: 10px;
}

.step-titles {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
  font-family: 'Roboto', sans-serif;
}

.step-descriptions {
  font-size: 1rem;
  line-height: 1.5;
  font-family: 'Roboto', sans-serif;
}

.curved-arrows {
  width: 121px;
  height: 61px;
  position: absolute;
  top: 10px;
  right: -66px;
  transform: rotate(0deg);
}

.arrow-path {
  stroke-dasharray: 4 2;
  animation: dash 1s linear infinite;
}
.arrow-head {
  animation: pulse 2s ease-in-out infinite;
  transform-origin: 90px 10px;
}
@keyframes dash {
  to {
    stroke-dashoffset: -20;
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
}

.curved-arrows svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

/* Ensure the arrows don't appear after the last step */
.steps-container .step:nth-child(4) .curved-arrow {
  display: none;
}
/* New Try here ends here*/

.section-heading {
  font-size: 2.5rem;
  font-family: 'Poppins', sans-serif;
  color: #333;
  margin-bottom: 40px;
  animation: fadeInUp 1s ease-out;
}

/* How it works css ends here */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
.why-choose {
  padding: 40px 20px;
  background: #f4f4f9;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.heading-container {
  text-align: center;
  margin-bottom: 30px;
}

.section-heading {
  font-size: 2.5rem;
  font-family: 'Poppins', sans-serif; /* Use the professional font */
  color: #333;
  animation: fadeInUp 1s ease-out;
}

/* Keyframes for the refined heading animation */
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

/*Why Choose section CSS above end */
.why-choose {
  padding: 40px 20px;
  background: #f4f4f9; /* Light background for contrast */
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px; /* Space between cards */
  justify-content: center;
}

.card {
  background: #fff; /* White background for a clean look */
  border-radius: 15px;
  padding: 20px;
  width: 250px;
  text-align: center;
  color: #333; /* Dark text for better readability */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}


.icon {
  font-size: 3rem; /* Large icon */
  margin-bottom: 10px;
  transition: transform 0.3s;
}

.card:hover .icon {
  transform: rotate(20deg); /* Rotate icon on hover */
}


/* Global Styles */
body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
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
  font-family: 'Roboto', sans-serif;
}

.feature-item p {
  font-size: 1em;
  color: #666;
  font-family: 'Roboto', sans-serif;
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
    font-family: 'Poppins', sans-serif;
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
.swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  background-size: cover;
  background-position: center;
  color: #fff;
  text-align: center;
  flex-direction: column;
  font-family: 'Poppins', sans-serif;
}
h1 {
  font-size: 3em;
}

p {
  font-size: 1.5em;
}
.get-started-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: brown;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  font-family: 'Poppins', sans-serif;

  /* Animation properties */
  opacity: 0; /* Start as invisible */
  transform: translateX(50px); /* Start shifted to the right */
  animation: slideIn 0.6s forwards; /* Apply the animation */
}

.get-started-button:hover {
  background-color: #0056b3;
}

/* Keyframes for sliding in */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
