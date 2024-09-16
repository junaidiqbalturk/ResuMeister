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
    <div class="nav-toggle">
      <button class="nav-toggle-btn" aria-label="Toggle navigation">
        <span class="nav-toggle-icon"></span>
      </button>
    </div>
    <div class="nav-items">
      <a href="#">Why ResuMeister</a>
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
   <section class="sliders">
      <div class="glide">
        <div class="glide__track" data-glide-el="track">
          <ul class="glide__slides">
            <li class="glide__slide" v-for="(item, index) in items" :key="index">
              <img :src="item.image" :alt="item.text" />
              <div class="slide-text"><h2>{{ item.text }}</h2></div>
              <div class="slide-description">{{ item.description }}</div>
              <div class="slide-buttons">
                <a v-for="(button, btnIndex) in item.buttons" :key="btnIndex" :href="button.link" class="btn" :class="{'btn-primary': btnIndex === 0, 'btn-secondary': btnIndex !== 0}">
                  {{ button.text }}
                </a>
              </div>
            </li>
          </ul>
        </div>
        <div class="glide__arrows" data-glide-el="controls">
          <button class="glide__arrow glide__arrow--left" data-glide-dir="<">&lt;</button>
          <button class="glide__arrow glide__arrow--right" data-glide-dir=">">&gt;</button>
        </div>
        <div class="glide__bullets" data-glide-el="controls[nav]">
          <button class="glide__bullet" v-for="(item, index) in items" :key="'bullet-'+index" :data-glide-dir="'='+index"></button>
        </div>
      </div>
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
              <circle class="inner-circle" cx="50" cy="50" r="44" fill="#489FB5" />
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
              stroke="#000000"
              stroke-width="2"
              stroke-dasharray="4,2"
            />
            <polygon
                class="arrow-head"
              points="85,5 85,15 95,10"
              fill="#000000"
            />
          </svg>
        </div>
      </div>
    </div>
  </section>
<!-- ends here-->
    <!-- Advertisement Section --->
    <section class = "cta-section">
      <h2>Ready to Land Your Dream Job?</h2>
      <p>Sign up today and start building your professional resume with ResuMeister.</p>

      <div class="clock">
        <div class="top"></div>
        <div class="right"></div>
        <div class="bottom"></div>
        <div class="left"></div>
        <div class="center"></div>
        <div class="shadow"></div>
        <div class="hour"></div>
        <div class="minute"></div>
        <div class="second"></div>
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
      <h2 class="typing-text">Not Sure Where to Start?</h2>
      <p>Explore Our Expert Resume Templates and Get Inspired to Create Yours!</p>
      <a href="/templates" class="cta btn">View Templates</a>

      <div class="floating-icons">
          <img src="/resume-icon1.png" alt="Resume Icon 1" class="floating-icon">
          <img src="/resume-icon2.png" alt="Resume Icon 2" class="floating-icon">
          <img src="/resume-icon3.png" alt="Resume Icon 3" class="floating-icon">
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
import Glide from '@glidejs/glide';
import '@glidejs/glide/dist/css/glide.core.min.css';
import '@glidejs/glide/dist/css/glide.theme.min.css';
export default {
  name: 'Home',
  data() {
    return {
      items: [
        {
          image: '/slide1.jpg',
          text: 'Craft Your Perfect Resume with ResuMeister!',
          description: 'Create professional resumes effortlessly and stand out from the crowd',
          buttons: [
          { text: 'Get Started Now', link: '#learn-more' },
        ]
        },
        {
          image: '/slide1.jpg',
          text: 'Why Choose ResuMeister?',
          description: 'Features That Make Resume Building Simple and Effective',
          buttons: [
          { text: 'Explore Features', link: '#learn-more' },
        ]
        },
        {
          image: '/slide1.jpg',
          text: 'Success Stories from Our Users',
          description: 'See How ResuMeister Has Helped Professionals Achieve Their Career Goals',
          buttons: [
          { text: 'Read Their Stories', link: '#learn-more' },
        ]
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
  },
  mounted() {
  this.$nextTick(() => {
    setTimeout(() => {
      this.initializeGlide();
    }, 100);
  });
},
  methods: {
    initializeGlide() {
      new Glide('.glide', {
        type: 'carousel',
        perView: 1,
        focusAt: 'center',
        gap: 0,
        autoplay: 5000,
        hoverpause: true,
        animationDuration: 1000,
        breakpoints: {
          800: {
            perView: 1
          }
        }
      }).mount();
    }
  }
};
</script>

<style scoped>
/* CLock section css */
.cta-section {
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 20px;
  text-align: center;
  background: #FF851B;
}

.cta-section h2{
  font-family: 'Poppins', sans-serif;
  color: #FFFFFF;
}

.cta-section p{
  font-family: 'Roboto', sans-serif;
  color: #FFFFFF;
}

@media (max-width: 768px) {
  .cta-section {
    flex-direction: column;
    text-align: center;
  }
}


.clock {
  position: relative;
  height: 200px;
  width: 200px;
  background: white;
  box-sizing: border-box;
  border-radius: 100%;
  border: 10px solid #67D2C8;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  .top {
    position: absolute;
    width: 3px;
    height: 8px;
    background: #262626;
    left: 0;
    right: 0;
    margin: 0 auto;
  }
  .right {
    position: absolute;
    width: 8px;
    height: 3px;
    background: #262626;
    top: 0;
    bottom: 0;
    right: 0;
    margin: auto 0;
  }
  .bottom {
    position: absolute;
    width: 3px;
    height: 8px;
    background: #262626;
    left: 0;
    right: 0;
    bottom: 0;
    margin: 0 auto;
  }
  .left {
    position: absolute;
    width: 8px;
    height: 3px;
    background: #262626;
    top: 0;
    bottom: 0;
    left: 0;
    margin: auto 0;
  }
  .center {
    height: 6px;
    width: 6px;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
    background: #262626;
    border-radius: 100%;
  }
  .shadow {
    height: 200px;
    width: 200px;
    position: absolute;
    left: 60px;
    top: 60px;
    transform: rotate(135deg);
    background: linear-gradient(transparent, rgba(000, 0.1));
  }
  .hour {
    width: 3px;
    height: 100%;
    position: absolute;
    left: 0;
    right: 0;
    margin: 0 auto;
    /*animation: time 86400s infinite linear;*/
    animation: time 60s infinite linear;
    &:before {
      position: absolute;
      content: "";
      background: #262626;
      height: 60px;
      width: 3px;
      top: 30px;
    }
  }
  .minute {
    width: 1px;
    height: 100%;
    position: absolute;
    left: 0;
    right: 0;
    margin: 0 auto;
    animation: time 30s infinite linear;
    &:before {
      position: absolute;
      content: "";
      background: #262626;
      height: 40px;
      width: 1px;
      top: 50px;
    }
  }
  .second {
    width: 2px;
    height: 100%;
    position: absolute;
    left: 0;
    right: 0;
    margin: 0 auto;
    animation: time 15s infinite linear;
    &:before {
      position: absolute;
      content: "";
      background: #fd1111;
      height: 45px;
      width: 2px;
      top: 45px;
    }
  }
}

@keyframes time {
  to {
    transform: rotate(360deg);
  }
}


/* Ends here*/
.slide-buttons {
  margin-top: 240px; /* Space between text and buttons */
  display: flex;
  justify-content: center; /* Center buttons horizontally */
  position: absolute;
}

.slide-buttons .btn {
  margin: 0 5px; /* Space between buttons */
  padding: 10px 20px; /* Padding inside buttons */
  text-decoration: none;
  color: white;
  border-radius: 5px; /* Optional: for rounded buttons */
}

.btn-primary {
  background-color: #001F3F; /* Primary button color */
}

.btn-secondary {
  background-color: #6c757d; /* Secondary button color */
}
/* glide carousel css */
.sliders {
  position: relative;
}
.slide-text {
  position: absolute;
  font-family: 'Poppins', sans-serif;
  bottom: 50%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, 50%); /* Adjust for centering */
  color: white;
  font-size: 24px;
  padding: 10px;
  border-radius: 5px; /* Optional: for a rounded look */
  text-align: center; /* Center text inside the box */
  z-index: 10; /* Ensures text appears above other content */
}
.glide {
  height: 100%;
}

.glide__track,
.glide__slides {
  height: 100%;
}

.glide__slide {
  position: relative;
  display: flex;
  align-items: center; /* Center vertically */
  justify-content: center; /* Center horizontally */
}


.glide__arrows {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
}

.glide__arrow {
  position: absolute;
  background-color: rgba(255, 255, 255, 0.7);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.glide__arrow--left {
  left: 20px;
}

.glide__arrow--right {
  right: 20px;
}

.glide__bullets {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
}
.slide-description {
  display: block; /* Ensure the description is a block-level element */
  width: 100%; /* Make the description span the full width of the container */
  margin-top: 120px; /* Optional: add some space between the heading and description */
  position: absolute;
  padding: 10px; /* Example padding */
  font-family: 'Roboto', sans-serif;
  color: white;
  font-size: 20px;
  text-align: center;
}
.glide__bullet {
  width: 10px;
  height: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  border: none;
  border-radius: 50%;
  cursor: pointer;
}

.glide__bullet--active {
  background-color: white;
}

/* Adjust layout for sections after the slider */

/*ends here */



/* New Try here ends here*/
.how-it-workss {
  background-color: #FFFFFF;
  padding: 50px 20px;
  color: #001F3F;
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
  fill: #489FB5;
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
/* for mobile devices and small devices responsiveness */
/* Add media queries for smaller screen sizes */
@media (max-width: 768px) {
  .how-it-workss {
    padding: 30px 10px;
  }

  .section-titles {
    font-size: 1.8rem;
    margin-bottom: 20px;
  }

  .steps-containers {
    flex-direction: column; /* Stack the steps vertically */
    align-items: center;
  }

  .steps {
    margin-bottom: 30px; /* Add margin between steps */
    text-align: center;
    flex: 1 1 100%; /* Make each step take full width */
  }

  .step-number-wrapper {
    width: 80px;
    height: 80px;
    margin-bottom: 10px;
  }

  .step-numbers {
    width: 80px;
    height: 80px;
  }

  .step-titles {
    font-size: 1.3rem;
  }

  .step-descriptions {
    font-size: 0.9rem;
    line-height: 1.3;
  }

  .curved-arrows {
    display: none; /* Hide arrows on smaller screens */
  }
}

@media (max-width: 480px) {
  .section-titles {
    font-size: 1.5rem;
    margin-bottom: 15px;
  }

  .step-number-wrapper {
    width: 60px;
    height: 60px;
  }

  .step-numbers {
    width: 60px;
    height: 60px;
  }

  .step-titles {
    font-size: 1.2rem;
  }

  .step-descriptions {
    font-size: 0.8rem;
  }
}

/* for mobile devices and small devices responsiveness */

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
  background: #FFDC00;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.heading-container {
  text-align: center;
  margin-bottom: 30px;
  color: #333333
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
  background: #FFDC00; /* Light background for contrast */
  color: #333333;
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
.navbar, .features, .how-it-works, .testimonials, .cta, footer {
  width: 100%;
  box-sizing: border-box;
}

body {
  overflow-x: hidden;
}


/* Navbar Styles */
.navbar {
  background-color: #001f3f;
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
  color: #00D1B2;
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
  background-color: #001F3F;
  color: #fff;
  border-color: #CC7700;
}

.btn-primary:hover {
  background-color: #00D1B2;
  border-color: #00D1B2;
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
  background-color: #F4F6F8;
  text-align: center;

}

.testimonials h2 {
  font-size: 2.5em;
  margin-bottom: 30px;
  color: #333333;
  font-family: 'Poppins', sans-serif;
}

.testimonials-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 30px;
  font-family: 'Roboto', sans-serif;
}

.testimonial {
  max-width: 350px;
  background-color: #F4F6F8;
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
  color: #333333;
  margin-bottom: 10px;
}

.testimonial-author {
  font-size: 1.1em;
  font-weight: bold;
  color: #333;
}

/* Call to Action Section */
.cta {
  position: relative;
  background: #2ECC40;
  color: #FFFFFF;
  text-align: center;
  padding: 50px 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden; /* To ensure floating icons don't go outside the container */

}

.cta h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif
}

.cta p {
  font-size: 1.2rem;
  margin-bottom: 30px;
  font-family: 'Roboto', sans-serif;
}

.cta .btn {
  background-color: #001F3F; /* Bright Neon Green */
  color: white;
  padding: 15px 30px;
  text-decoration: none;
  font-size: 1.2rem;
  border-radius: 5px;
  transition: background-color 0.3s ease;
  font-family: 'Roboto', sans-serif;
}

.cta .btn:hover {
   background-color: #00CC6E; /* Darker green on hover */
}
/* typing effect and floating in CTA */
.typing-text {
  white-space: nowrap;
  overflow: hidden;
  border-right: 2px solid;
  width: 0;
  animation: typing 3.5s steps(40, end) forwards, blink .75s step-end infinite;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  50% { border-color: transparent; }
}

/* Floating Icons */
.floating-icons {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.floating-icon {
  position: absolute;
  animation: float 6s ease-in-out infinite;
  width: 50px;
  opacity: 0.7;
}

.floating-icon:nth-child(1) {
  top: 43%;
  left: 10%;
  animation-duration: 5s;
}

.floating-icon:nth-child(2) {
  top: 40%;
  left: 80%;
  animation-duration: 7s;
}

.floating-icon:nth-child(3) {
  top: 70%;
  left: 58%;
  animation-duration: 6.5s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

@media (max-width: 768px) {
  .cta {
    padding: 30px 15px;
  }

  .cta h2 {
    font-size: 2rem;
  }

  .cta p {
    font-size: 1rem;
  }

  .cta btn {
    padding: 12px 25px;
    font-size: 1rem;
  }

  .floating-icon {
    width: 40px;
  }
}

/* Footer */
footer {
  padding: 30px 50px;
  background-color: #111111;
  color: #FFFFFF;
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
  color: #00D1B2;
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
