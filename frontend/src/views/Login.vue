<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input type="email" v-model="email" placeholder="Email" required>
      <input type="password" v-model="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/login', {
          email: this.email,
          password: this.password
        });
        // Handle successful login (e.g., redirect, store token, etc.)
        console.log(response.data);
      } catch (error) {
        console.error(error);
        // Handle login error
      }
    }
  }
};
</script>
