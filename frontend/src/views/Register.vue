<template>
  <div class="register-page">
    <!-- Left Section: Registration Form -->
    <div class="form-container">
      <div class="form-header">
        <h1>Welcome to ResuMeister</h1>
        <p>Create an account to craft your professional resume effortlessly.</p>
      </div>

      <form class="register-form" @submit.prevent="registerUser">
        <!-- Name -->
        <div class="form-group">
          <label for="username" class="form-label">Your Name</label>
          <input
            type="text"
            id="username"
            class="form-input"
            v-model="form.username"
            placeholder="Enter your name"
            required
          />
        </div>

        <!-- Email -->
        <div class="form-group">
          <label for="email" class="form-label">Email Address</label>
          <input
            type="email"
            id="email"
            class="form-input"
            v-model="form.email"
            placeholder="Enter your email"
            required
          />
        </div>

        <!-- Password -->
        <div class="form-group">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            id="password"
            class="form-input"
            v-model="form.password"
            placeholder="Create a password"
            required
          />
          <small class="form-helper">
            Password must be at least 8 characters long.
          </small>
        </div>

        <!-- Confirm Password -->
        <div class="form-group">
          <label for="confirmPassword" class="form-label">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            class="form-input"
            v-model="form.confirmPassword"
            placeholder="Re-enter your password"
            required
          />
        </div>

        <!-- Error Message -->
        <p v-if="errorMessage" class="form-error">{{ errorMessage }}</p>

        <!-- Submit Button -->
        <button type="submit" class="submit-button">Sign Up</button>
      </form>
    </div>

    <!-- Right Section: Visual and Information -->
    <div class="info-container">
      <div class="info-overlay">
        <h2>Your Journey Begins Here</h2>
        <p>
          Join thousands of professionals who trust ResuMeister to build their
          dream resumes.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async registerUser() {
      if (this.form.password !== this.form.confirmPassword) {
        this.errorMessage = "Passwords do not match.";
        return;
      }
      try {
        const response = await fetch("http://localhost:5000/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.form),
        });
        const data = await response.json();
        if (response.ok) {
          alert("Registration successful!");
          this.$router.push("/login");
        } else {
          this.errorMessage = data.message || "Registration failed.";
        }
      } catch (error) {
        this.errorMessage = "There was a problem with the registration.";
      }
    },
  },
};
</script>

<style scoped>
/* Container Setup */
.register-page {
  display: flex;
  flex-direction: row;
  height: 100vh;
  width: 100%;
  font-family: 'Arial', sans-serif;
}

/* Form Section */
.form-container {
  flex: 1;
  padding: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: #ffffff;
}

.form-header h1 {
  font-size: 32px;
  color: #333;
  margin-bottom: 10px;
}

.form-header p {
  font-size: 16px;
  color: #666;
  margin-bottom: 30px;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  margin-bottom: 8px;
  font-weight: bold;
  color: #444;
}

.form-input {
  padding: 12px 15px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.3);
}

.form-helper {
  font-size: 12px;
  color: #888;
  margin-top: 5px;
}

.form-error {
  color: #d9534f;
  font-size: 14px;
}

.submit-button {
  padding: 12px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}

/* Info Section */
.info-container {
  flex: 1;
  background: linear-gradient(135deg, #007bff, #0056b3);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.info-overlay {
  text-align: center;
  max-width: 80%;
}

.info-overlay h2 {
  font-size: 36px;
  margin-bottom: 15px;
}

.info-overlay p {
  font-size: 16px;
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .register-page {
    flex-direction: column;
  }

  .info-container {
    height: 50vh;
  }
}
</style>
