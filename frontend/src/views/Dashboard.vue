<template>
  <div class="dashboard-container">
    <h1>Welcome to Your Dashboard</h1>
    <div class="card-container">
      <div class="card" v-for="feature in features" :key="feature.title">
        <i :class="feature.icon"></i>
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
        <router-link :to="feature.link">Go to {{ feature.title }}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      features: [
        {
          title: 'Generate Resume',
          description: 'Create a professional resume using our templates.',
          icon: 'fas fa-file-alt',
          link: '/generate-resume',
        },
        {
          title: 'Edit Profile',
          description: 'Update your personal information and preferences.',
          icon: 'fas fa-user-edit',
          link: '/edit-profile',
        },
        {
          title: 'View Templates',
          description: 'Browse through available resume templates.',
          icon: 'fas fa-th-list',
          link: '/templates',
        },
      ],
    };
  },
};
</script>

<style scoped>
.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.card-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 30%;
  margin: 10px;
  padding: 20px;
  text-align: center;
  transition: transform 0.3s;
}

.card:hover {
  transform: translateY(-10px);
}

.card i {
  font-size: 48px;
  margin-bottom: 15px;
}

.card h3 {
  margin-bottom: 10px;
}

.card p {
  margin-bottom: 15px;
  color: #555;
}

.card a {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.card a:hover {
  text-decoration: underline;
}
</style>
