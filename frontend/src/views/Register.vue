<template>
  <div class="register-container">
    <!-- Left section for registration form -->
    <div class="register-form">
      <div class="back-link">
        <router-link to="/">←</router-link>
      </div>
      <div class="form-header">
        <h1>Sign Up</h1>
        <p>Secure Your Communications with ResuMeister</p>
      </div>
      <form @submit.prevent="submitForm">
        <div class="input-group">
          <label for="username">Username</label>
          <input
            type="text"
            v-model="form.username"
            required
          />
        </div>
        <div class="input-group">
          <label for="email">Email</label>
          <input
            type="email"
            v-model="form.email"
            required
          />
        </div>
        <div class="input-group password-group">
          <label for="password">Password</label>
          <input
            type="password"
            v-model="form.password"
            required
          />
          <div class="password-requirements">
            <p>• At least 8 characters</p>
            <p>• At least one number (0-9) or symbol</p>
            <p>• Lowercase (a-z) and Uppercase (A-Z)</p>
          </div>
        </div>
        <div class="input-group">
          <label for="confirmPassword">Confirm Password</label>
          <input
            type="password"
            v-model="form.confirmPassword"
            required
          />
        </div>
        <button type="submit" class="submit-btn">Sign Up</button>
        <div class="social-signup">
          <p>Or Sign Up with:</p>
          <div class="social-buttons">
            <button class="google">Google</button>
            <button class="facebook">Facebook</button>
          </div>
        </div>
      </form>
    </div>

    <!-- Right section for background -->
    <div class="register-background">
      <div class="visual-elements">
        <!-- Replace with appropriate image or SVG graphics -->
        <img src="/registration-graphics.jpg" alt="Graphics" />
        <div class="text-elements">
          <h3>Your data, your rules</h3>
          <p>Your data belongs to you, and our encryption ensures its security.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        errorMessage: '',
      },

    };
  },
  methods: {
    async registerUser() {
      if (this.password !== this.confirmPassword) {
        this.errorMessage = "Passwords do not match.";
        return;
      }
      try {
        const response = await fetch('http://localhost:5000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password,
            confirmPassword: this.confirmPassword,
          }),
        });
        const data = await response.json();
        if (response.ok) {
          alert('Registration successful!');
          this.$router.push('/login');
        } else {
          this.errorMessage = data.message;
        }
      } catch (error) {
        this.errorMessage = "There was a problem with the registration.";
      }
    },
  },
};
</script>

<style scoped>
/* General container */
.register-container {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  background-color: #f0f4fa;
}

/* Left form section */
.register-form {
  width: 50%;
  padding: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.back-link {
  margin-bottom: 20px;
}

.form-header h1 {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}

.form-header p {
  font-size: 16px;
  margin-bottom: 30px;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
}

.input-field {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  margin-top: 5px;
}

/* Password requirements styling */
.password-requirements {
  font-size: 14px;
  color: #888;
  margin-top: 8px;
}

.password-requirements ul {
  list-style-type: disc;
  padding-left: 20px;
}

.password-requirements li {
  margin-bottom: 5px;
}

/* Submit button */
.submit-btn {
  background-color: #4b61e1;
  color: white;
  padding: 15px;
  font-size: 18px;
  border: none;
  width: 100%;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 20px;
}

/* Social sign up section */
.social-signup {
  margin-top: 30px;
  text-align: center;
}

.social-signup p {
  font-size: 14px;
  margin-bottom: 10px;
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-button {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  background-color: #f1f1f1;
}

.google {
  background-color: #db4437;
  color: white;
}

.facebook {
  background-color: #3b5998;
  color: white;
}

/* Right background section */
.register-background {
  width: 50%;
  background: linear-gradient(to bottom right, #e0eafc, #cfdef3);
  display: flex;
  align-items: center;
  justify-content: center;
}

.visual-elements {
  text-align: center;
}

.visual-elements img {
  max-width: 100%;
}

.text-elements h3 {
  font-size: 24px;
  margin-top: 20px;
}

.text-elements p {
  font-size: 16px;
  color: #555;
}
</style>
