<template>
  <div class="fill-resume-page">
    <div class="container">
      <h1>Fill in Your Resume Details</h1>

      <form @submit.prevent="submitResume">
        <label for="name">Name:</label>
        <input type="text" v-model="name" placeholder="Enter your name" />

        <label for="contact">Contact:</label>
        <input type="text" v-model="contact" placeholder="Enter your contact info" />

        <label for="experience">Experience:</label>
        <textarea v-model="experience" placeholder="Describe your experience"></textarea>

        <button type="submit">Generate Resume</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      contact: '',
      experience: '',
      templateId: this.$route.params.templateId, // Fetch the template ID from route params
    };
  },
  methods: {
        async submitResume() {
      const resumeData = {
        name: this.name,
        contact: this.contact,
        experience: this.experience,
        templateId: this.templateId,
      };

      try {
        const response = await this.$axios.post('http://localhost:5000/generate-resume', resumeData);
        console.log(response.data); // Handle the response here
        // Example: You can redirect to the generated resume or show a download link
        window.location.href = `http://localhost:5000/${response.data.file_path}`; // Directly open the file
      } catch (error) {
        console.error('Error generating resume:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add styles for the form */
</style>
