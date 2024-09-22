<template>
  <div class="registration-container">
    <div class="form-section">
      <h1 class="form-title">Sign Up</h1>
      <p class="form-subtitle">Secure Your Communications with ResuMeister</p>

      <form class="form-body">
        <!-- Name Field -->
        <div class="input-group">
          <input type="text" id="username" class="input-field" v-model="form.username" required />
          <label for="username" class="floating-label">Your Name</label>
        </div>

        <!-- Email Field -->
        <div class="input-group">
          <input type="email" id="email" class="input-field" v-model="form.email" required />
          <label for="email" class="floating-label">Your Email</label>
        </div>

        <!-- Password Field -->
        <div class="input-group">
          <input type="password" id="password" class="input-field" v-model="form.password" required />
          <label for="password" class="floating-label">Password</label>
        </div>

        <!-- Confirm Password Field -->
        <div class="input-group">
          <input type="password" id="confirmPassword" class="input-field" v-model="form.confirmPassword" required />
          <label for="confirmPassword" class="floating-label">Re-Type Password</label>
        </div>

        <!-- Sign Up Button -->
        <button type="submit" class="submit-btn">Sign Up</button>
      </form>
    </div>

    <div class="info-section">
      <div class="info-box">
        <h2>Inbox</h2>
        <p class="info-count">176,18</p>
      </div>
      <div class="info-box">
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
/* Overall Page Layout */
.registration-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  min-height: 100vh;
  background-color: #f4f6f8;
}

.form-section {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #ffffff;
}

.info-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f0f4ff;
}

/* Form Styles */
.form-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}

.form-subtitle {
  font-size: 18px;
  margin-bottom: 30px;
}

.form-body {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-group {
  position: relative;
  margin-bottom: 20px;
}

.input-field {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  background-color: transparent;
}

.input-field:focus {
  outline: none;
  border-color: #007bff;
}

/* Floating Label */
.floating-label {
  position: relative;
}

.floating-label-text {
  position: absolute;
  top: 50%;
  left: 15px;
  font-size: 16px;
  color: #777;
  pointer-events: none;
  transition: 0.3s ease all;
  transform: translateY(-50%);
}

.input-field:focus ~ .floating-label-text,
.input-field:not(:placeholder-shown):not(:focus) ~ .floating-label-text {
  top: -10px;
  left: 10px;
  font-size: 12px;
  color: #007bff;
  background-color: #fff;
  padding: 0 5px;
}

/* Button Styles */
.submit-btn {
  padding: 12px 30px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  width: fit-content;
  align-self: flex-start;
}

.submit-btn:hover {
  background-color: #0056b3;
}

/* Info Section Styles */
.info-section {
  padding: 20px;
}

.info-box {
  background-color: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  text-align: center;
  width: 80%;
}

.info-count {
  font-size: 32px;
  font-weight: bold;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .registration-container {
    flex-direction: column;
  }

  .info-section {
    padding: 20px 10px;
  }
}
</style>
