<template>
  <div class="dashboard">
    <aside class="sidebar">
      <nav>
        <ul>
          <li @click="navigateTo('overview')">Dashboard Overview</li>
          <li @click="navigateTo('create')">Create New Resume</li>
          <li @click="navigateTo('resumes')">My Resumes</li>
          <li @click="navigateTo('settings')">Account Settings</li>
        </ul>
      </nav>
    </aside>

    <div class="main-content">
      <header>
        <div class="top-bar">
          <span>ResuMeister Dashboard</span>
          <div class="user-menu">
            <span @click="logout">Logout</span>
          </div>
        </div>
      </header>

      <section class="content">
        <div v-if="currentSection === 'overview'">
          <h2>Welcome, {{ userName }}!</h2>
          <p>Here's what's happening in your account today:</p>

          <!-- Card Section -->
          <div class="card-container">
            <div class="card" v-for="n in 6" :key="n">
              <h3>Card {{ n }}</h3>
              <p>This is the description of card {{ n }}. It contains useful information about your dashboard.</p>
              <button @click="handleCardAction(n)">Learn More</button>
            </div>
          </div>
        </div>
        <div v-else-if="currentSection === 'create'">
          <!-- Create new resume content here -->
        </div>
        <div v-else-if="currentSection === 'resumes'">
          <!-- List of resumes content here -->
        </div>
        <div v-else-if="currentSection === 'settings'">
          <!-- Account settings content here -->
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentSection: 'overview',
    };
  },
  methods: {
    navigateTo(section) {
      this.currentSection = section;
    },
    handleCardAction(cardNumber) {
      alert(`Card ${cardNumber} clicked`);
    },
    logout() {
      this.$router.push('/login');
    }
  }
};
</script>

<style>
/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard {
  display: flex;
  height: 100vh;
  width: 100vw;
}

.sidebar {
  width: 250px;
  background-color: #333;
  color: white;
  padding-top: 20px;
}

.sidebar ul {
  list-style-type: none;
}

.sidebar ul li {
  padding: 10px 20px;
  cursor: pointer;
}

.sidebar ul li:hover {
  background-color: #444;
}

.main-content {
  flex-grow: 1;
}

.top-bar {
  background-color: #001f3f;
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-menu {
  cursor: pointer;
}

.content {
  padding: 20px;
}

/* Card styles */
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-around;
}

.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 300px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card h3 {
  font-size: 1.5em;
  margin-bottom: 10px;
}

.card p {
  font-size: 1em;
  color: #555;
  margin-bottom: 20px;
}

.card button {
  padding: 10px 20px;
  background-color: #ff5733;
  border: none;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.card button:hover {
  background-color: #ff7853;
}

/* Responsive design */
@media (max-width: 768px) {
  .card-container {
    flex-direction: column;
    align-items: center;
  }
}
</style>
