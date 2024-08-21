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
          <!-- Overview content here -->
          <h2>Welcome, {{ userName }}!</h2>
          <p>Here's what's happening in your account today:</p>
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
    logout() {
      // Handle logout
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
  background-color: #555;
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

/* Other styles as needed */
</style>
