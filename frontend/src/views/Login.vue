<template>
  <div class="login-page">
    <!-- Background Section -->
    <div class="background"></div>

    <!-- Login Form Section -->
    <div class="login-container">
      <div class="login-box">
        <h2>Login</h2>

        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" v-model="email" class="form-control" id="email" required />
          </div>

          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" v-model="password" class="form-control" id="password" required />
          </div>

          <button type="submit" class="btn btn-primary btn-block">Login</button>
        </form>

        <div class="extra-links">
          <a href="#">Forgot Password?</a>
          <a href="/register">Sign Up</a>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        const data = await response.json();
        if (data.success) {
          // Handle successful login (e.g., redirect to dashboard)
          alert('Login successful');
          this.$router.push('/Dashboard');
        } else {
          // Handle error (e.g., display error message)
          alert('Login failed');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Background Styling */
.background {
  background-image: url('https://www.photofunky.net/output/image/a/9/9/e/a99e96/s500x200.gif'); /* Add your background image here */
  background-size: cover;
  background-position: center;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1;
}

/* Login Container */
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: 'Poppins', sans-serif;
}

.login-container {
  background: rgba(255, 255, 255, 0.85); /* Semi-transparent background */
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  max-width: 400px;
  width: 100%;
}

h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1rem;
  font-weight: 600;
  color: #333;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-control {
  width: 100%;
  padding: 0.75rem;
  border-radius: 5px;
  border: 1px solid #ddd;
  font-size: 1rem;
}

.btn-block {
  width: 100%;
  padding: 0.75rem;
  border-radius: 5px;
  background-color: #ff6f61; /* Accent color */
  color: white;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-block:hover {
  background-color: #ff5a4d; /* Hover effect */
}

.extra-links {
  text-align: center;
  margin-top: 1rem;
}

.extra-links a {
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  margin: 0 0.5rem;
}

.extra-links a:hover {
  text-decoration: underline;
}
</style>