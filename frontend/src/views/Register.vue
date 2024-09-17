<template>
  <div class="signup-container">
    <!-- Left section: Form -->
    <div class="signup-form">
      <div class="form-header">
        <h1>Sign Up</h1>
        <p>Secure Your Communications with Easymail</p>
      </div>
      <form class="form-body" @submit.prevent="onSubmit">
        <!-- Name input -->
        <div class="input-group">
          <svg class="icon"><!-- User Icon SVG --></svg>
          <input type="text" placeholder="Daniel Ahmadi" required />
          <svg class="valid-icon"><!-- Checkmark SVG --></svg>
        </div>
        <!-- Email input -->
        <div class="input-group">
          <svg class="icon"><!-- Email Icon SVG --></svg>
          <input type="email" placeholder="11Danielahmadi@gmail.com" required />
          <svg class="valid-icon"><!-- Checkmark SVG --></svg>
        </div>
        <!-- Password input -->
        <div class="input-group">
          <svg class="icon"><!-- Password Icon SVG --></svg>
          <input type="password" placeholder="Password" required />
          <svg class="visibility-icon"><!-- Eye Icon SVG --></svg>
        </div>
        <!-- Password requirements -->
        <ul class="password-requirements">
          <li>At least 8 characters</li>
          <li>At least one number (0-9) or a symbol</li>
          <li>Lowercase (a-z) and uppercase (A-Z)</li>
        </ul>
        <!-- Confirm password input -->
        <div class="input-group">
          <svg class="icon"><!-- Re-type Password Icon SVG --></svg>
          <input type="password" placeholder="Re-Type Password" required />
        </div>
        <!-- Submit button -->
        <button type="submit" class="submit-btn">Sign Up <svg><!-- Arrow Icon --></svg></button>
        <!-- Or login with social media -->
        <div class="social-login">
          <p>Or sign up with:</p>
          <div class="social-buttons">
            <button class="social-btn fb-btn"><svg><!-- Facebook Icon --></svg></button>
            <button class="social-btn google-btn"><svg><!-- Google Icon --></svg></button>
          </div>
        </div>
      </form>
    </div>

    <!-- Right section: Info cards -->
    <div class="signup-info">
      <div class="info-card">
        <p>Inbox</p>
        <h2>176,18</h2>
        <div class="graph"><!-- Placeholder for small graph SVG --></div>
      </div>
      <div class="info-card">
        <p>Your data, your rules</p>
        <p>Your data belongs to you, and our encryption ensures that...</p>
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
/* General styles */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f4f7ff;
}

.signup-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 100vh;
  background-color: #f0f4ff;
}

.signup-form {
  width: 50%;
  padding: 60px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
}

.form-header h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.form-header p {
  font-size: 1.1rem;
  color: #8e8e8e;
}

.form-body {
  margin-top: 20px;
}

.input-group {
  position: relative;
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
}

.input-group input {
  flex-grow: 1;
  border: none;
  padding: 0 15px;
  font-size: 1.1rem;
  outline: none;
}

.icon, .valid-icon, .visibility-icon {
  width: 20px;
  height: 20px;
  fill: #8e8e8e;
}

.password-requirements {
  list-style: none;
  padding: 10px;
  font-size: 0.85rem;
  color: #8e8e8e;
  margin-bottom: 20px;
}

.password-requirements li {
  margin-bottom: 5px;
}

.submit-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #4a90e2;
  color: #fff;
  border: none;
  padding: 15px;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 20px;
}

.submit-btn svg {
  margin-left: 10px;
}

.social-login {
  text-align: center;
  margin-top: 20px;
}

.social-login p {
  font-size: 0.9rem;
  color: #8e8e8e;
  margin-bottom: 10px;
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background-color: #f4f4f4;
}

.fb-btn {
  background-color: #3b5998;
}

.google-btn {
  background-color: #db4437;
}

.signup-info {
  width: 40%;
  padding: 40px;
}

.info-card {
  background-color: #fff;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}

.info-card p {
  font-size: 1.1rem;
  color: #8e8e8e;
}

.info-card h2 {
  font-size: 2rem;
  font-weight: bold;
}

.graph {
  width: 100px;
  height: 50px;
  background-color: #ececec;
  margin-top: 10px;
  border-radius: 5px;
}
</style>
