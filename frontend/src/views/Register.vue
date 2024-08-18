<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="Username" required>
      <input type="email" v-model="email" placeholder="Email" required>
      <input type="password" v-model="password" placeholder="Password" required>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/register', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        // Handle successful registration (e.g., redirect to login)
        console.log(response.data);
      } catch (error) {
        console.error(error);
        // Handle registration error
      }
    }
  }
};
</script>
